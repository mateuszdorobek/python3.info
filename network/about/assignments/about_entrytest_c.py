"""
* Assignment: About EntryTest ToListTuple
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Load `DATA` from JSON format
    2. Convert data to `result: list[tuple]`
    3. Add header as a first line
    4. Run doctests - all must succeed

Polish:
    1. Wczytaj `DATA` z formatu JSON
    2. Przekonwertuj dane do `result: list[tuple]`
    3. Dodaj nagłówek jako pierwszą linię
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> result = list(result)
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert len(result) > 0, \
    'Variable `result` should not be empty'
    >>> assert all(type(row) is tuple for row in result), \
    'Variable `result` should be a list[tuple]'

    >>> pprint(result)
    [('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
     (5.8, 2.7, 5.1, 1.9, 'virginica'),
     (5.1, 3.5, 1.4, 0.2, 'setosa'),
     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
     (6.3, 2.9, 5.6, 1.8, 'virginica'),
     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
     (4.7, 3.2, 1.3, 0.2, 'setosa')]
"""

DATA = [
    {'sepal_length': 5.8, 'sepal_width': 2.7, 'petal_length': 5.1, 'petal_width': 1.9, 'species': 'virginica'},
    {'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2, 'species': 'setosa'},
    {'sepal_length': 5.7, 'sepal_width': 2.8, 'petal_length': 4.1, 'petal_width': 1.3, 'species': 'versicolor'},
    {'sepal_length': 6.3, 'sepal_width': 2.9, 'petal_length': 5.6, 'petal_width': 1.8, 'species': 'virginica'},
    {'sepal_length': 6.4, 'sepal_width': 3.2, 'petal_length': 4.5, 'petal_width': 1.5, 'species': 'versicolor'},
    {'sepal_length': 4.7, 'sepal_width': 3.2, 'petal_length': 1.3, 'petal_width': 0.2, 'species': 'setosa'},
]


# Convert DATA from list[dict] to list[tuple]
# type: header = tuple[str,...]
# type: row = tuple[float,float,float,float,str]
# type: list[tuple[header|row,...]]
result = ...

# Solution
header = tuple(DATA[0].keys())
rows = [tuple(row.values()) for row in DATA]

result = []
result.append(header)
result.extend(rows)
