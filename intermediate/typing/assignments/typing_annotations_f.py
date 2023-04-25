"""
* Assignment: Typing Annotations Final
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Declare proper types for variables:
       a. Variable `a` with value ''
       b. Variable `b` with value 'abc'
       c. Variable `c` with value '123'
    2. Run doctests - all must succeed

Polish:
    1. Zadeklaruj zmienne z odpowiednim typem:
       a. Zmienna `a` z wartością ''
       b. Zmienna `b` z wartością 'abc'
       c. Zmienna `c` z wartością '123'
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


# add proper type annotation for following values
a = ''

# add proper type annotation for following values
b = 'abc'

# add proper type annotation for following values
c = '123'


# Solution
a: str = ''
b: str = 'abc'
c: str = '123'
