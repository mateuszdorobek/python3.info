"""
* Assignment: Function Parameters Echo
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define function `echo` with two parameters
    2. Parameter `a` is required
    3. Parameter `b` is required
    4. Return `a` and `b` as a `tuple`
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `echo` z dwoma parametrami
    2. Parametr `a` jest wymagany
    3. Parametr `b` jest wymagany
    4. zwróć `a` i `b` jako `tuple`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert echo is not Ellipsis, \
    'Write solution inside `echo` function'
    >>> assert isfunction(echo), \
    'Object `echo` must be a function'

    >>> echo(1, 2)
    (1, 2)
    >>> echo(3, 4)
    (3, 4)
"""


# Solution
def echo(a, b):
    return a, b
