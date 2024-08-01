import os
import sys

import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath("../../"))

project = "python-sage-meta"
copyright = "2024, sageteam.org info@sageteam.org"
author = "Radin Ghahremani radin@sageteam.org Sepher Akbarzade sepher@sageteam.org"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ["_templates"]
exclude_patterns = []

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]
exclude_patterns = []


html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
