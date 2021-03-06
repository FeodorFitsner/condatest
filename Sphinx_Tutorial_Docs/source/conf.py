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
# You will need to indicate in the conf.py file that Sphinx must go “up” 
# one directory level to find the Python package.
sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('C:\\projects\\publicappveyor\\Sphinx_Tutorial_Docs'))
sys.path.insert(0, os.path.abspath('C:\\projects\\publicappveyor\\Sphinx_Tutorial_Docs\\build\\html'))
sys.path.insert(0, os.path.abspath('C:\\projects\\publicappveyor\\Sphinx_Tutorial_py'))
sys.path.insert(0, os.path.abspath('C:\\Users\\emmie\\OneDrive\\FDS\\publicappveyor\\Sphinx_Tutorial_Docs'))


# -- Project information -----------------------------------------------------

project = 'Sphinx_Tutorial'
copyright = '2020, Space Exploration Engineering'
author = 'Emmie King'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage', 'sphinx.ext.napoleon', 'sphinx.ext.intersphinx']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'classic'
html_logo = '_static/logo-see-with-tagline.png'
html_theme_options = {
    "rightsidebar": "false",
    "relbarbgcolor": "black",
    "sidebarbgcolor": 'grey',
    "body_max_width": "none"
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

#html_additional_pages = {
#    'RepoSetup': '../build/html/BitBucketSetup.html',
#    'CISetup': '../AppVeyorSetup.html',
#    'OD': '../OD_members.html',
#    'IOD': '../IOD_members.html',
#    'OPGen': '../OutputGen_members.html',
#}