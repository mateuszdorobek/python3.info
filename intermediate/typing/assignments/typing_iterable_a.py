"""
* Assignment: Typing Annotations Tuple
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Declare proper types for variables:
       a. Variable `a` with value ()
       b. Variable `b` with value (1, 2, 3)
       c. Variable `c` with value (1, 2.0, 'three')
    2. Run doctests - all must succeed

Polish:
    1. Zadeklaruj zmienne z odpowiednim typem:
       a. Zmienna `a` z wartością ()
       b. Zmienna `b` z wartością (1, 2, 3)
       c. Zmienna `c` z wartością (1, 2.0, 'three')
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert a == (), \
    'Do not modify variable `a` value, just add type annotation'
    >>> assert b == (1, 2, 3), \
    'Do not modify variable `b` value, just add type annotation'
    >>> assert c == (1, 2.0, 'three'), \
    'Do not modify variable `c` value, just add type annotation'
"""


# add proper type annotation for following values
a = ()

# add proper type annotation for following values
b = (1, 2, 3)

# add proper type annotation for following values
c = (1, 2.0, 'three')


# Solution
a: tuple = ()
b: tuple[int,...] = (1, 2, 3)
c: tuple[int,float,str] = (1, 2.0, 'three')
