"""Product specs from the Chipsee website, pulled into _data/specs by tools/pull_specs.py.

A manual page with a data file gets:

- the ``spec-table`` directive, which renders its Key Features table, and
- substitutions for each spec, e.g. for ``Power Input``:

  ``|spec:Power Input|``
      the whole value.
  ``|spec-bare:Power Input|``
      the value without a trailing ``(optional…)`` or ``(default…)``, for prose that says so itself.
  ``|spec:Dimensions:P|``, ``|spec:Dimensions:CS10600RA5070E|``
      one product's part of a value listed per part number, like
      ``CS10600RA5070E: 190 x 108 x 28mm; CS10600RA5070P: 206 x 135 x 30mm``. The letter is the
      part number's last one (P panel, E embedded, A all in one). A value that isn't listed
      per part number belongs to every product on the page, so it's there for every letter.
  ``|spec-text:Touch|``
      the touch screen as a phrase, from Touch Point, Touch Technology and Glass:
      ``10-point capacitive touch screen with 1.0mm tempered glass``.
  ``|spec-text:Display|``
      the display as a phrase, from Display Size, the touch screen, Display Resolution and
      Brightness: ``10.1” 10-point capacitive touch screen with 1.0mm tempered glass, a
      resolution of 1280 x 800 pixels and a brightness of 500 cd/m2``.

  A phrase leaves out the specs a product doesn't have, and isn't there without Touch Technology.

Specs are plain text. A few typography rules are applied when they are rendered:
``®`` and the 2 in ``cd/m2`` are superscripted, and parentheses that start with ``optional``
or ``default``, like ``(optional)`` or ``(optional, not mounted by default)``, are bold.
"""

import json
import re
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.utils import column_width
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective

logger = logging.getLogger(__name__)

DATA_DIR = "_data/specs"

# docname -> {"products": [...], "specs": [{"name", "value"}, ...]}, loaded once per build.
SPECS: dict[str, dict] = {}

TYPOGRAPHY = re.compile(r"(?P<reg>®)|(?P<cdm2>(?<=cd/m)2\b)|(?P<bold>\((?:optional|default)\b[^()]*\))", re.IGNORECASE)
LIST_MARKER = re.compile(r"^(?:[-*+•]\s|#\.\s|\(?\w{1,3}[.)]\s)")
TRAILING_NOTE = re.compile(r"\s*\((?:optional|default)\b[^()]*\)\s*$", re.IGNORECASE)
# One product's part of a spec listed per part number, which has capitals and digits only:
# "CS10600RA5070E: 400g", "PPC-A8-070H-C (PN: CS10600T070P): 680g", "PPC-A7-070HB-C (CS10600U070P): 730g".
PART = re.compile(r"^(?:[A-Z][\w-]* \((?:PN: )?)?(?P<pn>[A-Z0-9-]*\d[A-Z0-9-]*)\)?:\s*(?P<value>.+)$")
VARIANTS = {"PPC": "P", "EPC": "E", "AIO": "A"}


def escape(text: str) -> str:
    return re.sub(r"([\\*`|_])", r"\\\1", text)


def to_rst(value: str) -> str:
    """Plain spec text as inline reStructuredText, with the typography rules applied."""
    parts = []
    pos = 0
    for match in TYPOGRAPHY.finditer(value):
        parts.append(escape(value[pos:match.start()]))
        if match["bold"]:
            parts.append(f"\\ **{escape(match['bold'])}**\\ ")
        else:
            parts.append(f"\\ :sup:`{match.group()}`\\ ")
        pos = match.end()
    parts.append(escape(value[pos:]))
    text = "".join(parts)
    # Keep a value like "- 2 x USB" a paragraph rather than a list.
    return "\\ " + text if LIST_MARKER.match(value) else text


def data_path(app, docname: str) -> Path:
    return Path(app.srcdir, DATA_DIR, f"{docname}.json")


def load_specs(app) -> None:
    SPECS.clear()
    root = Path(app.srcdir, DATA_DIR)
    for path in root.rglob("*.json"):
        SPECS[path.relative_to(root).with_suffix("").as_posix()] = json.loads(path.read_text(encoding="utf-8"))


def substitutions(data: dict) -> dict[str, str]:
    """Substitution name -> plain text, for every spec on a page."""
    subs = {}
    for spec in data["specs"]:
        name, value = spec["name"], spec["value"].strip()
        if not value:
            continue
        subs[f"spec:{name}"] = value
        subs[f"spec-bare:{name}"] = TRAILING_NOTE.sub("", value)

        parts = [PART.match(part.strip()) for part in value.split(";")]
        if all(parts):
            letters = [m["pn"][-1] for m in parts]
            for m in parts:
                subs[f"spec:{name}:{m['pn']}"] = m["value"]
                if letters.count(m["pn"][-1]) == 1 and m["pn"][-1] in VARIANTS.values():
                    subs[f"spec:{name}:{m['pn'][-1]}"] = m["value"]
            # A single part number is the page's only product, whatever letter it ends with.
            if len(parts) == 1:
                for letter in VARIANTS.values():
                    subs[f"spec:{name}:{letter}"] = parts[0]["value"]
        else:
            for letter in VARIANTS.values():
                subs[f"spec:{name}:{letter}"] = value
    return subs


def phrases(subs: dict[str, str]) -> dict[str, str]:
    """The display and touch screen as phrases for prose, from the specs they're split into."""
    if "spec:Touch Technology" not in subs:
        return {}
    point = subs.get("spec:Touch Point", "")
    touch = (f"{point.lower()}-point " if point else "") + subs["spec:Touch Technology"].lower() + " touch screen"
    glass = subs.get("spec:Glass", "").lower()
    details = [f"a resolution of {subs['spec:Display Resolution']} pixels"] if "spec:Display Resolution" in subs else []
    details += [f"a brightness of {subs['spec:Brightness']}"] if "spec:Brightness" in subs else []
    display = touch + (f" with {glass}," if glass and details else f" with {glass}" if glass else "")
    if details:
        display += (" with " if not glass else " ") + " and ".join(details)
    if "spec:Display Size" in subs:
        display = f"{subs['spec:Display Size']} {display}"
    return {"spec-text:Touch": touch + (f" with {glass}" if glass else ""), "spec-text:Display": display}


def add_substitutions(app, docname: str, source: list[str]) -> None:
    data = SPECS.get(docname)
    if data is None:
        return
    app.env.note_dependency(data_path(app, docname))
    subs = substitutions(data)
    subs.update(phrases(subs))
    definitions = [f".. |{name}| replace:: {to_rst(value)}" for name, value in subs.items()]
    source[0] += "\n\n" + "\n\n".join(definitions) + "\n"


def grid_table(header: list[str], rows: list[list[str | None]]) -> list[str]:
    """A grid table. The header is one cell spanning every column, one cell per column, or none.

    A row whose first cell is None continues the label of the row above (two columns only).
    """
    columns = len(rows[0])
    widths = [max(column_width(row[c] or "") for row in rows + ([header] if len(header) == columns else [])) for c in range(columns)]
    inner = sum(w + 2 for w in widths) + columns - 1
    if len(header) == 1 and column_width(header[0]) > inner - 2:
        widths[-1] += column_width(header[0]) - inner + 2
        inner = column_width(header[0]) + 2

    def pad(text: str, width: int) -> str:
        return text + " " * (width - column_width(text))

    rule = "+" + "+".join("-" * (w + 2) for w in widths) + "+"
    if len(header) == 1:
        lines = [f"+{'-' * inner}+", f"| {pad(header[0], inner - 2)} |", rule.replace("-", "=")]
    elif header:
        lines = [rule, "|" + "|".join(f" {pad(cell, w)} " for cell, w in zip(header, widths)) + "|", rule.replace("-", "=")]
    else:
        lines = [rule]
    for i, row in enumerate(rows):
        lines.append("|" + "|".join(f" {pad(cell or '', w)} " for cell, w in zip(row, widths)) + "|")
        if i + 1 < len(rows) and rows[i + 1][0] is None:
            lines.append("|" + " " * (widths[0] + 2) + rule[widths[0] + 3 :])
        else:
            lines.append(rule)
    return lines


class SpecTable(SphinxDirective):
    """Render the page's specs as the Key Features table.

    Takes the options of the ``table`` directive, and:

    ``:footnotes:``
        footnotes defined on the page for spec rows, e.g. ``Storage=tf, RS485=at``
        for ``[#tf]_`` and ``[#at]_``.
    ``:rowspan:``
        specs listed per product, e.g. ``Dimensions, Weight``, whose ``;``-separated parts
        get a row each under one label.
    ``:columns:``
        specs side by side in each row, 1 (default) or 2.
    ``:header:``
        the header row's text, ``.. centered:: |product|`` by default, or ``none``.
    ``:header-label:``
        a first header cell, which splits the header like a spec row, e.g. ``**Product**``.
    """

    option_spec = {
        "caption": directives.unchanged,
        "footnotes": directives.unchanged,
        "rowspan": directives.unchanged,
        "columns": directives.positive_int,
        "header": directives.unchanged,
        "header-label": directives.unchanged,
        "align": directives.unchanged,
        "width": directives.unchanged,
        "widths": directives.unchanged,
        "class": directives.unchanged,
    }
    TABLE_OPTIONS = ("align", "width", "widths", "class")

    def names_option(self, key: str) -> list[str]:
        return [part.strip() for part in self.options.get(key, "").split(",") if part.strip()]

    def run(self) -> list[nodes.Node]:
        data = SPECS.get(self.env.docname)
        if data is None:
            logger.warning("no specs for %s, run tools/pull_specs.py", self.env.docname, location=self.get_location())
            return []
        self.env.note_dependency(data_path(self.env.app, self.env.docname))

        footnotes = dict(item.partition("=")[::2] for item in self.names_option("footnotes"))
        footnotes = {name.strip(): label.strip() for name, label in footnotes.items()}
        rowspan = set(self.names_option("rowspan"))
        names = {s["name"] for s in data["specs"]}
        for name in (footnotes.keys() | rowspan) - names:
            logger.warning("spec-table option names unknown spec %r", name, location=self.get_location())

        cells = []
        for spec in data["specs"]:
            name, value = spec["name"], spec["value"].strip()
            if not value:
                continue
            values = [to_rst(part.strip()) for part in value.split(";")] if name in rowspan else [to_rst(value)]
            if name in footnotes:
                values[-1] += f"\\ [#{footnotes[name]}]_"
            cells.append((f"**{escape(name)}**", values))
        if not cells:
            return []

        columns = self.options.get("columns", 1)
        if columns == 1:
            rows = [[label if i == 0 else None, value] for label, values in cells for i, value in enumerate(values)]
        else:
            if any(len(values) > 1 for _, values in cells):
                logger.warning("spec-table can't combine :rowspan: and :columns:", location=self.get_location())
            flat = [[label, "; ".join(values)] for label, values in cells]
            flat += [["", ""]] * (-len(flat) % columns)
            rows = [sum(flat[i : i + columns], []) for i in range(0, len(flat), columns)]

        lines = [f".. table:: {self.options.get('caption', 'Key Features')}"]
        lines += [f"   :{key}: {self.options[key]}" for key in self.TABLE_OPTIONS if key in self.options]
        header = self.options.get("header", ".. centered:: |product|")
        header = [] if header == "none" else [self.options["header-label"], header] if "header-label" in self.options else [header]
        lines += [""] + ["   " + line for line in grid_table(header, rows)]
        return self.parse_text_to_nodes("\n".join(lines))


def setup(app):
    app.connect("builder-inited", load_specs)
    app.connect("source-read", add_substitutions)
    app.add_directive("spec-table", SpecTable)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
