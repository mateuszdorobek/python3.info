Series Getitem
==============


SetUp
-----
>>> import pandas as pd


Range Index
-----------
>>> s = pd.Series([1.1, 2.2, 3.3, None, 5.5])
>>> s
0    1.1
1    2.2
2    3.3
3    NaN
4    5.5
dtype: float64

>>> s.index
RangeIndex(start=0, stop=5, step=1)

>>> s[0]
1.1
>>> s[1]
2.2
>>> s[2]
3.3
>>> s[3]
nan
>>> s[4]
5.5

>>> s[5]
Traceback (most recent call last):
KeyError: 5

>>> s[-1]
Traceback (most recent call last):
KeyError: -1

>>> s[-100]
Traceback (most recent call last):
KeyError: -100


Float and Int Index
-------------------
>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, None, 5.5],
...     index = [1, 0, 3.3, 99, -1])
>>>
>>> s
 1.0     1.1
 0.0     2.2
 3.3     3.3
 99.0    NaN
-1.0     5.5
dtype: float64

>>> s.index
Index([1.0, 0.0, 3.3, 99.0, -1.0], dtype='float64')

>>> s[0]
2.2
>>>
>>> s[1]
1.1
>>>
>>> s[2]
Traceback (most recent call last):
KeyError: 2
>>>
>>> s[3]
Traceback (most recent call last):
KeyError: 3
>>>
>>> s[3.3]
3.3
>>>
>>> s[-1]
5.5


String Index
------------
>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, None, 5.5],
...     index = ['a', 'b', 'c', 'd', 'e'])
>>>
>>> s
a    1.1
b    2.2
c    3.3
d    NaN
e    5.5
dtype: float64

>>> s.index
Index(['a', 'b', 'c', 'd', 'e'], dtype='object')

>>> s['a']
1.1
>>>
>>> s['b']
2.2
>>>
>>> s['c']
3.3
>>>
>>> s['d']
nan
>>>
>>> s['e']
5.5
>>>
>>> s['f']
Traceback (most recent call last):
KeyError: 'f'

>>> s[0]
1.1
>>>
>>> s[3]
nan
>>>
>>> s[100]
Traceback (most recent call last):
IndexError: index 100 is out of bounds for axis 0 with size 5
>>> s[-1]
5.5
>>>
>>> s[-100]
Traceback (most recent call last):
IndexError: index -100 is out of bounds for axis 0 with size 5


Date Index
----------
>>> s = pd.Series(
...     data = [1.1, 2.2, 3.3, None, 5.5],
...     index = pd.date_range('1999-12-30', periods=5))
>>>
>>> s
1999-12-30    1.1
1999-12-31    2.2
2000-01-01    3.3
2000-01-02    NaN
2000-01-03    5.5
Freq: D, dtype: float64

>>> s.index
DatetimeIndex(['1999-12-30', '1999-12-31', '2000-01-01', '2000-01-02',
               '2000-01-03'],
              dtype='datetime64[ns]', freq='D')

>>> s['2000-01-03']
5.5

>>> s['2000-01']
2000-01-01    3.3
2000-01-02    NaN
2000-01-03    5.5
Freq: D, dtype: float64

>>> s['1999']
1999-12-30    1.1
1999-12-31    2.2
Freq: D, dtype: float64

>>> s[0]
1.1
>>>
>>> s[1]
2.2
>>>
>>> s[2]
3.3
>>>
>>> s[3]
nan
>>>
>>> s[4]
5.5
>>>
>>> s[5]
Traceback (most recent call last):
IndexError: index 5 is out of bounds for axis 0 with size 5
>>>
>>> s[-1]
5.5

>>> s['1999']
1999-12-30    1.1
1999-12-31    2.2
Freq: D, dtype: float64
>>>
>>> s[1999]
Traceback (most recent call last):
IndexError: index 1999 is out of bounds for axis 0 with size 5


Assignments
-----------
.. literalinclude:: assignments/pandas_series_getitem_a.py
    :caption: :download:`Solution <assignments/pandas_series_getitem_a.py>`
    :end-before: # Solution
