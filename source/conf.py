#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Config file for Sphinx."""

import os

extensions = [
    # 'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
]

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = 'Guia Tkinter'
copyright = '2015, Alvarez Alejandro'
author = 'Alvarez Alejandro'

version = '0.1'

release = '0.1.1'

language = 'es'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']

html_search_language = 'es'

# Options for LaTeX output

latex_elements = {

}

latex_documents = [
  (master_doc, 'GuiaTkinter.tex', 'Guia Tkinter Documentation',
   'Alvarez Alejandro', 'manual'),
]

intersphinx_mapping = {'https://docs.python.org/': None}

rst_epilog = """
.. |copyright| replace:: %s
.. |contact_email| replace:: eliluminado@codigopython.com.ar
.. |repository| replace:: https://github.com/eliluminado/tutorial_tkinter
.. |bugtracker_url| replace:: https://github.com/eliluminado/tutorial_tkinter/issues
""" % (copyright)
