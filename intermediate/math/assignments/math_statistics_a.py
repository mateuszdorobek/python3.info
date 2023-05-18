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

Hint:
    * Note, that in petal_length stdev is:
        a. Python 3.10: 1.8602739173624534
        b. Python 3.11: 1.8602739173624532


Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> stats(sepal_length)
    {'mean': 5.833333333333333, 'stdev': 0.9084785816591018, 'median': 5.7, 'variance': 0.8253333333333333}
    >>> stats(sepal_width)
    {'mean': 3.0619047619047617, 'stdev': 0.36670995415476587, 'median': 3.0, 'variance': 0.1344761904761905}
    >>> stats(petal_length)
    {'mean': 3.8523809523809525, 'stdev': 1.8602739173624532, 'median': 4.5, 'variance': 3.4606190476190477}
    >>> stats(petal_width)
    {'mean': 1.2333333333333334, 'stdev': 0.7741662181555931, 'median': 1.4, 'variance': 0.5993333333333334}
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
    (7.1, 3.0, 5.9, 2.1, 'virginica'),
    (4.6, 3.4, 1.4, 0.3, 'setosa'),
    (5.4, 3.9, 1.7, 0.4, 'setosa'),
    (5.7, 2.8, 4.5, 1.3, 'versicolor'),
    (5.0, 3.6, 1.4, 0.3, 'setosa'),
    (5.5, 2.3, 4.0, 1.3, 'versicolor'),
    (6.5, 3.0, 5.8, 2.2, 'virginica'),
    (6.5, 2.8, 4.6, 1.5, 'versicolor'),
    (6.3, 3.3, 6.0, 2.5, 'virginica'),
    (6.9, 3.1, 4.9, 1.5, 'versicolor'),
    (4.6, 3.1, 1.5, 0.2, 'setosa'),
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
        'variance': variance(values),
    }
