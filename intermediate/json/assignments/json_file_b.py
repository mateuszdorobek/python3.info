"""
* Assignment: JSON File Dump
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Extract from input a header and rows
    2. Create `result: list[dict]`:
        a. key - name from the header
        b. value - measurement or species
    3. Dump `result` to file `FILE` in JSON format
    4. Run doctests - all must succeed

Polish:
    1. Z danych wydziel nagłówek i wiersze
    2. Wygeneruj `result: list[dict]`:
        a. klucz - nazwa z nagłówka
        b. wartość - wyniki pomiarów lub gatunek
    3. Zrzuć `result` do pliku `FILE` w formacie JSON
    4. Uruchom doctesty - wszystkie muszą się powieść

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
    [{"sepal_length": 5.8, "sepal_width": 2.7, "petal_length": 5.1, "petal_width": 1.9, "species": "virginica"},
     {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2, "species": "setosa"},
     {"sepal_length": 5.7, "sepal_width": 2.8, "petal_length": 4.1, "petal_width": 1.3, "species": "versicolor"},
     {"sepal_length": 6.3, "sepal_width": 2.9, "petal_length": 5.6, "petal_width": 1.8, "species": "virginica"},
     {"sepal_length": 6.4, "sepal_width": 3.2, "petal_length": 4.5, "petal_width": 1.5, "species": "versicolor"},
     {"sepal_length": 4.7, "sepal_width": 3.2, "petal_length": 1.3, "petal_width": 0.2, "species": "setosa"},
     {"sepal_length": 7.0, "sepal_width": 3.2, "petal_length": 4.7, "petal_width": 1.4, "species": "versicolor"},
     {"sepal_length": 7.6, "sepal_width": 3.0, "petal_length": 6.6, "petal_width": 2.1, "species": "virginica"},
     {"sepal_length": 4.9, "sepal_width": 3.0, "petal_length": 1.4, "petal_width": 0.2, "species": "setosa"}]
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

# Extract from input a header and rows
# Create `result: list[dict]`:
#  a. key - name from the header
#  b. value - measurement or species
# Dump `result` to file `FILE` in JSON format
data = ...


# Solution
header, *rows = DATA
data = [dict(zip(header, row)) for row in rows]

with open(FILE, mode='w') as file:
    json.dump(data, file)
