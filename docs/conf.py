import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Spliit Client'
copyright = '2024, Abhinav'
author = 'Abhinav'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_logo = '_static/logo.png'
html_theme_options = {
    'logo_only': True,
    'display_version': True,
}
html_static_path = ['_static'] 