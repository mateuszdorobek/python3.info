"""
* Assignment: Protocol Reflection Setattr
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Create class `Point` with `x`, `y`, `z` attributes
    2. Prevent creation of new attributes
    3. Allow to modify values of `x`, `y`, `z`
    4. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `Point` z atrybutami `x`, `y`, `z`
    2. Zablokuj tworzenie nowych atrybutów
    3. Zezwól na modyfikowanie wartości `x`, `y`, `z`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pt = Point(1, 2, 3)
    >>> pt.x, pt.y, pt.z
    (1, 2, 3)
    >>> pt.notexisting = 10
    Traceback (most recent call last):
    PermissionError: Cannot set other attributes than x, y, z
    >>> pt.x = 10
    >>> pt.y = 20
    >>> pt.z = 30
    >>> pt.x, pt.y, pt.z
    (10, 20, 30)
"""

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    z: int


# Solution
@dataclass
class Point:
    x: int
    y: int
    z: int

    def __setattr__(self, name, value):
        if name not in ('x', 'y', 'z'):
            raise PermissionError('Cannot set other attributes than x, y, z')
        return super().__setattr__(name, value)
