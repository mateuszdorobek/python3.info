"""
* Assignment: Typing Annotations Any
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Declare proper types for variables:
       a. Variable `data` with value 1
       b. Variable `data` with value 1.0
       c. Variable `data` with value 'one'
    2. Use `Any` type
    2. Run doctests - all must succeed

Polish:
    1. Zadeklaruj zmienne z odpowiednim typem:
       a. Zmienna `data` z wartością 1
       b. Zmienna `data` z wartością 1.0
       c. Zmienna `data` z wartością 'one'
    2. Użyj typu `Any`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    # >>> assert data == 1, \
    # 'Do not modify variable `a` value, just add type annotation'
    # >>> assert data == 1.0, \
    # 'Do not modify variable `b` value, just add type annotation'
    >>> assert data == 'one', \
    'Do not modify variable `data` value, just add type annotation'
"""


# add proper type annotation for following values
data: ...

data = 1
data = 1.0
data = 'one'


# Solution
from typing import Any
data: Any
