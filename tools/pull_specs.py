"""Pull product specs from the Chipsee website into docs/source/_data/specs.

Each manual page gets one JSON file, named after the page, holding the products whose
doc_url points to it and their specs in display order. The files are committed, so a
pull shows up as a reviewable diff and builds don't need the network.

    python tools/pull_specs.py [--api URL]

With a staff API token in CHIPSEE_API_TOKEN, unpublished products are pulled too.
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--api", help=f"defaults to {DEFAULT_API}, or {STAFF_API} with a token")
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
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
            print(f"update {path.relative_to(ROOT)}")
        written.add(path)

    for path in sorted(DATA_DIR.rglob("*.json")):
        if path not in written:
            path.unlink()
            print(f"remove {path.relative_to(ROOT)}")

    print(f"{len(written)} pages, {sum(len(p) for p in pages.values())} products, {warnings} warnings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
