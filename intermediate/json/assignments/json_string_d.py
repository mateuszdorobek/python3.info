"""
* Assignment: JSON String LoadList
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Load `DATA` from JSON format
    2. Convert data to `result: list[dict]`
    3. Do not add header as a first line
    4. Run doctests - all must succeed

Polish:
    1. Wczytaj `DATA` z formatu JSON
    2. Przekonwertuj dane do `result: list[dict]`
    3. Nie dodawaj nagłówka jako pierwsza linia
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert len(result) > 0, \
    'Variable `result` should not be empty'
    >>> assert all(type(row) is dict for row in result), \
    'Variable `result` should be a list[dict]'

    >>> result[0]  # doctest: +NORMALIZE_WHITESPACE
    {'sepal_length': 5.8,
     'sepal_width': 2.7,
     'petal_length': 5.1,
     'petal_width': 1.9,
     'species': 'virginica'}

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'sepal_length': 5.8, 'sepal_width': 2.7, 'petal_length': 5.1, 'petal_width': 1.9, 'species': 'virginica'},
     {'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2, 'species': 'setosa'},
     {'sepal_length': 5.7, 'sepal_width': 2.8, 'petal_length': 4.1, 'petal_width': 1.3, 'species': 'versicolor'},
     {'sepal_length': 6.3, 'sepal_width': 2.9, 'petal_length': 5.6, 'petal_width': 1.8, 'species': 'virginica'},
     {'sepal_length': 6.4, 'sepal_width': 3.2, 'petal_length': 4.5, 'petal_width': 1.5, 'species': 'versicolor'},
     {'sepal_length': 4.7, 'sepal_width': 3.2, 'petal_length': 1.3, 'petal_width': 0.2, 'species': 'setosa'},
     {'sepal_length': 7.0, 'sepal_width': 3.2, 'petal_length': 4.7, 'petal_width': 1.4, 'species': 'versicolor'},
     {'sepal_length': 7.6, 'sepal_width': 3.0, 'petal_length': 6.6, 'petal_width': 2.1, 'species': 'virginica'},
     {'sepal_length': 4.9, 'sepal_width': 3.0, 'petal_length': 1.4, 'petal_width': 0.2, 'species': 'setosa'}]
"""

import json


DATA = (
    '[{"sepal_length":5.8,"sepal_width":2.7,"petal_length":5.1,"petal_widt'
    'h":1.9,"species":"virginica"},{"sepal_length":5.1,"sepal_width":3.5,"'
    'petal_length":1.4,"petal_width":0.2,"species":"setosa"},{"sepal_lengt'
    'h":5.7,"sepal_width":2.8,"petal_length":4.1,"petal_width":1.3,"specie'
    's":"versicolor"},{"sepal_length":6.3,"sepal_width":2.9,"petal_length"'
    ':5.6,"petal_width":1.8,"species":"virginica"},{"sepal_length":6.4,"se'
    'pal_width":3.2,"petal_length":4.5,"petal_width":1.5,"species":"versic'
    'olor"},{"sepal_length":4.7,"sepal_width":3.2,"petal_length":1.3,"peta'
    'l_width":0.2,"species":"setosa"},{"sepal_length":7.0,"sepal_width":3.'
    '2,"petal_length":4.7,"petal_width":1.4,"species":"versicolor"},{"sepa'
    'l_length":7.6,"sepal_width":3.0,"petal_length":6.6,"petal_width":2.1,'
    '"species":"virginica"},{"sepal_length":4.9,"sepal_width":3.0,"petal_l'
    'ength":1.4,"petal_width":0.2,"species":"setosa"}]'
)


# Load `DATA` from JSON format
# type: list[dict]
result = ...

# Solution
result = json.loads(DATA)
