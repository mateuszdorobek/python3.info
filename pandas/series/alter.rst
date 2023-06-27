Series Alter
============

SetUp
-----
>>> import pandas as pd
>>>
>>> s = pd.Series([1.0, 2.0, 2.0, None, 5.0])



Drop Rows
---------
* Drop element at index
* Works with ``inplace=True``

>>> s.drop(1)
0    1.0
2    2.0
3    NaN
4    5.0
dtype: float64

>>> s.drop([0,2,4])
1    2.0
3    NaN
dtype: float64


Drop Duplicates
---------------
* Works with ``inplace=True``

>>> s.drop_duplicates()
0    1.0
1    2.0
3    NaN
4    5.0
dtype: float64


Reset Index
-----------
* Works with ``inplace=True``
* ``drop=True`` prevents the old index being added as a column

>>> s.drop([0,1], inplace=True)
>>> s
2    2.0
3    NaN
4    5.0
dtype: float64

>>> s.reset_index()
   index    0
0      2  2.0
1      3  NaN
2      4  5.0

>>> s.reset_index(drop=True)
0    2.0
1    NaN
2    5.0
dtype: float64


Assignments
-----------
.. literalinclude:: assignments/pandas_series_alter_a.py
    :caption: :download:`Solution <assignments/pandas_series_alter_a.py>`
    :end-before: # Solution
