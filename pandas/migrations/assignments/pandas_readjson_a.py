"""
* Assignment: Pandas Read JSON
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Read data from `DATA` as `result: pd.DataFrame`
    2. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z DATA jako result: pd.DataFrame
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.DataFrame, \
    'Variable `result` must be a `pd.DataFrame` type'

    >>> result.loc[[0,10,20]]
        sepalLength  sepalWidth  petalLength  petalWidth     species
    0           5.1         3.5          1.4         0.2      setosa
    10          7.0         3.2          4.7         1.4  versicolor
    20          6.3         3.3          6.0         2.5   virginica
"""

import pandas as pd


DATA = 'https://python3.info/_static/iris.json'


# Read DATA from JSON
# type: pd.DataFrame
result = ...

# Solution
result = pd.read_json(DATA)
