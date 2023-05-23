"""
* Assignment: Typing Annotations Final
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Declare proper types for variables
    2. Use `Final` type with proper subtype
    3. Run doctests - all must succeed

Polish:
    1. Zadeklaruj odpowiedni typ zmiennych
    2. Użyj typu `Final` z odpowiednim subtypem
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert a == 1, \
    'Do not modify variable `a` value, just add type annotation'
    >>> assert b == 1.0, \
    'Do not modify variable `b` value, just add type annotation'
    >>> assert c == 'one', \
    'Do not modify variable `c` value, just add type annotation'
"""

# Declare proper types for variables
# Use `Final` type with proper subtype
T1 = ...
T2 = ...
T3 = ...

# Do not modify lines below
a: T1 = 1
b: T2 = 1.0
c: T3 = 'one'

# Solution
from typing import Final
T1 = Final[int]
T2 = Final[float]
T3 = Final[str]
