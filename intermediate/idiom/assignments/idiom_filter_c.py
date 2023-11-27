"""
* Assignment: Idiom Filter Apply
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Filter-out non-numeric (int or float) values from `DATA`
    2. Define `result: filter` with result
    3. Run doctests - all must succeed

Polish:
    1. Odfiltruj nie numeryczne (int lub float) wartości z `DATA`
    2. Zdefiniuj `result: filter` z wynikiem
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * filter()
    * isinstance()
    * type()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'

    >>> assert type(result) is filter, \
    'Variable `result` has invalid type, should be filter'

    >>> result = list(result)
    >>> assert type(result) is list, \
    'Evaluated `result` has invalid type, should be list'

    >>> assert all(type(x) in (int,float) for x in result), \
    'All rows in `result` should be str'

    >>> result
    [0, 2.0, 4, 5.0]
"""

DATA = [0, True, 2.0, 'three', 4, 5.0, ['six']]

# Filter-out non-numeric (int or float) values from `DATA`
# type: filter
result = ...

# Solution
def is_numeric(x):
    return type(x) in (int,float)


result = filter(is_numeric, DATA)
