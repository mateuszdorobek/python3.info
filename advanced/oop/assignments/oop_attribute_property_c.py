"""
* Assignment: Protocol Property Deleter
* Complexity: easy
* Lines of code: 6 lines
* Time: 3 min

English:
    1. Define class `Point` with `x`, `y`, `z` attributes
    2. Define property `position` in class `Point`
    3. Deleting `position` sets all attributes to 0 (`x=0`, `y=0`, `z=0`)
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Point` z atrybutami `x`, `y`, `z`
    2. Zdefiniuj property `position` w klasie `Point`
    3. Usunięcie `position` ustawia wszystkie atrybuty na 0 (`x=0`, `y=0`, `z=0`)
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pt = Point(x=1, y=2, z=3)
    >>> pt.x, pt.y, pt.z
    (1, 2, 3)
    >>> del pt.position
    >>> pt.x, pt.y, pt.z
    (0, 0, 0)
"""

from dataclasses import dataclass


# Define class `Point` with `x`, `y`, `z` attributes
# Define property `position` in class `Point`
# Deleting `position` sets all attributes to 0 (`x=0`, `y=0`, `z=0`)
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
    position = property()

    @position.deleter
    def position(self):
        self.x = 0
        self.y = 0
        self.z = 0
