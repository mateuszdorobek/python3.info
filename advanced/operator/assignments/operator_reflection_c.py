"""
* Assignment: Protocol Reflection Frozen
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Create class `Point` with `x`, `y`, `z` attributes
    2. Prevent creation of new attributes
    3. Allow to define `x`, `y`, `z` but only at the initialization
    4. Prevent later modification of `x`, `y`, `z`
    5. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `Point` z atrybutami `x`, `y`, `z`
    2. Zablokuj tworzenie nowych atrybutów
    3. Pozwól na zdefiniowanie `x`, `y`, `z` ale tylko przy inicjalizacji
    4. Zablokuj późniejsze modyfikacje `x`, `y`, `z`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pt = Point(1, 2, 3)
    >>> pt.x, pt.y, pt.z
    (1, 2, 3)

    >>> pt.notexisting = 10
    Traceback (most recent call last):
    PermissionError: Cannot set other attributes than x, y, z

    >>> pt.x = 10
    Traceback (most recent call last):
    PermissionError: Cannot modify existing attributes

    >>> pt.y = 20
    Traceback (most recent call last):
    PermissionError: Cannot modify existing attributes

    >>> pt.z = 30
    Traceback (most recent call last):
    PermissionError: Cannot modify existing attributes
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
        if hasattr(self, name):
            raise PermissionError('Cannot modify existing attributes')
        return super().__setattr__(name, value)
