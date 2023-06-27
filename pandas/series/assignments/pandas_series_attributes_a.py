"""
* Assignment: Pandas Series Attributes
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define `result: dict` with:
        a. number of dimensions;
        b. number of elements;
        c. data type;
        e. shape.
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: dict` z:
        a. liczbę wymiarów,
        b. liczbę elementów,
        c. typ danych,
        e. kształt.
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert all(type(x) is not Ellipsis for x in result.values()), \
    'Assign result to dict values in `result`'
    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be `dict`'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'number of dimensions': 1,
     'number of elements': 3,
     'data type': dtype('O'),
     'shape': (3,)}
"""

import pandas as pd

DATA = pd.Series(['a', 'b', 'c'])

# type: dict[str, int|dtype|tuple]
result = {
    'number of dimensions': ...,
    'number of elements': ...,
    'data type': ...,
    'shape': ...,
}


# Solution
result = {
    'number of dimensions': DATA.ndim,
    'number of elements': DATA.size,
    'data type': DATA.dtype,
    'shape': DATA.shape,
}
