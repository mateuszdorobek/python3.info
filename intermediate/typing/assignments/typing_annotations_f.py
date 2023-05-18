"""
* Assignment: Typing Annotations Final
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Declare proper types for variables:
       a. Variable `a` with value 1
       b. Variable `b` with value 1.0
       c. Variable `c` with value 'one'
    2. Use `Final` type with proper subtype
    2. Run doctests - all must succeed

Polish:
    1. Zadeklaruj zmienne z odpowiednim typem:
       a. Zmienna `a` z wartością 1
       b. Zmienna `b` z wartością 1.0
       c. Zmienna `c` z wartością 'one'
    2. Użyj typu `Final` z odpowiednim subtypem
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert a == 1, \
    'Do not modify variable `a` value, just add type annotation'
    >>> assert b == 1.0, \
    'Do not modify variable `b` value, just add type annotation'
    >>> assert c == 'one', \
    'Do not modify variable `c` value, just add type annotation'
"""


# add proper type annotation for following values
a = 1

# add proper type annotation for following values
b = 1.0

# add proper type annotation for following values
c = 'one'


# Solution
from typing import Final
a: Final[int] = 1
b: Final[float] = 1.0
c: Final[str] = 'one'
