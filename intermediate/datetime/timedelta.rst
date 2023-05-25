Datetime Timedelta
==================


Timedelta object
----------------
Shifting datetime objects:

>>> from datetime import datetime
>>>
>>>
>>> gagarin = datetime(1961, 4, 12, 6, 7)
>>> armstrong = datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> between_dates = armstrong - gagarin
>>>
>>> str(between_dates)
'3021 days, 20:49:15'
>>> between_dates
datetime.timedelta(days=3021, seconds=74955)
>>> between_dates.days
3021
>>> between_dates.seconds
74955
>>> between_dates.total_seconds()  # (days * seconds per day + seconds)
261089355.0


Simple Time Shift
-----------------
>>> from datetime import timedelta, datetime
>>>
>>>
>>> gagarin = datetime(1961, 4, 12)
>>>
>>> gagarin - timedelta(minutes=15)
datetime.datetime(1961, 4, 11, 23, 45)
>>>
>>> gagarin + timedelta(minutes=10)
datetime.datetime(1961, 4, 12, 0, 10)

>>> from datetime import timedelta, datetime
>>>
>>>
>>> armstrong = datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> armstrong - timedelta(hours=21)
datetime.datetime(1969, 7, 20, 5, 56, 15)
>>>
>>> armstrong + timedelta(hours=5)
datetime.datetime(1969, 7, 21, 7, 56, 15)

>>> from datetime import timedelta, date
>>>
>>>
>>> sputnik = date(1957, 10, 4)
>>>
>>> sputnik + timedelta(days=5)
datetime.date(1957, 10, 9)
>>>
>>> sputnik - timedelta(days=3)
datetime.date(1957, 10, 1)

>>> from datetime import datetime, timedelta
>>>
>>>
>>> gagarin = datetime(1961, 4, 12)
>>>
>>> gagarin + timedelta(weeks=2)
datetime.datetime(1961, 4, 26, 0, 0)
>>>
>>> gagarin - timedelta(weeks=3)
datetime.datetime(1961, 3, 22, 0, 0)


Complex Shifts
--------------
>>> from datetime import timedelta, datetime
>>>
>>>
>>> armstrong = datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> armstrong - timedelta(days=2, hours=21)
datetime.datetime(1969, 7, 18, 5, 56, 15)

>>> from datetime import timedelta, datetime
>>>
>>>
>>> armstrong = datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> duration = timedelta(
...     weeks=3,
...     days=2,
...     hours=21,
...     minutes=5,
...     seconds=12,
...     milliseconds=10,
...     microseconds=55)
>>>
>>> duration
datetime.timedelta(days=23, seconds=75912, microseconds=10055)
>>>
>>> armstrong - duration
datetime.datetime(1969, 6, 27, 5, 51, 2, 989945)


Month Shifts
------------
>>> from datetime import timedelta, date
>>>
>>>
>>> MONTH = timedelta(days=30.4375)
>>>
>>> gagarin = date(1961, 4, 12)
>>> gagarin - MONTH
datetime.date(1961, 3, 13)

>>> from calendar import _monthlen as monthlen
>>> from datetime import timedelta, date
>>>
>>>
>>> def month_before(dt):
...     MONTH = monthlen(dt.year, dt.month)
...     return dt - timedelta(days=MONTH)
>>>
>>>
>>> gagarin = date(1961, 4, 12)
>>> month_before(gagarin)
datetime.date(1961, 3, 13)


Duration
--------
* Period between two datetimes

>>> from datetime import datetime
>>>
>>>
>>> SECOND = 1
>>> MINUTE = 60 * SECOND
>>> HOUR = 60 * MINUTE
>>> DAY = 24 * HOUR
>>> MONTH = 30.4375 * DAY  # Average days a month in solar calendar
>>> YEAR = 365.25 * DAY  # Solar calendar
>>>
>>>
>>> def duration(td):
...     years, seconds = divmod(td.total_seconds(), YEAR)
...     months, seconds = divmod(seconds, MONTH)
...     days, seconds = divmod(seconds, DAY)
...     hours, seconds = divmod(td.seconds, HOUR)
...     minutes, seconds = divmod(seconds, MINUTE)
...     return {
...         'years': int(years),
...         'months': int(months),
...         'days': int(days),
...         'hours': int(hours),
...         'minutes': int(minutes),
...         'seconds': int(seconds)}
>>>
>>>
>>> gagarin = datetime(1961, 4, 12, 6, 7)
>>> armstrong = datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> td = armstrong - gagarin
>>> td
datetime.timedelta(days=3021, seconds=74955)
>>>
>>> duration(td)
{'years': 8, 'months': 3, 'days': 8, 'hours': 20, 'minutes': 49, 'seconds': 15}


Further Reading
---------------
* https://dateutil.readthedocs.io/en/stable/examples.html
* https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html


Assignments
-----------
.. literalinclude:: assignments/datetime_timedelta_a.py
    :caption: :download:`Solution <assignments/datetime_timedelta_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_timedelta_b.py
    :caption: :download:`Solution <assignments/datetime_timedelta_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_timedelta_c.py
    :caption: :download:`Solution <assignments/datetime_timedelta_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_timedelta_d.py
    :caption: :download:`Solution <assignments/datetime_timedelta_d.py>`
    :end-before: # Solution
