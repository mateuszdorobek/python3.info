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
    [('SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species'),
     (5.8, 2.7, 5.1, 1.9, 'virginica'),
     (5.1, 3.5, 1.4, 0.2, 'setosa'),
     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
     (6.3, 2.9, 5.6, 1.8, 'virginica'),
     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
     (4.7, 3.2, 1.3, 0.2, 'setosa')]
"""

DATA = [
    {'SepalLength': 5.8, 'SepalWidth': 2.7, 'PetalLength': 5.1, 'PetalWidth': 1.9, 'Species': 'virginica'},
    {'SepalLength': 5.1, 'SepalWidth': 3.5, 'PetalLength': 1.4, 'PetalWidth': 0.2, 'Species': 'setosa'},
    {'SepalLength': 5.7, 'SepalWidth': 2.8, 'PetalLength': 4.1, 'PetalWidth': 1.3, 'Species': 'versicolor'},
    {'SepalLength': 6.3, 'SepalWidth': 2.9, 'PetalLength': 5.6, 'PetalWidth': 1.8, 'Species': 'virginica'},
    {'SepalLength': 6.4, 'SepalWidth': 3.2, 'PetalLength': 4.5, 'PetalWidth': 1.5, 'Species': 'versicolor'},
    {'SepalLength': 4.7, 'SepalWidth': 3.2, 'PetalLength': 1.3, 'PetalWidth': 0.2, 'Species': 'setosa'}]


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
