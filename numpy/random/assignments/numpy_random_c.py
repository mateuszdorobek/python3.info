"""
* Assignment: Numpy Random Choice
* Complexity: medium
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Set random seed to zero
    2. Define `result: np.ndarray` with 6 random numbers
       without repetition from `DATA`
    3. Run doctests - all must succeed

Polish:
    1. Ustaw ziarno losowości na zero
    2. Zdefiniuj `result: np.ndarray` z 6 losowymi
       liczbami bez powtórzeń z `DATA`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is np.ndarray, \
    'Variable `result` has invalid type, expected: np.ndarray'

    >>> result
    array([30,  5, 27, 31, 33, 38])
"""

import numpy as np
np.random.seed(0)

DATA = np.arange(1, 50)
result = ...


# Solution
result = np.random.choice(DATA, size=6, replace=False)
