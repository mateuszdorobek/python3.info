"""
* Assignment: Operator Left Matmul
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Make object understand following call: `position @ (1, 2)`
    1. Overload `@` operator, to take `tuple[int, int]` as argument
    2. Set `x` and `y` coordinates based on passed values
    3. Run doctests - all must succeed

Polish:
    1. Spraw aby obiekt obsługiwał to wywołanie: `position @ (1, 2)`
    1. Przeciąż operator `@`, aby przyjmował `tuple[int, int]` jako argument
    2. Zmień koordynaty `x` i `y` na podstawie przekazanych wartości
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `object.__matmul__()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> position = Position()
    >>> position
    Position(x=0, y=0)
    >>> position @ (1, 2)
    >>> position
    Position(x=1, y=2)
"""

from dataclasses import dataclass


@dataclass
class Position:
    x: int = 0
    y: int = 0


# Solution
@dataclass
class Position:
    x: int = 0
    y: int = 0

    def __matmul__(self, other: tuple[int, int]) -> None:
        self.x = other[0]
        self.y = other[1]

    # Alternative Solution
    def __matmul__(self, other: tuple[int, int]) -> None:
        self.x, self.y = other
