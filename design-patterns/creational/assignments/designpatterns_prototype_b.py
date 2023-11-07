"""
* Assignment: DesignPatterns Creational PrototypeTime
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Create class `Time` with:
        a. `hour: int`
        b. `minute: int`
        c. `second: int`
        d. `microsecond: int`
        e. method `.clone()`
    2. Method `.clone()` returns another `Time` with the same values
    3. Use `vars(self)`
    4. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `Time` z:
        a. `hour: int`
        b. `minute: int`
        c. `second: int`
        d. `microsecond: int`
        e. metodą `.clone()`
     2. Metoda `.clone()` zwraca kolejny `Time` z tymi samymi wartościami
     3. Użyj `vars(self)`
     4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> time = Time(2, 56, 15)
    >>> result = time.clone()

    >>> result.hour
    2
    >>> result.minute
    56
    >>> result.second
    15
    >>> result.microsecond
    0
"""
from dataclasses import dataclass


@dataclass
class Time:
    hour: int = 0
    minute: int = 0
    second: int = 0
    microsecond: int = 0


# Solution
@dataclass
class Time:
    hour: int = 0
    minute: int = 0
    second: int = 0
    microsecond: int = 0

    def clone(self):
        return Time(**vars(self))
