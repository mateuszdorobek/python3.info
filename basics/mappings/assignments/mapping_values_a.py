"""
* Assignment: Mapping Values List
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: list[str]` with list of `DATA` values
    4. Run doctests - all must succeed

Polish:
    2. Zdefiniuj `result: list[str]` z listą wartości z `DATA`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `list()`
    * `dict.values()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is float for x in result), \
    'All elements in `result` should be float'

    >>> result
    [5.8, 2.7, 5.1, 1.9]
"""

DATA = {'sepal_length': 5.8,
        'sepal_width': 2.7,
        'petal_length': 5.1,
        'petal_width': 1.9}

# String with values from DATA
# type: list[float]
result = ...

# Solution
result = list(DATA.values())
