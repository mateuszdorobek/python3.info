"""
* Assignment: Unpack Arguments Define
* Complexity: easy
* Lines of code: 3 lines
* Time: 8 min

English:
    1. Define `result: list[dict]`
    2. Iterate over `DATA` separating `values` from `species`
    3. To `result` append dict with:
       a. key: `species`, value: species name
       b. key: `mean`, value: arithmetic mean of `values`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[dict]`
    2. Iteruj po `DATA` separując `values` od `species`
    3. Do `result` dodawaj dict z:
       a. klucz: `species`, wartość: nazwa gatunku
       b. klucz: `mean`, wartość: wynik średniej arytmetycznej `values`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list, \
    'Result must be a list'

    >>> assert all(type(row) is dict for row in result), \
    'All elements in result must be a dict'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'species': 'virginica', 'mean': 3.875},
     {'species': 'setosa', 'mean': 2.65},
     {'species': 'versicolor', 'mean': 3.475},
     {'species': 'virginica', 'mean': 6.0},
     {'species': 'versicolor', 'mean': 3.95},
     {'species': 'setosa', 'mean': 4.7}]
"""

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 5.7, 'virginica'),
    (6.4, 1.5, 'versicolor'),
    (4.7, 'setosa'),
]


def mean(*args):
    return sum(args) / len(args)


# calculate mean and append dict with {'species': ..., 'mean': ...}
# type: list[dict]
result = ...

# Solution
result = [{'species': species, 'mean': mean(*values)}
          for *values, species in DATA[1:]]

# Alternative Solution
result = []
for *values, species in DATA[1:]:
    result.append({'species': species, 'mean': mean(*values)})

# Alternative Solution
result = [{'species': species, 'mean': mean(*values)}
          for *values, species in DATA[1:]]

# Alternative Solution
result = [{'species': y, 'mean': mean(*X)}
          for *X, y in DATA[1:]]
