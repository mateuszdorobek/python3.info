Series Slicing
==============


SetUp
-----
>>> import pandas as pd


Numeric Index
-------------
>>> s = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
>>> s
0    1.0
1    2.0
2    3.0
3    4.0
4    5.0
dtype: float64

>>> s[:2]
0    1.0
1    2.0
dtype: float64

>>> s[2:]
2    3.0
3    4.0
4    5.0
dtype: float64

>>> s[1:-2]
1    2.0
2    3.0
dtype: float64

>>> s[::2]
0    1.0
2    3.0
4    5.0
dtype: float64

>>> s[1::2]
1    2.0
3    4.0
dtype: float64


String Index
------------
* Using string index upper and lower bound are inclusive!
* String indexes has also numeric index underneath

>>> s = pd.Series(
...     data = [1.0, 2.0, 3.0, 4.0, 5.0],
...     index = ['a', 'b', 'c', 'd', 'e'])
>>> s
a    1.0
b    2.0
c    3.0
d    4.0
e    5.0
dtype: float64

>>> s['a':'d']
a    1.0
b    2.0
c    3.0
d    4.0
dtype: float64

>>> s['a':'d':2]
a    1.0
c    3.0
dtype: float64

>>> s['a':'d':'b']
Traceback (most recent call last):
TypeError: '>=' not supported between instances of 'str' and 'int'

>>> s['d':'a']
Series([], dtype: float64)

>>> s[:2]
a    1.0
b    2.0
dtype: float64

>>> s[2:]
c    3.0
d    4.0
e    5.0
dtype: float64

>>> s[1:-2]
b    2.0
c    3.0
dtype: float64

>>> s[::2]
a    1.0
c    3.0
e    5.0
dtype: float64

>>> s[1::2]
b    2.0
d    4.0
dtype: float64

>>> s = pd.Series(
...     data = [1.0, 2.0, 3.0, 4.0, 5.0],
...     index = ['aaa', 'bbb', 'ccc', 'ddd', 'eee'])
>>>
>>> s
aaa    1.0
bbb    2.0
ccc    3.0
ddd    4.0
eee    5.0
dtype: float64
>>>
>>> s['a':'b']
aaa    1.0
dtype: float64
>>>
>>> s['a':'c']
aaa    1.0
bbb    2.0
dtype: float64


Date Index
----------
>>> s = pd.Series(
...     data = [1.0, 2.0, 3.0, 4.0, 5.0],
...     index = pd.date_range('1999-12-30', periods=5))
>>>
>>> s
1999-12-30    1.0
1999-12-31    2.0
2000-01-01    3.0
2000-01-02    4.0
2000-01-03    5.0
Freq: D, dtype: float64

>>> s['2000-01-02':'2000-01-04']
2000-01-02    4.0
2000-01-03    5.0
Freq: D, dtype: float64

>>> s['1999-12-30':'2000-01-04':2]
1999-12-30    1.0
2000-01-01    3.0
2000-01-03    5.0
Freq: 2D, dtype: float64

>>> s['1999-12-30':'2000-01-04':-1]
Series([], Freq: -1D, dtype: float64)

>>> s['2000-01-04':'1999-12-30':-1]
2000-01-03    5.0
2000-01-02    4.0
2000-01-01    3.0
1999-12-31    2.0
1999-12-30    1.0
Freq: -1D, dtype: float64

>>> s[:'1999']
1999-12-30    1.0
1999-12-31    2.0
Freq: D, dtype: float64

>>> s['2000':]
2000-01-01    3.0
2000-01-02    4.0
2000-01-03    5.0
Freq: D, dtype: float64

>>> s[:'1999-12']
1999-12-30    1.0
1999-12-31    2.0
Freq: D, dtype: float64

>>> s['2000-01':]
2000-01-01    3.0
2000-01-02    4.0
2000-01-03    5.0
Freq: D, dtype: float64

>>> s[:'2000-01-02']
1999-12-30    1.0
1999-12-31    2.0
2000-01-01    3.0
2000-01-02    4.0
Freq: D, dtype: float64

>>> s['2000-01-02':]
2000-01-02    4.0
2000-01-03    5.0
Freq: D, dtype: float64

>>> s['1999-12':'1999-12']
1999-12-30    1.0
1999-12-31    2.0
Freq: D, dtype: float64

>>> s['2000-01':'2000-01-05']
2000-01-01    3.0
2000-01-02    4.0
2000-01-03    5.0
Freq: D, dtype: float64

>>> s[:'2000-01-05':2]
1999-12-30    1.0
2000-01-01    3.0
2000-01-03    5.0
Freq: 2D, dtype: float64

>>> s[:'2000-01-03':-1]
2000-01-03    5.0
Freq: -1D, dtype: float64

Despite ``DatetimeIndex``, this series also has ``RangeIndex`` underneath,
which you can slice.

>>> s[1:3]
1999-12-31    2.0
2000-01-01    3.0
Freq: D, dtype: float64
>>>
>>> s[:3]
1999-12-30    1.0
1999-12-31    2.0
2000-01-01    3.0
Freq: D, dtype: float64
>>>
>>> s[:3:2]
1999-12-30    1.0
2000-01-01    3.0
Freq: 2D, dtype: float64
>>>
>>> s[::-1]
2000-01-03    5.0
2000-01-02    4.0
2000-01-01    3.0
1999-12-31    2.0
1999-12-30    1.0
Freq: -1D, dtype: float64


Assignments
-----------
.. literalinclude:: assignments/pandas_series_slice_a.py
    :caption: :download:`Solution <assignments/pandas_series_slice_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_series_slice_b.py
    :caption: :download:`Solution <assignments/pandas_series_slice_b.py>`
    :end-before: # Solution
