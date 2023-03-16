Type Annotation Primitives
==========================


Alias
-----
* Used to make types more readable

Declaration:

>>> data = int | float

Example:

>>> number = int | float
>>>
>>> age: number = 10      # ok
>>> age: number = 10.5    # ok
>>> age: number = None    # error


Union
-----
* Used to inform static type checker that the variable should either X or Y
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y
* ``int | str == str | int``

Declaration:

>>> data: int | float

>>> data: int | float = 1337
>>> data: int | float = 1.337

Example:

>>> data: int | float
>>>
>>> data = 1337     # ok
>>> data = 1.337    # ok
>>> data = 'hello'  # error

Result of this expression would then be valid in ``isinstance()``
and ``issubclass()``:

>>> isinstance(1337, int|float)
True


Optional
--------
* Used to inform static type checker that the variable should be X or None
* ``int | None == None | int``

Declaration:

>>> data: int | None

>>> data: int | None = 1337
>>> data: int | None = None

Example:

>>> number: int | None
>>>
>>> number = 1337    # ok
>>> number = None    # ok
>>> number = 1.0     # error

Result of this expression would then be valid in ``isinstance()``
and ``issubclass()``:

>>> isinstance(1337, int|None)
True


Final
-----
* Used to inform static type checker the value should not change
* Used to define constants
* Since Python 3.8: :pep:`591` -- Adding a final qualifier to typing

In Python there is not such thing as constants. All values can be changed
during the runtime. However using ``Final`` we can achieve similar effect.
Static type checker will ensure that the value should not change during
the program.

SetUp:

>>> from typing import Final

Declaration:

>>> data: Final
>>> data: Final[int]
>>> data: Final[float]
>>> data: Final[bool]
>>> data: Final[str]

Definition:

>>> pressure: Final[float] = 1013.25    # ok
>>> pressure = 1024.00                  # error


Literal
-------
* Since Python 3.8: :pep:`586` -- Literal Types
* Literal de-duplicates parameters
* Equality comparisons of Literal objects are not order dependent
* https://docs.python.org/3/library/typing.html#typing.Literal

SetUp:

>>> from typing import Literal

Declaration:

>>> data: Literal['one', 'two', 'three']

Problem:

>>> agency: str
>>>
>>> agency = 'NASA'         # ok
>>> agency = 'ESA'          # ok
>>> agency = 'Not existing' # ok

Solution:

>>> agency: Literal['NASA', 'ESA', 'POLSA']
>>>
>>> agency = 'NASA'          # ok
>>> agency = 'ESA'           # ok
>>> agency = 'Not existing'  # error


Any
---
SetUp:

>>> from typing import Any

Declaration:

>>> x: Any = 1
>>> x: Any = 'one'
>>> x: Any = None
>>> x: Any = [1,2,3]


Use Case - 0x01
---------------
>>> firstname: str = 'Mark'
>>> lastname: str = 'Watney'
>>> age: int | float = 40
>>> adult: bool = True
>>> agency: Literal['NASA', 'ESA', 'POLSA'] = 'NASA'
>>> job: str | None = None
>>> height: int | float | None = 185
>>> weight: int | float | None = None


Use Case - 0x02
---------------
>>> SECOND: Final[int] = 1
>>> MINUTE: Final[int] = 60 * SECOND
>>> HOUR: Final[int] = 60 * MINUTE
>>> DAY: Final[int] = 24 * HOUR


Further Reading
---------------
* More information in `cicd-tools`
* https://www.infoq.com/presentations/dynamic-static-typing/
* https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505


References
----------
.. [#Briggs2021] Briggs, J. Type Annotations in Python. Year: 2021. Retrieved: 2022-04-08. URL: https://towardsdatascience.com/type-annotations-in-python-d90990b172dc
