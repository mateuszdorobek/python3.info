"""
* Assignment: Series Arithmetic
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Set random seed to zero
    2. Generate `data: ndarray` with 5 random digits [0, 9]
    3. Create `index: list` with index names as sequential letters in english alphabet
    4. Create `s: pd.Series` from `data` and `index`
    5. Multiply `s` by 10
    6. Multiply `s` by `s`
    7. Run doctests - all must succeed

Polish:
    1. Ustaw random ziarno losowości na zero
    2. Wygeneruj `data: np.ndarray` z 5 losowymi cyframi <0, 9>
    3. Stwórz `index: list` z indeksami jak kolejne listery alfabetu angielskiego
    4. Stwórz `s: pd.Series` z `data` oraz `index`
    5. Pomnóż `s` przez 10
    6. Pomnóż `s` przez  wartości `s`
    7. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.Series, \
    'Variable `result` has invalid type, should be `pd.Series`'

    >>> result
    a    55
    b     0
    c    33
    d    33
    e    77
    dtype: int64
"""

import pandas as pd
import numpy as np
np.random.seed(0)


# type: pd.Series
result = ...


# Solution
s = pd.Series(
    data=np.random.randint(0, 10, size=5),
    index=['a', 'b', 'c', 'd', 'e'])

result = (s*10) + s
