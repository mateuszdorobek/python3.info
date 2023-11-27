"""
* Assignment: Loop For Months
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Convert `MONTH` into `result: dict[int,str]`:
        a. Keys: month number
        b. Values: month name
    2. Do not use `enumerate`
    3. Run doctests - all must succeed

Polish:
    1. Przekonwertuj `MONTH` w `result: dict[int,str]`:
        a. klucz: numer miesiąca
        b. wartość: nazwa miesiąca
    2. Nie używaj `enumerate`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'

    >>> assert all(type(x) is int for x in result.keys())
    >>> assert all(type(x) is str for x in result.values())
    >>> assert all(x in result.keys() for x in range(1, 13))
    >>> assert all(x in result.values() for x in MONTHS)

    >>> 13 not in result
    True
    >>> 0 not in result
    True

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {1: 'January',
     2: 'February',
     3: 'March',
     4: 'April',
     5: 'May',
     6: 'June',
     7: 'July',
     8: 'August',
     9: 'September',
     10: 'October',
     11: 'November',
     12: 'December'}
"""

MONTHS = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']

# Dict with month number and name. Start with 1
# type: dict[int,str]
result = ...

# Solution
result = {}
i = 1

for month in MONTHS:
    result[i] = month
    i += 1
