"""
* Assignment: OOP Relations Syntax
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Use Dataclass to define class `Point` with attributes:
        a. `x: int` with default value `0`
        b. `y: int` with default value `0`
    2. Use Dataclass to define class `Path` with attributes:
        a. `points: list[Point]` with default empty list
    3. Run doctests - all must succeed

Polish:
    1. Użyj Dataclass do zdefiniowania klasy `Point` z atrybutami:
        a. `x: int` z domyślną wartością `0`
        b. `y: int` z domyślną wartością `0`
    2. Użyj Dataclass do zdefiniowania klasy `Path` z atrybutami:
        a. `points: list[Point]` z domyślną pustą listą
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Point)
    >>> assert isclass(Path)
    >>> assert hasattr(Point, 'x')
    >>> assert hasattr(Point, 'y')

    >>> Point()
    Point(x=0, y=0)
    >>> Point(x=0, y=0)
    Point(x=0, y=0)
    >>> Point(x=1, y=2)
    Point(x=1, y=2)

    >>> Path([Point(x=0, y=0),
    ...       Point(x=0, y=1),
    ...       Point(x=1, y=0)])
    Path(points=[Point(x=0, y=0), Point(x=0, y=1), Point(x=1, y=0)])
"""

from dataclasses import dataclass, field


# Solution
@dataclass
class Point:
    x: int = 0
    y: int = 0


@dataclass
class Path:
    points: list[Point] = field(default_factory=list)
