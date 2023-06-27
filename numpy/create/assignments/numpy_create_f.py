"""
* Assignment: Numpy Create Linspace
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: np.ndarray`:
       a. dtype: do not change, leave default
       a. values: from 0 to 10 (without 10)
       b. use: `np.linspace()`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: np.ndarray`:
       a. dtype: nie zmieniaj, pozostaw domyślny
       a. wartości: od 0 do 10 (bez 10)
       b. użyj: `np.linspace()`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is np.ndarray, \
    'Variable `result` has invalid type, expected: np.ndarray'

    >>> result
    array([ 0.        ,  0.20408163,  0.40816327,  0.6122449 ,  0.81632653,
            1.02040816,  1.2244898 ,  1.42857143,  1.63265306,  1.83673469,
            2.04081633,  2.24489796,  2.44897959,  2.65306122,  2.85714286,
            3.06122449,  3.26530612,  3.46938776,  3.67346939,  3.87755102,
            4.08163265,  4.28571429,  4.48979592,  4.69387755,  4.89795918,
            5.10204082,  5.30612245,  5.51020408,  5.71428571,  5.91836735,
            6.12244898,  6.32653061,  6.53061224,  6.73469388,  6.93877551,
            7.14285714,  7.34693878,  7.55102041,  7.75510204,  7.95918367,
            8.16326531,  8.36734694,  8.57142857,  8.7755102 ,  8.97959184,
            9.18367347,  9.3877551 ,  9.59183673,  9.79591837, 10.        ])
"""

import numpy as np


# dtype: do not change, leave default
# values: from 0 to 10 (without 10)
# use: `np.linspace()`
# type: np.ndarray
result = ...


# Solution
result = np.linspace(0, 10)
