Module Distributing
===================


Installing Packages
-------------------
* ``pip search``
* ``pip install``
* ``pip install -r requirements.txt``


``__init__.py``
---------------
* Since Python 3.3 - :pep:`420` -- Implicit Namespace Packages
* https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/__init__.py
* https://github.com/django/django/blob/master/django/views/generic/__init__.py

It is true that Python 3.3+ supports Implicit Namespace Packages that allows it to create a package without an __init__.py file. This is called a namespace package in contrast to a regular package which does have an __init__.py file (empty or not empty).

However, creating a namespace package should ONLY be done if there is a need for it. For most use cases and developers out there, this doesn't apply so you should stick with EMPTY __init__.py files regardless.

Namespace package use case

To demonstrate the difference between the two types of python packages, lets look at the following example:

.. code-block:: text

    google_pubsub/              <- Package 1
        google/                 <- Namespace package (there is no __init__.py)
            cloud/              <- Namespace package (there is no __init__.py)
                pubsub/         <- Regular package (with __init__.py)
                    __init__.py <- Required to make the package a regular package
                    foo.py

    google_storage/             <- Package 2
        google/                 <- Namespace package (there is no __init__.py)
            cloud/              <- Namespace package (there is no __init__.py)
                storage/        <- Regular package (with __init__.py)
                    __init__.py <- Required to make the package a regular package
                    bar.py

google_pubsub and google_storage are separate packages but they share the same namespace google/cloud. In order to share the same namespace, it is required to make each directory of the common path a namespace package, i.e. google/ and cloud/. This should be the only use case for creating namespace packages, otherwise, there is no need for it.

It's crucial that there are no __init__py files in the google and google/cloud directories so that both directories can be interpreted as namespace packages. In Python 3.3+ any directory on the sys.path with a name that matches the package name being looked for will be recognized as contributing modules and subpackages to that package. As a result, when you import both from google_pubsub and google_storage, the Python interpreter will be able to find them.

This is different from regular packages which are self-contained meaning all parts live in the same directory hierarchy. When importing a package and the Python interpreter encounters a subdirectory on the sys.path with an __init__.py file, then it will create a single directory package containing only modules from that directory, rather than finding all appropriately named subdirectories outside that directory. This is perfectly fine for packages that don't want to share a namespace. I highly recommend taking a look at Traps for the Unwary in Python's Import System to get a better understanding of how Python importing behaves with regular and namespace package and what __init__.py traps to watch out for.

Summary:

    - Only skip __init__.py files if you want to create namespace packages. Only create namespace packages if you have different libraries that reside in different locations and you want them each to contribute a subpackage to the parent package, i.e. the namespace package.
    - Keep on adding empty __init__py to your directories because 99% of the time you just want to create regular packages. Also, Python tools out there such as mypy and pytest require empty __init__.py files to interpret the code structure accordingly. This can lead to weird errors if not done with care.

* Source: https://stackoverflow.com/a/48804718/228517

``__all__``
-----------
* https://github.com/django/django/blob/master/django/views/generic/__init__.py

.. code-block:: python

    from backend.api_v2.models.click import Click
    from backend.api_v2.models.event import Event
    from backend.api_v2.models.survey import Survey
    from backend.api_v2.models.trial import Trial


    __all__ = ['Click', 'Event', 'Survey', 'Trial']


Creating packages
-----------------

TOML
----
* PEP 518 -- Specifying Minimum Build System Requirements for Python Projects
* https://www.python.org/dev/peps/pep-0518/
* https://snarky.ca/what-the-heck-is-pyproject-toml/

.. code-block:: toml

    [build-system]
    requires = ["flit"]
    build-backend = "flit.buildapi"

    [tool.flit.metadata]
    module = "fastapi"
    author = "Sebastián Ramírez"
    author-email = "tiangolo@gmail.com"
    home-page = "https://github.com/tiangolo/fastapi"
    classifiers = [
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development",
        "Typing :: Typed",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP",
    ]
    requires = [
        "starlette ==0.14.2",
        "pydantic >=1.6.2,!=1.7,!=1.7.1,!=1.7.2,!=1.7.3,!=1.8,!=1.8.1,<2.0.0"
    ]
    description-file = "README.md"
    requires-python = ">=3.6"

    [tool.flit.metadata.urls]
    Documentation = "https://fastapi.tiangolo.com/"

    [tool.flit.metadata.requires-extra]
    test = [
        "pytest ==5.4.3",
        "pytest-cov ==2.10.0",
        "pytest-asyncio >=0.14.0,<0.15.0",
        "mypy ==0.812",
        "flake8 >=3.8.3,<4.0.0",
        "black ==20.8b1",
        "isort >=5.0.6,<6.0.0",
        "requests >=2.24.0,<3.0.0",
        "httpx >=0.14.0,<0.15.0",
        "email_validator >=1.1.1,<2.0.0",
        "sqlalchemy >=1.3.18,<1.4.0",
        "peewee >=3.13.3,<4.0.0",
        "databases[sqlite] >=0.3.2,<0.4.0",
        "orjson >=3.2.1,<4.0.0",
        "ujson >=4.0.1,<5.0.0",
        "async_exit_stack >=1.0.1,<2.0.0",
        "async_generator >=1.10,<2.0.0",
        "python-multipart >=0.0.5,<0.0.6",
        "aiofiles >=0.5.0,<0.6.0",
        "flask >=1.1.2,<2.0.0"
    ]
    doc = [
        "mkdocs >=1.1.2,<2.0.0",
        "mkdocs-material >=7.1.9,<8.0.0",
        "markdown-include >=0.6.0,<0.7.0",
        "mkdocs-markdownextradata-plugin >=0.1.7,<0.2.0",
        "typer-cli >=0.0.12,<0.0.13",
        "pyyaml >=5.3.1,<6.0.0"
    ]
    dev = [
        "python-jose[cryptography] >=3.3.0,<4.0.0",
        "passlib[bcrypt] >=1.7.2,<2.0.0",
        "autoflake >=1.3.1,<2.0.0",
        "flake8 >=3.8.3,<4.0.0",
        "uvicorn[standard] >=0.12.0,<0.14.0",
        "graphene >=2.1.8,<3.0.0"
    ]
    all = [
        "requests >=2.24.0,<3.0.0",
        "aiofiles >=0.5.0,<0.6.0",
        "jinja2 >=2.11.2,<3.0.0",
        "python-multipart >=0.0.5,<0.0.6",
        "itsdangerous >=1.1.0,<2.0.0",
        "pyyaml >=5.3.1,<6.0.0",
        "graphene >=2.1.8,<3.0.0",
        "ujson >=4.0.1,<5.0.0",
        "orjson >=3.2.1,<4.0.0",
        "email_validator >=1.1.1,<2.0.0",
        "uvicorn[standard] >=0.12.0,<0.14.0",
        "async_exit_stack >=1.0.1,<2.0.0",
        "async_generator >=1.10,<2.0.0"
    ]

    [tool.isort]
    profile = "black"
    known_third_party = ["fastapi", "pydantic", "starlette"]


``distutils``
-------------
* Provides support for building and installing additional modules into a Python.
* The new modules may be either 100%-pure Python, or may be extension modules written in C, or may be collections of Python packages which include modules coded in both Python and C.

``setuptools``
--------------
* Enhanced alternative to distutils that provides:

    #. support for declaring project dependencies
    #. additional mechanisms for configuring which files to include in source releases (including plugins for integration with version control systems)
    #. the ability to declare project "entry points", which can be used as the basis for application plugin systems
    #. the ability to automatically generate Windows command line executables at installation time rather than needing to prebuild them
    #. consistent behaviour across all supported Python versions

Setuptools is a fully-featured, actively-maintained, and stable library designed to facilitate packaging Python projects, where packaging includes:

    * Python package and module definitions
    * Distribution package metadata
    * Test hooks
    * Project installation
    * Platform-specific details
    * Python 3 support

``wheel`` vs. ``egg``
---------------------
* to build a python wheel package
* ``sdist`` will generate a ``.tar.gz`` file in ``dist/``
* ``bdist_wheel`` will generate a ``.whl`` file in ``dist/``

.. code-block:: console

    $ python setup.py sdist bdist_wheel

.. code-block:: console

    $ python setup.py sdist bdist_wheel --universal

``requirements.txt`` vs ``setup.py``
------------------------------------

``setup.py``
------------

.. code-block:: python

    from setuptools import find_packages
    from setuptools import setup
    from os import path


    assert sys.version_info >= (3, 6), "Python 3.6+ required."


    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    # Get the long description from the relevant file
    with open(path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as file:
        long_description = file.read()


    # Get the project requirements from requirements.txt file
    with open(path.join(BASE_DIR, 'requirements.txt'), encoding='utf-8') as file:
        requirements = file.read().splitlines()


    setup(
        name='HabitatOS',

        # Versions should comply with PEP440.  For a discussion on single-sourcing
        # the version across setup.py and the project code, see
        # https://packaging.python.org/en/latest/single_source_version.html
        version='0.5.0',

        description='Analog Habitat Operating System',
        long_description=long_description,

        # The project's main homepage.
        url='https://github.com/astromatt/HabitatOS',

        # Author details
        author='Matt Harasymczuk',
        author_email='dev@habitatos.space',

        # Choose your license
        license='MIT',

        # See https://pypi.python.org/pypi?:action=list_classifiers
        classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 4 - Beta',

            # Indicate who your project is intended for
            'Intended Audience :: Science/Research',
            'Topic :: Scientific/Engineering',
            'Topic :: System :: Operating System',

            # Pick your license as you wish (should match "license" above)
            'License :: OSI Approved :: MIT License',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 3.6',
        ],

        # What does your project relate to?
        keywords='space exploration analog analogue habitat operating system',

        # You can just specify the packages manually here if your project is
        # simple. Or you can use find_packages().
        packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

        # List run-time dependencies here.  These will be installed by pip when
        # your project is installed. For an analysis of "install_requires" vs pip's
        # requirements files see:
        # https://packaging.python.org/en/latest/requirements.html
        install_requires=requirements,

        # List additional groups of dependencies here (e.g. development
        # dependencies). You can install these using the following syntax,
        # for example:
        # $ pip install -e .[dev,test]
        extras_require={
            'dev': ['check-manifest'],
            'test': ['coverage', 'pep8'],
        },

        # If there are data files included in your packages that need to be
        # installed, specify them here.  If using Python 2.6 or less, then these
        # have to be included in MANIFEST.in as well.
        package_data={
            # 'sample': ['package_data.dat'],
        },

        # Although 'package_data' is the preferred approach, in some case you may
        # need to place data files outside of your packages. See:
        # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
        # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
        # data_files=[('my_data', ['data/data_file.txt'])],

        # To provide executable scripts, use entry points in preference to the
        # "scripts" keyword. Entry points provide cross-platform support and allow
        # pip to create the appropriate form of executable for the target platform.
        entry_points={
            'console_scripts': [
                'habitatOS=habitat:manage',
            ],
        },
    )

``setup.cfg``
-------------
* Configuring setup() using setup.cfg files
* A setup.py file containing a setup() function call is still required even if your configuration resides in setup.cfg.

.. code-block:: ini

    [bdist_wheel]
    universal = 1

    [metadata]
    license_file = LICENSE

    [pycodestyle]
    max-line-length = 999
    exclude = */migrations/*
    ignore = E402,W391

.. code-block:: ini

    [metadata]
    name = my_package
    version = attr: src.VERSION
    description = My package description
    long_description = file: README.rst, CHANGELOG.rst, LICENSE.rst
    keywords = one, two
    license = BSD 3-Clause License
    classifiers =
        Framework :: Django
        License :: OSI Approved :: BSD License
        Programming Language :: Python :: 3
        Programming Language :: Python :: 3.5

    [options]
    zip_safe = False
    include_package_data = True
    packages = find:
    scripts =
      bin/first.py
      bin/second.py
    install_requires =
      requests
      importlib; python_version == "2.6"

    [options.package_data]
    * = *.txt, *.rst
    hello = *.msg

    [options.extras_require]
    pdf = ReportLab>=1.2; RXP
    rest = docutils>=0.3; pack ==1.1, ==1.3

    [options.packages.find]
    exclude =
        src.subpackage1
        src.subpackage2

    [options.data_files]
    /etc/my_package =
        site.d/00_default.conf
        host.d/00_default.conf
    data = data/img/logo.png, data/svg/icon.svg

``python setup.py sdist upload``
--------------------------------
* upload is deprecated in favor of using ``twine``

``twine``
---------
.. code-block:: console

    pip install twine
    $ python setup.py sdist bdist_wheel

    # Upload with twine to Test PyPI and verify things look right.
    $ twine upload --repository-url https://test.pypi.org/legacy/ dist/*

    # Upload to PyPI
    $ twine upload dist/*

Signing packages
----------------
.. code-block:: console

    # Remove any old distributions
    $ rm -rf dist/

    # Create new tar.gz and wheel files
    # Only create a universal wheel if py2/py3 compatible and no C extensions
    $ python setup.py bdist_wheel --universal

    # Sign the distributions
    $ gpg --detach-sign -a dist/*

    # Upload to PyPI
    $ twine upload dist/*

Artifactory
-----------
* https://www.jfrog.com/confluence/display/RTF/PyPI+Repositories#PyPIRepositories-PublishingtoArtifactory

.. code-block:: console

    $ docker run --name artifactory -d -p 8081:8081 docker.bintray.io/jfrog/artifactory-oss:latest

``~/.pypirc``:

.. code-block:: ini

    [distutils]
    index-servers =
        local
        pypi

    [pypi]
    repository: https://pypi.org/pypi
    username: myusername
    password: mypassword

    [local]
    repository: http://localhost:8081/artifactory/api/pypi/pypi-local
    username: myusername
    password: mypassword

.. code-block:: console

    $ python setup.py sdist upload -r local
    $ python setup.py bdist_wheel upload -r local
    $ python setup.py sdist bdist_wheel upload -r local

Search:

.. code-block:: console

    $ pip search myapp --index http://localhost:8081/artifactory/api/pypi/pypi-local/
    myapp                   - My Simple App


Further Reading
---------------
* https://www.youtube.com/watch?v=jOiAp3wtx18
* https://www.youtube.com/watch?v=Oc9khbXBes8
