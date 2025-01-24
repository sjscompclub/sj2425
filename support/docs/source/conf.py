# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "St. Joseph's Computer Club Support Page"
copyright = '2024, THAPA Damar'
author = 'THAPA Damar'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.intersphinx', 'sphinx_favicon' ]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_nefertiti'
#html_static_path = ['_static']
#html_static_path = ['assets/images']
html_theme_options = {
  #  "sans_serif_font": "Mulish",
  #  "monospace_font": "Ubuntu Mono",
    "monospace_font_size": "1.1rem",
  #  "project_name_font": "Montserrat",
   # "documentation_font": "Open Sans",
    "documentation_font_size": "1.1rem",
  #  "doc_headers_font": "Georgia",
    "style": "green",
    "pygments_dark_style": "solarized-dark",
}



favicons = [
    {"href": "assets/images/favicon.ico"},  # => use `_static/icon.svg`
]


# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/style.css',
]
