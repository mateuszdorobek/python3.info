"""
* Assignment: Typing Annotations Any
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Declare proper types for variables
    2. Use `Any` type
    3. Run doctests - all must succeed

Polish:
    1. Zadeklaruj odpowiedni typ zmiennych
    2. Użyj typu `Any`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    # >>> assert data == 1, \
    # 'Do not modify variable `a` value, just add type annotation'
    # >>> assert data == 1.0, \
    # 'Do not modify variable `b` value, just add type annotation'
    >>> assert data == 'one', \
    'Do not modify variable `data` value, just add type annotation'
"""

# Declare proper types for variables
# Use alias with | notation (pipe)
T = ...

# Do not modify lines below
data: T = 1
data: T = 1.0
data: T = 'one'

# Solution
from typing import Any

T = Any
