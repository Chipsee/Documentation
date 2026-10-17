"""PDF manuals: which pages get one, and the download button on them.

Every page gets a PDF unless its metadata says ``:pdf-build: False``. The metadata also sets
the cover and the file name:

``:pdf-title:``, ``:pdf-subtitle:``
    the cover's title and subtitle, the page title by default.
``:pdf-type:``
    the kind of product, shown on the cover and in the footer: ``ipc``, ``displays`` or
    ``hmi display``.
``:pdf-revision:``
    a revision shown on the cover.
``:pdf-filename:``
    the PDF's name, next to the page's HTML, the page name by default.

The PDFs are rendered from the built HTML by tools/build_pdfs.py, which reads the pages
from pdf_manifest.json, written here at the end of the build.
"""

import json
import posixpath
import re
from pathlib import Path

from markupsafe import escape

MANIFEST = "pdf_manifest.json"

BUTTON = (
    '<a class="md-content__button md-icon pdf-download" style="margin:0;float:right;" href="{href}" download title="Download PDF">'
    '<img src="{icon}" alt="Download PDF" width="40" height="40"></a>'
)


def pdf_info(app, docname: str) -> dict | None:
    meta = app.env.metadata.get(docname, {})
    if str(meta.get("pdf-build", "")).strip().lower() == "false" or docname == app.config.root_doc:
        return None
    filename = meta.get("pdf-filename") or posixpath.basename(docname)
    # A name that's safe in a URL: "EPC/PPC-A8-050-C" is EPC_PPC-A8-050-C, "Nano&NX" is NanoNX.
    filename = re.sub(r"[^\w.-]", "", filename.replace("/", "_").replace(" ", "_")) + ".pdf"
    title = app.env.titles[docname].astext() if docname in app.env.titles else docname
    return {
        "html": app.builder.get_target_uri(docname),
        "pdf": posixpath.join(posixpath.dirname(docname), filename),
        "title": meta.get("pdf-title") or title,
        "subtitle": meta.get("pdf-subtitle", ""),
        "type": meta.get("pdf-type", "ipc"),
        "revision": meta.get("pdf-revision", ""),
    }


def add_button(app, pagename, templatename, context, doctree) -> None:
    info = pdf_info(app, pagename) if doctree is not None else None
    if info is None or "body" not in context:
        return
    href = posixpath.basename(info["pdf"])
    icon = context["pathto"]("_static/images/pdf_download.svg", 1)
    context["body"] = BUTTON.format(href=escape(href), icon=escape(icon)) + context["body"]


def write_manifest(app, exception) -> None:
    if exception is not None or app.builder.format != "html":
        return
    pages = {docname: info for docname in sorted(app.env.found_docs) if (info := pdf_info(app, docname))}
    Path(app.outdir, MANIFEST).write_text(json.dumps(pages, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def setup(app):
    app.connect("html-page-context", add_button)
    app.connect("build-finished", write_manifest)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
