"""
* Assignment: Typing Basic Str
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

    >>> assert a == '', \
    'Do not modify variable `a` value, just add type annotation'
    >>> assert b == 'abc', \
    'Do not modify variable `b` value, just add type annotation'
    >>> assert c == '123', \
    'Do not modify variable `c` value, just add type annotation'
"""

# Declare proper types for variables
a: ... = ''
b: ... = 'abc'
c: ... = '123'

# Solution
a: str = ''
b: str = 'abc'
c: str = '123'
