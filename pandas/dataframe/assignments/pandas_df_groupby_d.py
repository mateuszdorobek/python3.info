"""
* Assignment: DataFrame Groupby Astro EVA
* Complexity: medium
* Lines of code: 13 lines
* Time: 21 min

English:
    1. Read data from `DATA` as `df: pd.DataFrame`
    2. Create ranking of astronauts with the most time spent on EVA (ExtraVehicular Activity)
    3. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. Stwórz ranking astronautów z największym czasem EVA (Spacerów kosmicznych)
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Note, that file delimiter is semicolon ";" (not comma)
    * Parse CSV and replace newlines inside fields with `","`
    * Split names into separate columns for each spacewalker (first, second, third)
    * Split names into separate rows for each spacewalker (use ffill)
    * Split times into separate columns (hours, minutes)

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
                                 Duration
    Astronaut
    Anatoliy Solovyov     3 days 06:48:00
    Michael Lopez-Alegria 2 days 19:40:00
    Peggy Whitson         2 days 12:21:00
    Fyodor Yurchikhin     2 days 11:29:00
    Jerry Ross            2 days 10:38:00
    ...                               ...
    Aleksei Yeliseyev     0 days 00:53:00
    Edward White          0 days 00:46:00
    Alfred Worden         0 days 00:39:00
    Alexi Leonov          0 days 00:23:00
    Zhai Zhi-gang         0 days 00:14:00
    <BLANKLINE>
    [226 rows x 1 columns]
"""

import pandas as pd


DATA = 'https://python3.info/_static/astro-eva.csv'

# type: pd.DataFrame
result = ...


# Solution
df = pd.read_csv(DATA, delimiter=';')
df[['EV1', 'EV2', 'EV3']] = df['Participants'].str.split(', ', expand=True)
df['Duration'] = pd.to_timedelta(df['Duration'])

result = (pd.concat([
           df[['EV1', 'Duration']].rename(columns={'EV1': 'Astronaut'}),
           df[['EV2', 'Duration']].rename(columns={'EV2': 'Astronaut'}),
           df[['EV3', 'Duration']].rename(columns={'EV3': 'Astronaut'})
       ], axis='rows')
       .groupby('Astronaut')
       .sum()
       .sort_values('Duration', ascending=False))
