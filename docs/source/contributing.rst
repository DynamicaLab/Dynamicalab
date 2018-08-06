How to contribute
--------------------


1. Clone the repository
=======================

Clone the `DynamicaLab <https://github.com/DynamicaUL/Dynamica-lab>`_. repository. Do your modifications in the code on a separate branch. 

We suggest the `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ style guide for Python code. Even though it won't be enforced, we suggest implementing test functions for each method. 


2. Link your packages
=======================

If your modification includes adding functions or modules, please add them into the main module. This is done by modifying the corresponding ``__init__.py`` that is found in the directory of the module.

For instance, if you add a file into the drawing module, then you should add in ``/drawing/__init__.py``:

.. code-block:: python
	
	from .new_file import *


If you plan to add a new submodule to ``DynamicaLab``, then use ``__init__.py`` located into the root directory.



3. Add documentation page
==========================

For each new function or modification, we require an up-to-date documentation. The documentation should be included into the source code. We use `Sphinx <http://sphinx.pocoo.org>`_. to automatically generate documentation, so you should use ``rst`` format. To add images, please place them in ``docs/source/_static/assets/``.

After documenting your code, you need to link the methods or modules into Sphinx generator. To do so, locate the directory ``doc/source/reference``. Then, select the appropriate ``index.rst``, and add your new method below ``.. autosummary::`` . For example:

.. code-block:: rst

	.. autosummary::
	   :toctree: generated/

	   method_1
	   method_2
	   new_method



Compile the documentation by doing:


.. code-block:: bash

	make html


You can verify the documentation by opening ``/docs/index.html``.

4. Create a new pull request
============================

When everything is tested and cleaned, create a new pull request on the ``master`` branch of the repo (See `Github instructions <https://help.github.com/articles/creating-a-pull-request/>`_). Your pull request will be reviewed. If everything goes well, your modification will be merged on the ``master`` branch.















