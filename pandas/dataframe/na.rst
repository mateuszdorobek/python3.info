DataFrame NA
============
* Represents missing values
* ``axis=0`` - rows
* ``axis=1`` - columns


SetUp
-----
>>> import pandas as pd
>>> import numpy as np
>>>
>>>
>>> df = pd.DataFrame({
...     'A': [1, 2, np.nan, np.nan, 3, np.nan, 4],
...     'B': [1.1, 2.2, np.nan, np.nan, 3.3, np.nan, 4.4],
...     'C': ['a', 'b', np.nan, np.nan, 'c', np.nan, 'd'],
...     'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
... })
>>>
>>> df
     A    B    C   D
0  1.0  1.1    a NaN
1  2.0  2.2    b NaN
2  NaN  NaN  NaN NaN
3  NaN  NaN  NaN NaN
4  3.0  3.3    c NaN
5  NaN  NaN  NaN NaN
6  4.0  4.4    d NaN


Check if Any
------------
>>> df.any()
A     True
B     True
C     True
D    False
dtype: bool


Check if All
------------
>>> df.all()
A    True
B    True
C    True
D    True
dtype: bool


Check if Null
-------------
>>> df.isnull()
       A      B      C     D
0  False  False  False  True
1  False  False  False  True
2   True   True   True  True
3   True   True   True  True
4  False  False  False  True
5   True   True   True  True
6  False  False  False  True


Check if NA
-----------
>>> df.isna()
       A      B      C     D
0  False  False  False  True
1  False  False  False  True
2   True   True   True  True
3   True   True   True  True
4  False  False  False  True
5   True   True   True  True
6  False  False  False  True



Fill With Scalar Value
----------------------
>>> df.fillna(0.0)
     A    B    C    D
0  1.0  1.1    a  0.0
1  2.0  2.2    b  0.0
2  0.0  0.0  0.0  0.0
3  0.0  0.0  0.0  0.0
4  3.0  3.3    c  0.0
5  0.0  0.0  0.0  0.0
6  4.0  4.4    d  0.0


Fill With Dict Values
---------------------
>>> df.fillna({
...     'A': 99,
...     'B': 88,
...     'C': 77
... })
      A     B   C   D
0   1.0   1.1   a NaN
1   2.0   2.2   b NaN
2  99.0  88.0  77 NaN
3  99.0  88.0  77 NaN
4   3.0   3.3   c NaN
5  99.0  88.0  77 NaN
6   4.0   4.4   d NaN


Fill Forwards
-------------
``ffill``: propagate last valid observation forward:

>>> df.fillna(method='ffill')
     A    B  C   D
0  1.0  1.1  a NaN
1  2.0  2.2  b NaN
2  2.0  2.2  b NaN
3  2.0  2.2  b NaN
4  3.0  3.3  c NaN
5  3.0  3.3  c NaN
6  4.0  4.4  d NaN


Fill Backwards
--------------
``bfill``: use NEXT valid observation to fill gap:

>>> df.fillna(method='bfill')
     A    B  C   D
0  1.0  1.1  a NaN
1  2.0  2.2  b NaN
2  3.0  3.3  c NaN
3  3.0  3.3  c NaN
4  3.0  3.3  c NaN
5  4.0  4.4  d NaN
6  4.0  4.4  d NaN


Interpolate
-----------
>>> df.interpolate()
          A         B    C   D
0  1.000000  1.100000    a NaN
1  2.000000  2.200000    b NaN
2  2.333333  2.566667  NaN NaN
3  2.666667  2.933333  NaN NaN
4  3.000000  3.300000    c NaN
5  3.500000  3.850000  NaN NaN
6  4.000000  4.400000    d NaN

.. list-table:: Interpolation techniques
    :widths: 25, 75
    :header-rows: 1

    * - Method
      - Description

    * - ``linear``
      - Ignore the index and treat the values as equally spaced. This is the
        only method supported on MultiIndexes

    * - ``time``
      - Works on daily and higher resolution data to interpolate given length
        of interval

    * - ``index``, ``values``
      - use the actual numerical values of the index.

    * - ``pad``
      - Fill in NA using existing values

    * - ``nearest``, ``zero``, ``slinear``, ``quadratic``, ``cubic``,
        ``spline``, ``barycentric``, ``polynomial``
      - Passed to ``scipy.interpolate.interp1d``. These methods use the
        numerical values of the index.  Both ``polynomial`` and ``spline``
        require that you also specify an ``order`` (int), e.g.
        ``df.interpolate(method='polynomial', order=5)``

    * - ``krogh``, ``piecewise_polynomial``, ``spline``, ``pchip``, ``akima``
      - Wrappers around the SciPy interpolation methods of similar names

    * - ``from_derivatives``
      - Refers to ``scipy.interpolate.BPoly.from_derivatives`` which replaces
        ``piecewise_polynomial`` interpolation method in scipy 0.18.


Drop Rows with NA
-----------------
>>> df.dropna(how='all')
     A    B  C   D
0  1.0  1.1  a NaN
1  2.0  2.2  b NaN
4  3.0  3.3  c NaN
6  4.0  4.4  d NaN

>>> df.dropna(how='all', axis='rows')
     A    B  C   D
0  1.0  1.1  a NaN
1  2.0  2.2  b NaN
4  3.0  3.3  c NaN
6  4.0  4.4  d NaN

>>> df.dropna(how='all', axis=0)
     A    B  C   D
0  1.0  1.1  a NaN
1  2.0  2.2  b NaN
4  3.0  3.3  c NaN
6  4.0  4.4  d NaN

>>> df.dropna(how='any')
Empty DataFrame
Columns: [A, B, C, D]
Index: []

>>> df.dropna(how='any', axis=0)
Empty DataFrame
Columns: [A, B, C, D]
Index: []

>>> df.dropna(how='any', axis='rows')
Empty DataFrame
Columns: [A, B, C, D]
Index: []


Drop Columns with NA
--------------------
>>> df.dropna(how='all', axis='columns')
     A    B    C
0  1.0  1.1    a
1  2.0  2.2    b
2  NaN  NaN  NaN
3  NaN  NaN  NaN
4  3.0  3.3    c
5  NaN  NaN  NaN
6  4.0  4.4    d

>>> df.dropna(how='all', axis=1)
     A    B    C
0  1.0  1.1    a
1  2.0  2.2    b
2  NaN  NaN  NaN
3  NaN  NaN  NaN
4  3.0  3.3    c
5  NaN  NaN  NaN
6  4.0  4.4    d

>>> df.dropna(how='all', axis=-1)
Traceback (most recent call last):
ValueError: No axis named -1 for object type <class 'pandas.core.frame.DataFrame'>

>>> df.dropna(how='any', axis='columns')
Empty DataFrame
Columns: []
Index: [0, 1, 2, 3, 4, 5, 6]

>>> df.dropna(how='any', axis=1)
Empty DataFrame
Columns: []
Index: [0, 1, 2, 3, 4, 5, 6]

>>> df.dropna(how='any', axis=-1)
Traceback (most recent call last):
ValueError: No axis named -1 for object type <class 'pandas.core.frame.DataFrame'>


Recap
-----
>>> data = pd.DataFrame({
...     'A': [1,2,3,4,5,6,7,8,9],
...     'B': [1,2,np.nan,np.nan,5,6,7,8,9]
... })
>>>
>>> a = data['A'].isnull()
>>> b = data['B'].isnull()
>>> c = data['B'].isnull().any()
>>> d = data['B'].isnull().all()
>>>
>>> e = data.fillna(0)
>>>
>>> f = data.dropna()
>>> g = data.dropna(how='any')
>>> h = data.dropna(how='any', axis='rows')
>>> i = data.dropna(how='all', axis='columns')
>>>
>>> j = data.ffill()
>>> k = data.bfill()
>>> l = data.interpolate('linear')
>>> m = data.interpolate('quadratic')
>>> n = data.interpolate('polynomial', order=3)



Assignments
-----------
.. literalinclude:: assignments/pandas_df_na_a.py
    :caption: :download:`Solution <assignments/pandas_df_na_a.py>`
    :end-before: # Solution
