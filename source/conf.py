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

project = 'DENT-OIP'
copyright = '2024, open-ortho.org'
author = 'Toni Magni'
master_doc = 'index'
subject = 'Dentistry - Orthodontic Imaging Profile'

try:
    # The full version, including alpha/beta/rc tags
    with open('_VERSION', 'r') as version_file:
        release = version_file.read().strip()
except FileNotFoundError:
    # I'm parsing this conf from view_maker, which will cause the above to not find the file, because this file is being parsed from a parent folder of how sphinx normally calls it. So i'm catching the FileNotFound to work around this problem.
    pass


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'docxbuilder'
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
# html_theme = 'alabaster'
# html_theme = 'classic'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for docx output -------------------------------------------------

docx_documents = [
    ('index', f'{project}.docx', {
        'title': project,
        'created': author,
        'subject': subject,
        'keywords': ['Interoperability', 'Orthodontics']
    }, True),
]
# docx_style = 'path/to/custom_style.docx'
docx_pagebreak_before_section = 2
