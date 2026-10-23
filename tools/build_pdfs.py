"""Render the PDF manuals from a Sphinx HTML build.

    python tools/build_pdfs.py HTML_DIR [--previous DIR] [--jobs N] [--only PATTERN] [--force]

The pages come from HTML_DIR/pdf_manifest.json, written by the pdf extension. Each PDF is
the page's article with a cover and contents (docs/source/_pdf), written next to its HTML.

A PDF is rendered again only when its input changed: the article, the images, fonts and
stylesheets it uses, or this script. Each PDF's input fingerprint is kept in
HTML_DIR/pdf_fingerprints.json; with --previous, the PDFs of an earlier output (the
docs-build branch) whose fingerprint is unchanged are copied instead of rendered.
"""

import argparse
import fnmatch
import hashlib
import json
import os
import posixpath
import re
import shutil
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from functools import cache
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

from bs4 import BeautifulSoup, Tag
from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "docs" / "source"
ASSETS = SOURCE / "_pdf"
BASE_URL = "https://chipsee.com/docs/"
FINGERPRINTS = "pdf_fingerprints.json"
LABELS = {
    "ipc": "Industrial PC",
    "displays": "Industrial Display",
    "hmi display": "Industrial HMI Display",
    "rugged tablet": "Rugged Tablet PC",
    "rugged laptop": "Rugged Laptop",
}
TOC_LEVELS = ("h2", "h3", "h4")
# Images are embedded at no more than this resolution, which is plenty for print.
DPI = 200
JPEG_QUALITY = 85
SHORT_TABLE = 20


def local_file(page: Path, url: str) -> Path | None:
    """The file a relative URL in a built page points to, if it's local."""
    parts = urlsplit(url)
    if parts.scheme or parts.netloc or not parts.path:
        return None
    return (page.parent / unquote(parts.path)).resolve()


def absolute_link(page_url: str, href: str) -> str:
    """A link from the page, made to work outside the site: other pages go to the website."""
    if href.startswith("#") or urlsplit(href).scheme:
        return href
    target = urljoin(BASE_URL + page_url, href)
    path, _, fragment = target.partition("#")
    if path == BASE_URL + page_url:
        return "#" + fragment if fragment else "#"
    return target


@cache
def media_pngs() -> dict[str, Path]:
    return {path.name: path for path in SOURCE.joinpath("Media").rglob("*.png")}


def cover_image(src: str) -> str:
    """The cover's product image, shown as it is.

    The gallery shows a photo, e.g. CS12800RA5101P-Front-Low.jpg; the cover prefers the
    product's PNG, CS12800RA5101P-Front.png, if there is one.
    """
    stem = re.sub(r"(-Low)?\.\w+$", "", posixpath.basename(unquote(src)))
    png = media_pngs().get(stem + ".png")
    return png.as_uri() if png is not None else src


def wrap_figures(main: Tag) -> None:
    """Keep each centered image together with its caption below.

    An image is centered either in a paragraph, ``|image|`` in a ``text-center`` paragraph,
    or by itself, ``.. image::`` with ``:align: center``.
    """
    images = [p for p in main.select("p.text-center") if p.find("img") is not None]
    images += [img for img in main.select("img.align-center") if img.parent.name not in ("p", "td", "th", "figure")]
    for image in images:
        if image.find_parent(class_="figure"):
            continue
        figure = image.wrap(main.new_tag("div", attrs={"class": "figure"}))
        caption = figure.find_next_sibling()
        if isinstance(caption, Tag) and caption.name == "p" and "text-center" in caption.get("class", []) and caption.find("img") is None:
            caption["class"] = caption.get("class", []) + ["caption"]
            figure.append(caption.extract())


def prepare(html_dir: Path, page_url: str) -> tuple[Markup, list[dict], tuple[str, bool] | None]:
    """The page's article for print, its contents entries and its first product image."""
    page = html_dir / page_url
    soup = BeautifulSoup(page.read_text(encoding="utf-8"), "html.parser")
    main = soup.find(attrs={"role": "main"})

    # The product views gallery at the top of hardware manuals is for the website only;
    # print it as a grid with captions.
    views = [(img["src"], img.get("alt", "")) for img in main.select("img.product-img")]
    for node in main.select(".html-only, a.headerlink, a.pdf-download, script, style, .copybtn, .caption-number"):
        node.decompose()
    for node in main.select("p.page-break"):
        parent = node.parent
        node.decompose()
        if parent.name == "p" and not parent.get_text(strip=True) and parent.find("img") is None:
            parent.decompose()
    for iframe in main.select("iframe"):
        link = soup.new_tag("a", href=iframe.get("src", ""))
        link.string = iframe.get("src", "")
        para = soup.new_tag("p", attrs={"class": "video-link"})
        para.append("Video: ")
        para.append(link)
        iframe.replace_with(para)

    if views:
        grid = soup.new_tag("div", attrs={"class": "views"})
        for src, alt in views:
            figure = soup.new_tag("figure")
            figure.append(soup.new_tag("img", src=src, alt=alt))
            if alt:
                caption = soup.new_tag("figcaption")
                caption.string = alt
                figure.append(caption)
            grid.append(figure)
        h1 = main.find("h1")
        if h1 is not None:
            h1.insert_after(grid)
        else:
            main.insert(0, grid)

    # A link around an image opens the image on the website; in print it's just the image.
    for a in main.select("a"):
        if a.find("img") is not None and a.get_text(strip=True) == "":
            a.unwrap()
        elif a.get("href"):
            a["href"] = absolute_link(page_url, a["href"])

    wrap_figures(main)

    # A short table stays on one page, with its caption.
    for table in main.select("table"):
        if len(table.find_all("tr")) <= SHORT_TABLE:
            table["class"] = table.get("class", []) + ["short"]

    # Number the headings, and list them in the contents.
    toc = []
    counters = [0] * len(TOC_LEVELS)
    for heading in main.find_all(TOC_LEVELS):
        level = TOC_LEVELS.index(heading.name)
        counters[level] += 1
        counters[level + 1 :] = [0] * (len(TOC_LEVELS) - level - 1)
        number = ".".join(str(n) for n in counters[: level + 1])
        section = heading.find_parent("section")
        anchor = section.get("id") if section is not None and section.find(TOC_LEVELS) is heading else None
        if not anchor:
            anchor = heading.get("id") or f"heading-{len(toc)}"
            heading["id"] = anchor
        title = " ".join(heading.get_text(" ").split())
        span = soup.new_tag("span", attrs={"class": "number"})
        span.string = number
        heading.insert(0, span)
        span.insert_after(" ")
        heading["data-title"] = title
        heading["data-bookmark"] = f"{number} {title}"
        toc.append({"level": level + 2, "id": anchor, "number": number, "title": title})

    return Markup(main.decode_contents()), toc, cover_image(views[0][0]) if views else None


def assets_used(html_dir: Path, page_url: str, body: str) -> list[Path]:
    page = html_dir / page_url
    files = [p for p in ASSETS.rglob("*") if p.is_file()]
    files += [ROOT / "docs/source/_static/images/cover.svg", ROOT / "docs/source/_static/images/logo_header.png", Path(__file__).resolve()]
    files += sorted(ASSETS.parent.joinpath("_static/vendor/google-fonts/files").glob("*.ttf"))
    files.append(html_dir / "_static" / "pygments.css")
    for src in re.findall(r'src="([^"]+)"', body):
        path = Path(unquote(urlsplit(src).path)) if src.startswith("file:") else local_file(page, src)
        if path is not None and path.is_file():
            files.append(path)
    return files


@cache
def file_digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fingerprint(page: Path, html: str, files: list[Path]) -> str:
    """A digest of a manual's input that's the same wherever the build is.

    Sphinx numbers same-named images (Antenna1.jpeg, Antenna2.jpeg) in an order that changes
    between parallel builds, so images in the build are identified by their content.
    """

    def built_image(match: re.Match) -> str:
        path = local_file(page, match.group())
        return file_digest(path) if path is not None and path.is_file() else match.group()

    html = re.sub(r"(?:\.\./)*_images/[^\"'\s]+", built_image, html.replace(SOURCE.as_uri(), ""))
    digest = hashlib.sha256(html.encode())
    for content in sorted({file_digest(p) for p in files}):
        digest.update(content.encode())
    return digest.hexdigest()


def document(html_dir: Path, info: dict) -> tuple[str, list[Path]]:
    """The print HTML of a manual, and the files it uses."""
    body, toc, image = prepare(html_dir, info["html"])
    env = Environment(loader=FileSystemLoader(ASSETS), autoescape=True)
    html = env.get_template("manual.html.j2").render(
        title=info["title"],
        subtitle=info["subtitle"],
        revision=info["revision"],
        label=LABELS.get(info["type"].lower(), f"Industrial {info['type'].title()}"),
        image=image,
        url="www.chipsee.com",
        toc=toc,
        body=body,
        assets=ASSETS.as_uri(),
        pygments=posixpath.relpath("_static/pygments.css", posixpath.dirname(info["html"])),
    )
    return html, assets_used(html_dir, info["html"], html)


def render(html_dir: str, docname: str, info: dict, html: str) -> tuple[str, float]:
    import logging

    from weasyprint import HTML

    # fontTools complains about the bold flags of the bundled fonts while subsetting them.
    logging.getLogger("fontTools").setLevel(logging.ERROR)
    start = time.monotonic()
    target = Path(html_dir, info["pdf"])
    HTML(string=html, base_url=Path(html_dir, info["html"]).as_uri()).write_pdf(
        target,
        presentational_hints=True,
        optimize_images=True,
        dpi=DPI,
        jpeg_quality=JPEG_QUALITY,
    )
    return docname, time.monotonic() - start


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("html", type=Path, help="the Sphinx HTML output")
    parser.add_argument("--previous", type=Path, help="an earlier output whose unchanged PDFs are reused")
    parser.add_argument("--jobs", type=int, default=os.cpu_count(), help="PDFs rendered at a time")
    parser.add_argument("--only", help="render only pages matching this pattern, e.g. 'PCs/ESP32/*'")
    parser.add_argument("--force", action="store_true", help="render every PDF, even if unchanged")
    parser.add_argument("--keep-html", action="store_true", help="also write the print HTML next to each PDF, for debugging")
    args = parser.parse_args()
    args.html = args.html.resolve()

    manifest = json.loads(args.html.joinpath("pdf_manifest.json").read_text(encoding="utf-8"))
    if args.only:
        manifest = {d: i for d, i in manifest.items() if fnmatch.fnmatch(d, args.only)}
    previous = {}
    if args.previous and args.previous.joinpath(FINGERPRINTS).is_file():
        previous = json.loads(args.previous.joinpath(FINGERPRINTS).read_text(encoding="utf-8"))
    fingerprints_path = args.html / FINGERPRINTS
    fingerprints = json.loads(fingerprints_path.read_text(encoding="utf-8")) if fingerprints_path.is_file() else {}

    todo, reused = [], 0
    for docname, info in manifest.items():
        html, files = document(args.html, info)
        digest = fingerprint(args.html / info["html"], html, files)
        target = args.html / info["pdf"]
        if args.keep_html:
            target.with_suffix(".print.html").write_text(html, encoding="utf-8")
        if not args.force:
            if fingerprints.get(info["pdf"]) == digest and target.is_file():
                reused += 1
                continue
            old = args.previous / info["pdf"] if args.previous else None
            if previous.get(info["pdf"]) == digest and old is not None and old.is_file():
                shutil.copyfile(old, target)
                fingerprints[info["pdf"]] = digest
                reused += 1
                continue
        todo.append((docname, info, html, digest))

    print(f"{len(manifest)} PDFs: {reused} unchanged, {len(todo)} to render with {args.jobs} jobs", flush=True)
    failed = 0
    start = time.monotonic()
    with ProcessPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(render, str(args.html), d, i, h): (d, i, digest) for d, i, h, digest in todo}
        for n, future in enumerate(as_completed(futures), 1):
            docname, info, digest = futures[future]
            try:
                _, seconds = future.result()
            except Exception as error:  # noqa: BLE001 - report every failure, keep going
                failed += 1
                print(f"[{n}/{len(todo)}] FAILED {docname}: {error!r}", flush=True)
                continue
            fingerprints[info["pdf"]] = digest
            print(f"[{n}/{len(todo)}] {info['pdf']} ({seconds:.1f}s)", flush=True)

    fingerprints_path.write_text(json.dumps(dict(sorted(fingerprints.items())), indent=1) + "\n", encoding="utf-8")
    print(f"done in {time.monotonic() - start:.0f}s, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
