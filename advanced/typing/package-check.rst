Typing Check
============
* ``mypy`` - the reference implementation for type checkers
* ``pyre`` - written in OCaml and optimized for performance
* ``pyright`` - a type checker that emphasizes speed
* ``pytype`` - checks and infers types for unannotated code


Python
------
* https://docs.python.org/3/howto/annotations.html
* ``inspect.get_annotations()``
* ``object.__annotations__``


MyPy
----
* Type Checking
* https://mypy-lang.org/
* https://github.com/python/mypy

.. code-block:: console

    $ pip install mypy
    $ mypy FILE

Configuration in ``pyproject.toml`` file:

.. code-block:: toml

    [tool.mypy]
    # Import discovery
    files = ["src"]
    namespace_packages = false
    explicit_package_bases = false
    ignore_missing_imports = false
    follow_imports = "normal"
    follow_imports_for_stubs = false
    no_site_packages = false
    no_silence_site_packages = false
    # Platform configuration
    python_version = "3.10"
    platform = "linux-64"
    # Disallow dynamic typing
    disallow_any_unimported = false # TODO
    disallow_any_expr = false # TODO
    disallow_any_decorated = false # TODO
    disallow_any_explicit = false # TODO
    disallow_any_generics = true
    disallow_subclassing_any = true
    # Untyped definitions and calls
    disallow_untyped_calls = true
    disallow_untyped_defs = true
    disallow_incomplete_defs = true
    check_untyped_defs = true
    disallow_untyped_decorators = true
    # None and Optional handling
    no_implicit_optional = true
    strict_optional = true
    # Configuring warnings
    warn_redundant_casts = true
    warn_unused_ignores = true
    warn_no_return = true
    warn_return_any = true
    warn_unreachable = false # GH#27396
    # Suppressing errors
    show_none_errors = true
    ignore_errors = false
    enable_error_code = "ignore-without-code"
    # Miscellaneous strictness flags
    allow_untyped_globals = false
    allow_redefinition = false
    local_partial_types = false
    implicit_reexport = true
    strict_equality = true
    # Configuring error messages
    show_error_context = false
    show_column_numbers = false
    show_error_codes = true


PyType
------
* Pytype checks and infers types for your Python code - without requiring type annotations
* https://github.com/google/pytype
* https://pypi.org/project/pytype/

.. code-block:: console

    $ pip install pytype
    $ pytype -V 3.11 myfile.py


Pyre
----
* Pyre is a performant type checker for Python compliant with PEP 484. Pyre can analyze codebases with millions of lines of code incrementally – providing instantaneous feedback to developers as they write code
* https://pyre-check.org/
* https://pypi.org/project/pyre-check/
