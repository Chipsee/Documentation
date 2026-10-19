"""Pull product specs from the Chipsee C3 website into docs/source/_data/specs.

Each manual page gets one JSON file, named after the page, holding the products whose
doc_url points to it and their specs in display order. The files are committed, so a
pull shows up as a reviewable diff and builds don't need the network.

    python tools/pull_specs.py [--api URL] [--summary PATH]

With a staff API token in CHIPSEE_API_TOKEN, unpublished products are pulled too.
--summary writes what changed, spec by spec, as Markdown (to stdout with "-"), e.g. for a
pull request's description.
"""

import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "docs" / "source"
DATA_DIR = SOURCE_DIR / "_data" / "specs"
DOCS_BASE_URL = "https://chipsee.com/docs/"
DEFAULT_API = "https://c3.printfinn.com/api/v1/products"
STAFF_API = "https://c3.printfinn.com/api/v1/staff/products"
PRODUCT_FIELDS = ("id", "slug", "title", "pn", "shop_url")
# GitHub cuts a pull request's description at 65536 characters.
SUMMARY_LIMIT = 50000  # leaves room for the build result


def fetch(api: str, token: str | None) -> list[dict]:
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(api, headers=headers)
    with urllib.request.urlopen(request, timeout=60) as response:
        body = json.load(response)
    products = body["products"]
    if body.get("meta", {}).get("count", len(products)) != len(products):
        sys.exit(f"API returned {len(products)} of {body['meta']['count']} products; pagination isn't supported")
    return products


def docname(doc_url: str) -> str | None:
    if not doc_url or not doc_url.startswith(DOCS_BASE_URL) or not doc_url.endswith(".html"):
        return None
    return doc_url.removeprefix(DOCS_BASE_URL).removesuffix(".html")


def cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ") or "—"


def changes(name: str, old: dict | None, new: dict | None) -> str:
    """What changed on one page, as Markdown."""
    titles = lambda data: [p["title"] for p in data["products"]] if data else []
    heading = f"**{', '.join(titles(new) or titles(old))}** (`{name}`)"
    if new is None:
        return f"{heading}\n\n⚠️ Removed: no product's doc_url points to this page any more, so its manual has no specs.\n"
    if old is None:
        rows = [f"| {cell(s['name'])} | {cell(s['value'])} |" for s in new["specs"]]
        return "\n".join([heading, "", "New page.", "", "| Spec | Value |", "|---|---|", *rows]) + "\n"
    lines = [heading, ""]
    lines += [f"- Product added: {t}" for t in titles(new) if t not in titles(old)]
    lines += [f"- Product removed: {t}" for t in titles(old) if t not in titles(new)]
    before = {s["name"]: s["value"] for s in old["specs"]}
    after = {s["name"]: s["value"] for s in new["specs"]}
    rows = [(n, before.get(n, ""), v) for n, v in after.items() if before.get(n) != v]
    rows += [(n, v, "") for n, v in before.items() if n not in after]
    if rows:
        if lines[-1]:
            lines.append("")
        lines += ["| Spec | Before | After |", "|---|---|---|"]
        lines += [f"| {cell(n)} | {cell(b)} | {cell(a)} |" for n, b, a in rows]
    elif len(lines) == 2:
        lines.append("Only the order of specs or products' other fields changed.")
    return "\n".join(lines) + "\n"


def write_summary(path: str, sections: list[str]) -> None:
    text = f"{len(sections)} page{"s" * (len(sections) != 1)} changed.\n\n" if sections else "No spec changed.\n"
    for n, section in enumerate(sections):
        if path != "-" and len(text) + len(section) > SUMMARY_LIMIT:
            text += f"\n…and {len(sections) - n} more pages; see Files changed.\n"
            break
        text += section + "\n"
    if path == "-":
        print(text, end="")
    else:
        Path(path).write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--api", help=f"defaults to {DEFAULT_API}, or {STAFF_API} with a token")
    parser.add_argument("--summary", help='write what changed as Markdown to this file, or "-" for stdout')
    args = parser.parse_args()
    token = os.environ.get("CHIPSEE_API_TOKEN") or None
    api = args.api or (STAFF_API if token else DEFAULT_API)

    pages: dict[str, list[dict]] = {}
    warnings = 0
    for product in fetch(api, token):
        name = docname(product.get("doc_url") or "")
        if name is None or not SOURCE_DIR.joinpath(f"{name}.rst").is_file():
            print(f"skip   {product['title']}: no manual page for doc_url {product.get('doc_url')!r}")
            warnings += 1
            continue
        pages.setdefault(name, []).append(product)

    written = set()
    sections = []
    for name, products in sorted(pages.items()):
        products.sort(key=lambda p: p["id"])
        specs = [{"name": s["name"], "value": s["value"]} for s in products[0]["specs"]]
        for other in products[1:]:
            if [{"name": s["name"], "value": s["value"]} for s in other["specs"]] != specs:
                print(f"warn   {name}: {other['title']} has different specs from {products[0]['title']}; using {products[0]['title']}'s")
                warnings += 1
        data = {"products": [{k: p.get(k) for k in PRODUCT_FIELDS} for p in products], "specs": specs}

        path = DATA_DIR / f"{name}.json"
        text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
        if not path.is_file() or path.read_text(encoding="utf-8") != text:
            old = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else None
            sections.append(changes(name, old, data))
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
            print(f"update {path.relative_to(ROOT)}")
        written.add(path)

    for path in sorted(DATA_DIR.rglob("*.json")):
        if path not in written:
            name = path.relative_to(DATA_DIR).with_suffix("").as_posix()
            sections.append(changes(name, json.loads(path.read_text(encoding="utf-8")), None))
            path.unlink()
            print(f"remove {path.relative_to(ROOT)}")

    print(f"{len(written)} pages, {sum(len(p) for p in pages.values())} products, {warnings} warnings")
    if args.summary:
        write_summary(args.summary, sections)
    return 0


if __name__ == "__main__":
    sys.exit(main())
