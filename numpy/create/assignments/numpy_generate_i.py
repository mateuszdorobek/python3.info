"""
* Assignment: Numpy Generate Identity
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: np.ndarray`:
       a. dtype: int
       b. values: all 0s with 1s across
       c. shape: 3 rows, 3 columns
       d. use: `np.identity()`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: np.ndarray`:
       a. dtype: int
       b. wartości: same 0 z 1-kami na skos
       c. shape: 3 wiersze, 3 kolumny
       d. użyj: `np.identity()`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is np.ndarray, \
    'Variable `result` has invalid type, expected: np.ndarray'

    >>> assert result.dtype == np.dtype('int')
    >>> assert result.itemsize == 8
    >>> assert result.shape == (3, 3)
    >>> assert result.strides == (24, 8)

    >>> result
    array([[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]])
"""

import numpy as np


# dtype: int
# values: all 0s with 1s across
# shape: 3 rows, 3 columns
# use: `np.identity()`
# type: np.ndarray
result = ...


# Solution
result = np.identity(3, dtype='int')
