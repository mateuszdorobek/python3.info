Date Calendar
=============


Business Days
-------------
>>> import pandas as pd
>>> from pandas.tseries.holiday import USFederalHolidayCalendar
>>> from pandas.tseries.offsets import CustomBusinessDay
>>>
>>>
>>> pd.date_range(
...     start='2000-12-20',
...     end='2000-12-31',
...     freq= CustomBusinessDay(calendar=USFederalHolidayCalendar()))  # doctest: +NORMALIZE_WHITESPACE
DatetimeIndex(['2000-12-20', '2000-12-21', '2000-12-22', '2000-12-26',
               '2000-12-27', '2000-12-28', '2000-12-29'],
               dtype='datetime64[ns]', freq='C')


Business Hours
--------------
>>> from datetime import datetime, time
>>> import pandas as pd
>>> from pandas.tseries.holiday import USFederalHolidayCalendar
>>>
>>>
>>> today = datetime(2020, 1, 4, 15, 0, 0)
>>>
>>> BUSINESS_HOURS = pd.offsets.CustomBusinessHour(
...     calendar=USFederalHolidayCalendar(),
...     start='08:00',
...     end=time(16, 0),
...     weekmask='Mon Tue Wed Thu Fri')
>>>
>>>
>>> today + 5*BUSINESS_HOURS
Timestamp('2020-01-06 13:00:00')


Custom Calendar
---------------
>>> import pandas as pd
>>> from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, EasterMonday, Easter
>>> from pandas.tseries.offsets import Day, CustomBusinessDay, CustomBusinessHour
>>>
>>>
>>> class PLHolidayCalendar(AbstractHolidayCalendar):
...     """
...     Custom Holiday calendar for Poland based on
...     https://en.wikipedia.org/wiki/Public_holidays_in_Poland
...     """
...     rules = [
...         Holiday('New Years Day', month=1, day=1),
...         Holiday('Epiphany', month=1, day=6),
...         Holiday('Easter', month=1, day=1, offset=[Easter()]),
...         EasterMonday,
...         Holiday('May Day', month=5, day=1),
...         Holiday('Constitution Day', month=5, day=3),
...         Holiday('Pentecost Sunday', month=1, day=1, offset=[Easter(), Day(49)]),
...         Holiday('Corpus Christi', month=1, day=1, offset=[Easter(), Day(60)]),
...         Holiday('Assumption of the Blessed Virgin Mary', month=8, day=15),
...         Holiday('All Saints Day', month=11, day=1),
...         Holiday('Independence Day', month=11, day=11),
...         Holiday('Christmas Day', month=12, day=25),
...         Holiday('Second Day of Christmastide', month=12, day=26),
...     ]

>>> pl_holidays_2000 = PLHolidayCalendar().holidays(start='2000-01-01', end='2000-12-31')
>>> pl_holidays_2000  # doctest: +NORMALIZE_WHITESPACE
DatetimeIndex(['2000-01-01', '2000-01-06', '2000-04-23', '2000-04-24',
               '2000-05-01', '2000-05-03', '2000-06-11', '2000-06-22',
               '2000-08-15', '2000-11-01', '2000-11-11', '2000-12-25',
               '2000-12-26'], dtype='datetime64[ns]', freq=None)


Custom mask
-----------
>>> import pandas as pd
>>>
>>> jan2000 = pd.bdate_range(start='2000-01-01',
...                          end='2000-01-31',
...                          freq='C',
...                          weekmask='Mon Tue Wed Thu Fri',
...                          holidays=['2000-01-01', '2000-01-06'])
>>>
>>> jan2000
DatetimeIndex(['2000-01-03', '2000-01-04', '2000-01-05', '2000-01-07',
               '2000-01-10', '2000-01-11', '2000-01-12', '2000-01-13',
               '2000-01-14', '2000-01-17', '2000-01-18', '2000-01-19',
               '2000-01-20', '2000-01-21', '2000-01-24', '2000-01-25',
               '2000-01-26', '2000-01-27', '2000-01-28', '2000-01-31'],
              dtype='datetime64[ns]', freq='C')


Use Case - 0x01
---------------
>>> import pandas as pd
>>> from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, EasterMonday, Easter
>>> from pandas.tseries.offsets import Day, CustomBusinessDay, CustomBusinessHour
>>>
>>>
>>> class PLHolidayCalendar(AbstractHolidayCalendar):
...     """
...     Custom Holiday calendar for Poland based on
...     https://en.wikipedia.org/wiki/Public_holidays_in_Poland
...     """
...     rules = [
...         Holiday('New Years Day', month=1, day=1),
...         Holiday('Epiphany', month=1, day=6),
...         Holiday('Easter', month=1, day=1, offset=[Easter()]),
...         EasterMonday,
...         Holiday('May Day', month=5, day=1),
...         Holiday('Constitution Day', month=5, day=3),
...         Holiday('Pentecost Sunday', month=1, day=1, offset=[Easter(), Day(49)]),
...         Holiday('Corpus Christi', month=1, day=1, offset=[Easter(), Day(60)]),
...         Holiday('Assumption of the Blessed Virgin Mary', month=8, day=15),
...         Holiday('All Saints Day', month=11, day=1),
...         Holiday('Independence Day', month=11, day=11),
...         Holiday('Christmas Day', month=12, day=25),
...         Holiday('Second Day of Christmastide', month=12, day=26),
...     ]

>>> BUSINESS_DAY = CustomBusinessDay(
...     calendar=PLHolidayCalendar(),
...     weekmask='Mon Tue Wed Thu Fri')
>>>
>>> BUSINESS_HOURS = CustomBusinessHour(
...     calendar=PLHolidayCalendar(),
...     start='08:00',
...     end='16:00',
...     weekmask='Mon Tue Wed Thu Fri')

>>> today = pd.Timestamp('2000-01-01 00:00')
>>>
>>>
>>> today + 2*BUSINESS_DAY
Timestamp('2000-01-04 00:00:00')
>>>
>>> today + 3*BUSINESS_DAY
Timestamp('2000-01-05 00:00:00')
>>>
>>> today + 4*BUSINESS_DAY
Timestamp('2000-01-07 00:00:00')
>>>
>>> today + 5*BUSINESS_DAY
Timestamp('2000-01-10 00:00:00')

>>> now = pd.Timestamp('2000-01-01 00:00')
>>>
>>>
>>> now + 23*BUSINESS_HOURS
Timestamp('2000-01-05 15:00:00')
>>>
>>> now + 24*BUSINESS_HOURS
Timestamp('2000-01-07 08:00:00')
>>>
>>> now + 25*BUSINESS_HOURS
Timestamp('2000-01-07 09:00:00')
>>>
>>> now + 26*BUSINESS_HOURS
Timestamp('2000-01-07 10:00:00')
