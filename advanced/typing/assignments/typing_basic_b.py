"""
* Assignment: Typing Basic Float
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Declare proper types for variables
    2. Run doctests - all must succeed

Polish:
    1. Zadeklaruj odpowiedni typ zmiennych
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert a == 1.0, \
    'Do not modify variable `a` value, just add type annotation'
    >>> assert b == 0.0, \
    'Do not modify variable `b` value, just add type annotation'
    >>> assert c == -1.0, \
    'Do not modify variable `c` value, just add type annotation'
"""

# Declare proper types for variables
a: ... = 1.0
b: ... = 0.0
c: ... = -1.0


# Solution
a: float = 1.0
b: float = 0.0
c: float = -1.0
