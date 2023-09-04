import os
import sys

import django

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath(".."))
sys.path.append(os.path.abspath("../tests"))
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

django.setup()

# -- General configuration ---------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "django-import-export-extensions"
copyright = "2022-2023, Saritasa"
author = "Saritasa"


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
try:
    from import_export_extensions import __version__

    # The short X.Y version.
    version = ".".join(__version__.split(".")[:2])
    # The full version, including alpha/beta/rc tags.
    release = __version__
except ImportError:
    version = release = "dev"


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "django-import-export-extensions"


# -- Options for LaTeX output ------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "django-import-export-extensions.tex",
        "django-import-export-extensions Documentation",
        author,
        "manual",
    ),
]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        "django-import-export-extensions",
        "django-import-export-extensions Documentation",
        [author],
        1,
    ),
]


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "django-import-export-extensions",
        "django-import-export-extensions Documentation",
        author,
        "django-import-export-extensions",
        "Utils for import/export data for Django",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
texinfo_appendices = []

# intersphinx documentation
intersphinx_mapping = {
    "tablib": ("https://tablib.readthedocs.io/en/stable/", None),
    "django-import-export": ("https://django-import-export.readthedocs.io/en/latest/", None),
}
