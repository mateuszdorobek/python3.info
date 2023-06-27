"""
* Assignment: Numpy Create LinspaceNum
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: np.ndarray`:
       a. dtype: do not change, leave default
       b. values: from 0 to 10 steps 11
       c. use: `np.linspace()`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: np.ndarray`:
       a. dtype: nie zmieniaj, pozostaw domyślny
       b. wartości: od 0 do 10 krków 11
       c. użyj: `np.linspace()`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is np.ndarray, \
    'Variable `result` has invalid type, expected: np.ndarray'

    >>> result
    array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])
"""

import numpy as np


# dtype: do not change, leave default
# values: from 0 to 10 steps 11
# use: `np.linspace()`
# type: np.ndarray
result = ...


# Solution
result = np.linspace(0, 10, num=11)
