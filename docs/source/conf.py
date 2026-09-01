# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from pathlib import Path
import hashlib
import shutil
from urllib.parse import urljoin

from docutils.parsers.rst.directives.images import Image
from sphinx.environment import BuildEnvironment
from sphinx.util.osutil import relpath

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = "Chipsee Documentation Sample"
copyright = "2026, Chipsee"
author = "Chipsee"
version = "1.1"

# The full version, including alpha/beta/rc tags
release = "1.1"

# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# sphinx-prompt must be the first of these two.
extensions = [
    "sphinx-prompt",
    "sphinx_substitution_extensions",
    "sphinx_material",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_pdf_generate",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# Required theme setup
html_theme = "sphinx_material"
# Set the logo and favicon
html_logo = "_static/images/logo-chipsee-white.png"
html_favicon = "_static/images/favicon.webp"
# Set link name generated in the top bar.
html_title = "Chipsee"
# Public URL used for canonical links and Open Graph page URLs.
html_baseurl = "https://chipsee.com/docs/"
# Material theme options (see theme.conf for more information)
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    "nav_title": "Home",
    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    "base_url": "https://chipsee.com/docs/",
    # Set the color and the accent color
    "color_primary": "deep-orange",
    "color_accent": "deep-orange",
    # Visible levels of the global TOC; -1 means unlimited
    "globaltoc_depth": 4,
    # If False, expand all TOC entries
    "globaltoc_collapse": True,
    # If True, show hidden TOC entries
    "globaltoc_includehidden": True,
    # 'html_minify': True,
    "css_minify": True,
}
html_sidebars = {
    "**": ["localtoc.html", "searchbox.html"],
}

html_css_files = ["css/material_custom.css"]
# html_js_files = [('js/material_custom.js', {'async': 'async'},)]
file_insertion_enabled = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_extra_path = ["./index.html", "./robots.txt"]

numfig = True
numfig_secnum_depth = 1

numfig_format = {"figure": "Figure %s: "}
html_show_sphinx = False  # shows sphinx footer link
html_show_sourcelink = False  # shows link to rst file that generates page

rst_epilog = """

.. |Chipsee| replace:: Chipsee\ :sup:`®`

.. |Intel| replace:: Intel\ :sup:`®`

.. |Celeron| replace:: Celeron\ :sup:`®`

.. |Arm| replace:: Arm\ :sup:`®`

.. |Cortex| replace:: Cortex\ :sup:`®`

.. |Pi| replace:: Pi\ :sup:`®`

.. |Core| replace:: Core™

.. |br| raw:: html 

   <br>

.. _cstore: https://chipsee.com/

.. |cstore| replace:: Chipsee Store

.. |mguide| replace:: :ref:`Mount IPC Guide <MIPCG>`

.. _email: support@chipsee.com

.. |email| replace:: **support@chipsee.com**

.. |cd| replace:: cd/m\ :sup:`2`

.. |r| replace:: :sup:`®`

.. _contact: https://chipsee.com/contact/

.. |contact| replace:: **Contact us**

.. _custom_order: https://chipsee.com/custom/

.. |custom_order| replace:: customized version

"""

html_last_updated_fmt = "%b %d, %Y"
pygments_style = "perldoc"


# Sphinx-PDF-Generate configurations
pdfgen_verbose = False
pdfgen_site_url = "https://docs.chipsee.com"
# pdfgen_debug = True
# pdfgen_debug_target = "PCs/ESP32/P4/Manuals/Hardware/CS12800-ESP32P4-101A.rst"
# pdfgen_debug_target = "PCs/Pi/A72/Manuals/Hardware/CS19108RA4215-KK.rst"
pdfgen_author = "Chipsee"
pdfgen_copyright = copyright
pdfgen_disclaimer = "Content can change at anytime. It's best to refer to website for latest information."
pdfgen_cover = True
# pdfgen_cover_title = ""
# pdfgen_cover_subtitle = ""
pdfgen_custom_template_path = "cover_templates"
pdfgen_custom_css_path = "_static/css"
pdfgen_toc = True
pdfgen_toc_numbering = True
pdfgen_toc_title = "Contents"
pdfgen_toc_level = 6
pdfgen_cover_images = {"default": "_static/images/cover.png"}
pdfgen_plugin_handler_path = "custom_code.py"


class CustomImageDirective(Image):
    def run(self):
        # Get the Sphinx Build environment
        build_env: BuildEnvironment = self.state.document.settings.env
        directives_options = self.options

        if 'target' in directives_options:
            # Correct the :target: option's URI by resolving the URI
            # based on the document in which the `..image` directive was used.
            target_opt: str = directives_options['target']
            if target_opt.startswith("/") and target_opt.endswith(".html"):
                src_dir = Path(build_env.srcdir)
                base = src_dir.joinpath(build_env.docname).parent
                target_to = src_dir.joinpath(f"{target_opt.lstrip('/').removesuffix('.html')}.rst")
                resolve_relpath = relpath(
                    path=str(target_to),
                    start=str(base)
                )
                new_target = f"{resolve_relpath.removesuffix('.rst')}.html"
                directives_options["target"] = new_target

        # Call the run method of the parent (default Sphinx Image Directive) class
        image_nodes = super().run()
        return image_nodes


def _fingerprinted_name(path: Path) -> str:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()[:8]
    return f"{path.stem}.{digest}{path.suffix}"


def _fingerprinted_name_for_content(path: Path, content: str) -> str:
    digest = hashlib.sha256(content.encode("utf-8")).hexdigest()[:8]
    return f"{path.stem}.{digest}{path.suffix}"


def _replace_static_references(file_path: Path, replacements: dict[str, str]) -> None:
    text = file_path.read_text(encoding="utf-8")
    original_text = text

    for old_rel, new_rel in replacements.items():
        text = text.replace(old_rel, new_rel)

    if text != original_text:
        file_path.write_text(text, encoding="utf-8")


def fingerprint_static_assets(app, exception) -> None:
    if exception is not None or app.builder.name != "html":
        return

    static_dir = Path(app.outdir).joinpath("_static")
    if not static_dir.is_dir():
        return

    independent_assets = [
        Path("3d_models/aliases.json"),
        Path("vendor/google-fonts/fonts.css"),
        Path("images/icons/carousel-control-next.svg"),
        Path("images/icons/carousel-control-prev.svg"),
        Path("images/icons/navbar-toggler.svg"),
    ]

    replacements: dict[str, str] = {}

    for rel_path in independent_assets:
        asset_path = static_dir.joinpath(rel_path)
        if not asset_path.is_file():
            continue

        fingerprinted_name = _fingerprinted_name(asset_path)
        fingerprinted_path = asset_path.with_name(fingerprinted_name)
        shutil.copy2(asset_path, fingerprinted_path)

        replacements[rel_path.as_posix()] = rel_path.with_name(fingerprinted_name).as_posix()

    dependent_assets = [
        Path("css/material_custom.css"),
        Path("js/material_custom.js"),
        Path("js/three_d.js"),
    ]

    for rel_path in dependent_assets:
        asset_path = static_dir.joinpath(rel_path)
        if not asset_path.is_file():
            continue

        text = asset_path.read_text(encoding="utf-8")
        for old_rel, new_rel in replacements.items():
            text = text.replace(old_rel, new_rel)

        fingerprinted_name = _fingerprinted_name_for_content(asset_path, text)
        fingerprinted_path = asset_path.with_name(fingerprinted_name)
        fingerprinted_path.write_text(text, encoding="utf-8")

        replacements[rel_path.as_posix()] = rel_path.with_name(fingerprinted_name).as_posix()

    for path in Path(app.outdir).rglob("*.html"):
        _replace_static_references(path, replacements)

    for rel_path in dependent_assets:
        asset_path = static_dir.joinpath(rel_path)
        if asset_path.is_file():
            _replace_static_references(asset_path, replacements)


def add_breadcrumb_context(app, pagename, templatename, context, doctree) -> None:
    context["breadcrumb_items"] = []
    pageurl = context.get("pageurl")
    if app.builder.name != "html" or doctree is None or pagename == "index" or not pageurl:
        return

    items = [{"name": "Chipsee Documentation", "url": html_baseurl}]
    for parent in context.get("parents", []):
        if parent.get("title") and parent.get("link"):
            items.append({
                "name": parent["title"],
                "url": urljoin(pageurl, parent["link"]),
            })

    if context.get("title"):
        items.append({"name": context["title"], "url": None})
        context["breadcrumb_items"] = items


def setup(app):
    # Override the existing image directive with our custom image directive
    app.add_directive("image", CustomImageDirective)
    app.connect("html-page-context", add_breadcrumb_context)
    app.connect("build-finished", fingerprint_static_assets)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
