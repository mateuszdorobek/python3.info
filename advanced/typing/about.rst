Typing About
============
* Also known as: "type annotations", "type hints", "gradual typing"
* Types are not required, and never will be
* Good IDE will give you hints
* Types are used extensively in system libraries
* More and more books and documentations use types
* Introduced in Python 3.5
* To type check use: ``mypy``, ``pyre-check``, ``pytypes``


Python Steering Committee
-------------------------
.. epigraph::

    Types are not required, and never will be.
    -- Guido van Rossum, Python initiator, core developer, former BDFL

.. epigraph::

    It should be emphasized that Python will remain a dynamically typed
    language, and the authors have no desire to ever make type hints
    mandatory, even by convention.
    -- Python Software Foundation

.. figure:: img/typeannotation-timeline.png

    Timeline of changes to type annotations from Python 3.0 to now [#Briggs2021]_


History
-------
* Since Python 3.5: :pep:`484` -- Type Hints
* Since Python 3.6: :pep:`526` -- Syntax for Variable Annotations
* Since Python 3.8: :pep:`544` -- Protocols: Structural subtyping (static duck typing)
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y


Typing PEPs
-----------
* https://peps.python.org/topic/typing
* PEP 482, literature overview on type hints
* PEP 483, background on type hints
* PEP 484, type hints
* PEP 526, variable annotations and ClassVar
* PEP 544, Protocol
* PEP 561, distributing typed packages
* PEP 563, from __future__ import annotations
* PEP 585, subscriptable generics in the standard library
* PEP 586, Literal
* PEP 589, TypedDict
* PEP 591, Final
* PEP 593, Annotated
* PEP 604, union syntax with |
* PEP 612, ParamSpec
* PEP 613, TypeAlias
* PEP 646, variadic generics and TypeVarTuple
* PEP 647, TypeGuard
* PEP 649 (draft), from __future__ import co_annotations
* PEP 655, Required and NotRequired
* PEP 673, Self
* PEP 675, LiteralString
* PEP 677 (rejected), (int, str) -> bool callable type syntax
* PEP 681 @dataclass_transform()
* PEP 688 Buffer
* PEP 692 Unpack[TypedDict] for **kwargs
* PEP 695 class Class[T]: type parameter syntax
* PEP 696 (draft), defaults for type variables
* PEP 698 @override
* PEP 702 (draft), @deprecated()
* PEP 705 (draft), TypedMapping


Checkers
--------
* ``mypy`` - the reference implementation for type checkers
* ``pyre`` - written in OCaml and optimized for performance
* ``pyright`` - a type checker that emphasizes speed
* ``pytype`` - checks and infers types for unannotated code


Further Reading
---------------
* More information in `cicd-tools`
* https://www.infoq.com/presentations/dynamic-static-typing/
* https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505


References
----------
.. [#Briggs2021] Briggs, J. Type Annotations in Python. Year: 2021. Retrieved: 2022-04-08. URL: https://towardsdatascience.com/type-annotations-in-python-d90990b172dc
