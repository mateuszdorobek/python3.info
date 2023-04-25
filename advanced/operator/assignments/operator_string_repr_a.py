"""
* Assignment: Operator String Repr
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Overload `repr()`
    2. Run doctests - all must succeed

Polish:
    1. Przeciąż `repr()`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod

    >>> assert isclass(Iris)
    >>> iris = Iris(DATA)

    >>> assert hasattr(Iris, '__repr__')
    >>> assert ismethod(iris.__repr__)
    >>> repr(iris)
    "Iris(features=[4.7, 3.2, 1.3, 0.2], label='setosa')"
"""

DATA = (4.7, 3.2, 1.3, 0.2, 'setosa')

# repr() -> Iris(features=[4.7, 3.2, 1.3, 0.2], label='setosa')
class Iris:
    features: list
    label: str

    def __init__(self, data):
        self.features = list(data[:-1])
        self.label = str(data[-1])


# Solution
class Iris:
    features: list
    label: str

    def __init__(self, data):
        self.features = list(data[:-1])
        self.label = str(data[-1])

    def __repr__(self):
        features = self.features
        label = self.label
        return f'Iris({features=}, {label=})'
