"""
* Assignment: Datetime ISO List
* Complexity: medium
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: map` with parsed `DATA` dates
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: map` ze sparsowanymi datami `DATA`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `map()`
    * `datetime.fromisoformat()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'

    >>> assert type(result) is map, \
    'Variable `result` has invalid type, should be map'

    >>> result = list(result)
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, must be a list'

    >>> assert all(type(element) is datetime for element in result), \
    'All elements in `result` must be a datetime'

    >>> pprint(result, width=30)
    [datetime.datetime(1961, 4, 12, 6, 7),
     datetime.datetime(1961, 4, 12, 6, 7)]
"""

from datetime import datetime

DATA = [
    '1961-04-12 06:07',
    '1961-04-12 06:07:00',
]

# Define `result: map` with parsed `DATA` dates
# type: map
result = ...

# Solution
result = map(datetime.fromisoformat, DATA)
