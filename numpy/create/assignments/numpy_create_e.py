"""
* Assignment: Numpy Create ArangeDtype
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: np.ndarray`:
       a. dtype: float
       b. values: from 0 to 10 step 2 (even numbers)
       c. use: `np.arange()`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: np.ndarray`:
       a. dtype: float
       b. wartości: od 0 do 10 krok 2 (liczby parzyste)
       c. użyj: `np.arange()`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is np.ndarray, \
    'Variable `result` has invalid type, expected: np.ndarray'

    >>> result
    array([0., 2., 4., 6., 8.])
"""

import numpy as np


# dtype: float
# values: from 0 to 10 step 2 (even numbers)
# use: `np.arange()`
# type: np.ndarray
result = ...


# Solution
result = np.arange(0, 10, step=2, dtype='float')
