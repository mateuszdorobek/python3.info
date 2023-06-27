Series Sample
=============


SetUp
-----
>>> import pandas as pd
>>> import numpy as np
>>> np.random.seed(0)
>>>
>>>
>>> s = pd.Series(
...     data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
...     index = pd.date_range(start='1999-12-28', periods=10))
>>> s
1999-12-28    0
1999-12-29    1
1999-12-30    2
1999-12-31    3
2000-01-01    4
2000-01-02    5
2000-01-03    6
2000-01-04    7
2000-01-05    8
2000-01-06    9
Freq: D, dtype: int64


Head
----
>>> s.head(2)
1999-12-28    0
1999-12-29    1
Freq: D, dtype: int64

>>> s.head(n=1)
1999-12-28    0
Freq: D, dtype: int64


Tail
----
>>> s.tail(2)
2000-01-05    8
2000-01-06    9
Freq: D, dtype: int64

>>> s.tail(n=1)
2000-01-06    9
Freq: D, dtype: int64


First
-----
>>> s.first('Y')
1999-12-28    0
1999-12-29    1
1999-12-30    2
1999-12-31    3
Freq: D, dtype: int64

>>> s.first('M')
1999-12-28    0
1999-12-29    1
1999-12-30    2
1999-12-31    3
Freq: D, dtype: int64

>>> s.first('D')
1999-12-28    0
Freq: D, dtype: int64

>>> s.first('3D')
1999-12-28    0
1999-12-29    1
1999-12-30    2
Freq: D, dtype: int64

>>> s.first('W')
1999-12-28    0
1999-12-29    1
1999-12-30    2
1999-12-31    3
2000-01-01    4
2000-01-02    5
Freq: D, dtype: int64


Last
----
>>> s.last('Y')
2000-01-01    4
2000-01-02    5
2000-01-03    6
2000-01-04    7
2000-01-05    8
2000-01-06    9
Freq: D, dtype: int64

>>> s.last('M')
2000-01-01    4
2000-01-02    5
2000-01-03    6
2000-01-04    7
2000-01-05    8
2000-01-06    9
Freq: D, dtype: int64

>>> s.last('D')
2000-01-06    9
Freq: D, dtype: int64

>>> s.last('2D')
2000-01-05    8
2000-01-06    9
Freq: D, dtype: int64

>>> s.last('W')
2000-01-03    6
2000-01-04    7
2000-01-05    8
2000-01-06    9
Freq: D, dtype: int64


Sample
------
* 1/4 is 25%
* .05 is 5%
* 0.5 is 50%
* 1.0 is 100%

`n` number or fraction random rows with and without repetition:

>>> s.sample()
1999-12-30    2
Freq: D, dtype: int64

>>> s.sample(2)
1999-12-31    3
2000-01-02    5
Freq: 2D, dtype: int64

>>> s.sample(n=2, replace=True)
2000-01-04    7
2000-01-04    7
dtype: int64

>>> s.sample(frac=1/4)
1999-12-30    2
1999-12-31    3
Freq: D, dtype: int64

>>> s.sample(frac=0.5)
2000-01-01    4
1999-12-29    1
2000-01-04    7
2000-01-05    8
1999-12-30    2
dtype: int64


Reset Index
-----------
>>> s.sample(frac=1.0).reset_index()
       index  0
0 2000-01-02  5
1 1999-12-30  2
2 2000-01-04  7
3 2000-01-01  4
4 1999-12-29  1
5 1999-12-28  0
6 2000-01-03  6
7 2000-01-05  8
8 2000-01-06  9
9 1999-12-31  3


Assignments
-----------
.. literalinclude:: assignments/pandas_series_sample_a.py
    :caption: :download:`Solution <assignments/pandas_series_sample_a.py>`
    :end-before: # Solution
