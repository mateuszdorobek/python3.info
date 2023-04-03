DataFrame Aggregations
======================
* ``.count()``
* ``.sum()``
* ``.nunique()``
* ``.mean()``
* ``.median()``
* ``.std()``
* ``.std2()``
* ``.min()``
* ``.quantile()``
* ``.max()``
* ``.first()``
* ``.last()``
* ``lambda column:``


SetUp
-----
>>> import pandas as pd
>>>
>>> pd.set_option('display.width', 250)
>>> pd.set_option('display.max_columns', 20)
>>> pd.set_option('display.max_rows', 30)
>>>
>>>
>>> DATA = 'https://python3.info/_static/phones-en.csv'
>>>
>>> df = (pd
...       .read_csv(DATA, parse_dates=['date'])
...       .drop(columns='index')
... )

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


Single Statistic
----------------
The groupby output will have an index or multi-index on rows corresponding to
your chosen grouping variables. To avoid setting this index, pass
``as_index=False`` to the groupby operation:

>>> df.groupby('month', as_index=False).agg({'duration': 'sum'})
     month   duration
0  2014-11  26639.441
1  2014-12  14641.870
2  2015-01  18223.299
3  2015-02  15522.299
4  2015-03  22750.441


Multiple Statistics per Group
-----------------------------
Group the data frame by month and item and extract a number of stats from each
group:

>>> df.groupby(['month', 'item']).agg({
...     'duration': 'sum',        # Sum duration per group
...     'network_type': 'count',  # get the count of networks
...     'date': 'first',          # get the first date per group
... })  # doctest: +NORMALIZE_WHITESPACE
               duration  network_type                date
month   item
2014-11 call  25547.000           107 2014-10-15 06:58:00
        data    998.441            29 2014-10-15 06:58:00
        sms      94.000            94 2014-10-16 22:18:00
2014-12 call  13561.000            79 2014-11-14 17:24:00
        data   1032.870            30 2014-11-13 06:58:00
        sms      48.000            48 2014-11-14 17:28:00
2015-01 call  17070.000            88 2014-12-15 20:03:00
        data   1067.299            31 2014-12-13 06:58:00
        sms      86.000            86 2014-12-15 19:56:00
2015-02 call  14416.000            67 2015-01-15 10:36:00
        data   1067.299            31 2015-01-13 06:58:00
        sms      39.000            39 2015-01-15 12:23:00
2015-03 call  21727.000            47 2015-12-02 20:15:00
        data    998.441            29 2015-02-13 06:58:00
        sms      25.000            25 2015-02-19 18:46:00


Applying multiple functions to columns in groups
------------------------------------------------
Group the data frame by month and item and extract a number of stats from each
group:

>>> df.groupby(['month', 'item']).agg({
...
...     # Find the min, max, and sum of the duration column
...     'duration': ['min', 'max', 'sum'],
...
...     # find the number of network type entries
...     'network_type': 'count',
...
...     # minimum, first, and number of unique dates
...     'date': ['min', 'first', 'nunique']
... })  # doctest: +NORMALIZE_WHITESPACE
             duration                       network_type                date
                  min        max        sum        count                 min               first nunique
month   item
2014-11 call    1.000   1940.000  25547.000          107 2014-01-11 15:13:00 2014-10-15 06:58:00     104
        data   34.429     34.429    998.441           29 2014-01-11 06:58:00 2014-10-15 06:58:00      29
        sms     1.000      1.000     94.000           94 2014-03-11 08:40:00 2014-10-16 22:18:00      79
2014-12 call    2.000   2120.000  13561.000           79 2014-02-12 11:40:00 2014-11-14 17:24:00      76
        data   34.429     34.429   1032.870           30 2014-01-12 06:58:00 2014-11-13 06:58:00      30
        sms     1.000      1.000     48.000           48 2014-01-12 12:51:00 2014-11-14 17:28:00      41
2015-01 call    2.000   1859.000  17070.000           88 2014-12-15 20:03:00 2014-12-15 20:03:00      84
        data   34.429     34.429   1067.299           31 2014-12-13 06:58:00 2014-12-13 06:58:00      31
        sms     1.000      1.000     86.000           86 2014-12-15 19:56:00 2014-12-15 19:56:00      58
2015-02 call    1.000   1863.000  14416.000           67 2015-01-02 13:33:00 2015-01-15 10:36:00      67
        data   34.429     34.429   1067.299           31 2015-01-02 06:58:00 2015-01-13 06:58:00      31
        sms     1.000      1.000     39.000           39 2015-01-15 12:23:00 2015-01-15 12:23:00      27
2015-03 call    2.000  10528.000  21727.000           47 2015-01-03 12:19:00 2015-12-02 20:15:00      47
        data   34.429     34.429    998.441           29 2015-01-03 06:58:00 2015-02-13 06:58:00      29
        sms     1.000      1.000     25.000           25 2015-02-03 09:19:00 2015-02-19 18:46:00      17


Named Aggregations
------------------
Named Aggregations:

>>> df[df['item'] == 'call'].groupby('month').agg(
...
...     # Get max of the duration column for each group
...     max_duration=('duration', 'max'),
...
...     # Get min of the duration column for each group
...     min_duration=('duration', 'min'),
...
...     # Get sum of the duration column for each group
...     total_duration=('duration', 'sum'),
...
...     # Apply a lambda to date column
...     num_days=('date', lambda x: (max(x) - min(x)).days)
... )  # doctest: +NORMALIZE_WHITESPACE
         max_duration  min_duration  total_duration  num_days
month
2014-11        1940.0           1.0         25547.0       334
2014-12        2120.0           2.0         13561.0       305
2015-01        1859.0           2.0         17070.0       350
2015-02        1863.0           1.0         14416.0       243
2015-03       10528.0           2.0         21727.0       333

>>> df.groupby(['month', 'item']).agg(
...     duration_count=('duration', 'count'),
...     duration_sum=('duration', 'sum'),
...     duration_min=('duration', 'min'),
...     duration_max=('duration', 'max'),
...     duration_mean=('duration', 'mean'),
...     duration_mean_round=('duration', lambda column: column.mean().astype(int)),
...     duration_median=('duration', 'median'),
...     first=('date', 'first'),
...     last=('date', 'last'),
... )  # doctest: +NORMALIZE_WHITESPACE
              duration_count  duration_sum  duration_min  duration_max  duration_mean  duration_mean_round  duration_median               first                last
month   item
2014-11 call             107     25547.000         1.000      1940.000     238.757009                  238           48.000 2014-10-15 06:58:00 2014-12-11 19:01:00
        data              29       998.441        34.429        34.429      34.429000                   34           34.429 2014-10-15 06:58:00 2014-12-11 06:58:00
        sms               94        94.000         1.000         1.000       1.000000                    1            1.000 2014-10-16 22:18:00 2014-11-13 22:31:00
2014-12 call              79     13561.000         2.000      2120.000     171.658228                  171           55.000 2014-11-14 17:24:00 2014-12-14 19:54:00
        data              30      1032.870        34.429        34.429      34.429000                   34           34.429 2014-11-13 06:58:00 2014-12-12 06:58:00
        sms               48        48.000         1.000         1.000       1.000000                    1            1.000 2014-11-14 17:28:00 2014-07-12 23:22:00
2015-01 call              88     17070.000         2.000      1859.000     193.977273                  193           55.500 2014-12-15 20:03:00 2015-01-14 20:47:00
        data              31      1067.299        34.429        34.429      34.429000                   34           34.429 2014-12-13 06:58:00 2015-12-01 06:58:00
        sms               86        86.000         1.000         1.000       1.000000                    1            1.000 2014-12-15 19:56:00 2015-01-14 23:36:00
2015-02 call              67     14416.000         1.000      1863.000     215.164179                  215           89.000 2015-01-15 10:36:00 2015-09-02 17:54:00
        data              31      1067.299        34.429        34.429      34.429000                   34           34.429 2015-01-13 06:58:00 2015-12-02 06:58:00
        sms               39        39.000         1.000         1.000       1.000000                    1            1.000 2015-01-15 12:23:00 2015-10-02 21:40:00
2015-03 call              47     21727.000         2.000     10528.000     462.276596                  462          107.000 2015-12-02 20:15:00 2015-04-03 12:29:00
        data              29       998.441        34.429        34.429      34.429000                   34           34.429 2015-02-13 06:58:00 2015-03-13 06:58:00
        sms               25        25.000         1.000         1.000       1.000000                    1            1.000 2015-02-19 18:46:00 2015-03-14 00:16:00

Renaming index
--------------
* using ``droplevel`` and ``ravel``
* Dictionary ``groupby`` format is deprecated

Drop the top level (using ``.droplevel()``) of the newly created multi-index
on columns using:

>>> grouped = df.groupby('month').agg({'duration': ['min', 'max', 'mean']})
>>> grouped  # doctest: +NORMALIZE_WHITESPACE
        duration
             min      max        mean
month
2014-11      1.0   1940.0  115.823657
2014-12      1.0   2120.0   93.260318
2015-01      1.0   1859.0   88.894141
2015-02      1.0   1863.0  113.301453
2015-03      1.0  10528.0  225.251891

>>> grouped.columns = grouped.columns.droplevel(level=0)
>>> grouped  # doctest: +NORMALIZE_WHITESPACE
         min      max        mean
month
2014-11  1.0   1940.0  115.823657
2014-12  1.0   2120.0   93.260318
2015-01  1.0   1859.0   88.894141
2015-02  1.0   1863.0  113.301453
2015-03  1.0  10528.0  225.251891

>>> grouped.rename(columns={
...     'min': 'min_duration',
...     'max': 'max_duration',
...     'mean': 'mean_duration'
... }, inplace=True)
>>> grouped  # doctest: +NORMALIZE_WHITESPACE
         min_duration  max_duration  mean_duration
month
2014-11           1.0        1940.0     115.823657
2014-12           1.0        2120.0      93.260318
2015-01           1.0        1859.0      88.894141
2015-02           1.0        1863.0     113.301453
2015-03           1.0       10528.0     225.251891

Quick renaming of grouped columns from the groupby() multi-index can be
achieved using the ravel() function:

>>> grouped = df.groupby('month').agg({
...     'duration': ['min', 'max', 'mean']
... })
>>> grouped  # doctest: +NORMALIZE_WHITESPACE
        duration
             min      max        mean
month
2014-11      1.0   1940.0  115.823657
2014-12      1.0   2120.0   93.260318
2015-01      1.0   1859.0   88.894141
2015-02      1.0   1863.0  113.301453
2015-03      1.0  10528.0  225.251891

Using ravel, and a string join, we can create better names for the columns:

>>> grouped.columns = ['_'.join(x) for x in grouped.columns]
>>> grouped  # doctest: +NORMALIZE_WHITESPACE
         duration_min  duration_max  duration_mean
month
2014-11           1.0        1940.0     115.823657
2014-12           1.0        2120.0      93.260318
2015-01           1.0        1859.0      88.894141
2015-02           1.0        1863.0     113.301453
2015-03           1.0       10528.0     225.251891


Use Case - 0x01
---------------
>>> import pandas as pd
>>>
>>>
>>> DATA = 'https://python3.info/_static/phones-pl.csv'
>>>
>>> result = (
...     pd
...     .read_csv(DATA, parse_dates=['datetime'])
...     .set_index('datetime', drop=True)
...     .drop(columns=['id'])
...     .loc['2000-01-01':'2000-03-01']
...     .query('item == "sms"')
...     .groupby(['period','item'])
...     .agg(
...         duration_count = ('duration', 'count'),
...         duration_sum = ('duration', 'sum'),
...         duration_median = ('duration', 'median'),
...         duration_mean = ('duration', 'mean'),
...         duration_std = ('duration', 'std'),
...         duration_var = ('duration', 'var'),
...         value = ('duration', lambda column: column.mean().astype(int))
...     )
... )


Use Case - 0x02
---------------
>>> import pandas as pd
>>>
>>>
>>> def quantile25(column):
...     return column.quantile(.25)
>>>
>>> def quantile50(column):
...     return column.quantile(.50)
>>>
>>> def quantile75(column):
...     return column.quantile(.75)
>>>
>>>
>>> DATA = 'https://python3.info/_static/phones-en.csv'
>>> df = pd.read_csv(DATA, parse_dates=['date'])
>>> df.drop(columns='index', inplace=True)
>>>
>>> result = df.groupby(['month','item']).agg(
...     duration_count=('duration', 'count'),
...     duration_sum=('duration', 'sum'),
...     duration_nunique=('duration', 'nunique'),
...
...     duration_mean=('duration', 'mean'),
...     duration_median=('duration', 'median'),
...     duration_std=('duration', 'std'),
...     duration_std2=('duration', lambda column: column.std().astype(int)),
...
...     duration_min=('duration', 'min'),
...     duration_q25=('duration', quantile25),
...     duration_q50=('duration', quantile50),
...     duration_q75=('duration', quantile75),
...     duration_max=('duration', 'max'),
...
...     when_first=('date', 'first'),
...     when_last=('date', 'last'),
... )
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
              duration_count  duration_sum  duration_nunique  duration_mean  duration_median  duration_std  duration_std2  duration_min  duration_q25  duration_q50  duration_q75  duration_max          when_first           when_last
month   item
2014-11 call             107     25547.000                76     238.757009           48.000    387.128905            387         1.000         5.500        48.000       328.000      1940.000 2014-10-15 06:58:00 2014-12-11 19:01:00
        data              29       998.441                 1      34.429000           34.429      0.000000              0        34.429        34.429        34.429        34.429        34.429 2014-10-15 06:58:00 2014-12-11 06:58:00
        sms               94        94.000                 1       1.000000            1.000      0.000000              0         1.000         1.000         1.000         1.000         1.000 2014-10-16 22:18:00 2014-11-13 22:31:00
2014-12 call              79     13561.000                61     171.658228           55.000    324.731798            324         2.000        10.500        55.000       152.000      2120.000 2014-11-14 17:24:00 2014-12-14 19:54:00
        data              30      1032.870                 1      34.429000           34.429      0.000000              0        34.429        34.429        34.429        34.429        34.429 2014-11-13 06:58:00 2014-12-12 06:58:00
        sms               48        48.000                 1       1.000000            1.000      0.000000              0         1.000         1.000         1.000         1.000         1.000 2014-11-14 17:28:00 2014-07-12 23:22:00
2015-01 call              88     17070.000                70     193.977273           55.500    300.671661            300         2.000        15.500        55.500       273.500      1859.000 2014-12-15 20:03:00 2015-01-14 20:47:00
        data              31      1067.299                 1      34.429000           34.429      0.000000              0        34.429        34.429        34.429        34.429        34.429 2014-12-13 06:58:00 2015-12-01 06:58:00
        sms               86        86.000                 1       1.000000            1.000      0.000000              0         1.000         1.000         1.000         1.000         1.000 2014-12-15 19:56:00 2015-01-14 23:36:00
2015-02 call              67     14416.000                63     215.164179           89.000    329.672914            329         1.000        30.000        89.000       241.000      1863.000 2015-01-15 10:36:00 2015-09-02 17:54:00
        data              31      1067.299                 1      34.429000           34.429      0.000000              0        34.429        34.429        34.429        34.429        34.429 2015-01-13 06:58:00 2015-12-02 06:58:00
        sms               39        39.000                 1       1.000000            1.000      0.000000              0         1.000         1.000         1.000         1.000         1.000 2015-01-15 12:23:00 2015-10-02 21:40:00
2015-03 call              47     21727.000                46     462.276596          107.000   1552.192218           1552         2.000        33.500       107.000       320.000     10528.000 2015-12-02 20:15:00 2015-04-03 12:29:00
        data              29       998.441                 1      34.429000           34.429      0.000000              0        34.429        34.429        34.429        34.429        34.429 2015-02-13 06:58:00 2015-03-13 06:58:00
        sms               25        25.000                 1       1.000000            1.000      0.000000              0         1.000         1.000         1.000         1.000         1.000 2015-02-19 18:46:00 2015-03-14 00:16:00

>>> result.loc[('2015-01','call')]
duration_count                       88
duration_sum                    17070.0
duration_nunique                     70
duration_mean                193.977273
duration_median                    55.5
duration_std                 300.671661
duration_std2                       300
duration_min                        2.0
duration_q25                       15.5
duration_q50                       55.5
duration_q75                      273.5
duration_max                     1859.0
when_first          2014-12-15 20:03:00
when_last           2015-01-14 20:47:00
Name: (2015-01, call), dtype: object

>>> result.loc['2015-01']  # doctest: +NORMALIZE_WHITESPACE
      duration_count  duration_sum  duration_nunique  duration_mean  duration_median  duration_std  duration_std2  duration_min  duration_q25  duration_q50  duration_q75  duration_max          when_first           when_last
item
call              88     17070.000                70     193.977273           55.500    300.671661            300         2.000        15.500        55.500       273.500      1859.000 2014-12-15 20:03:00 2015-01-14 20:47:00
data              31      1067.299                 1      34.429000           34.429      0.000000              0        34.429        34.429        34.429        34.429        34.429 2014-12-13 06:58:00 2015-12-01 06:58:00
sms               86        86.000                 1       1.000000            1.000      0.000000              0         1.000         1.000         1.000         1.000         1.000 2014-12-15 19:56:00 2015-01-14 23:36:00

>>> result.loc['2015-01'].transpose()
item                             call                 data                  sms
duration_count                     88                   31                   86
duration_sum                  17070.0             1067.299                 86.0
duration_nunique                   70                    1                    1
duration_mean              193.977273               34.429                  1.0
duration_median                  55.5               34.429                  1.0
duration_std               300.671661                  0.0                  0.0
duration_std2                     300                    0                    0
duration_min                      2.0               34.429                  1.0
duration_q25                     15.5               34.429                  1.0
duration_q50                     55.5               34.429                  1.0
duration_q75                    273.5               34.429                  1.0
duration_max                   1859.0               34.429                  1.0
when_first        2014-12-15 20:03:00  2014-12-13 06:58:00  2014-12-15 19:56:00
when_last         2015-01-14 20:47:00  2015-12-01 06:58:00  2015-01-14 23:36:00

>>> sms = result.index.get_level_values('item') == 'sms'
>>> sms
array([False, False,  True, False, False,  True, False, False,  True,
       False, False,  True, False, False,  True])
>>>
>>> result[sms]  # doctest: +NORMALIZE_WHITESPACE
              duration_count  duration_sum  duration_nunique  duration_mean  duration_median  duration_std  duration_std2  duration_min  duration_q25  duration_q50  duration_q75  duration_max          when_first           when_last
month   item
2014-11 sms               94          94.0                 1            1.0              1.0           0.0              0           1.0           1.0           1.0           1.0           1.0 2014-10-16 22:18:00 2014-11-13 22:31:00
2014-12 sms               48          48.0                 1            1.0              1.0           0.0              0           1.0           1.0           1.0           1.0           1.0 2014-11-14 17:28:00 2014-07-12 23:22:00
2015-01 sms               86          86.0                 1            1.0              1.0           0.0              0           1.0           1.0           1.0           1.0           1.0 2014-12-15 19:56:00 2015-01-14 23:36:00
2015-02 sms               39          39.0                 1            1.0              1.0           0.0              0           1.0           1.0           1.0           1.0           1.0 2015-01-15 12:23:00 2015-10-02 21:40:00
2015-03 sms               25          25.0                 1            1.0              1.0           0.0              0           1.0           1.0           1.0           1.0           1.0 2015-02-19 18:46:00 2015-03-14 00:16:00

Cross-section:

>>> result.xs('sms', level='item')  # doctest: +NORMALIZE_WHITESPACE
         duration_count  duration_sum  duration_nunique  duration_mean  duration_median  duration_std  duration_std2  duration_min  duration_q25  duration_q50  duration_q75  duration_max          when_first           when_last
month
2014-11              94          94.0                 1            1.0              1.0           0.0              0           1.0           1.0           1.0           1.0           1.0 2014-10-16 22:18:00 2014-11-13 22:31:00
2014-12              48          48.0                 1            1.0              1.0           0.0              0           1.0           1.0           1.0           1.0           1.0 2014-11-14 17:28:00 2014-07-12 23:22:00
2015-01              86          86.0                 1            1.0              1.0           0.0              0           1.0           1.0           1.0           1.0           1.0 2014-12-15 19:56:00 2015-01-14 23:36:00
2015-02              39          39.0                 1            1.0              1.0           0.0              0           1.0           1.0           1.0           1.0           1.0 2015-01-15 12:23:00 2015-10-02 21:40:00
2015-03              25          25.0                 1            1.0              1.0           0.0              0           1.0           1.0           1.0           1.0           1.0 2015-02-19 18:46:00 2015-03-14 00:16:00

Slicer Object:

>>> result.loc[(slice(None), 'sms'), :]  # doctest: +NORMALIZE_WHITESPACE
              duration_count  duration_sum  duration_nunique  duration_mean  duration_median  duration_std  duration_std2  duration_min  duration_q25  duration_q50  duration_q75  duration_max          when_first           when_last
month   item
2014-11 sms               94          94.0                 1            1.0              1.0           0.0              0           1.0           1.0           1.0           1.0           1.0 2014-10-16 22:18:00 2014-11-13 22:31:00
2014-12 sms               48          48.0                 1            1.0              1.0           0.0              0           1.0           1.0           1.0           1.0           1.0 2014-11-14 17:28:00 2014-07-12 23:22:00
2015-01 sms               86          86.0                 1            1.0              1.0           0.0              0           1.0           1.0           1.0           1.0           1.0 2014-12-15 19:56:00 2015-01-14 23:36:00
2015-02 sms               39          39.0                 1            1.0              1.0           0.0              0           1.0           1.0           1.0           1.0           1.0 2015-01-15 12:23:00 2015-10-02 21:40:00
2015-03 sms               25          25.0                 1            1.0              1.0           0.0              0           1.0           1.0           1.0           1.0           1.0 2015-02-19 18:46:00 2015-03-14 00:16:00


References
----------
.. [#PandasAggregations] Lynn, Shane. Summarising, Aggregating, and Grouping data in Python Pandas. https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/ Access date: 2019-12-03. 2019.


.. todo:: Assignments
