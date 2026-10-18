# Developer guide

How to build and preview the docs, update product specs, and render the PDF manuals.

## Setup

Python 3.13 (see `mise.toml`) in a virtualenv named `venv` at the repository root, which the Makefile uses:

```bash
python3.13 -m venv venv
venv/bin/pip install -r docs/source/requirements.txt
```

Rendering PDFs locally also needs Pango:

```bash
brew install pango            # macOS
sudo apt install libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz-subset0   # Debian/Ubuntu
```

## Common commands

| Command | What it does |
|---|---|
| `make html` | Build the whole site into `docs/build/html`. Fails on any Sphinx warning, after listing them all. |
| `make watch` | Serve the site at http://localhost:8000 and rebuild the pages you edit. Faster, but only reports warnings for the pages it rebuilds, so run `make html` before opening a pull request. |
| `make pdf` | `make html`, then render the PDF manuals that changed since the last `make pdf`, next to their HTML. |
| `make pull-specs` | Pull the product specs from the website into `docs/source/_data/specs`. |
| `make clean` / `make rebuild` | Delete the build output / delete it and build again. |

Open `docs/build/html/index.html` in a browser to view a build.

### PDFs

`make pdf` renders every PDF the first time and only changed ones after that. To work on one manual, build the HTML once and render just that page:

```bash
make html
venv/bin/python tools/build_pdfs.py docs/build/html --only 'PCs/ESP32/P4/Manuals/Hardware/*'
```

| Option | What it does |
|---|---|
| `--only PATTERN` | Render only the pages matching the pattern (page paths without `.html`, `*` matches anything). |
| `--force` | Render even if nothing changed, e.g. after upgrading WeasyPrint. |
| `--keep-html` | Also write the HTML each PDF is rendered from, as `<name>.print.html`, to debug the layout in a browser. |
| `--jobs N` | PDFs rendered at a time; the number of CPU cores by default. |

The PDF layout is `docs/source/_pdf/manual.html.j2` (cover and contents) and `docs/source/_pdf/manual.css`. The cover background is `docs/source/_static/images/cover.svg`. Changing any of them, or `tools/build_pdfs.py`, renders every PDF again.

### Comparing two builds

To check that a change to the theme, an extension or many pages didn't change any content, build before and after and compare the articles page by page:

```bash
venv/bin/python tools/compare_builds.py OLD_HTML_DIR NEW_HTML_DIR
venv/bin/python tools/compare_builds.py OLD_HTML_DIR NEW_HTML_DIR --structure   # also compare the markup
```

## Product specs

Specs (the Key Features table and the spec values in the text) are maintained on the Chipsee website, not in the rst files.

1. Change the spec on the website.
2. Pull the specs, either way:
   - Run `make pull-specs`. With `CHIPSEE_API_TOKEN` set to a staff API token it also pulls unpublished products. It prints what changed, spec by spec.
   - Or run the **Pull specs** workflow on GitHub (Actions → Pull specs → Run workflow), which opens a pull request listing what changed. It pulls published products only, so a product that isn't published yet loses its specs there; pull it locally instead.
3. Review the diff of `docs/source/_data/specs/*.json` and commit it.

Don't edit the JSON files by hand: the next pull overwrites them.

In a manual page, the Key Features table is

```rst
.. spec-table::
```

and a spec value in the text is `|spec:Power Input|`. See `docs/source/_ext/specs.py` for the options.

## Manual page options

The PDF of a page is set by fields at the top of its rst file:

```rst
:pdf-title: PIM-101-C
:pdf-subtitle: PN: CS-D101
:pdf-filename: PIM-101-C
:pdf-type: displays
:pdf-revision: 1.1
```

- `:pdf-type:` is `ipc` (default), `displays` or `hmi display`; it's shown on the cover.
- `:pdf-build: False` gives the page no PDF.
- Anything with the `html-only` class is left out of the PDF.

The PDF breaks pages by itself; `:pagebreak:` has no effect.

## GitHub workflows

| Workflow | When | What it does |
|---|---|---|
| Pull Request Docs Check (`sphinx_test.yml`) | Pull requests to `main` | Builds the HTML, failing on any warning. Nothing is published. |
| Build docs and update docs-build branch (`main.yml`) | Push to `main` | Builds the HTML and changed PDFs and publishes them to the `docs-build` branch, which chipsee.com/docs pulls. A Sphinx warning or a PDF that fails to render stops the deploy, and the site stays as it was. Run it by hand with **all_pdfs** to render every PDF again. |
| Pull specs (`pull_specs.yml`) | By hand | Pulls the specs of published products and opens a pull request. |

A pull request opened by the Pull specs workflow doesn't start the Docs Check, so the workflow builds the HTML itself and says in the pull request whether it builds without warnings. A spec page is removed when no published product's `doc_url` points to it any more; its manual page then has no specs and the build fails.

## Things to watch out for

- File and folder names are case sensitive on GitHub but not on macOS. An include or image path whose case doesn't match builds fine locally and fails the pull request check.
- Images with the same file name in different folders are fine: Sphinx renames the copies.
- Keep product images under 1.5 MB.
