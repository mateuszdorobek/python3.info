"""
* Assignment: OOP MethodClassmethod FromDatetime
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

English:
    1. Define class `DateTime` with:
        a. Field `year: int`
        b. Field `month: int`
        c. Field `day: int`
        d. Field `hour: int`
        e. Field `minute: int`
        f. Field `second: int`
        g. Field `tzinfo: str`
        h. Method `from_datetime()` with parameter: `dt: datetime`
    2. Method `from_datetime()` returns instance of a class on which was called
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `DateTime` z:
        a. Polem `year: int`
        b. Polem `month: int`
        c. Polem `day: int`
        d. Polem `hour: int`
        e. Polem `minute: int`
        f. Polem `second: int`
        g. Polem `tzinfo: str`
        h. Metodą `from_datetime()` z parametrem `dt: str`
    2. Metoda `from_datetime()` zwraca instancję klasy na której została wykonana
    3. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * zoneinfo.ZoneInfo()
    * datetime.datetime()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(DateTime)
    >>> assert isclass(UTC)
    >>> assert isclass(CET)
    >>> assert isclass(CEST)

    >>> dt = datetime(1969, 7, 21, 2, 56, 15)
    >>> utc = UTC.from_datetime(dt)
    >>> assert utc.year == 1969
    >>> assert utc.month == 7
    >>> assert utc.day == 21
    >>> assert utc.hour == 2
    >>> assert utc.minute == 56
    >>> assert utc.second == 15
    >>> assert utc.tzinfo == ZoneInfo('Etc/UTC')

    >>> dt = datetime(1969, 7, 21, 2, 56, 15)
    >>> cet = CET.from_datetime(dt)
    >>> assert cet.year == 1969
    >>> assert cet.month == 7
    >>> assert cet.day == 21
    >>> assert cet.hour == 2
    >>> assert cet.minute == 56
    >>> assert cet.second == 15
    >>> assert cet.tzinfo == ZoneInfo('Etc/GMT-1')

    >>> dt = datetime(1969, 7, 21, 2, 56, 15)
    >>> cest = CEST.from_datetime(dt)
    >>> assert cest.year == 1969
    >>> assert cest.month == 7
    >>> assert cest.day == 21
    >>> assert cest.hour == 2
    >>> assert cest.minute == 56
    >>> assert cest.second == 15
    >>> assert cest.tzinfo == ZoneInfo('Etc/GMT-2')
"""

from datetime import datetime
from zoneinfo import ZoneInfo


class DateTime:
    tzname: str

    def __init__(self, year, month, day, hour, minute, second, tzinfo):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.tzinfo = tzinfo

# Method `from_datetime()` with parameter: `dt: datetime`
# Method `from_datetime()` returns instance of a class on which was called
# type: Callable[[type[Self], datetime], Self]
    def from_datetime():
        ...

class UTC(DateTime):
    tzname = 'Etc/UTC'


class CET(DateTime):
    tzname = 'Etc/GMT-1'


class CEST(DateTime):
    tzname = 'Etc/GMT-2'


# Solution
class DateTime:
    tzname: str

    def __init__(self, year, month, day, hour, minute, second, tzinfo):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.tzinfo = tzinfo

    @classmethod
    def from_datetime(cls, dt: datetime):
        year = dt.year
        month = dt.month
        day = dt.day
        hour = dt.hour
        minute = dt.minute
        second = dt.second
        tzinfo = ZoneInfo(cls.tzname)
        return cls(year, month, day, hour, minute, second, tzinfo)


class UTC(DateTime):
    tzname = 'Etc/UTC'


class CET(DateTime):
    tzname = 'Etc/GMT-1'


class CEST(DateTime):
    tzname = 'Etc/GMT-2'
