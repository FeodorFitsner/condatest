Welcome to SEE's Getting Started with Sphinx documentation!
===========================================================
**Getting Starting with Sphinx**

In this article, we'll be going through the basics of generating
documentation from docstrings in your Python code, checking your
documentation changes, and syncing your changes with a BitBucket
repository to automatically update ReadTheDocs.

**Step 1: Installing Sphinx**

You'll need to install *sphinx*. I found it easiest to install
using `pip <https://pypi.org/project/Sphinx/>`_.

.. code-block:: html
    :linenos:

    $ pip install sphinx


**Step 2: Setup your Project with Quickstart**

When you install the *sphinx* package, a number of command line
utilities are setup as well. One of those, 

.. code-block:: html
    :linenos:

    $ sphinx-quickstart

will generate a basic configuration file and directory
structure for your documentation.

Run this command at the base directory of your project 
(e.g. the BitBucket repo root). In my example, I have
set up a public BitBucket repo under my personal name
for development called "PublicAppVeyor". It will ask 
you a number of questions that will determine it's actions.

.. code-block:: html
    :linenos:

    Welcome to the Sphinx 2.4.4 quickstart utility.

    Please enter values for the following settings (just press Enter to
    accept a default value, if one is given in brackets).

    Selected root path: .

    You have two options for placing the build directory for Sphinx output.
    Either, you use a directory "_build" within the root path, or you separate
    "source" and "build" directories within the root path.
    > Separate source and build directories (y/n) [n]:     **y**   

    The project name will occur in several places in the built documentation.
    > Project name:     **Sphinx_Tutorial_Docs**
    > Author name(s):    **Emmie King**
    > Project release []:      **press enter to accept the default value**

    If the documents are to be written in a language other than English,
    you can select a language here by its language code. Sphinx will then
    translate text that it generates into that language.

    For a list of supported codes, see
    https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
    > Project language [en]:     **en**

    Creating file .\source\conf.py.
    Creating file .\source\index.rst.
    Creating file .\Makefile.
    Creating file .\make.bat.

    Finished: An initial directory structure has been created.

    You should now populate your master file .\source\index.rst and create other documentation
    source files. Use the Makefile to build the docs, like so:
        make builder
    where "builder" is one of the supported builders, e.g. html, latex or linkcheck.


After the program has run, you'll notice that the following
files and folders have been created in "PublicAppVeyor":

* build folder
* source folder
* make.bat
* Makefile

I decided to create a new folder with the Project Name that you added above and
to create a new folder with the base name of the Project and append _py.

* Sphinx_Tutorial_Docs [for Sphinx documentation files]
* Sphinx_Tutorial_py [for python scripts]

I then moved the 2 sphinx folders and 2 sphinx files into Sphinx_Tutorial_Docs.



.. automodule:: Sphinx_Tutorial_py.OD.main_OD
    :members:

.. automodule:: Sphinx_Tutorial_py.IOD.main_IOD
    :members:

.. automodule:: Sphinx_Tutorial_py.OutputGen.main_OutputGen
    :members:


.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
