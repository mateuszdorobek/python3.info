"""
* Assignment: DataFrame Groupby Phones
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Read data from `DATA` as `df: pd.DataFrame`
    2. Give information about total number of all phone calls for each calendar month
    3. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. Podaj informacje o łącznej liczbie wszystkich połączeń telefonicznych dla każdego miesiąca kalendarzowego
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.Series, \
    'Variable `result` must be a `pd.Series` type'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    year  month
    1999  10       16309.0
          11       16780.0
          12       14861.0
    2000  1        18705.0
          2        11019.0
          3        14647.0
    Name: duration, dtype: float64
"""

import pandas as pd


DATA = 'https://python3.info/_static/phones-pl.csv'


# type: pd.DataFrame
result = ...


# Solution
df = pd.read_csv(DATA, parse_dates=['datetime'])
df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
calls = df[df['item'] == 'call']
result = calls.groupby(['year', 'month'])['duration'].sum()
