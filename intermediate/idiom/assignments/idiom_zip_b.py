"""
* Assignment: Idiom Zip List[Dict]
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Define `result: list[dict]`:
    2. Convert `DATA` from `list[tuple]` to `list[dict]`
        a. key - name from the header
        b. value - numerical value or species name
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[dict]`:
    2. Przekonwertuj `DATA` z `list[tuple]` do `list[dict]`
        a. klucz - nazwa z nagłówka
        b. wartość - wartość numeryczna lub nazwa gatunku
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> result = list(result)
    >>> assert type(result) is list, \
    'Result must be a list'
    >>> assert len(result) > 0, \
    'Result cannot be empty'
    >>> assert all(type(element) is dict for element in result), \
    'All elements in result must be a dict'

    >>> pprint(result)
    [{'petal_length': 5.1,
      'petal_width': 1.9,
      'sepal_length': 5.8,
      'sepal_width': 2.7,
      'species': 'virginica'},
     {'petal_length': 1.4,
      'petal_width': 0.2,
      'sepal_length': 5.1,
      'sepal_width': 3.5,
      'species': 'setosa'},
     {'petal_length': 4.1,
      'petal_width': 1.3,
      'sepal_length': 5.7,
      'sepal_width': 2.8,
      'species': 'versicolor'},
     {'petal_length': 5.6,
      'petal_width': 1.8,
      'sepal_length': 6.3,
      'sepal_width': 2.9,
      'species': 'virginica'},
     {'petal_length': 4.5,
      'petal_width': 1.5,
      'sepal_length': 6.4,
      'sepal_width': 3.2,
      'species': 'versicolor'},
     {'petal_length': 1.3,
      'petal_width': 0.2,
      'sepal_length': 4.7,
      'sepal_width': 3.2,
      'species': 'setosa'}]
"""

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]


# Convert DATA from list[tuple] to list[dict]
# type: list[dict[str,float|str]]
result = ...


# Solution
header, *rows = DATA
result = [dict(zip(header, row)) for row in rows]
