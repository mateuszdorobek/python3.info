"""
* Assignment: Operator String Str
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Overload `str()`
    2. While printing object show: species name and a sum of `self.features`,
       example: `label='setosa', total=9.4`
    3. Result of sum round to one decimal place
    4. Run doctests - all must succeed

Polish:
    1. Przeciąż `str()`
    2. Przy wypisywaniu obiektu pokaż: nazwę gatunku i sumę `self.features`,
       przykład: `label='setosa', total=9.4`
    3. Wynik sumowania zaokrąglij do jednego miejsca po przecinku
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * f'{var=:.1f}'

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> for *features, label in DATA:
    ...     iris = Iris(features, label)
    ...     print(iris)
    label='setosa', total=9.4
    label='versicolor', total=16.3
    label='virginica', total=19.3
"""

DATA = [
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
]


class Iris:
    features: list
    label: str

    def __init__(self, features, label):
        self.features = features
        self.label = label


# Solution
class Iris:
    features: list
    label: str

    def __init__(self, features, label):
        self.features = features
        self.label = label

    def __str__(self):
        label = self.label
        total = sum(self.features)
        return f'{label=}, {total=:.1f}'
