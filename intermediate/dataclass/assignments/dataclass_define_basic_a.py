"""
* Assignment: Dataclass DefineBasic Syntax
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Use Dataclass to define class `Point` with attributes:
        a. `x: int` with default value `0`
        b. `y: int` with default value `0`
    2. Run doctests - all must succeed

Polish:
    1. Użyj Dataclass do zdefiniowania klasy `Point` z atrybutami:
        a. `x: int` z domyślną wartością `0`
        b. `y: int` z domyślną wartością `0`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass
    >>> from dataclasses import is_dataclass

    >>> assert isclass(Point), 'Point is not a class'
    >>> assert is_dataclass(Point), 'Point is not a dataclass, add decorator'
    >>> assert hasattr(Point, 'x')
    >>> assert hasattr(Point, 'y')

    >>> Point()
    Point(x=0, y=0)

    >>> Point(x=0, y=0)
    Point(x=0, y=0)

    >>> Point(x=1, y=2)
    Point(x=1, y=2)
"""

from dataclasses import dataclass


# Use Dataclass to define class `Point` with attributes `x` and `y`
# type: type
class Point:
    ...


# Solution
@dataclass
class Point:
    x: int = 0
    y: int = 0
