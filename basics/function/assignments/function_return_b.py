"""
* Assignment: Function Return Tuple
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define function `result`
    2. Function should return a tuple: 'hello', 'world'
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `result`
    2. Funkcja powinna zwracać krotkę: 'hello', 'world'
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert result is not Ellipsis, \
    'Write solution inside `result` function'
    >>> assert isfunction(result), \
    'Object `result` must be a function'

    >>> result()
    ('hello', 'world')
"""


# Solution
def result():
    return 'hello', 'world'
