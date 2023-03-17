"""
* Assignment: DesignPatterns Creational PrototypeDragon
* Complexity: easy
* Lines of code: 6 lines
* Time: 8 min

English:
    1. Create class `Dragon`
    2. Dragon has attributes:
        a. `name: str`
        b. `position: tuple[int,int]` default `(0, 0)`
        c. `health: int` random from 50 to 100
        d. `gold: int` random from 1 to 100
        e. method `.clone()`
    3. Method `.clone()` returns another `Dragon` with the same values
    4. Use `random.randint()` to generate pseudorandom numbers
    5. Run doctests - all must succeed

Polish:
    TODO: Polish translation

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> from random import seed
    >>> seed(0)

    >>> dragon = Dragon('Wawelski')
    >>> result = dragon.clone()

    >>> result.name
    'Wawelski'

    >>> result.health
    74

    >>> result.gold
    98

    >>> result.position
    (0, 0)
"""
from dataclasses import dataclass, field
from random import randint


@dataclass
class Dragon:
    ...


# Solution
@dataclass
class Dragon:
    name: str
    position: tuple[int,int] = (0,0)
    health: int = field(default_factory=lambda: randint(50, 100))
    gold: int = field(default_factory=lambda: randint(1, 100))

    def clone(self):
        return Dragon(**vars(self))
