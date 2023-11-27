"""
* Assignment: Function Parameters Default
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define function `default` with two parameters
    2. Parameter `a` is required
    3. Parameter `b` is optional and has default value `None`
    4. If only one argument was passed, consider second equal to the first one
    5. Return `a` and `b` as a `dict`, i.e. {'a': 1, 'b': 1}
    6. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `default` z dwoma parametrami
    2. Parametr `a` jest wymagany
    3. Parametr `b` jest opcjonalny i ma domyślną wartość `None`
    4. Jeżeli tylko jeden argument był podany, przyjmij drugi równy pierwszemu
    5. Zwróć `a` i `b` jako `dict`, np. {'a': 1, 'b': 1}
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert default is not Ellipsis, \
    'Write solution inside `default` function'
    >>> assert isfunction(default), \
    'Object `default` must be a function'

    >>> default(1)
    {'a': 1, 'b': 1}
    >>> default(2, 3)
    {'a': 2, 'b': 3}
"""


# Solution
def default(a, b=None):
    if b is None:
        b = a
    return {'a': a, 'b': b}
