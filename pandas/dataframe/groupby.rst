DataFrame Group By
==================
* ``.size()``
* ``.mean()``
* ``.nunique()``
* ``.sum()``
* ``.count()``
* ``.max()``
* ``.first()``


SetUp
-----
>>> import pandas as pd
>>>
>>>
>>> DATA = 'https://python3.info/_static/phones-en.csv'
>>>
>>> df = pd.read_csv(DATA, parse_dates=['date'])
>>> df.drop(columns='index', inplace=True)

date
    The date and time of the entry

duration
    The duration (in seconds) for each call, the amount of data (in MB) for
    each data entry, and the number of texts sent (usually 1) for each sms
    entry

item
    A description of the event occurring – can be one of call, sms, or data

month
    The billing month that each entry belongs to – of form ``YYYY-MM``

network
    The mobile network that was called/texted for each entry

network_type
    Whether the number being called was a mobile, international ('world'),
    voicemail, landline, or other ('special') number.

Source [#PandasAggregations]_


Grouping
--------
Group by one item:

>>> df.groupby('item')  # doctest: +ELLIPSIS
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x...>

Group by multiple items:

>>> df.groupby(['month', 'item'])  # doctest: +ELLIPSIS
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x...>


Groupby Methods
---------------
* Group series using mapper (dict or key function, apply given function to group, return result as series) or by a series of columns
* ``.size()``
* ``.mean()``
* ``.nunique()``
* ``.sum()``
* ``.count()``
* ``.max()``
* ``.first()``


Size
----
>>> df.groupby('item').size()
item
call    388
data    150
sms     292
dtype: int64

>>> df.groupby(['month', 'item']).size()
month    item
2014-11  call    107
         data     29
         sms      94
2014-12  call     79
         data     30
         sms      48
2015-01  call     88
         data     31
         sms      86
2015-02  call     67
         data     31
         sms      39
2015-03  call     47
         data     29
         sms      25
dtype: int64


Mean
----
>>> df.groupby('item')['duration'].mean()
item
call    237.940722
data     34.429000
sms       1.000000
Name: duration, dtype: float64

>>> df.groupby(['month', 'item'])['duration'].mean()
month    item
2014-11  call    238.757009
         data     34.429000
         sms       1.000000
2014-12  call    171.658228
         data     34.429000
         sms       1.000000
2015-01  call    193.977273
         data     34.429000
         sms       1.000000
2015-02  call    215.164179
         data     34.429000
         sms       1.000000
2015-03  call    462.276596
         data     34.429000
         sms       1.000000
Name: duration, dtype: float64


Number of Uniques
-----------------
>>> df.groupby('item').nunique()  # doctest: +NORMALIZE_WHITESPACE
      date  duration  month  network  network_type
item
call   378       220      5        6             3
data   150         1      5        1             1
sms    222         1      5        6             3

>>> df.groupby(['month', 'item']).nunique()  # doctest: +NORMALIZE_WHITESPACE
              date  duration  network  network_type
month   item
2014-11 call   104        76        6             3
        data    29         1        1             1
        sms     79         1        5             2
2014-12 call    76        61        6             3
        data    30         1        1             1
        sms     41         1        5             2
2015-01 call    84        70        6             3
        data    31         1        1             1
        sms     58         1        4             1
2015-02 call    67        63        6             3
        data    31         1        1             1
        sms     27         1        5             2
2015-03 call    47        46        6             3
        data    29         1        1             1
        sms     17         1        4             2


Sum
---
>>> df.groupby('item')['duration'].sum()  # doctest: +NORMALIZE_WHITESPACE
item
call    92321.00
data     5164.35
sms       292.00
Name: duration, dtype: float64

>>> df.groupby(['month', 'item'])['duration'].sum()  # doctest: +NORMALIZE_WHITESPACE
month    item
2014-11  call    25547.000
         data      998.441
         sms        94.000
2014-12  call    13561.000
         data     1032.870
         sms        48.000
2015-01  call    17070.000
         data     1067.299
         sms        86.000
2015-02  call    14416.000
         data     1067.299
         sms        39.000
2015-03  call    21727.000
         data      998.441
         sms        25.000
Name: duration, dtype: float64


Count
-----
>>> df.groupby('item').count()  # doctest: +NORMALIZE_WHITESPACE
      date  duration  month  network  network_type
item
call   388       388    388      388           388
data   150       150    150      150           150
sms    292       292    292      292           292

>>> df.groupby(['month', 'item']).count()  # doctest: +NORMALIZE_WHITESPACE
              date  duration  network  network_type
month   item
2014-11 call   107       107      107           107
        data    29        29       29            29
        sms     94        94       94            94
2014-12 call    79        79       79            79
        data    30        30       30            30
        sms     48        48       48            48
2015-01 call    88        88       88            88
        data    31        31       31            31
        sms     86        86       86            86
2015-02 call    67        67       67            67
        data    31        31       31            31
        sms     39        39       39            39
2015-03 call    47        47       47            47
        data    29        29       29            29
        sms     25        25       25            25


Minimum
-------
>>> df.groupby('item').min()  # doctest: +NORMALIZE_WHITESPACE
                    date  duration    month network network_type
item
call 2014-01-11 15:13:00     1.000  2014-11  Meteor     landline
data 2014-01-11 06:58:00    34.429  2014-11    data         data
sms  2014-01-12 12:51:00     1.000  2014-11  Meteor       mobile

>>> df.groupby(['month', 'item']).min()  # doctest: +NORMALIZE_WHITESPACE
                            date  duration network network_type
month   item
2014-11 call 2014-01-11 15:13:00     1.000  Meteor     landline
        data 2014-01-11 06:58:00    34.429    data         data
        sms  2014-03-11 08:40:00     1.000  Meteor       mobile
2014-12 call 2014-02-12 11:40:00     2.000  Meteor     landline
        data 2014-01-12 06:58:00    34.429    data         data
        sms  2014-01-12 12:51:00     1.000  Meteor       mobile
2015-01 call 2014-12-15 20:03:00     2.000  Meteor     landline
        data 2014-12-13 06:58:00    34.429    data         data
        sms  2014-12-15 19:56:00     1.000  Meteor       mobile
2015-02 call 2015-01-02 13:33:00     1.000  Meteor     landline
        data 2015-01-02 06:58:00    34.429    data         data
        sms  2015-01-15 12:23:00     1.000  Meteor       mobile
2015-03 call 2015-01-03 12:19:00     2.000  Meteor     landline
        data 2015-01-03 06:58:00    34.429    data         data
        sms  2015-02-03 09:19:00     1.000   Tesco       mobile


Maximum
-------
>>> df.groupby('item').max()  # doctest: +NORMALIZE_WHITESPACE
                    date   duration    month    network network_type
item
call 2015-12-02 20:51:00  10528.000  2015-03  voicemail    voicemail
data 2015-12-03 06:58:00     34.429  2015-03       data         data
sms  2015-12-01 18:26:00      1.000  2015-03      world        world

>>> df.groupby(['month', 'item']).max()  # doctest: +NORMALIZE_WHITESPACE
                            date   duration    network network_type
month   item
2014-11 call 2014-12-11 19:01:00   1940.000  voicemail    voicemail
        data 2014-12-11 06:58:00     34.429       data         data
        sms  2014-12-11 19:20:00      1.000    special      special
2014-12 call 2014-12-14 19:54:00   2120.000  voicemail    voicemail
        data 2014-12-12 06:58:00     34.429       data         data
        sms  2014-11-30 14:44:00      1.000      world        world
2015-01 call 2015-12-01 18:23:00   1859.000  voicemail    voicemail
        data 2015-12-01 06:58:00     34.429       data         data
        sms  2015-12-01 18:26:00      1.000   Vodafone       mobile
2015-02 call 2015-09-02 17:54:00   1863.000  voicemail    voicemail
        data 2015-12-02 06:58:00     34.429       data         data
        sms  2015-10-02 21:40:00      1.000    special      special
2015-03 call 2015-12-02 20:51:00  10528.000  voicemail    voicemail
        data 2015-12-03 06:58:00     34.429       data         data
        sms  2015-04-03 10:30:00      1.000      world        world


First
-----
>>> df.groupby('item').first()  # doctest: +NORMALIZE_WHITESPACE
                    date  duration    month   network network_type
item
call 2014-10-15 06:58:00    13.000  2014-11  Vodafone       mobile
data 2014-10-15 06:58:00    34.429  2014-11      data         data
sms  2014-10-16 22:18:00     1.000  2014-11    Meteor       mobile

>>> df.groupby(['month', 'item']).first()  # doctest: +NORMALIZE_WHITESPACE
                            date  duration    network network_type
month   item
2014-11 call 2014-10-15 06:58:00    13.000   Vodafone       mobile
        data 2014-10-15 06:58:00    34.429       data         data
        sms  2014-10-16 22:18:00     1.000     Meteor       mobile
2014-12 call 2014-11-14 17:24:00   124.000  voicemail    voicemail
        data 2014-11-13 06:58:00    34.429       data         data
        sms  2014-11-14 17:28:00     1.000   Vodafone       mobile
2015-01 call 2014-12-15 20:03:00     4.000      Three       mobile
        data 2014-12-13 06:58:00    34.429       data         data
        sms  2014-12-15 19:56:00     1.000      Three       mobile
2015-02 call 2015-01-15 10:36:00    28.000      Three       mobile
        data 2015-01-13 06:58:00    34.429       data         data
        sms  2015-01-15 12:23:00     1.000    special      special
2015-03 call 2015-12-02 20:15:00    69.000   landline     landline
        data 2015-02-13 06:58:00    34.429       data         data
        sms  2015-02-19 18:46:00     1.000   Vodafone       mobile


Last
----
>>> df.groupby('item').last()  # doctest: +NORMALIZE_WHITESPACE
                    date   duration    month   network network_type
item
call 2015-04-03 12:29:00  10528.000  2015-03  landline     landline
data 2015-03-13 06:58:00     34.429  2015-03      data         data
sms  2015-03-14 00:16:00      1.000  2015-03     world        world

>>> df.groupby(['month', 'item']).last()  # doctest: +NORMALIZE_WHITESPACE
                            date   duration   network network_type
month   item
2014-11 call 2014-12-11 19:01:00      7.000  Vodafone       mobile
        data 2014-12-11 06:58:00     34.429      data         data
        sms  2014-11-13 22:31:00      1.000  Vodafone       mobile
2014-12 call 2014-12-14 19:54:00     25.000     Three       mobile
        data 2014-12-12 06:58:00     34.429      data         data
        sms  2014-07-12 23:22:00      1.000     world        world
2015-01 call 2015-01-14 20:47:00     36.000     Three       mobile
        data 2015-12-01 06:58:00     34.429      data         data
        sms  2015-01-14 23:36:00      1.000     Three       mobile
2015-02 call 2015-09-02 17:54:00     89.000     Three       mobile
        data 2015-12-02 06:58:00     34.429      data         data
        sms  2015-10-02 21:40:00      1.000  Vodafone       mobile
2015-03 call 2015-04-03 12:29:00  10528.000  landline     landline
        data 2015-03-13 06:58:00     34.429      data         data
        sms  2015-03-14 00:16:00      1.000     world        world


Output format
-------------
* Series or DataFrame?

Produces Pandas Series:

>>> df.groupby('month')['duration'].sum()  # doctest: +NORMALIZE_WHITESPACE
month
2014-11    26639.441
2014-12    14641.870
2015-01    18223.299
2015-02    15522.299
2015-03    22750.441
Name: duration, dtype: float64

Produces Pandas DataFrame:

>>> df.groupby('month')[['duration']].sum()  # doctest: +NORMALIZE_WHITESPACE
          duration
month
2014-11  26639.441
2014-12  14641.870
2015-01  18223.299
2015-02  15522.299
2015-03  22750.441


Use Case - 0x01
---------------
>>> list(df.groupby(['month']).groups.keys())
['2014-11', '2014-12', '2015-01', '2015-02', '2015-03']

>>> len(df.groupby(['month']).groups['2014-11'])
230


Use Case - 0x02
---------------
Get the first entry for each month:

>>> df.groupby('month').first()  # doctest: +NORMALIZE_WHITESPACE
                       date  duration  item   network network_type
month
2014-11 2014-10-15 06:58:00    34.429  data      data         data
2014-12 2014-11-13 06:58:00    34.429  data      data         data
2015-01 2014-12-13 06:58:00    34.429  data      data         data
2015-02 2015-01-13 06:58:00    34.429  data      data         data
2015-03 2015-12-02 20:15:00    69.000  call  landline     landline


Use Case - 0x03
---------------
Get the sum of the durations per month:

>>> df.groupby('month')['duration'].sum()  # doctest: +NORMALIZE_WHITESPACE
month
2014-11    26639.441
2014-12    14641.870
2015-01    18223.299
2015-02    15522.299
2015-03    22750.441
Name: duration, dtype: float64


Use Case - 0x04
---------------
Get the number of dates / entries in each month:

>>> df.groupby('month')['date'].count()  # doctest: +NORMALIZE_WHITESPACE
month
2014-11    230
2014-12    157
2015-01    205
2015-02    137
2015-03    101
Name: date, dtype: int64


Use Case - 0x05
---------------
What is the sum of durations, for calls only, to each network:

>>> df.loc[df['item'] == 'call'].groupby('network')['duration'].sum()  # doctest: +NORMALIZE_WHITESPACE
network
Meteor        7200.0
Tesco        13828.0
Three        36464.0
Vodafone     14621.0
landline     18433.0
voicemail     1775.0
Name: duration, dtype: float64


Use Case - 0x06
---------------
How many calls, sms, and data entries are in each month?:

>>> df.groupby(['month', 'item'])['date'].count()  # doctest: +NORMALIZE_WHITESPACE
month    item
2014-11  call    107
         data     29
         sms      94
2014-12  call     79
         data     30
         sms      48
2015-01  call     88
         data     31
         sms      86
2015-02  call     67
         data     31
         sms      39
2015-03  call     47
         data     29
         sms      25
Name: date, dtype: int64


Use Case - 0x07
---------------
How many calls, texts, and data are sent per month, split by network_type?:

>>> df.groupby(['month', 'network_type'])['date'].count()  # doctest: +NORMALIZE_WHITESPACE
month    network_type
2014-11  data             29
         landline          5
         mobile          189
         special           1
         voicemail         6
2014-12  data             30
         landline          7
         mobile          108
         voicemail         8
         world             4
2015-01  data             31
         landline         11
         mobile          160
         voicemail         3
2015-02  data             31
         landline          8
         mobile           90
         special           2
         voicemail         6
2015-03  data             29
         landline         11
         mobile           54
         voicemail         4
         world             3
Name: date, dtype: int64


Datasets
--------
* https://finance.yahoo.com/quote/SPCE/history
* https://www.kaggle.com/jessemostipak/astronaut-database
* https://www.kaggle.com/nasa/astronaut-yearbook
* https://www.kaggle.com/samruddhim/international-astronaut-database
* https://www.kaggle.com/spacex/spacex-missions
* https://www.kaggle.com/rosetabares/spacemissionsflightstatus
* https://www.kaggle.com/rohanrao/rspacex-data
* https://www.kaggle.com/agirlcoding/all-space-missions-from-1957


References
----------
.. [#PandasAggregations] Lynn, Shane. Summarising, Aggregating, and Grouping data in Python Pandas. https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/ Access date: 2019-12-03. 2019.


Assignments
-----------
.. literalinclude:: assignments/pandas_df_groupby_a.py
    :caption: :download:`Solution <assignments/pandas_df_groupby_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_df_groupby_b.py
    :caption: :download:`Solution <assignments/pandas_df_groupby_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_df_groupby_c.py
    :caption: :download:`Solution <assignments/pandas_df_groupby_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_df_groupby_d.py
    :caption: :download:`Solution <assignments/pandas_df_groupby_d.py>`
    :end-before: # Solution
