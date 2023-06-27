Import Read SQL
===============
* File paths works also with URLs
* SQL functions uses SQLAlchemy, which supports many RDBMS
* Read SQL query or database table into a DataFrame

>>> import pandas as pd

Read SQL query or database table into a DataFrame:

>>> pd.read_sql()  # doctest: +SKIP

Read SQL query into a DataFrame

>>> pd.read_sql_query()  # doctest: +SKIP

Read SQL database table into a DataFrame

>>> pd.read_sql_table()  # doctest: +SKIP
>>> pd.read_table()  # doctest: +SKIP


Read SQL
--------
>>> import sqlite3
>>> import requests
>>>
>>>
>>> DATA = 'https://python3.info/_static/apollo11.db'
>>> DATABASE = '/tmp/apollo11.db'
>>>
>>> SQL = """
...     SELECT *
...     FROM apollo11
... """
>>>
>>>
>>> # Download database
>>> with open(DATABASE, mode='wb') as db:
...     resp = requests.get(DATA)
...     db.write(resp.content)
49152
>>>
>>>
>>> # Read data from database
>>> with sqlite3.connect(DATABASE) as db:
...     df = pd.read_sql(SQL, db, parse_dates=['datetime', 'date'], index_col='datetime')

>>> df.info(memory_usage='deep')  # doctest: +NORMALIZE_WHITESPACE
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 250 entries, 1969-07-14 21:00:00 to 1969-08-27 00:00:00
Data columns (total 5 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   date      250 non-null    datetime64[ns]
 1   time      250 non-null    object
 2   met       250 non-null    int64
 3   category  250 non-null    object
 4   event     250 non-null    object
dtypes: datetime64[ns](1), int64(1), object(3)
memory usage: 61.9 KB

>>> df['event'].head(n=5)  # doctest: +NORMALIZE_WHITESPACE
datetime
1969-07-14 21:00:00                          Terminal countdown started.
1969-07-15 16:00:00                 Scheduled 11-hour hold at T-9 hours.
1969-07-16 03:00:00                      Countdown resumed at T-9 hours.
1969-07-16 08:30:00    Scheduled 1-hour 32-minute hold at T-3 hours 3...
1969-07-16 10:02:00           Countdown resumed at T-3 hours 30 minutes.
Name: event, dtype: object


Assignments
-----------
