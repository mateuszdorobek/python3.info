Module venv
===========
* Isolated Python environment
* Allows to have multiple versions of Python for one project
* For testing on different versions: ``python3.9``, ``python3.10``, ``python3.11``
* Test libraries and frameworks before upgrading (create venv, install requirements, run tests, delete if fails)
* Allows to have different versions of libraries and frameworks for each project
* Difference between ``venv`` and ``virtualenv``
* ``venv`` is bundled with Python since 3.3 (no installation required)
* ``virtualenv`` is independent package installed via ``pip``
* ``virtualenvwrapper`` is additionally installed command line tools


Venv vs Virtualenv
------------------
Both ``venv`` and ``virtualenv`` are used to create isolated
Python environments. Since Python 3.3, a subset of ``virtualenv``
has been integrated into the standard library under the ``venv`` module.

Both ``venv`` and ``virtualenv``:

    * Author: Bernat Gabor
    * Support: Python 3

Module ``venv``:

    * Python: version 3 only
    * Install: not required - bundled with Python since Python 3.3
    * Usage: ``python3.11 -m venv DIRECTORY``
    * Development: synchronized with Python releases
    * Features: all you need

Module ``virtualenv``:

    * Python: version 2 and 3
    * Install: ``pip install virtualenv``
    * Usage: ``virtualenv DIRECTORY``
    * Development: independent from Python releases
    * Features: all from ``venv`` plus extra (which typically you don't need)

In my opinion builtin ``venv`` is all you need. Moreover no installation
is required to use it.


Create
------
* ``.venv-py311`` is the name of venv folder
* See "Directory Naming Convention" below

.. code-block:: console

    # Go to project directory
    $ cd PROJECT

    # Create virtual environment in directory named ``.venv-py311``
    $ python3.11 -m venv .venv-py311


Run Ad-Hoc
----------
* Will run python with from virtual environment
* With all the modules already installed

.. code-block:: console

    # Go to project directory
    $ cd PROJECT

    # Run ``myscript.py`` using virtual environment
    $ venv-py311/bin/python3 myscript.py


Activate
--------
* ``bin`` for macOS, Linux, BSD
* ``Scripts`` for Windows
* Note the direction of slash and backslash (OS dependent)

macOS, Linux, BSD:

.. code-block:: console

    # Go to project directory
    $ cd PROJECT

    # Activate virtual environment
    $ source venv-py311/bin/activate

Windows:

.. code-block:: console

    # Go to project directory
    $ cd PROJECT

    # Activate virtual environment
    $ venv-py311\Scripts\activate.bat


Install Modules
---------------
Ad-hoc:

.. code-block:: console

    # Go to project directory
    $ cd PROJECT

    # Install new module
    $ venv-py311/bin/python3 -m pip install MODULE

    # Install modules listed in `requirements.txt`
    $ venv-py311/bin/python3 -m pip install -r requirements.txt

    # Upgrade modules listed in `requirements.txt`
    $ venv-py311/bin/python3 -m pip install --upgrade -r requirements.txt

    # Check installed modules
    $ venv-py311/bin/python3 -m pip freeze

Activated:

.. code-block:: console

    # Go to project directory
    $ cd PROJECT

    # Activate virtual environment
    $ source venv-py311/bin/activate

    # Install new module
    $ python3 -m pip install PACKAGE

    # Install modules listed in `requirements.txt`
    $ python3 -m pip install -r requirements.txt

    # Upgrade modules listed in `requirements.txt`
    $ python3 -m pip install --upgrade -r requirements.txt

    # Check installed modules
    $ python3 -m pip freeze


Directory Naming Convention
---------------------------
* No standard naming convention
* Naming directory like module (``venv``) name is a good idea
* Adding Python version is also a good practice
* Optionally naming per main framework/library version
* Dot at the beginning hides directory on Linux and macOS (but doesn't work on Windows)
* Underscore is Python convention for private/protected, but does not work for OS and Git

.. code-block:: text

    venv  # may be confused with `venv` Python module, mind: `sys.path`
    venv-py
    venv-py310
    venv-py311
    venv-py312a1
    venv-py312b1
    venv-py312rc1
    venv-py311-dj40
    venv-py311-dj41
    venv-py311-dj42
    venv-py311-dj50a1
    venv-py311-dj50b1
    venv-py311-dj50rc1
    venv-py311-np124-pd15
    venv-py311-np124-pd20


Good Practices
--------------
* ``python3.11 -m venv -h``
* ``python3.11 -m venv --upgrade-deps venv-py311``
* Name venv directory similar to python version ``venv-py3.11``
* Place in your project directory
* Add venv directory to ``.gitignore`` (important!)
* Change prompt by appending at the end of ``venv-3.11/bin/activate``:


Bash Prompt
-----------
* Default on most Linux distributions
* ``\e[``  – This string tells bash prompt to apply color from next character.
* ``0;32m``  – This string represents the colors. The number before the; represent typeface. And the number after the ; represent color code.
* ``\e[0m`` – This string will tell the bash prompt to apply the color to the previous character.

Typeface:

* 0 – Normal
* 1 – Bold
* 2 – Dim
* 4 – Underlined

Color codes:

* 30 – Black
* 31 – Red
* 32 – Green
* 33 – Brown
* 34 – Blue
* 35 – Purple
* 36 – Cyan
* 37 – Light gray

.. code-block:: bash

    red='\e[0;31m'
    green='\e[0;32m'
    brown='\e[0;33m'
    blue='\e[0;34m'
    purple='\e[0;35m'
    cyan='\e[0;36m'
    gray='\e[0;37m'
    white='\e[0;39m'

    project_name='My Project'
    export PS1="\n${cyan}${project_name}> ${white}"


Zsh Prompt
----------
* Default on macOS
* Colors: black, red, green, yellow, blue, magenta, cyan, white

.. code-block:: zsh

    export PROMPT='%F{cyan}project_name> %F{white}'


Further Reading
---------------
* https://github.com/pypa/virtualenv/issues/2007


Assignments
-----------
.. literalinclude:: assignments/modules_venv.py
    :caption: :download:`Solution <assignments/modules_venv.py>`
    :end-before: # Solution
