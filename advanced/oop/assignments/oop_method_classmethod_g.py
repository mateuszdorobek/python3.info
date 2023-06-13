"""
* Assignment: OOP MethodClassmethod FromTimestamp
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define class `Timezone` with:
        a. Field `timesamp: int`
        b. Field `tzname: str`
        c. Method `from_timestamp()`
    2. Method `from_timestamp()`:
        a. Parameter `data: int`, example: 1234567890
        b. Returns instance of a class on which was called
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Timezone` z:
        a. Polem `timesamp: int`
        b. Polem `tzname: str`
        c. Metodą `from_timestamp()`
    2. Metoda `from_timestamp()`:
        a. Parametr `data: int`, przykład: 1234567890
        b. Zwraca instancję klasy na której została wykonana
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * datetime.fromtimestamp()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Timezone)
    >>> assert isclass(CET)
    >>> assert isclass(CEST)

    >>> cet = CET.from_timestamp(1234567890)
    >>> assert type(cet.tzname) is str
    >>> assert type(cet.dt) is datetime
    >>> assert cet.tzname == 'Central European Time'
    >>> assert cet.dt == datetime(2009, 2, 14, 0, 31, 30)

    >>> cest = CEST.from_timestamp(1234567890)
    >>> assert type(cest.tzname) is str
    >>> assert type(cest.dt) is datetime
    >>> assert cest.tzname == 'Central European Summer Time'
    >>> assert cest.dt == datetime(2009, 2, 14, 0, 31, 30)
"""
from datetime import datetime


class Timezone:
    tzname: str
    dt: datetime

    def __init__(self, dt):
        self.dt = dt

# Method `from_timestamp()` with parameter: `data: int`
# Method `from_timestamp()` returns instance of a class on which was called
# type: Callable[[type[Timezone], int], Timezone]
    def from_timestamp():
        ...


class CET(Timezone):
    tzname = 'Central European Time'


class CEST(Timezone):
    tzname = 'Central European Summer Time'


# Solution
class Timezone:
    dt: datetime
    tzname: str

    def __init__(self, dt):
        self.dt = dt

    @classmethod
    def from_timestamp(cls, data: int):
        dt = datetime.fromtimestamp(data)
        return cls(dt)


class CET(Timezone):
    tzname = 'Central European Time'


class CEST(Timezone):
    tzname = 'Central European Summer Time'
