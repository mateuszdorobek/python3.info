"""
* Assignment: Datetime Parse List
* Complexity: medium
* Lines of code: 8 lines
* Time: 3 min

English:
    1. Define `result: list[datetime]` with parsed `DATA` dates
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[datetime]` ze sparsowanymi datami `DATA`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `for ... in`
    * `try ... except`
    * ``dt.strptime()``
    * ``list.append()``

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> result = list(result)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, must be a list'
    >>> assert all(type(element) is datetime for element in result), \
    'All elements in `result` must be a datetime'

    >>> pprint(result, width=30)
    [datetime.datetime(1969, 7, 21, 0, 0),
     datetime.datetime(1969, 7, 22, 0, 0)]
"""

from datetime import date, datetime


DATA = [
    'July 21st, 1969',
    'July 22nd, 1969',
]

# parsed DATA
# type: list[date]
result = ...


# Solution
def parse(string):
    try:
        return datetime.strptime(string, '%B %dst, %Y')
    except ValueError:
        return datetime.strptime(string, '%B %dnd, %Y')

result = map(parse, DATA)


# Alternative
result = []

for line in DATA:
    try:
        dt = datetime.strptime(line, '%B %dst, %Y')
    except ValueError:
        dt = datetime.strptime(line, '%B %dnd, %Y')
    result.append(dt)
