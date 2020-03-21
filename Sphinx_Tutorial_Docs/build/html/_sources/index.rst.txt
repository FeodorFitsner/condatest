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
