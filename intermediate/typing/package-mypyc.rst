Typing Mypyc
============
* Mypyc compiles Python modules to C extensions.
* It uses standard Python type hints to generate fast code.
* Source: https://mypyc.readthedocs.io/en/latest/

.. figure:: img/typeannotation-mypy.png

    Mypyc algorithm [#Langa2022]_


About
-----
* Source [#MypycDocs]_

Mypyc compiles Python modules to C extensions.
It uses standard Python type hints to generate fast code.

The compiled language is a strict, gradually typed Python variant.
It restricts the use of some dynamic Python features to gain performance,
but it's mostly compatible with standard Python.

Mypyc uses mypy to perform type checking and type inference. Most type
system features in the stdlib typing module are supported.

Compiled modules can import arbitrary Python modules and third-party
libraries. You can compile anything from a single performance-critical
module to your entire codebase. You can run the modules you compile
also as normal, interpreted Python modules.

Existing code with type annotations is often 1.5x to 5x faster when compiled.
Code tuned for mypyc can be 5x to 10x faster.

Mypyc currently aims to speed up non-numeric code, such as server
applications. Mypyc is also used to compile itself (and mypy).

Mypyc advantages:

- Easy to get started
- Expressive types
- Python ecosystem
- Fast program startup
- Migration path for existing code
- Compilation is optional
- Runtime and static type safety

Mypyc vs Cython:

- No need for non-standard syntax
- First-class static typing support
- Powerful type inference
- Strict enforcement of types at runtime = easier debugging

How is mypyc fast?
- No interpreter overhead
- Type checks only at static typing boundaries
- Unboxed ints and bools (value types)
- Final attributes, and functions and classes are immutable
- Name references are resolved at compile time (no monkey patching)

Mypyc limitations:

- Classes support single inheritance
- Classes are "native classes"
- Most metaclasses are not supported
- Most class decorators are not supported
- Attributes are slotted
- No dict
- No operator overloading
- No custom descriptors

Required changes:
- Type everything, including blib2to3
- Make the types really true
- Use dataclasses instead of attrs
- Restructure code that initializes variables to None


Differences from Cython
-----------------------
* Source [#MypycDocs]_
* https://mypyc.readthedocs.io/en/latest/introduction.html#differences-from-cython
* https://mypyc.readthedocs.io/en/latest/differences_from_python.html#differences-from-python

Mypyc targets many similar use cases as Cython. Mypyc does many things
differently, however:

* No need to use non-standard syntax, such as cpdef, or extra decorators
  to get good performance. Clean, normal-looking type-annotated Python
  code can be fast without language extensions. This makes it practical
  to compile entire codebases without a developer productivity hit.

* Mypyc has first-class support for features in the typing module,
  such as tuple types, union types and generics.

* Mypyc has powerful type inference, provided by mypy. Variable type
  annotations are not needed for optimal performance.

* Mypyc fully integrates with mypy for robust and seamless static type
  checking.

* Mypyc performs strict enforcement of type annotations at runtime,
  resulting in better runtime type safety and easier debugging.

Unlike Cython, mypyc doesn't directly support interfacing with C libraries
or speeding up numeric code.


How does it work
----------------
* Source [#MypycDocs]_

Mypyc uses several techniques to produce fast code:

* Mypyc uses ahead-of-time compilation to native code. This removes CPython
  interpreter overhead.

* Mypyc enforces type annotations (and type comments) at runtime, raising
  TypeError if runtime values don't match annotations. Value types only
  need to be checked in the boundaries between dynamic and static typing.

* Compiled code uses optimized, type-specific primitives.

* Mypyc uses early binding to resolve called functions and name references
  at compile time. Mypyc avoids many dynamic namespace lookups.

* Classes are compiled to C extension classes. They use vtables for fast
  method calls and attribute access.

* Mypyc treats compiled functions, classes, and attributes declared Final
  as immutable.

* Mypyc has memory-efficient, unboxed representations for integers
  and booleans.


Development Status
------------------
Mypyc is currently alpha software. It's only recommended for production use
cases with careful testing, and if you are willing to contribute fixes
or to work around issues you will encounter.


Example
-------
* Source [#MypycDocs]_

File ``mylib.py``:

>>> def fib(n: int) -> int:
...     if n <= 1:
...         return n
...     else:
...         return fib(n-2) + fib(n-1)

File ``main.py``:

>>> # doctest: +SKIP
... from time import time
... from mylib import fib
...
...
... start = time()
... fib(32)
... stop = time()
...
... duration = round(stop-start, 4)
... print(f'Duration in seconds: {duration}')

.. code-block:: console

    $ python main.py
    Duration in seconds: 0.4125

.. code-block:: console

    $ mypyc mylib.py
    $ python main.py
    Duration in seconds: 0.0409

After compilation, the program is about 10x faster.

Mypy will generate a C extension for fib in the current working directory.
For example, on a Linux system the generated file may be called:
``fib.cpython-311m-x86_64-linux-gnu.so``

Since C extensions can't be run as programs, use ``python3 -c`` to run
the compiled module as a program or import it from the other Python file.


Automation
----------
>>> # doctest: +SKIP
... from setuptools import setup
... from mypyc.build import mypycify
...
...
... setup(
...     name='mylib',
...     packages=['mylib'],
...     ext_modules=mypycify([
...         'mylib/__init__.py',
...         'mylib/mod.py',
...     ]),
... )

.. code-block:: console

    $ python3 setup.py bdist_wheel

The wheel is created under ``dist/``.

You can include most mypy command line options in the list of arguments
passed to ``mypycify()``. For example, here we use the
``--disallow-untyped-defs`` flag to require that all functions
have type annotations

>>> # doctest: +SKIP
... from setuptools import setup
... from mypyc.build import mypycify
...
...
... setup(
...     name='frobnicate',
...     packages=['frobnicate'],
...     ext_modules=mypycify([
...         '--disallow-untyped-defs',  # Pass a mypy flag
...         'frobnicate.py',
...     ]),
... )  # doctest: +SKIP


Configuration
-------------
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


Runtime type checking
---------------------
* https://mypyc.readthedocs.io/en/latest/differences_from_python.html#differences-from-python

Non-erased types in annotations will be type checked at runtime.
For example, consider this function:

>>> def twice(x: int) -> int:
...     return x * 2

If you try to call this function with a float or str argument, you'll
get a type error on the call site, even if the call site is not being
type checked:

>>> result = twice(2)       # OK
>>> result = twice(2.0)     # TypeError
>>> result = twice('two')   # TypeError


Final values
------------
* Source [#MypycDocs]_

Compiled code replaces a reference to an attribute declared ``Final``
with the value of the attribute computed at compile time. This is
an example of early binding. Example:

SetUp:

>>> from typing import Final

Code:

>>> MAX: Final = 100
>>>
>>> def limit_to_max(x: int) -> int:
...      if x > MAX:
...          return MAX
...      return x

Change to:

>>> def limit_to_max(x: int) -> int:
...      if x > 100:
...          return 100
...      return x

The two references to ``MAX`` don't involve any module namespace lookups,
and are equivalent to the second code listing.


Recommended Workflow
--------------------
* Source [#MypycDocs]_

A simple way to use mypyc is to always compile your code after any code
changes, but this can get tedious, especially if you have a lot of code.
Instead, you can do most development in interpreted mode. This development
workflow has worked smoothly for developing mypy and mypyc (often we forget
that we aren't working on a vanilla Python project):

* During development, use interpreted mode. This gives you a fast edit-run
  cycle.

* Use type annotations liberally and use mypy to type check your code during
  development. Mypy and tests can find most errors that would break your
  compiled code, if you have good type annotation coverage. (Running mypy
  is pretty quick.)

* After you've implemented a feature or a fix, compile your project
  and run tests again, now in compiled mode. Usually nothing will break here,
  assuming your type annotation coverage is good. This can happen locally
  or in a Continuous Integration (CI) job. If you have CI, compiling locally
  may be rarely needed.

* Release or deploy a compiled version. Optionally, include a fallback
  interpreted version for platforms that mypyc doesn't support.

This mypyc workflow only involves minor tweaks to a typical Python workflow.
Most of development, testing and debugging happens in interpreted mode.
Incremental mypy runs, especially when using the mypy daemon, are very
quick (often a few hundred milliseconds).


Further Reading
---------------
* https://mypyc.readthedocs.io/en/latest/
* https://mypyc.readthedocs.io/en/latest/introduction.html#differences-from-cython
* https://mypyc.readthedocs.io/en/latest/differences_from_python.html#differences-from-python


References
----------
.. [#MypycDocs] Mypyc team. Mypyc Documentation. Year: 2022. Retrieved: 2022-11-15. URL: https://mypyc.readthedocs.io/en/latest/
.. [#Langa2022] Langa, Ł. Use typing to speed up your apps with mypyc. Year: 2022. Retrieved: 2022-11-03. URL: https://youtu.be/kFKRbo9tFNw?t=1244
