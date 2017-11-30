===================
Dlux Say Hi Program
===================

PBR ENABLED INSTALLATION

Basic say hi python program, packaged and ready to be installed.

Package Structure

.. code-block:: bash

  sayHiPackDemo
  ├── dluxsay
  │   ├── __init__.py
  │   ├── say_hi.py           <- Main python module
  │   └── tests
  │       ├── __init__.py
  │       └── test_sayhi.py   <- Unit testing file
  ├── doc
  │   ├── build               <- Renderized documentation (HTMLs)
  │   ├── Makefile            <- Executable to build the docs 'make html'
  │   └── source
  │       ├── conf.py         <- Sphinx configuration file
  │       ├── index.rst       <- Main top node
  │       ├── _static
  │       └── _templates
  ├── LICENSE
  ├── README.rst
  ├── requirements.tx         <- Package requirements
  ├── setup.cfg               <- Description of the package for PBR
  └── setup.py                <- To build, distribute, & install 'dluxsay' package VIA PBR


Installation
------------

Clone the repository

.. code-block:: bash

  $ git clone https://github.com/dlux/sayHiPackDemo.git 

Install package from src

.. code-block:: bash

  $ pip install ./sayHiPackageDemo
  # To verify instalation:
  $ pip freeze | grep dluxsay

Create an installation egg

.. code-block:: bash

  $ python ./sayHiPackageDemo/setup.py sdist

DluxSay Usage
-------------

Using installed module

.. code-block:: bash
  
  $ dluxsay
  Hi Stranger

  # With additional parameters
  $ dluxsay AnyName
  Hi AnyName

  # Other module operations
  $ dlux_say sum 20 20 10
  Sum is = 50

DluxSay package uninstall
-------------------------

Uninstall package

.. code-block:: bash

  $ pip uninstall dluxsay

Unit Testing
------------

Run unit test cases

.. code-block:: bash

  $ python -m unittest dluxsay.tests.test_sayhi
  $ python -m unittest discover

Generate and Visualize the documentation
----------------------------------------

Add RST documentation files on doc/source folder.

.. code-block:: bash

  $ python setup.py build_sphinx

  # OR
  $ sphinx-build -b html doc/source doc/build

  # OR
  $ cd doc/
  $ make html

  # OR
  $ tox -e docs

**TIP:** To visualize generated htmls 

.. code-block:: bash

  $ python -m SimpleHTTPServer 8000

Open http://localhost:8000 on a browser

Some References
---------------

Further information on setuptools
https://pythonhosted.org/setuptools/setuptools.html
Further information on pbr
https://docs.openstack.org/developer/pbr

