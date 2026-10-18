"""The ``:pagebreak:`` role, formerly provided by sphinx-pdf-generate.

The HTML it emits is unchanged, so existing CSS and the PDF step keep working.
"""

from docutils import nodes


def page_break_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    return [nodes.raw("", '<p class="page-break" style="margin: 0"></p>', format="html")], []


def setup(app):
    app.add_role("pagebreak", page_break_role)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
