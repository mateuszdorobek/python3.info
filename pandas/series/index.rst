Series Index
============
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

More Information: https://pandas.pydata.org/pandas-docs/dev/user_guide/advanced.html#index-types


Definition
----------
>>> from pandas import RangeIndex, Index, Index, Index, DatetimeIndex

>>> index = RangeIndex(start=0, stop=5, step=1)
>>> index = Index([0, 1, 2, 3, 4], dtype='int64')
>>> index = Index([0.0, 1.1, 2.2, 3.3, 4.4], dtype='float64')
>>> index = Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
>>> index = DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03',
...                        '2000-01-04', '2000-01-05'], dtype='datetime64[ns]',
...                        freq='D')


Usage
-----
>>> DATA = [11, 22, 33, 44, 55]

Range index:

>>> r1 = pd.Series(DATA)
>>> r2 = pd.Series(DATA, index=range(5))
>>> r3 = pd.Series(DATA, index=range(len(DATA)))

Integer index:

>>> i1 = pd.Series(DATA, index=[0, 1, 2, 3, 4])
>>> i2 = pd.Series(DATA, index=np.arange(5))
>>> i3 = pd.Series(DATA, index=np.arange(len(DATA)))
>>> i4 = pd.Series(DATA, index=[99, 3, -5, 0, 77])

Float index:

>>> f1 = pd.Series(DATA, index=[0.0, 1.1, 2.2, 3.3, 4.4])
>>> f2 = pd.Series(DATA, index=np.arange(0.0, 5.5, 1.1))
>>> f3 = pd.Series(DATA, index=[99.9, 3.14, -5.99, 0.0, 77.1])

Object index:

>>> o1 = pd.Series(DATA, index=['a', 'b', 'c', 'd', 'e'])
>>> o2 = pd.Series(DATA, index=list('abcde'))
>>> o3 = pd.Series(DATA, index=list('abcdefghijklmnopqrstuvwz')[:len(DATA)])
>>> o4 = pd.Series(DATA, index=['aaa', 'baba', 'cac', 'do or not', 'e,c,h,o'])

Datetime index:

>>> d1 = pd.Series(DATA, index=pd.date_range('2000-01-01', periods=len(DATA)))
>>> d2 = pd.Series(DATA, index=pd.date_range('2000-01-01', periods=len(DATA), freq='D'))
>>> d3 = pd.Series(DATA, index=[
...     pd.Timestamp('2000-01-01'),
...     pd.Timestamp('1999-01-28'),
...     pd.Timestamp('1961-04-12'),
...     pd.Timestamp('1969-07-21'),
...     pd.Timestamp('1970-01-01')])


Range Index
-----------
* Default

Define Range Index:

>>> s = pd.Series([11, 22, 33, 44])
>>> s
0    11
1    22
2    33
3    44
dtype: int64
>>>
>>> s.index
RangeIndex(start=0, stop=4, step=1)

>>> s = pd.Series([11, 22, 33, 44], index=range(4))
>>> s
0    11
1    22
2    33
3    44
dtype: int64
>>>
>>> s.index
RangeIndex(start=0, stop=4, step=1)

>>> s = pd.Series([1.0, 2.0, 3.0, 4.0])
>>> s
0    1.0
1    2.0
2    3.0
3    4.0
dtype: float64
>>>
>>> s.index
RangeIndex(start=0, stop=4, step=1)

>>> s = pd.Series(['a', 'b', 'c', 'd'])
>>> s
0    a
1    b
2    c
3    d
dtype: object
>>>
>>> s.index
RangeIndex(start=0, stop=4, step=1)


Int64 Index
-----------
>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, 4.4],
...     index = [2, -1, 0, 1])
>>>
>>> s
 2    1.1
-1    2.2
 0    3.3
 1    4.4
dtype: float64
>>>
>>> s.index
Index([2, -1, 0, 1], dtype='int64')



Float64 Index
-------------
>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, 4.4],
...     index = [2.2, -1.1, 0.0, 1.1])
>>>
>>> s
 2.2    1.1
-1.1    2.2
 0.0    3.3
 1.1    4.4
dtype: float64
>>>
>>> s.index
Index([2.2, -1.1, 0.0, 1.1], dtype='float64')


String Index
------------
* Also has ``RangeIndex``
* ``string.ascii_lowercase``
* ``string.ascii_uppercase``
* ``string.ascii_letters``
* ``string.hexdigits``
* ``string.digits``


>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, 4.4],
...     index = ['a', 'b', 'c', 'd'])
>>>
>>> s
a    1.1
b    2.2
c    3.3
d    4.4
dtype: float64
>>>
>>> s.index
Index(['a', 'b', 'c', 'd'], dtype='object')

>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, 4.4],
...     index = list('abcd'))
>>>
>>> s
a    1.1
b    2.2
c    3.3
d    4.4
dtype: float64
>>>
>>> s.index
Index(['a', 'b', 'c', 'd'], dtype='object')

>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, 4.4],
...     index = ['aaa', 'bbb', 'ccc', 'ddd'])
>>>
>>> s
aaa    1.1
bbb    2.2
ccc    3.3
ddd    4.4
dtype: float64
>>>
>>> s.index
Index(['aaa', 'bbb', 'ccc', 'ddd'], dtype='object')

>>> import string
>>>
>>>
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
>>>
>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>>
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>>
>>> string.digits
'0123456789'
>>>
>>> string.hexdigits
'0123456789abcdefABCDEF'
>>>
>>>
>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, 4.4],
...     index = list(string.ascii_lowercase)[:4])
>>>
>>> s
a    1.1
b    2.2
c    3.3
d    4.4
dtype: float64
>>>
>>> s.index
Index(['a', 'b', 'c', 'd'], dtype='object')


Datetime Index
--------------
* Also has ``RangeIndex``
* Default is "Daily"
* Works also with ISO time format ``1970-01-01T00:00:00``
* ``00:00:00`` is assumed if time is not provided

>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, 4.4],
...     index = pd.date_range('1999-12-30', periods=4))
>>>
>>> s
1999-12-30    1.1
1999-12-31    2.2
2000-01-01    3.3
2000-01-02    4.4
Freq: D, dtype: float64
>>>
>>> s.index  # doctest: +NORMALIZE_WHITESPACE
DatetimeIndex(['1999-12-30', '1999-12-31', '2000-01-01', '2000-01-02'],
              dtype='datetime64[ns]', freq='D')

Every year:

>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, 4.4],
...     index = pd.date_range('1999-12-30', periods=4, freq='Y'))
>>>
>>> s
1999-12-31    1.1
2000-12-31    2.2
2001-12-31    3.3
2002-12-31    4.4
Freq: A-DEC, dtype: float64
>>>
>>> s.index  # doctest: +NORMALIZE_WHITESPACE
DatetimeIndex(['1999-12-31', '2000-12-31', '2001-12-31', '2002-12-31'],
              dtype='datetime64[ns]', freq='A-DEC')

Every quarter:

>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, 4.4],
...     index = pd.date_range('1999-12-30', periods=4, freq='Q'))
>>>
>>> s
1999-12-31    1.1
2000-03-31    2.2
2000-06-30    3.3
2000-09-30    4.4
Freq: Q-DEC, dtype: float64
>>>
>>> s.index  # doctest: +NORMALIZE_WHITESPACE
DatetimeIndex(['1999-12-31', '2000-03-31', '2000-06-30', '2000-09-30'],
              dtype='datetime64[ns]', freq='Q-DEC')

Every month:

>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, 4.4],
...     index = pd.date_range('1999-12-30', periods=4, freq='M'))
>>>
>>> s
1999-12-31    1.1
2000-01-31    2.2
2000-02-29    3.3
2000-03-31    4.4
Freq: M, dtype: float64
>>>
>>> s.index  # doctest: +NORMALIZE_WHITESPACE
DatetimeIndex(['1999-12-31', '2000-01-31', '2000-02-29', '2000-03-31'],
              dtype='datetime64[ns]', freq='M')

Every day:

>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, 4.4],
...     index = pd.date_range('1999-12-30', periods=4, freq='D'))
>>>
>>> s
1999-12-30    1.1
1999-12-31    2.2
2000-01-01    3.3
2000-01-02    4.4
Freq: D, dtype: float64
>>>
>>> s.index  # doctest: +NORMALIZE_WHITESPACE
DatetimeIndex(['1999-12-30', '1999-12-31', '2000-01-01', '2000-01-02'],
              dtype='datetime64[ns]', freq='D')

Every two days:

>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, 4.4],
...     index = pd.date_range('1999-12-30', periods=4, freq='2D'))
>>>
>>> s
1999-12-30    1.1
2000-01-01    2.2
2000-01-03    3.3
2000-01-05    4.4
Freq: 2D, dtype: float64
>>>
>>> s.index  # doctest: +NORMALIZE_WHITESPACE
DatetimeIndex(['1999-12-30', '2000-01-01', '2000-01-03', '2000-01-05'],
              dtype='datetime64[ns]', freq='2D')

Every hour:

>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, 4.4],
...     index = pd.date_range('1999-12-30', periods=4, freq='H'))
>>>
>>> s
1999-12-30 00:00:00    1.1
1999-12-30 01:00:00    2.2
1999-12-30 02:00:00    3.3
1999-12-30 03:00:00    4.4
Freq: H, dtype: float64
>>>
>>> s.index  # doctest: +NORMALIZE_WHITESPACE
DatetimeIndex(['1999-12-30 00:00:00', '1999-12-30 01:00:00',
               '1999-12-30 02:00:00', '1999-12-30 03:00:00'],
              dtype='datetime64[ns]', freq='H')

Every minute:

>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, 4.4],
...     index = pd.date_range('1999-12-30', periods=4, freq='T'))
>>>
>>> s
1999-12-30 00:00:00    1.1
1999-12-30 00:01:00    2.2
1999-12-30 00:02:00    3.3
1999-12-30 00:03:00    4.4
Freq: T, dtype: float64
>>>
>>> s.index  # doctest: +NORMALIZE_WHITESPACE
DatetimeIndex(['1999-12-30 00:00:00', '1999-12-30 00:01:00',
               '1999-12-30 00:02:00', '1999-12-30 00:03:00'],
              dtype='datetime64[ns]', freq='T')

Every second:

>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, 4.4],
...     index = pd.date_range('1999-12-30', periods=4, freq='S'))
>>>
>>> s
1999-12-30 00:00:00    1.1
1999-12-30 00:00:01    2.2
1999-12-30 00:00:02    3.3
1999-12-30 00:00:03    4.4
Freq: S, dtype: float64
>>>
>>> s.index  # doctest: +NORMALIZE_WHITESPACE
DatetimeIndex(['1999-12-30 00:00:00', '1999-12-30 00:00:01',
               '1999-12-30 00:00:02', '1999-12-30 00:00:03'],
              dtype='datetime64[ns]', freq='S')

Every business day.

>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, 4.4],
...     index = pd.date_range('1999-12-30', periods=4, freq='B'))
>>>
>>> s
1999-12-30    1.1
1999-12-31    2.2
2000-01-03    3.3
2000-01-04    4.4
Freq: B, dtype: float64
>>>
>>> s.index  # doctest: +NORMALIZE_WHITESPACE
DatetimeIndex(['1999-12-30', '1999-12-31', '2000-01-03', '2000-01-04'],
              dtype='datetime64[ns]', freq='B')


Further Reading
---------------
* More information in `Date and Time Frequency`
* More information in `Date and Time Calendar`


.. todo:: Assignments
