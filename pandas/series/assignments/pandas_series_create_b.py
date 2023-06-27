"""
* Assignment: Series Create Even
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Create `result: pd.Series` with 10 even numbers
    2. Run doctests - all must succeed

Polish:
    1. Stwórz `result: pd.Series` z 10 liczbami parzystymi
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.Series, \
    'Variable `result` has invalid type, should be `pd.Series`'

    >>> result
    0     0
    1     2
    2     4
    3     6
    4     8
    5    10
    6    12
    7    14
    8    16
    9    18
    dtype: int64
"""

import pandas as pd
import numpy as np


# type: pd.Series
result = ...

# Solution
data = np.arange(0, 20, 2)
result = pd.Series(data)


# Alternative Solution
# s = pd.Series(range(0, 20, 2))


# Alternative Solution
# s = pd.Series([x for x in range(0, 20) if x % 2 == 0])
