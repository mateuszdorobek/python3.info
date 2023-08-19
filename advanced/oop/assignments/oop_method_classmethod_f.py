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
        h. Method `from_datetime()`
    2. Method `from_datetime()`:
        a. Parameter `dt: datetime`, example: datetime(1969, 7, 21, 2, 56, 15)
        b. Returns instance of a class on which was called
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
        h. Metodą `from_datetime()`
    2. Metoda `from_datetime()`:
        a. Parametr `dt: datetime`, przykład: datetime(1969, 7, 21, 2, 56, 15)
        b. Zwraca instancję klasy na której została wykonana
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

    >>> data = datetime(1969, 7, 21, 2, 56, 15)
    >>> utc = UTC.from_datetime(data)
    >>> assert type(utc.year) is int
    >>> assert type(utc.month) is int
    >>> assert type(utc.day) is int
    >>> assert type(utc.hour) is int
    >>> assert type(utc.minute) is int
    >>> assert type(utc.second) is int
    >>> assert type(utc.tzinfo) is ZoneInfo
    >>> assert utc.year == 1969
    >>> assert utc.month == 7
    >>> assert utc.day == 21
    >>> assert utc.hour == 2
    >>> assert utc.minute == 56
    >>> assert utc.second == 15
    >>> assert utc.tzinfo == ZoneInfo('Etc/UTC')

    >>> data = datetime(1969, 7, 21, 2, 56, 15)
    >>> cet = CET.from_datetime(data)
    >>> assert type(cet.year) is int
    >>> assert type(cet.month) is int
    >>> assert type(cet.day) is int
    >>> assert type(cet.hour) is int
    >>> assert type(cet.minute) is int
    >>> assert type(cet.second) is int
    >>> assert type(cet.tzinfo) is ZoneInfo
    >>> assert cet.year == 1969
    >>> assert cet.month == 7
    >>> assert cet.day == 21
    >>> assert cet.hour == 2
    >>> assert cet.minute == 56
    >>> assert cet.second == 15
    >>> assert cet.tzinfo == ZoneInfo('Etc/GMT-1')

    >>> data = datetime(1969, 7, 21, 2, 56, 15)
    >>> cest = CEST.from_datetime(data)
    >>> assert type(cest.year) is int
    >>> assert type(cest.month) is int
    >>> assert type(cest.day) is int
    >>> assert type(cest.hour) is int
    >>> assert type(cest.minute) is int
    >>> assert type(cest.second) is int
    >>> assert type(cest.tzinfo) is ZoneInfo
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

    # parameter: `dt: datetime`
    # example: datetime(1969, 7, 21, 2, 56, 15)
    # hint: tzinfo = ZoneInfo(cls.tzname)
    # return: instance of a class on which was called
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
