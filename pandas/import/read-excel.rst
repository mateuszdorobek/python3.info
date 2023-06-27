Import Read Excel
=================
* File paths works also with URLs


SetUp
-----
>>> import pandas as pd


Use Case - 0x01
---------------
>>> import pandas as pd
>>>
>>>
>>> DATA = 'https://python3.info/_static/astro-trl.xlsx'
>>>
>>> df = pd.read_excel(
...     io=DATA,
...     sheet_name='Polish',
...     header=1,
...     index_col=0)


Use Case - 0x02
---------------
>>> import pandas as pd
>>>
>>>
>>> DATA = 'https://python3.info/_static/sensors-optima.xlsx'
>>>
>>> df = pd.read_excel(
...     io=DATA,
...     sheet_name='Luminance',
...     header=1,
...     parse_dates=['datetime', 'date', 'time'],
...     index_col='datetime')
