"""
* Assignment: Typing Annotations Literal
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Declare proper types for variables
    2. Use `Literal` type
    3. Run doctests - all must succeed

Polish:
    1. Zadeklaruj odpowiedni typ zmiennych
    2. Użyj typu `Literal`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert a == 'user', \
    'Do not modify variable `a` value, just declare type annotation'
    >>> assert b == 'staff', \
    'Do not modify variable `b` value, just declare type annotation'
    >>> assert c == 'admin', \
    'Do not modify variable `c` value, just declare type annotation'
"""

# Declare proper types for variables
# Use alias with | notation (pipe)
T = ...

# Do not modify lines below
a: T = 'user'
b: T = 'staff'
c: T = 'admin'


# Solution
from typing import Literal
T = Literal['user', 'staff', 'admin']
