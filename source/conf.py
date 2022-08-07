# type: ignore
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Hello Python'
copyright = '2022, William Grigor, Brandon Wenning'
author = 'William Grigor, Brandon Wenning'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage', 'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# import guzzle_sphinx_theme

# html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'sphinx_rtd_theme'

# Register the theme as an extension to generate a sitemap.xml
# extensions.append("guzzle_sphinx_theme")

# Guzzle theme options (see theme.conf for more information)
# html_theme_options = {
    # Set the name of the project to appear in the sidebar
    # "project_nav_name": "Project Name",
# }

html_static_path = ['_static']
