"""
* Assignment: Typing Annotations Literal
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Declare proper types for variables:
       a. Variable `data` with value 'users'
       b. Variable `data` with value 'staff'
       c. Variable `data` with value 'admins'
    2. Use `Literal` type
    3. Run doctests - all must succeed

Polish:
    1. Zadeklaruj zmienne z odpowiednim typem:
       a. Zmienna `data` z wartością 'users'
       b. Zmienna `data` z wartością 'staff'
       c. Zmienna `data` z wartością 'admins'
    2. Użyj typu `Literal`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    # >>> assert data == 'users', \
    # 'Do not modify variable `data` value, just add type annotation'
    # >>> assert data == 'staff', \
    # 'Do not modify variable `data` value, just add type annotation'
    >>> assert data == 'admins', \
    'Do not modify variable `data` value, just add type annotation'
"""


# add proper type annotation for following values
data: ...

data = 'users'
data = 'staff'
data = 'admins'


# Solution
from typing import Literal
data: Literal['users', 'staff', 'admins']
