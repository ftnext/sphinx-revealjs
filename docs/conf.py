# -*- coding: utf-8 -*-
import re
from pathlib import Path
from sphinx_revealjs import __version__

PROJ_ROOT = Path(__file__).parents[1]

# -- Project information -----------------------------------------------------
project = "sphinx-revealjs"
copyright = "2018, Kazuya Takei"
author = "Kazuya Takei"
version = __version__
release = __version__

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.todo",
]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = None

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# -- Options for HTMLHelp output ---------------------------------------------
htmlhelp_basename = "sphinx-revealjsdoc"

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {
}
latex_documents = [
    (
        master_doc,
        "sphinx-revealjs.tex",
        "sphinx-revealjs Documentation",
        "Kazuya Takei",
        "manual",
    ),
]

# -- Options for manual page output ------------------------------------------
man_pages = [
    (master_doc, "sphinx-revealjs", "sphinx-revealjs Documentation", [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------
texinfo_documents = [
    (
        master_doc,
        "sphinx-revealjs",
        "sphinx-revealjs Documentation",
        author,
        "sphinx-revealjs",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# -- Options for Epub output -------------------------------------------------
epub_title = project
epub_exclude_files = ["search.html"]

# -- Extension configuration -------------------------------------------------
# For sphinx.ext.todo
todo_include_todos = True
