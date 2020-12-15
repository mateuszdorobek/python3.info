"""
* Assignment: Series Create Randint
* Filename: pandas_series_create_randint.py
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Set random seed to zero
    2. Create `result: pd.Series` with 10 random digits (`int` from `0` to `9`)

Polish:
    1. Ustaw ziarno losowości na zero
    2. Stwórz `result: pd.Series` z 10 losowymi cyframi  (`int` from `0` to `9`)

Tests:
    >>> type(result) is pd.Series
    True
    >>> result
    0    5
    1    0
    2    3
    3    3
    4    7
    5    9
    6    3
    7    5
    8    2
    9    4
    dtype: int64
"""


# Given
import numpy as np
import pandas as pd
np.random.seed(0)


result = ...


# Solution
data = np.random.randint(0, 10, size=10)
result = pd.Series(data)

