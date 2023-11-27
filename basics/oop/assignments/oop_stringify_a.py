"""
* Assignment: OOP Stringify Str
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. While printing object show: species name and a sum of `self.features`
    2. Result of sum round to one decimal place
    3. Run doctests - all must succeed

Polish:
    1. Przy wypisywaniu obiektu pokaż: nazwę gatunku i sumę `self.features`
    2. Wynik sumowania zaokrąglij do jednego miejsca po przecinku
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> for *features, label in DATA:
    ...     iris = Iris(features, label)
    ...     print(iris)
    setosa 9.4
    versicolor 16.3
    virginica 19.3
"""

DATA = [
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
]


class Iris:
    def __init__(self, features, label):
        self.features = features
        self.label = label


# Solution
class Iris:
    def __init__(self, features, label):
        self.features = features
        self.label = label

    def __str__(self):
        total = sum(self.features)
        return f'{self.label} {total:.1f}'
