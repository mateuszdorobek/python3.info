"""
* Assignment: Numpy Create ArrayDtype
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: np.ndarray`:
       a. dtype: float
       b. values: from 0 to 10 (without 10)
       c. use: `np.array()`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: np.ndarray`:
       a. dtype: float
       b. wartości: od 0 do 10 (bez 10)
       c. użyj: `np.array()`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is np.ndarray, \
    'Variable `result` has invalid type, expected: np.ndarray'

    >>> result
    array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])
"""

import numpy as np


# dtype: float
# values: from 0 to 10 (without 10)
# use: `np.array()`
# type: np.ndarray
result = ...


# Solution
result = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype='float')
