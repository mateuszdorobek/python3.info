Datetime Timezone
=================
* Always keep dates and times only in UTC (**important!**)
* Datetimes should be converted to local time only when displaying to user
* Computerphile Time & Time Zones [#ytComputerphileTimeZones]_
* Abolition of Time Zones [#wikiAbolitionOfTimeZones]_
* Since Python 3.9: :pep:`615` -- Support for the IANA Time Zone Database in the Standard Library
* ``pip install tzdata``


SetUp
-----
>>> from datetime import date, time, datetime, timedelta, timezone
>>> from zoneinfo import ZoneInfo


Daylight Saving Time
--------------------
* Daylight Saving Time date is different for each country and even US state
* Australia is 9h 30m shifted
* India is 3h 30m shifted
* Nepal is 3h 45m shifted
* In southern hemisphere the Daylight Saving Time is opposite direction
* They subtract hour in March and add in October
* Samoa is on the international date line
* Samoa changed from UTC-1200 to UTC+1200 for easier trades with Australia
* During World War II England was GMT+0200
* Libya in 2013 discontinued DST with couple of days notice
* Israel is on a different timezone than Palestine (multiple timezones in one location, based on nationality)
* Change from Julian to Gregorian calendar caused to skip few weeks
* In 18th century World change from Julian to Gregorian calendar
* In 20th century Russia change from Julian to Gregorian calendar (different days which was skipped than for worldwide change)
* In britain until 16th century the year started on 25th of March
* Mind leap seconds (add, subtract)
* UTC includes leap seconds
* Astronomical time does not include leap seconds
* Google invented smear second (on the day of leap second) they add a small fraction of a second to each second that day until midnight

Comparing datetime works only when all has the same timezone (UTC):

.. figure:: img/datetime-compare.png


Timezone Naive Datetimes
------------------------
>>> datetime(1957, 10, 4, 19, 28, 34)
datetime.datetime(1957, 10, 4, 19, 28, 34)

>>> datetime.now()  # doctest: +SKIP
datetime.datetime(1957, 10, 4, 19, 28, 34)


Timezone Aware Datetimes
------------------------
>>> datetime.now(timezone.utc)  # doctest: +SKIP
datetime.datetime(1957, 10, 4, 19, 28, 34, tzinfo=datetime.timezone.utc)

>>> datetime(1957, 10, 4, 19, 28, 34, tzinfo=timezone.utc)
datetime.datetime(1957, 10, 4, 19, 28, 34, tzinfo=datetime.timezone.utc)

>>> dt = datetime(1957, 10, 4, 19, 28, 34)
>>> dt.replace(tzinfo=timezone.utc)
datetime.datetime(1957, 10, 4, 19, 28, 34, tzinfo=datetime.timezone.utc)


UTCNow
------
* ``datetime.utcnow()`` produces timezone naive datetimes!

>>> datetime.utcnow()  # doctest: +SKIP
datetime.datetime(1957, 10, 4, 17, 28, 34)

>>> datetime.utcnow(tz=timezone.utc)
Traceback (most recent call last):
TypeError: datetime.utcnow() takes no keyword arguments

>>> datetime.utcnow(timezone.utc)
Traceback (most recent call last):
TypeError: datetime.utcnow() takes no arguments (1 given)


IANA Time Zone Database
-----------------------
* https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
* https://www.iana.org/time-zones
* https://pypi.org/project/tzdata/
* https://en.wikipedia.org/wiki/Time_in_Antarctica
* ``pip install tzdata``

IANA 2017a timezone database [#IANA]_:

.. figure:: img/datetime-timezone-iana2017a.png


ZoneInfo
--------
* Since Python 3.9: :pep:`615` -- Support for the IANA Time Zone Database in the Standard Library
* https://docs.python.org/3/library/zoneinfo.html

>>> utc = ZoneInfo('UTC')
>>> est = ZoneInfo('US/Eastern')
>>> cet = ZoneInfo('Europe/Warsaw')
>>> alm = ZoneInfo('Asia/Almaty')

Working with ``ZoneInfo`` objects:

>>> dt = datetime(1969, 7, 21, 2, 56, 15, tzinfo=ZoneInfo('UTC'))
>>> print(dt)
1969-07-21 02:56:15+00:00

>>> dt += timedelta(days=7)
>>> print(dt)
1969-07-28 02:56:15+00:00

``ZoneInfo`` objects knows Daylight Saving Time:

>>> dt = datetime(2000, 1, 1, tzinfo=ZoneInfo('America/Los_Angeles'))  # Daylight saving time
>>>
>>> dt.tzname()
'PST'
>>>
>>> dt += timedelta(days=100)  # Standard time
>>> dt.tzname()
'PDT'


Use Case - 0x01
---------------
>>> from datetime import datetime
>>> from zoneinfo import ZoneInfo
>>>
>>>
>>> UTC = ZoneInfo('UTC')
>>> BAJKONUR = ZoneInfo('Asia/Almaty')
>>> WAW = ZoneInfo('Europe/Warsaw')
>>> LOS_ANGELES = ZoneInfo('America/Los_Angeles')
>>>
>>>
>>> dt = datetime(1961, 4, 12, 6, 7, tzinfo=UTC)
>>> dt
datetime.datetime(1961, 4, 12, 6, 7, tzinfo=zoneinfo.ZoneInfo(key='UTC'))
>>>
>>> dt.astimezone(BAJKONUR)
datetime.datetime(1961, 4, 12, 12, 7, tzinfo=zoneinfo.ZoneInfo(key='Asia/Almaty'))
>>>
>>> dt.astimezone(WAW)
datetime.datetime(1961, 4, 12, 7, 7, tzinfo=zoneinfo.ZoneInfo(key='Europe/Warsaw'))
>>>
>>> dt.astimezone(LOS_ANGELES)
datetime.datetime(1961, 4, 11, 22, 7, tzinfo=zoneinfo.ZoneInfo(key='America/Los_Angeles'))


Use Case - 0x02
---------------
Descriptor Timezone Converter:

>>> from dataclasses import dataclass
>>> from datetime import datetime
>>> from zoneinfo import ZoneInfo
>>>
>>>
>>> class Timezone:
...     def __init__(self, name):
...         self.timezone = ZoneInfo(name)
...
...     def __get__(self, parent, *args):
...         utc = parent.utc.replace(tzinfo=ZoneInfo('UTC'))
...         return utc.astimezone(self.timezone)
...
...     def __set__(self, parent, new_datetime):
...         local_time = new_datetime.replace(tzinfo=self.timezone)
...         parent.utc = local_time.astimezone(ZoneInfo('UTC'))
>>>
>>>
>>> @dataclass
... class Time:
...     utc = datetime.now(tz=ZoneInfo('UTC'))
...     warsaw = Timezone('Europe/Warsaw')
...     eastern = Timezone('America/New_York')
...     pacific = Timezone('America/Los_Angeles')
>>>
>>>
>>> t = Time()
>>>
>>> # Gagarin's launch to space
>>> t.utc = datetime(1961, 4, 12, 6, 7)
>>>
>>> print(t.utc)
1961-04-12 06:07:00
>>> print(t.warsaw)
1961-04-12 07:07:00+01:00
>>> print(t.eastern)
1961-04-12 01:07:00-05:00
>>> print(t.pacific)
1961-04-11 22:07:00-08:00
>>>
>>>
>>> # Armstrong's first Lunar step
>>> t.warsaw = datetime(1969, 7, 21, 3, 56, 15)
>>>
>>> print(t.utc)
1969-07-21 02:56:15+00:00
>>> print(t.warsaw)
1969-07-21 03:56:15+01:00
>>> print(t.eastern)
1969-07-20 22:56:15-04:00
>>> print(t.pacific)
1969-07-20 19:56:15-07:00


References
----------
.. [#wikiAbolitionOfTimeZones] Wikipedia. Abolition of Time Zones. Leap Second. Year: 2019. Retrieved: 2022-05-10. URL: https://en.wikipedia.org/wiki/Abolition_of_time_zones
.. [#IANA] IANA. Time Zone Database. Year: 2017. Retrieved: 2019-08-05.
.. [#ytComputerphileTimeZones] Computerphile. The Problem with Time & Timezones. Year: 2019. Retrieved: 2019-04-05. URL: https://www.youtube.com/watch?v=-5wpm-gesOY


Assignments
-----------
.. literalinclude:: assignments/datetime_timezone_a.py
    :caption: :download:`Solution <assignments/datetime_timezone_a.py>`
    :end-before: # Solution
