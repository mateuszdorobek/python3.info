"""
* Assignment: DataFrame Mapping Translate
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Read data from `DATA` as `df: pd.DataFrame`
    2. Convert Polish month names to English
    3. Parse dates to `datetime` objects
    4. Select columns ['firstname', 'lastname', 'born']
    4. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. Przekonwertuj polskie nazwy miesięcy na angielskie
    3. Sparsuj daty do obiektów `datetime`
    4. Wybierz kolumny ['firstname', 'lastname', 'born']
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `pd.Series.replace(regex=True)`
    * `pd.to_datetime()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.DataFrame, \
    'Variable `result` must be a `pd.DataFrame` type'

    >>> result[['firstname', 'lastname', 'born']]  # doctest: +NORMALIZE_WHITESPACE
      firstname   lastname       born
    0      Mark     Watney 1994-10-12
    1   Melissa      Lewis 1995-07-07
    2      Rick   Martinez 1996-01-21
    3      Alex      Vogel 1994-11-15
    4      Beth  Johanssen 2006-05-09
    5     Chris       Beck 1999-08-02
"""

import pandas as pd


DATA = 'https://python3.info/_static/martian-pl.csv'
MONTHS_PLEN = {'styczeń': 'January',
               'luty': 'February',
               'marzec': 'March',
               'kwiecień': 'April',
               'maj': 'May',
               'czerwiec': 'June',
               'lipiec': 'July',
               'sierpień': 'August',
               'wrzesień': 'September',
               'październik': 'October',
               'listopad': 'November',
               'grudzień': 'December'}

# type: pd.DataFrame
result = ...


# Solution
result = (
    pd
    .read_csv(DATA)
    .replace(MONTHS_PLEN, regex=True)
    .loc[:, ['firstname', 'lastname', 'born']]
    .apply(pd.to_datetime, errors='ignore')
)
