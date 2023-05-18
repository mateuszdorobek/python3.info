"""
* Assignment: Math Statistics Stats
* Complexity: easy
* Lines of code: 11 lines
* Time: 13 min

English:
    1. For columns:
        a. sepal_length,
        b. sepal_width,
        c. petal_length,
        d. petal_width.
    2. Print calculated values:
        a. mean,
        b. median,
        c. standard deviation,
        d. variance.
    3. Use `statistics` module from Python standard library
    4. Run doctests - all must succeed

Polish:
    1. Dla kolumn:
        a. sepal_length,
        b. sepal_width,
        c. petal_length,
        d. petal_width.
    2. Wypisz wyliczone wartości:
        a. średnią,
        b. medianę,
        c. odchylenie standardowe,
        d. wariancję.
    3. Użyj modułu `statistics` z biblioteki standardowej Python
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> stats(sepal_length)  # doctest: +NORMALIZE_WHITESPACE
    {'mean': 5.84,
     'stdev': 0.9777525249264252,
     'median': 5.75,
     'variance': 0.9559999999999997}

    >>> stats(sepal_width)  # doctest: +NORMALIZE_WHITESPACE
    {'mean': 3.0,
     'stdev': 0.2905932629027116,
     'median': 3.0,
     'variance': 0.08444444444444446}

    >>> stats(petal_length)  # doctest: +NORMALIZE_WHITESPACE
    {'mean': 3.92,
     'stdev': 1.8937323523196783,
     'median': 4.5,
     'variance': 3.5862222222222218}

    >>> stats(petal_width)  # doctest: +NORMALIZE_WHITESPACE
     {'mean': 1.23,
      'stdev': 0.7484057129065165,
      'median': 1.45,
      'variance': 0.5601111111111111}
"""

from statistics import mean, stdev, variance, median


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
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
]


# Solution
header, *rows = DATA
sepal_length = [row[0] for row in rows]
sepal_width = [row[1] for row in rows]
petal_length = [row[2] for row in rows]
petal_width = [row[3] for row in rows]


def stats(values):
    return {
        'mean': mean(values),
        'stdev': stdev(values),
        'median': median(values),
        'variance': variance(values)}
