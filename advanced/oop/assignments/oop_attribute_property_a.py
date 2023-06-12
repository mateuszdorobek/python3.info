"""
* Assignment: Protocol Property Getter
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define class `Point` with `x`, `y`, `z` attributes
    2. Define property `position` in class `Point`
    3. Accessing `position` returns `(x, y, z)`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Point` z atrybutami `x`, `y`, `z`
    2. Zdefiniuj property `position` w klasie `Point`
    3. Dostęp do `position` zwraca `(x, y, z)`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pt = Point(x=1, y=2, z=3)
    >>> pt.x, pt.y, pt.z
    (1, 2, 3)
    >>> pt.position
    (1, 2, 3)
"""

from dataclasses import dataclass


# Define class `Point` with `x`, `y`, `z` attributes
# Define property `position` in class `Point`
# Accessing `position` returns `(x, y, z)`
# type: type[Point]
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

    @property
    def position(self):
        return self.x, self.y, self.z
