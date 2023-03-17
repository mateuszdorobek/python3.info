"""
* Assignment: DesignPatterns Creational PrototypeDate
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Create class `Date` with:
        a. `year: int`
        b. `month: int`
        c. `day: int`
        d. method `.clone()`
    2. Method `.clone()` returns another `Date` with the same values
    3. Run doctests - all must succeed

Polish:
    TODO: Polish translation

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> date = Date(1969, 7, 21)
    >>> result = date.clone()

    >>> result.year
    1969
    >>> result.month
    7
    >>> result.day
    21
"""
from dataclasses import dataclass


@dataclass
class Date:
    year: int
    month: int
    day: int


# Solution
@dataclass
class Date:
    year: int
    month: int
    day: int

    def clone(self):
        return Date(
            year = self.year,
            month = self.month,
            day = self.day)
