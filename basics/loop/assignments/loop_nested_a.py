"""
* Assignment: Loop Nested Mean
* Type: class assignment
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Calculate mean `sepal_length` value
    2. Run doctests - all must succeed

Polish:
    1. Wylicz średnią wartość `sepal_length`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is float, \
    'Variable `result` has invalid type, should be float'

    >>> result
    5.911111111111111
"""

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
    (4.6, 3.1, 1.5, 0.2, 'setosa'),
]

# Arithmetic mean from `sepal_length` column
# type: float
result = ...

# Solution
values = []

for row in DATA[1:]:
    values.append(row[0])

result = sum(values) / len(values)
