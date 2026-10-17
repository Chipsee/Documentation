"""Compare the content of two Sphinx HTML builds page by page.

Only the main article of each page is compared, reduced to text, images and links,
so theme and docutils markup changes don't show up as differences.

    python tools/compare_builds.py OLD_HTML_DIR NEW_HTML_DIR [--show N] [--structure]

--structure also compares how elements nest, with their classes and inline styles,
which catches markup changes such as a lost </div> or bold text that's no longer bold.
"""

import argparse
import difflib
import hashlib
import posixpath
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

BLOCK_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "th", "td", "caption", "dt", "dd", "figcaption", "pre", "tr"}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def resolve(root: Path, page: str, url: str) -> str:
    """Resolve a relative URL against the page path, so it reads the same in both builds.

    Sphinx numbers same-named images from different folders (Power2.png, Power3.png) in build
    order, so files under _images/ are identified by their content instead of their name.
    """
    if not url or re.match(r"^[a-z]+:", url) or url.startswith("#"):
        return url
    url = re.sub(r"\?v=[0-9a-f]+$", "", url)
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(page), url))
    if resolved.startswith("_images/") and root.joinpath(resolved).is_file():
        digest = hashlib.sha256(root.joinpath(resolved).read_bytes()).hexdigest()[:12]
        return f"_images/<{digest}>{Path(resolved).suffix}"
    return resolved


def page_lines(root: Path, page: str, structure: bool = False) -> list[str]:
    soup = BeautifulSoup(root.joinpath(page).read_text(encoding="utf-8"), "html.parser")
    main = soup.find(attrs={"role": "main"})
    if main is None:
        return []
    for node in main.select("a.headerlink"):
        node.decompose()
    # Docutils 0.18+ renders footnotes as <aside> with bracket spans and back links
    # instead of <dl>/<dt>/<dd>.
    for node in main.select(
        "span.fn-bracket, aside.footnote > span.label, span.backrefs, a[role=doc-backlink], dl.footnote > dt"
    ):
        node.decompose()
    for node in main.select("dl.footnote > dd"):
        node.name = "div"

    lines: list[str] = []
    depth = 0

    def walk(node: Tag, buf: list[str]) -> None:
        nonlocal depth
        for child in node.children:
            if isinstance(child, NavigableString):
                buf.append(str(child))
                continue
            if not isinstance(child, Tag):
                continue
            if child.name in ("script", "style"):
                continue
            if structure:
                attrs = " ".join(child.get("class", [])) + (f" style={child['style']}" if child.get("style") else "")
                lines.append(f"{'  ' * depth}<{child.name}{' ' + attrs if attrs else ''}>")
                depth += 1
            if child.name == "img":
                alt = normalize(child.get("alt", ""))
                if "_images/" in alt:
                    alt = resolve(root, page, alt)
                lines.append(f"IMG {resolve(root, page, child.get('src', ''))} alt={alt}")
                if structure:
                    depth -= 1
                continue
            if child.name == "a" and child.get("href"):
                lines.append(f"LINK {resolve(root, page, child['href'])}")
            if child.name in BLOCK_TAGS:
                inner: list[str] = []
                walk(child, inner)
                text = normalize("".join(inner))
                if child.name == "tr":
                    lines.append("ROW")
                elif text:
                    lines.append(f"{child.name.upper()} {text}")
                buf.append(" " + "".join(inner) + " ")
            else:
                walk(child, buf)
            if structure:
                depth -= 1

    walk(main, [])
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("old", type=Path)
    parser.add_argument("new", type=Path)
    parser.add_argument("--show", type=int, default=3, help="pages to print a diff for")
    parser.add_argument("--structure", action="store_true", help="also compare element nesting, classes and styles")
    args = parser.parse_args()

    old_pages = {p.relative_to(args.old).as_posix() for p in args.old.rglob("*.html")}
    new_pages = {p.relative_to(args.new).as_posix() for p in args.new.rglob("*.html")}
    ignored = re.compile(r"^(_static|_sphinx_design_static|_images|_downloads)/")
    old_pages = {p for p in old_pages if not ignored.match(p)}
    new_pages = {p for p in new_pages if not ignored.match(p)}

    for p in sorted(old_pages - new_pages):
        print(f"MISSING  {p}")
    for p in sorted(new_pages - old_pages):
        print(f"ADDED    {p}")

    changed = 0
    for page in sorted(old_pages & new_pages):
        a = page_lines(args.old, page, args.structure)
        b = page_lines(args.new, page, args.structure)
        if a == b:
            continue
        changed += 1
        print(f"CHANGED  {page}")
        if changed <= args.show:
            for line in difflib.unified_diff(a, b, "old", "new", n=1, lineterm=""):
                print("    " + line[:200])

    total = len(old_pages & new_pages)
    print(f"\n{total} pages compared, {changed} changed, "
          f"{len(old_pages - new_pages)} missing, {len(new_pages - old_pages)} added")
    return 1 if changed or old_pages != new_pages else 0


if __name__ == "__main__":
    sys.exit(main())
