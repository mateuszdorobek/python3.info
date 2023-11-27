"""
* Assignment: Idiom Map Apply
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Use `map()` to apply function `str.upper()` to DATA
    2. Do not define own function
    3. Define `result: map` with result
    4. Run doctests - all must succeed

Polish:
    1. Użyj `map()` aby zaaplikować funkcję `str.upper()` do DATA
    2. Nie definiuj własnej funkcji
    3. Zdefiniuj `result: map` z wynikiem
    4. Uruchom doctesty - wszystkie muszą się powieść

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

    >>> assert all(type(x) is str for x in result), \
    'All rows in `result` should be str'

    >>> result
    ['A', 'B', 'C']
"""

DATA = ['a', 'b', 'c']

# Use `map()` to apply function `str.upper()` to DATA
# type: map
result = ...

# Solution
result = map(str.upper, DATA)
