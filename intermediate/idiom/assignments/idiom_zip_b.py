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
    [{'PetalLength': 5.1,
      'PetalWidth': 1.9,
      'SepalLength': 5.8,
      'SepalWidth': 2.7,
      'Species': 'virginica'},
     {'PetalLength': 1.4,
      'PetalWidth': 0.2,
      'SepalLength': 5.1,
      'SepalWidth': 3.5,
      'Species': 'setosa'},
     {'PetalLength': 4.1,
      'PetalWidth': 1.3,
      'SepalLength': 5.7,
      'SepalWidth': 2.8,
      'Species': 'versicolor'},
     {'PetalLength': 5.6,
      'PetalWidth': 1.8,
      'SepalLength': 6.3,
      'SepalWidth': 2.9,
      'Species': 'virginica'},
     {'PetalLength': 4.5,
      'PetalWidth': 1.5,
      'SepalLength': 6.4,
      'SepalWidth': 3.2,
      'Species': 'versicolor'},
     {'PetalLength': 1.3,
      'PetalWidth': 0.2,
      'SepalLength': 4.7,
      'SepalWidth': 3.2,
      'Species': 'setosa'}]
"""

DATA = [
    ('SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa')]


# Convert DATA from list[tuple] to list[dict]
# type: list[dict[str,float|str]]
result = ...


# Solution
header, *rows = DATA
result = [dict(zip(header, row)) for row in rows]
