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
import sphinx_material

# -- Project information -----------------------------------------------------

project = 'Chipsee Documentation Sample'
copyright = '2021, Chipsee'
author = 'Randy'
version = '1.1'

# The full version, including alpha/beta/rc tags
release = '1.1'

# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# sphinx-prompt must be the first of these two.
extensions = ['sphinx-prompt', 'sphinx_substitution_extensions']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# Required theme setup
html_theme = 'sphinx_material'
# Set the logo and favicon
html_logo = 'logo-chipsee-white.png'
html_favicon = 'favicon.webp'
# Set link name generated in the top bar.
html_title = 'Chipsee'
# Material theme options (see theme.conf for more information)
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    'nav_title': 'Home',
    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://docs.chipsee.com',
    # Set the color and the accent color
    'color_primary': 'deep-orange',
    'color_accent': 'deep-orange',
    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 3,
    # If False, expand all TOC entries
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': True,
    'html_minify': True,
    'css_minify': True,
    'theme_color': '2D445E'
}
html_sidebars = {
    "**": ["globaltoc.html", "localtoc.html", "searchbox.html"]
}

html_style = 'css/material_custom.css'
file_insertion_enabled = True
# html_js_files = ['js/expand_tabs.js']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_extra_path = ['./index.php']

numfig = True
numfig_secnum_depth = 1

numfig_format = {'figure': 'Figure %s: ',
                 'table': 'Table %s: ',
                 'code-block': 'Codes %s: ',
                 }
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

html_last_updated_fmt = '%b %d, %Y'

# tablecaption = 'below'
pygments_style = "sphinx"

# PDF output
latex_engine = 'pdflatex'
latex_logo = './Media/Chipsee_Logo_Full.png'

# Sphinx internationalization details
# language = "zh_CN"
# locale_dirs = ['locale/']   # path is example but recommended.
# gettext_compact = False     # optional
