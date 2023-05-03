"""
* Assignment: OOP ObjectConstructor Syntax
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Define class `Point` with methods:
        a. `__new__()` returning new `Point` class instances
        b. `__init__()` taking `x` and `y` and stores them as attributes
        c. Use `object.__new__(cls)`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Point` z metodami:
        a. `__new__()` zwraca nową instancję klasy `Point`
        b. `__init__()` przyjmuje `x` i `y` i zapisuje je jako atrybuty
        c. Użyj `object.__new__(cls)`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * Despite PyCharm suggestion, __new__ and __init__ signatures are different

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Point)
    >>> assert hasattr(Point, '__new__')
    >>> assert hasattr(Point, '__init__')
    >>> pt = Point.__new__(Point)
    >>> assert type(pt) is Point
    >>> pt.__init__(1, 2)
    >>> assert pt.x == 1
    >>> assert pt.y == 2
"""


# Define class `Point` with methods:
# - `__new__()` returning new `Point` class instances
# - `__init__()` taking `x` and `y` and stores them as attributes
# - Use `object.__new__(cls)`
# - Despite PyCharm suggestion, __new__ and __init__ signatures are different
# type: type
class Point:
    ...


# Solution
class Point:
    def __new__(cls):
        return object.__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y
