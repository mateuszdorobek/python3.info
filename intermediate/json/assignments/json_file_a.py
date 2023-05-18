"""
* Assignment: JSON File Dump
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Dump `result` to file `FILE` in JSON format
    2. Run doctests - all must succeed

Polish:
    1. Zrzuć `result` do pliku `FILE` w formacie JSON
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)
    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'
    >>> assert len(result) > 0, \
    'Variable `result` should not be empty'

    >>> print(result)  # doctest: +NORMALIZE_WHITESPACE
    [["sepal_length", "sepal_width", "petal_length", "petal_width", "species"],
     [5.8, 2.7, 5.1, 1.9, "virginica"],
     [5.1, 3.5, 1.4, 0.2, "setosa"],
     [5.7, 2.8, 4.1, 1.3, "versicolor"],
     [6.3, 2.9, 5.6, 1.8, "virginica"],
     [6.4, 3.2, 4.5, 1.5, "versicolor"],
     [4.7, 3.2, 1.3, 0.2, "setosa"],
     [7.0, 3.2, 4.7, 1.4, "versicolor"],
     [7.6, 3.0, 6.6, 2.1, "virginica"],
     [4.9, 3.0, 1.4, 0.2, "setosa"]]
"""

import json

FILE = '_temporary.json'

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
]

# Dump `result` to file `FILE` in JSON format

# Solution
with open(FILE, mode='w') as file:
    json.dump(DATA, file)
