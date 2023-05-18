"""
* Assignment: OOP Method Call
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Iterate over `DATA` skipping header and separating features from labels
    2. Call `mean()` method of `Stats` class instance passing list of features
    3. Define `result: list[float]` with list of means from each row
    4. Run doctests - all must succeed

Polish:
    1. Iteruj po `DATA` pomijając nagłówek i rodzielając cechy od etykiet
    2. Wywołuj metodę `mean()` instancji klasy `Stats` przekazując listę cech
    3. Zdefiniuj `result: list[float]` z listą średnich każdego z wierszy
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `round()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list
    >>> assert all(type(x) is float for x in result)

    >>> result
    [3.9, 2.5, 3.5, 4.1, 3.9, 2.4]
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


class Stats:
    def mean(self, data):
        avg = sum(data) / len(data)
        return round(avg, 1)


stats = Stats()

# Apply `mean()` to each feature
# type: list[float]
result = ...

# Solution
result = [stats.mean(X) for *X, y in DATA[1:]]
