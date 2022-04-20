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
import os
import sys

sys.path.insert(0, os.path.abspath("../plugins/dtdoc"))
sys.path.insert(0, os.path.abspath("../.."))


# -- Project information -----------------------------------------------------

project = "Analog Devices, Inc. Prototyping Platform"
copyright = "2022, Systems Development Group"
author = "Systems Development Group"

# The full version, including alpha/beta/rc tags
release = "2021.1"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # Our custom extension, only meant for Furo's own documentation.
    "furo.sphinxext",
    # External stuff
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_inline_tabs",
    "sphinx_panels",
    "dtdoc",
    "sphinx_substitution_extensions",
    "sphinx_click",
]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    # "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    # "strikethrough",
    "substitution",
    "tasklist",
]


d = os.path.dirname(__file__)
s = os.path.split(d)
s = os.path.split(s[0])
s = os.path.join(s[0], "linux", "Documentation/devicetree/bindings")
dt_bindings_include_path = s

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"
# html_theme = "sphinx_book_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = [
    "sdg_logo.css",
]

# Shared variables
myst_substitutions = {
    "release_version": "master",
    "release_version_bold": "master",
    "vivado_version": "2021.1",
    "quartus_version": "21.2.0",
    "linux_branch": "master",
    "no_os_branch": "master",
}
rst_prolog = "".join(
    f".. |{key}| replace:: {value}\n" for key, value in myst_substitutions.items()
)
