DataFrame Index
===============
* ``DataFrame.index``
* ``pd.DataFrame(index=...)``
* Range Index
* Index
* Object Index
* Datetime Index
* Timedelta Index
* Period Index
* Interval Index
* Categorical Index
* Multi Index


SetUp
-----
>>> import pandas as pd
>>> import numpy as np


Deprecation
-----------
.. note:: Non-monotonic indexes require exact matches. If the index of a Series
          or DataFrame is monotonically increasing or decreasing, then the
          bounds of a label-based slice can be outside the range of the index,
          much like slice indexing a normal Python list. Monotonicity of an
          index can be tested with the is_monotonic_increasing() and
          is_monotonic_decreasing() attributes. [#pdDocAdvanced]_

.. note:: Compared with standard Python sequence slicing in which the slice
          endpoint is not inclusive, label-based slicing in pandas is
          inclusive. The primary reason for this is that it is often not
          possible to easily determine the "successor" or next element after
          a particular label in an index. [#pdDocAdvanced]_

>>> pd.Index([1, 2, 3], dtype='int64')
Index([1, 2, 3], dtype='int64')


Range Index
-----------
>>> df = pd.DataFrame({
...     'A': [10, 11, 12],
...     'B': [20, 21, 22],
...     'C': [30, 31, 32]})
>>>
>>> df
    A   B   C
0  10  20  30
1  11  21  31
2  12  22  32
>>>
>>> df.index
RangeIndex(start=0, stop=3, step=1)


Integer Index
-------------
* Int64Index, UInt64Index and Float64Index have been deprecated in favor of
  the base Index class and will be removed in Pandas 2.0 [#pd14releasenotes]_

>>> df = pd.DataFrame(
...     data = np.arange(16).reshape(4,4),
...     index = [99, 88, 77, 66],
...     columns = ['A', 'B', 'C', 'D'])
>>>
>>> df
     A   B   C   D
99   0   1   2   3
88   4   5   6   7
77   8   9  10  11
66  12  13  14  15
>>>
>>> df.index
Index([99, 88, 77, 66], dtype='int64')


Object Index
------------
>>> df = pd.DataFrame(
...     data = np.arange(16).reshape(4,4),
...     index = ['a', 'b', 'c', 'd'],
...     columns = ['A', 'B', 'C', 'D'])
>>>
>>> df
    A   B   C   D
a   0   1   2   3
b   4   5   6   7
c   8   9  10  11
d  12  13  14  15
>>>
>>> df.index
Index(['a', 'b', 'c', 'd'], dtype='object')


Datetime Index
--------------
>>> np.random.seed(0)
>>>
>>>
>>> df = pd.DataFrame(
...     columns = ['Morning', 'Noon', 'Evening', 'Midnight'],
...     index = pd.date_range('1999-12-30', periods=7),
...     data = np.random.randn(7, 4))
>>>
>>> df
             Morning      Noon   Evening  Midnight
1999-12-30  1.764052  0.400157  0.978738  2.240893
1999-12-31  1.867558 -0.977278  0.950088 -0.151357
2000-01-01 -0.103219  0.410599  0.144044  1.454274
2000-01-02  0.761038  0.121675  0.443863  0.333674
2000-01-03  1.494079 -0.205158  0.313068 -0.854096
2000-01-04 -2.552990  0.653619  0.864436 -0.742165
2000-01-05  2.269755 -1.454366  0.045759 -0.187184
>>>
>>> df.index
DatetimeIndex(['1999-12-30', '1999-12-31', '2000-01-01', '2000-01-02',
               '2000-01-03', '2000-01-04', '2000-01-05'],
              dtype='datetime64[ns]', freq='D')


Set Index
---------
>>> df = pd.DataFrame([
...     {'id': 1, 'firstname': 'Mark', 'lastname': 'Watney'},
...     {'id': 2, 'firstname': 'Melissa', 'lastname': 'Lewis'},
...     {'id': 3, 'firstname': 'Rick', 'lastname': 'Martinez'},
...     {'id': 4, 'firstname': 'Alex', 'lastname': 'Vogel'},
... ])
>>>
>>> df  # doctest: +NORMALIZE_WHITESPACE
   id firstname  lastname
0   1      Mark    Watney
1   2   Melissa     Lewis
2   3      Rick  Martinez
3   4      Alex     Vogel
>>>
>>> df.set_index('id')  # doctest: +NORMALIZE_WHITESPACE
   firstname  lastname
id
1       Mark    Watney
2    Melissa     Lewis
3       Rick  Martinez
4       Alex     Vogel


Use Case - 0x01
---------------
>>> import pandas as pd
>>>
>>> pd.set_option('display.width', 250)
>>> pd.set_option('display.max_columns', 20)
>>> pd.set_option('display.max_rows', 30)
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
.. [#pd14releasenotes] https://pandas.pydata.org/pandas-docs/dev/whatsnew/v1.4.0.html#deprecated-int64index-uint64index-float64index
.. [#pdDocAdvanced] https://pandas.pydata.org/pandas-docs/dev/user_guide/advanced.html#non-monotonic-indexes-require-exact-matches


.. todo:: Assignments
