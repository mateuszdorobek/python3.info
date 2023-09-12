"""
* Assignment: OOP Property Setter
* Complexity: easy
* Lines of code: 9 lines
* Time: 5 min

English:
    1. Define class `Point` with:
        a. Attribute `x: int`
        b. Attribute `y: int`
        c. Attribute `z: int`
        d. Property `position`
    2. Setting `position`:
        a. If argument is not list, tuple, set raise Type Error
        b. If argument has length other than 3, raise Value
        b. Else sets `x`, `y`, `z` attributes from sequence
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Point` z:
        a. Atrybut `x: int`
        b. Atrybut `y: int`
        c. Atrybut `z: int`
        d. Property `position`
    2. Ustawianie `position`:
        a. Jeżeli argument nie jest list, tuple, set podnieś TypeError
        b. Jeżeli argument nie ma długości 3, podnieś ValueError
        b. W przeciwnym wypadku ustaw kolejne atrybuty `x`, `y`, `z` z sekwencji
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pt = Point()

    >>> pt.position = 1, 2, 3
    >>> assert pt.x == 1
    >>> assert pt.y == 2
    >>> assert pt.z == 3

    >>> pt.position = (4, 5, 6)
    >>> assert pt.x == 4
    >>> assert pt.y == 5
    >>> assert pt.z == 6

    >>> pt.position = [7, 8, 9]
    >>> assert pt.x == 7
    >>> assert pt.y == 8
    >>> assert pt.z == 9

    >>> pt.position = {'a':1, 'b':2, 'c':3}
    Traceback (most recent call last):
    TypeError

    >>> pt.position = 1, 2
    Traceback (most recent call last):
    ValueError
"""

from dataclasses import dataclass


# Define class `Point` with `x`, `y`, `z` attributes
# Define property `position` in class `Point`
# Setting `position`:
# - If argument is not list, tuple, set raise Type Error
# - If argument has length other than 3, raise Value
# - Else sets `x`, `y`, `z` attributes from sequence
# type: type[Point]
class Point:
    x: int
    y: int
    z: int


# Solution
class Point:
    x: int
    y: int
    z: int
    position = property()

    @position.setter
    def position(self, new_value):
        if type(new_value) not in (list, tuple, set):
            raise TypeError
        elif len(new_value) != 3:
            raise ValueError
        else:
            self.x, self.y, self.z = new_value
