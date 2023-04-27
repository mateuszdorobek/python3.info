"""
* Assignment: Idiom Enumerate ZeroPadded
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Use dict comprehension and enumerate
    2. Convert `MONTH` into `result: dict[str,str]`:
        a. Keys: month number
        b. Values: month name
    3. Month number must be two letter string
       (zero padded) - `f'{number:02}'`
    4. Run doctests - all must succeed

Polish:
    1. Użyj rozwinięcia słownikowego i enumeracji
    2. Przekonwertuj `MONTH` w `result: dict[str,str]`:
        a. klucz: numer miesiąca
        b. wartość: nazwa miesiąca
    3. Numer miesiąca ma być dwuznakowym stringiem
       (wypełnij zerem) - `f'{number:02}'`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `enumerate()`
    * `f'{number:02}'`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'dict'>
    >>> '00' not in result
    True
    >>> '13' not in result
    True
    >>> result['01'] == 'January'
    True

    >>> assert all(type(x) is str for x in result.keys())
    >>> assert all(type(x) is str for x in result.values())
    >>> assert all(len(x) == 2 for x in result.keys())

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'01': 'January',
     '02': 'February',
     '03': 'March',
     '04': 'April',
     '05': 'May',
     '06': 'June',
     '07': 'July',
     '08': 'August',
     '09': 'September',
     '10': 'October',
     '11': 'November',
     '12': 'December'}
"""

MONTHS = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']

# With zero-padded number and month name
# type: dict[str,str]
result = ...

# Solution
result = {f'{number:02}': month
          for number, month in enumerate(MONTHS, start=1)}
