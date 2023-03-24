"""
* Assignment: Unpack Arguments Define
* Complexity: easy
* Lines of code: 3 lines
* Time: 8 min

English:
    1. Define `result: list[dict]`
    2. Iterate over `DATA` separating `features` from `label`
    3. To `result` append dict with:
       a. key: `label`, value: species name
       b. key: `mean`, value: arithmetic mean of `features`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[dict]`
    2. Iteruj po `DATA` separując `features` od `label`
    3. Do `result` dodawaj dict z:
       a. klucz: `label`, wartość: nazwa gatunku
       b. klucz: `mean`, wartość: wynik średniej arytmetycznej `features`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list, \
    'Result must be a list'

    >>> assert all(type(row) is dict for row in result), \
    'All elements in result must be a dict'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'label': 'virginica', 'mean': 3.875},
     {'label': 'setosa', 'mean': 2.65},
     {'label': 'versicolor', 'mean': 3.475},
     {'label': 'virginica', 'mean': 6.0},
     {'label': 'versicolor', 'mean': 3.95},
     {'label': 'setosa', 'mean': 4.7}]
"""

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 5.7, 'virginica'),
    (6.4, 1.5, 'versicolor'),
    (4.7, 'setosa')]


def mean(*args):
    return sum(args) / len(args)


# calculate mean and append dict with {'label': ..., 'mean': ...}
# type: list[dict]
result = ...

# Solution
result = [{'label': label, 'mean': mean(*features)}
          for *features, label in DATA[1:]]

# Alternative Solution
result = []
for *features, label in DATA[1:]:
    result.append({'label': label, 'mean': mean(*features)})

# Alternative Solution
result = [{'label': label, 'mean': mean(*features)}
          for *features, label in DATA[1:]]

# Alternative Solution
result = [{'label': y, 'mean': mean(*X)}
          for *X, y in DATA[1:]]
