# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

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
copyright = "2021, Chipsee"
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
html_title = "Home"
# Material theme options (see theme.conf for more information)
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    "nav_title": "Home",
    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    "base_url": "https://docs.chipsee.com",
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
html_sidebars = {"**": ["globaltoc.html", "localtoc.html", "searchbox.html"]}

html_css_files = ["css/material_custom.css"]
# html_js_files = [('js/material_custom.js', {'async': 'async'},)]
file_insertion_enabled = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_extra_path = ["./index.html", "./index.php"]

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

.. |cstore| replace:: **Chipsee Store**

.. |mguide| replace:: :ref:`Mount IPC Guide <MIPCG>`

.. _email: service@chipsee.com

.. |email| replace:: **service@chipsee.com**

.. |cd| replace:: cd/m\ :sup:`2`

.. |r| replace:: :sup:`®`

.. _contact: https://chipsee.com/contact/

.. |contact| replace:: **Contact us**

.. _custom_order: https://chipsee.com/custom/

.. |custom_order| replace:: customized version

"""

html_last_updated_fmt = "%b %d, %Y"

# tablecaption = 'below'
pygments_style = "sphinx"

# Sphinx-PDF-Generate configurations
pdfgen_verbose = False
pdfgen_site_url = "https://docs.chipsee.com"
pdfgen_debug = True
pdfgen_debug_target = "PCs/ARM/AM335X/Manuals/Hardware/CS10600T070.rst"
pdfgen_author = "Chipsee"
pdfgen_author_logo = "_static/images/logo_header.png"
pdfgen_copyright = copyright
pdfgen_disclaimer = "Disclaimer: Content can change at anytime and best to refer to website for latest information."
pdfgen_cover = True
# pdfgen_cover_title = ""
# pdfgen_cover_subtitle = ""
pdfgen_custom_template_path = "cover_templates"
pdfgen_custom_css_path = "_static/css"
pdfgen_toc = True
pdfgen_toc_numbering = True
pdfgen_toc_title = "Contents"
pdfgen_toc_level = 6
pdfgen_cover_images = {
    "default": "_static/images/cover.jpg"
}
pdfgen_plugin_handler_path = "custom_code.py"
