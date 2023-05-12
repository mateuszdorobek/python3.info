"""
* Assignment: Pandas CaseStudy ESPN
* Complexity: medium
* Lines of code: 10 lines
* Time: 21 min

English:
    1. Create `result: pd.DataFrame` for input data
    2. Run doctests - all must succeed

Polish:
    1. Stwórz `result: pd.DataFrame` dla danych wejściowych
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Use selection with `alt` key in your IDE

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
                          Team   W   L    PCT   GB  ...    PPG OPP PPG  DIFF STRK  L10
    0       Los Angeles Lakers  11   4  0.733    -  ...  115.3   105.1  10.2   L1  8-2
    1                Utah Jazz  10   4  0.714  0.5  ...  111.1   105.1   6.0   W6  8-2
    2              LA Clippers  10   4  0.714  0.5  ...  114.9   108.6   6.3   W4  7-3
    3           Boston Celtics   8   4  0.667  1.5  ...  110.8   109.5   1.3   L1  7-3
    4          Milwaukee Bucks   9   5  0.643  1.5  ...  120.4   110.6   9.8   L1  7-3
    ..                     ...  ..  ..    ...  ...  ...    ...     ...   ...  ...  ...
    25        Sacramento Kings   5   9  0.357  5.5  ...  114.3   123.6  -9.3   L3  2-8
    26         Houston Rockets   4   8  0.333  5.5  ...  110.2   112.7  -2.5   L2  4-6
    27      Washington Wizards   3   8  0.273    6  ...  120.5   121.3  -0.8   W1  3-7
    28  Minnesota Timberwolves   3   9  0.250  6.5  ...  107.7   117.8 -10.1   L2  2-8
    29         Detroit Pistons   3  10  0.231    7  ...  108.9   113.6  -4.7   L1  3-7
    <BLANKLINE>
    [30 rows x 14 columns]
"""


import pandas as pd

DATA = 'https://python3.info/_static/espn-standing.html'
# DATA = 'https://www.espn.com/nba/standings/_/group/league'


# type: pd.DataFrame
result = ...

# Solution
tables = pd.read_html(DATA)
teams = tables[0]
scores = tables[1]

first = pd.Series(teams.columns)
teams = pd.concat((first, teams.iloc[:, 0])).reset_index(drop=True)
teams = pd.DataFrame(teams, columns=['Team'])

result = teams.join(scores)
result['Team'] = result['Team'].str.replace(r'[A-Z]+([A-Z])', r'\1', regex=True)

q = result['Team'] == 'A Clippers'
result.loc[q, 'Team'] = 'LA Clippers'
