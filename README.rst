Say Hi Program
=====================

Basic say hi python program, packaged and ready to be installed.

Package Structure

.. code-block:: bash

  sayHiPackDemo
  ├── demo
  │   ├── __init__.py
  │   ├── cmd
  │   │   ├── __init__.py
  │   │   ├── say_hi.py       <- Main python module
  │   └── tests
  │       ├── __init__.py
  │       └── test_sayhi.py   <- Unit testing file
  ├── README.rst
  ├── requirements.txt        <- Package requirements
  ├── setup.py                <- To build, distribute, & install 'dluxsay' package
  └── test_requirements.txt

============
Installation
============

Clone the repository

.. code-block:: bash

  $ git clone https://github.com/dlux/sayHiPackDemo.git 

Install package from src

.. code-block:: bash

  $ pip install -e ./sayHiPackageDemo
  # To verify instalation:
  $ pip list | grep dluxsay

Using installed module

.. code-block:: bash
  
  $ dluxsay
  Hi Stranger

  # With additional parameters
  $ dluxsay AnyName
  Hi AnyName

  # Other module operations
  $ dlux_say a_sum 20 20 10
  Sum is = 50

Uninstall package

.. code-block:: bash

  $ pip uninstall dluxsay

Create an installation egg

.. code-block:: bash

  $ python ./sayHiPackageDemo/setup.py sdist


Further information on setuptools 
https://pythonhosted.org/setuptools/setuptools.html


