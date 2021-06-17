"""
* Assignment: Loop Comprehension Months
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Use dict comprehension and enumerate
    2. Convert `MONTH` into dict:
        a. Keys: month number
        b. Values: month name
    3. Run doctests - all must succeed

Polish:
    1. Użyj rozwinięcia słownikowego i enumeracji
    2. Przekonwertuj `MONTH` w słownik:
        a. klucz: numer miesiąca
        b. wartość: nazwa miesiąca
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'dict'>
    >>> 0 not in result
    True
    >>> 13 not in result
    True
    >>> result[1] == 'January'
    True

    >>> assert all(type(x) is int for x in result.keys())
    >>> assert all(type(x) is str for x in result.values())

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

# dict[str,str]: number and month name
result = ...

# Solution
result = {i: month for i, month in enumerate(MONTHS, start=1)}
