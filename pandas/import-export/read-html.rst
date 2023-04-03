Pandas Read HTML
================
* File paths works also with URLs


SetUp
-----
>>> import pandas as pd
>>>
>>> pd.set_option('display.width', 250)
>>> pd.set_option('display.max_columns', 20)
>>> pd.set_option('display.max_rows', 30)


Read HTML
---------
>>> DATA = 'https://python3.info/_static/apollo11.html'
>>>
>>> tables = pd.read_html(DATA)
>>> df = tables[0]
>>>
>>> df.head(n=5)
                                                   0                 1          2            3
0                                              Event  GET  (hhh:mm:ss)  GMT  Time    GMT  Date
1                       Terminal countdown  started.        -028:00:00   21:00:00  14 Jul 1969
2              Scheduled 11-hour hold  at T-9 hours.        -009:00:00   16:00:00  15 Jul 1969
3                   Countdown resumed at  T-9 hours.        -009:00:00   03:00:00  16 Jul 1969
4  Scheduled 1-hour  32-minute hold at T-3 hours ...        -003:30:00   08:30:00  16 Jul 1969


User Agent
----------
>>> import requests
>>>
>>>
>>> DATA = 'https://python3.info/_static/apollo11.html'
>>> USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
...              '(KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
>>>
>>> resp = requests.get(DATA, headers={'User-Agent': USER_AGENT})
>>> tables = pd.read_html(resp.content)
>>> df = tables[0]
>>>
>>> df.head(n=5)
                                                   0                 1          2            3
0                                              Event  GET  (hhh:mm:ss)  GMT  Time    GMT  Date
1                       Terminal countdown  started.        -028:00:00   21:00:00  14 Jul 1969
2              Scheduled 11-hour hold  at T-9 hours.        -009:00:00   16:00:00  15 Jul 1969
3                   Countdown resumed at  T-9 hours.        -009:00:00   03:00:00  16 Jul 1969
4  Scheduled 1-hour  32-minute hold at T-3 hours ...        -003:30:00   08:30:00  16 Jul 1969


Assignments
-----------
.. literalinclude:: assignments/pandas_readhtml_a.py
    :caption: :download:`Solution <assignments/pandas_readhtml_a.py>`
    :end-before: # Solution
