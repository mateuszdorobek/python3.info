"""
* Assignment: DataFrame Groupby Astro Flights
* Complexity: medium
* Lines of code: 5 lines
* Time: 13 min

English:
    1. Read data from `DATA`
    2. Create ranking of the most experienced astronauts (number of flights)
    3. Drop duplicates
    4. Reset index
    5. Define `result: pd.Dataframe` with top 10
    6. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA`
    2. Stwórz ranking najbardziej doświadczonych astronautów (liczba lotów)
    3. Usuń duplikaty
    4. Zresetuj indeks
    5. Zdefiniuj `result: pd.Dataframe` z top 10
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.DataFrame, \
    'Variable `result` must be a `pd.DataFrame` type'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
                           name  total_number_of_missions
    0   Chang-Diaz, Franklin R.                         7
    1            Ross, Jerry L.                         7
    2       Wetherbee, James D.                         6
    3  Musgrave, Franklin Story                         6
    4          Krikalev, Sergei                         6
    5         Malenchenko, Yuri                         6
    6     Brown, Curtis L., Jr.                         6
    7         Foale, C. Michael                         6
    8            Young, John W.                         6
    9         Gibson, Robert L.                         5
"""

import pandas as pd

DATA = 'https://python3.info/_static/astro-selection.csv'

# type: pd.DataFrame
result = ...


# Solution
result = (pd
    .read_csv(DATA)
    .loc[:,['name','total_number_of_missions']]
    .sort_values('total_number_of_missions', ascending=False)
    .drop_duplicates()
    .reset_index(drop=True)
    .head(10)
)
