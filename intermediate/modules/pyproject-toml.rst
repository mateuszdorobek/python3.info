Modules pyproject.toml
======================
* https://packaging.python.org/en/latest/tutorials/packaging-projects/
* https://peps.python.org/pep-0517/
* https://peps.python.org/pep-0518/
* https://peps.python.org/pep-0621/
* https://peps.python.org/pep-0639/#add-license-files-key
* https://peps.python.org/pep-0660/
* https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html

Modern Python packages can contain a pyproject.toml file, first introduced
in PEP 518 and later expanded in PEP 517, PEP 621 and PEP 660. This file
contains build system requirements and information, which are used by pip
to build the package. [#pyproject]_


Metadata
--------
There are two kinds of metadata: static and dynamic. Static metadata is
specified in the pyproject.toml file directly and cannot be specified or
changed by a tool. Dynamic metadata is listed via the dynamic key (defined
later in this specification) and represents metadata that a tool will later
provide [#packageMetadata]_.

The keys defined in this specification MUST be in a table named ``[project]``
in ``pyproject.toml``. No tools may add keys to this table which are not
defined by this specification. For tools wishing to store their own settings
in ``pyproject.toml``, they may use the ``[tool]`` table as defined in the
build dependency declaration specification. The lack of a ``[project]`` table
implicitly means the build back-end will dynamically provide all keys.

.. csv-table:: Project Metadata [#packaging]_
    :header: "Configuration", "Description"
    :widths: 20, 80

    "name",              "is the distribution name of your package. This can be any name as long as it only contains letters, numbers, ., _ , and -. It also must not already be taken on PyPI. Be sure to update this with your username for this tutorial, as this ensures you won't try to upload a package with the same name as one which already exists."
    "version",           "is the package version. See the version specifier specification for more details on versions. Some build backends allow it to be specified another way, such as from a file or a git tag."
    "authors",           "is used to identify the author of the package; you specify a name and an email for each author. You can also list maintainers in the same format."
    "description",       "is a short, one-sentence summary of the package."
    "readme",            "is a path to a file containing a detailed description of the package. This is shown on the package detail page on PyPI. In this case, the description is loaded from README.md (which is a common pattern). There also is a more advanced table form described in the project metadata specification."
    "requires-python",   "gives the versions of Python supported by your project. Installers like pip will look back through older versions of packages until it finds one that has a matching Python version."
    "classifiers",       "gives the index and pip some additional metadata about your package. In this case, the package is only compatible with Python 3, is licensed under the MIT license, and is OS-independent. You should always include at least which version(s) of Python your package works on, which license your package is available under, and which operating systems your package will work on. For a complete list of classifiers, see https://pypi.org/classifiers/."
    "urls",              "lets you list any number of extra links to show on PyPI. Generally this could be to the source, documentation, issue trackers, etc."

More information in here [#packageMetadata]_


Example
-------
.. code-block:: toml

    # https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#specification
    [project]
    name = "myproject"
    version = "1.0.0"
    requires-python = ">=3.11"
    readme = "README.md"
    authors = [{name = "Mark Watney", email = "mwatney@nasa.gov"}]

    # License
    # https://peps.python.org/pep-0639/#add-license-files-key
    # https://peps.python.org/pep-0639/#mapping-license-classifiers-to-spdx-identifiers
    # https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#license
    license = {file = "LICENSE"}

    keywords = [
        "ares",
        "mars",
        "nasa",
        "human-spaceflight"]

    # Each project's maintainers provide PyPI with a list of
    # "Trove classifiers" to categorize each release, describing who it's for,
    # what systems it can run on, and how mature it is.
    # https://peps.python.org/pep-0301/#distutils-trove-classification
    # https://pypi.org/classifiers/
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 4.1",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: English",
        "Natural Language :: Polish",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"]

    ## Dependencies
    # https://peps.python.org/pep-0440/#version-specifiers

    dependencies = [
        "django == 4.1.*",
        "django-ninja == 0.19.*"]

    [project.optional-dependencies]
    test = [
        "autopep8",
        "coverage",
        "flake8",
        "mccabe",
        "mypy",
        "pycodestyle",
        "pydocstyle",
        "pyflakes",
        "pylint",
        "rope",
        "whatthepatch"
        "yapf",
    ]


    urls.homepage = "https://github.com/myusername/myproject"
    urls.repository = "https://github.com/myusername/myproject.git"
    urls.documentation = "https://github.com/myusername/myproject"
    urls.changelog = "https://github.com/myusername/myproject/releases"
    urls.bugtracker = "https://github.com/myusername/myproject/issues"

    ## Console scripts
    # https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#entry-points
    #
    # Builder will install a shell script named `myapp-cli` in venv's
    # bin directory: `.venv/bin/myapp-cli`

    [project.scripts]
    myproject-cli = "myproject.manage:main"

    [project.gui-scripts]
    myproject-gui = "myproject.manage:gui"

    # An "entry point" is typically a function (or other callable
    # function-like object) that a developer or user of your Python
    # package might want to use. The most popular kind of entry point
    # is the console_scripts entry point, which points to a function
    # that you want made available as a command-line tool to whoever
    # installs your package.
    [project.entry-points.console_scripts]
    myproject-run = "myproject.manage:main"


    ## Build System

    [build-system]
    requires = ['setuptools >= 65.6']
    build-backend = 'setuptools.build_meta'

    [tool.setuptools]
    license-files = ["LICENSE"]

    [tool.setuptools_scm]
    write_to = "src/__version__.py"
    write_to_template = "__version__ = \"{version}\"\n"  # VERSION_INFO is populated in __main__

    [tool.setuptools.packages.find]
    where = ["src"]
    exclude = ["myproject.*.tests*"]

    [tool.setuptools.dynamic]
    # version.attr = "myproject.__version__"  ## if 'version' in dynamic


    ## External Tools Configuration

    # https://ichard26-testblackdocs.readthedocs.io/en/refactor_docs/pyproject_toml.html
    [tool.black]
    line-length = 79
    target_version = ["py311"]
    include = '\.pyi?$'
    exclude = [
        '*.egg-info',
        ".git",
        ".mypy_cache",
        ".venv",
        "build",
        "dist",
    ]

    # https://coverage.readthedocs.io/en/latest/config.html#run
    [tool.coverage.run]
    concurrency = ["multiprocessing", "thread"]
    include = ["src", "tests"]
    omit = ["contrib"]

    # https://mypy.readthedocs.io/en/stable/config_file.html
    # https://mypy.readthedocs.io/en/stable/config_file.html#using-a-pyproject-toml-file
    [tool.mypy]
    python_version = "3.11"
    files = ["src"]
    modules = ["myproject"]
    exclude = [
        '*.egg-info',
        ".git",
        ".mypy_cache",
        "build",
        "dist"]
    warn_return_any = true
    warn_unused_configs = true
    # namespace_packages = false
    # explicit_package_bases = false
    # ignore_missing_imports = false
    # follow_imports = "normal"
    # follow_imports_for_stubs = false
    # no_site_packages = false
    # no_silence_site_packages = false
    # # Platform configuration
    # platform = "linux-64"
    # # Disallow dynamic typing
    # disallow_any_unimported = false # TODO
    # disallow_any_expr = false # TODO
    # disallow_any_decorated = false # TODO
    # disallow_any_explicit = false # TODO
    # disallow_any_generics = true
    # disallow_subclassing_any = true
    # # Untyped definitions and calls
    # disallow_untyped_calls = true
    # disallow_untyped_defs = true
    # disallow_incomplete_defs = true
    # check_untyped_defs = true
    # disallow_untyped_decorators = true
    # # None and Optional handling
    # no_implicit_optional = true
    # strict_optional = true
    # # Configuring warnings
    # warn_redundant_casts = true
    # warn_unused_ignores = true
    # warn_no_return = true
    # warn_return_any = true
    # warn_unreachable = false # GH#27396
    # # Suppressing errors
    # show_none_errors = true
    # ignore_errors = false
    # enable_error_code = "ignore-without-code"
    # # Miscellaneous strictness flags
    # allow_untyped_globals = false
    # allow_redefinition = false
    # local_partial_types = false
    # implicit_reexport = true
    # strict_equality = true
    # # Configuring error messages
    # show_error_context = false
    # show_column_numbers = false
    # show_error_codes = true

    # https://pycqa.github.io/isort/docs/configuration/options.html
    [tool.isort]
    atomic = true                           # Ensures the output doesn't save if the resulting file contains syntax errors
    combine_as_imports = false              # Combines as imports on the same line
    combine_star = true                     # Ensures that if a star import is present, nothing else is imported from that namespace
    ensure_newline_before_comments = true   # Inserts a blank line before a comment following an import
    force_alphabetical_sort = false         # Force all imports to be sorted as a single section
    force_alphabetical_sort_within_sections = true  # Force all imports to be sorted alphabetically within a section
    force_sort_within_sections = true       # Don't sort straight-style imports (like import sys) before from-style imports (like from itertools import groupby). Instead, sort the imports by module, independent of import style
    group_by_package = false                # If True isort will automatically create section groups by the top-level package they come from
    honor_noqa = true                       # Tells isort to honor noqa comments to enforce skipping those comments
    include_trailing_comma = true           # Includes a trailing comma on multi line imports that include parentheses
    lexicographical = false                 # Lexicographical order is strictly alphabetical order. For example by default isort will sort 1, 10, 2 into 1, 2, 10 - but with lexicographical sorting enabled it will remain 1, 10, 2
    line_length = 79                        # The max length of an import line (used for wrapping long imports)
    lines_after_imports = 2                 # The number of blank lines to place after imports
    lines_between_sections = -1             # The number of lines to place between sections
    lines_between_types = 0                 # The number of lines to place between direct and from imports
    multi_line_output = 9                   # Multi line output (0-grid, 1-vertical, 2-hanging, 3-vert-hanging, 4-vert-grid, 5-vert-grid-grouped, 6-deprecated-alias-for-5, 7-noqa, 8-vertical-hanging-indent-bracket, 9-vertical-prefix-from-module-import, 10-hanging-indent-with-parentheses)
    order_by_type = true                    # Order imports by type, which is determined by case, in addition to alphabetically
    profile = "black"                       # Base profile type to use for configuration. Profiles include: black, django, pycharm, google, open_stack, plone, attrs, hug, wemake, appnexus
    py_version=3                            # Tells isort to set the known standard library based on the specified Python version
    remove_redundant_aliases = true         # Tells isort to remove redundant aliases from imports, such as `import os as os`
    skip = [".gitignore", ".dockerignore"]  # Files that isort should skip over
    skip_gitignore = true                   # Treat project as a git repository and ignore files listed in .gitignore
    skip_glob = ["docs/*"]                  # Files that isort should skip over
    skip_glob = ["tests/*"]                 # Files that isort should skip over
    src_paths = ["src", "tests"]            # Add an explicitly defined source path (modules within src paths have their imports automatically categorized as first_party). Glob expansion (* and **) is supported for this option


    # https://github.com/pytest-dev/pytest/blob/main/pyproject.toml
    [tool.pytest.ini_options]
    testpaths = ["tests"]
    addopts = "--strict-config --strict-markers --doctest-modules"
    doctest_optionflags = "NORMALIZE_WHITESPACE ELLIPSIS"
    python_files = ["test_*.py", "*_test.py", "test/*.py", "tests/*.py"]


    # pylint --generate-toml-config >> pyproject.toml
    [tool.pylint]
    max-line-length = 79
    ignore = [".git"]
    good-names = ["i", "j", "k", "x", "Run", "_"]
    design.max-args = 5                     # Maximum number of arguments for function / method.
    design.max-attributes = 7               # Maximum number of attributes for a class (see R0902).
    design.max-bool-expr = 5                # Maximum number of boolean expressions in an if statement (see R0916).
    design.max-branches = 12                # Maximum number of branch for function / method body.
    design.max-locals = 15                  # Maximum number of locals for function / method body.
    design.max-parents = 7                  # Maximum number of parents for a class (see R0901).
    design.max-public-methods = 20          # Maximum number of public methods for a class (see R0904).
    design.max-returns = 6                  # Maximum number of return / yield for function / method body.
    design.max-statements = 50              # Maximum number of statements in function / method body.
    design.min-public-methods = 2           # Minimum number of public methods for a class (see R0903).
    format.ignore-long-lines = "^(\\s*(# )?<?https?://\\S+>?$|.*models.))"  # Regexp for a line that is allowed to be longer than the limit.
    format.max-line-length = 79             # Maximum number of characters on a single line.
    format.max-module-lines = 1000          # Maximum number of lines in a module.
    logging.logging-format-style = "new"    # The type of string formatting that logging methods do. `old` means using % formatting, `new` is for `{}` formatting.
    logging.logging-modules = ["logging"]   # Logging modules to check that the string format arguments are in logging function parameter format.
    refactoring.max-nested-blocks = 5       # Maximum number of nested blocks for function / method body
    reports.output-format = "parseable"     # Set the output format. Available formats are text, parseable, colorized, json, and msvs (visual studio)
    reports.reports = true                  # Tells whether to display a full report or only the messages.
    reports.score = true                    # Activate the evaluation score.
    similarities.min-similarity-lines = 4   # Minimum lines number of a similarity.
    disable = [
        "missing-module-docstring",         # "C0114"
        "missing-class-docstring",          # "C0115"
        "missing-function-docstring",       # "C0116"
        "too-few-public-methods",           # "R0903"
        "too-many-arguments",               # "R0913"
    ]


Verify
------
* To verify use: ``pip install .``

.. code-block:: console

    $ pip install .


Build
-----
.. code-block:: console

    $ python3 -m pip install --upgrade build
    $ python3 -m build

Result:

.. code-block:: text

    dist/
    ├── example_package_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
    └── example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz


Upload
------
The first thing you'll need to do is register an account on TestPyPI, which
is a separate instance of the package index intended for testing and
experimentation. It's great for things like this tutorial where we don't
necessarily want to upload to the real index. To register an account, go
to https://test.pypi.org/account/register/ and complete the steps on that
page. You will also need to verify your email address before you're able
to upload any packages. For more details, see Using TestPyPI [#pypiUpload]_.

To securely upload your project, you'll need a PyPI API token.
Create one at https://test.pypi.org/manage/account/#api-tokens,
setting the "Scope" to "Entire account". Don't close the page until
you have copied and saved the token — you won't see that token again
[#pypiUpload]_.

Now that you are registered, you can use twine to upload the distribution
packages [#pypiUpload]_.

You will be prompted for a username and password. For the username,
use ``__token__``. For the password, use the token value, including
the ``pypi-`` prefix [#pypiUpload]_.

.. code-block:: console

    $ python3 -m pip install --upgrade twine
    $ python3 -m twine upload --repository testpypi dist/*
    Uploading distributions to https://test.pypi.org/legacy/
    Enter your username: __token__
    Uploading myproject-1.0.0-py3-none-any.whl
    100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 kB • 00:01 • ?
    Uploading myproject-1.0.0.tar.gz
    100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.8/6.8 kB • 00:00 • ?

Once uploaded, your package should be viewable on TestPyPI;
for example: https://test.pypi.org/project/myproject


Install
-------
.. code-block:: console

    $ python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps myproject
    Collecting myproject
      Downloading https://test-files.pythonhosted.org/packages/.../myproject_1.0.0-py3-none-any.whl
    Installing collected packages: myproject
    Successfully installed myproject-1.0.0

This example uses ``--index-url`` flag to specify TestPyPI instead of live
PyPI. Additionally, it specifies ``--no-deps``. Since TestPyPI doesn't have
the same packages as the live PyPI, it's possible that attempting to install
dependencies may fail or install something unexpected. While our example
package doesn't have any dependencies, it's a good practice to avoid
installing dependencies when using TestPyPI [#pypiUpload]_.


Usage
-----
>>> from myproject import mymodule  # doctest: +SKIP
>>> mymodule.run()  # doctest: +SKIP


Further Reading
---------------
* https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#example


References
----------
.. [#pyproject] Pip developers. "pyproject.toml". Year: 2022. Retrieved: 2022-12-01. URL: https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/
.. [#packaging] Python Packaging Authority (PyPA). Packaging Python Projects. Year: 2023. Retrieved: 2023-01-29. URL: https://packaging.python.org/en/latest/tutorials/packaging-projects/#configuring-metadata
.. [#packageMetadata] Python Packaging Authority (PyPA). Declaring project metadata. Year: 2023. Retrieved: 2023-01-29. URL: https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata
.. [#pypiUpload] Python Packaging Authority (PyPA). Packaging Python Projects. Uploading the distribution archives. https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives
