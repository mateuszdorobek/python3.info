"""
* Assignment: Function Return Expression
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define function `result`
    2. Function should return sum of `1` and `2`
    3. Define `result` with result of function call
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `result`
    2. Funkcja powinna zwracać sumę `1` i `2`
    3. Zdefiniuj `result` z wynikiem wywołania funkcji
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert result is not Ellipsis, \
    'Write solution inside `result` function'
    >>> assert isfunction(result), \
    'Object `result` must be a function'

    >>> result()
    3
"""


# Solution
def result():
    return 1 + 2
