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
#import os
#import sys
#sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'QGIS Quickguide'
copyright = '2021, Karen Soenen'
author = 'Karen Soenen'

# The full version, including alpha/beta/rc tags
release = 'September 13, 2021'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['myst_parser', 'rinoh.frontend.sphinx']
#myst_enable_extensions = ["html_image"]


source_suffix = {'.md': 'markdown','.rst': 'restructuredtext'}
source_encoding = 'utf-8-sig'
master_doc = 'index'
 

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []
 
# -- Options for Latex output -----------------------------------------------------------
# -- From: https://www.sphinx-doc.org/en/1.0/config.html#options-for-latex-output -------
# https://sphinxguide.readthedocs.io/en/latest/sphinx_basics/settings.html

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto, manual, or own class]).
rinoh_documents = [dict(doc='index', target='manual')]
latex_documents = [(master_doc, 'QGIS.tex', 'Hands-on QGIS Quickguide for Cruise Planning','Karen Soenen', 'manual')]
latex_engine = 'pdflatex'


 
# -- Options for LaTeX output ------------------------------------------------
 
latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',
 
# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',
 
# Additional stuff for the LaTeX preamble.
'preamble': '''
\\hypersetup{unicode=true}
\\usepackage{CJKutf8}
\\AtBeginDocument{\\begin{CJK}{UTF8}{gbsn}}
\\AtEndDocument{\\end{CJK}}
''',
}



# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']