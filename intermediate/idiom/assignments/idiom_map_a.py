"""
* Assignment: Idiom Map Float
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Use `map()` to apply function `float()` to DATA
    2. Define `result: map` with result
    3. Run doctests - all must succeed

Polish:
    1. Użyj `map()` aby zaaplikować funkcję `float()` do DATA
    2. Zdefiniuj `result: map` z wynikiem
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * map()
    * str.upper()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'

    >>> assert type(result) is map, \
    'Variable `result` has invalid type, should be map'

    >>> result = list(result)
    >>> assert type(result) is list, \
    'Evaluated `result` has invalid type, should be list'

    >>> assert all(type(x) is float for x in result), \
    'All rows in `result` should be float'

    >>> result
    [1.0, 2.0, 3.0]
"""

DATA = [1, 2, 3]


# Use `map()` to apply function `float()` to DATA
# type: map
result = ...

# Solution
result = map(float, DATA)
