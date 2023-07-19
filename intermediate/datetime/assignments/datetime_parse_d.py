"""
* Assignment: Datetime Parse Many
* Complexity: medium
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Define `result: list[datetime]` with parsed `DATA` dates
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[datetime]` ze sparsowanymi datami `DATA`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `for ... in`
    * nested `try ... except`
    * FORMATS = []
    * for fmt in FORMATS
    * helper function

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> result = list(result)
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, must be a list'
    >>> assert all(type(element) is datetime for element in result), \
    'All elements in `result` must be a datetime'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [datetime.datetime(1969, 7, 21, 0, 0),
     datetime.datetime(1969, 7, 22, 0, 0),
     datetime.datetime(1969, 7, 23, 0, 0),
     datetime.datetime(1969, 7, 24, 0, 0)]
"""

from datetime import datetime, date


DATA = [
    'July 21st, 1969',
    'July 22nd, 1969',
    'July 23rd, 1969',
    'July 24th, 1969',
]

FORMATS = [
    '%B %dst, %Y',
    '%B %dnd, %Y',
    '%B %drd, %Y',
    '%B %dth, %Y',
]


# DATA elements in datetime format
# type: list[date]
result = ...


# Solution
def parse(dt):
    for fmt in FORMATS:
        try:
            return datetime.strptime(dt, fmt)
        except ValueError:
            continue

result = map(parse, DATA)


# Alternative solution
result = map(datetime.strptime, DATA, FORMATS)
