Series NA
=========
* https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
* https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#missing-data-na
* Experimental: the behaviour of pd.NA can still change without warning.
* ``None``
* ``float('nan')``
* ``np.nan``
* ``pd.NA``


SetUp
-----
>>> import pandas as pd
>>> import numpy as np


Boolean Value
-------------
>>> bool(None)
False

>>> bool(float('nan'))
True

>>> bool(np.nan)
True

>>> bool(pd.NA)
Traceback (most recent call last):
TypeError: boolean value of NA is ambiguous


Type
----
>>> pd.Series([1, None, 3]).dtype
dtype('float64')
>>> pd.Series([1.0, None, 3.0]).dtype
dtype('float64')
>>> pd.Series([True, None, False]).dtype
dtype('O')
>>> pd.Series(['a', None, 'c']).dtype
dtype('O')

>>> pd.Series([1, float('nan'), 3]).dtype
dtype('float64')
>>> pd.Series([1.0, float('nan'), 3.0]).dtype
dtype('float64')
>>> pd.Series([True, float('nan'), False]).dtype
dtype('O')
>>> pd.Series(['a', float('nan'), 'c']).dtype
dtype('O')

>>> pd.Series([1, np.nan, 3]).dtype
dtype('float64')
>>> pd.Series([1.0, np.nan, 3.0]).dtype
dtype('float64')
>>> pd.Series([True, np.nan, False]).dtype
dtype('O')
>>> pd.Series(['a', np.nan, 'c']).dtype
dtype('O')

>>> pd.Series([1, pd.NA, 3]).dtype
dtype('O')
>>> pd.Series([1.0, pd.NA, 3.0]).dtype
dtype('O')
>>> pd.Series([True, pd.NA, False]).dtype
dtype('O')
>>> pd.Series(['a', pd.NA, 'c']).dtype
dtype('O')


Comparison
----------
>>> None == None
True
>>> None == float('nan')
False
>>> None == np.nan
False
>>> None == pd.NA
False

>>> float('nan') == None
False
>>> float('nan') == float('nan')
False
>>> float('nan') == np.nan
False
>>> float('nan') == pd.NA
<NA>

>>> np.nan == None
False
>>> np.nan == float('nan')
False
>>> np.nan == np.nan
False
>>> np.nan == pd.NA
<NA>

>>> pd.NA == None
False
>>> pd.NA == float('nan')
<NA>
>>> pd.NA == np.nan
<NA>
>>> pd.NA == pd.NA
<NA>


Identity
--------
>>> None is None
True
>>> None is float('nan')
False
>>> None is np.nan
False
>>> None is pd.NA
False

>>> float('nan') is None
False
>>> float('nan') is float('nan')
False
>>> float('nan') is np.nan
False
>>> float('nan') is pd.NA
False

>>> np.nan is None
False
>>> np.nan is float('nan')
False
>>> np.nan is np.nan
True
>>> np.nan is pd.NA
False

>>> pd.NA is None
False
>>> pd.NA is float('nan')
False
>>> pd.NA is np.nan
False
>>> pd.NA is pd.NA
True


Check
-----
* Negated ``~`` versions of all above methods

>>> s = pd.Series([1.0, np.nan, 3.0])
>>> s
0    1.0
1    NaN
2    3.0
dtype: float64

>>> s.any()
True
>>> ~s.any()
False

>>> s.all()
True
>>> ~s.all()
False


Select
------
* ``s.isnull()`` and ``s.notnull()``
* ``s.isna()`` and ``s.notna()``
* Negated ``~`` versions of all above methods

>>> s = pd.Series([1.0, np.nan, 3.0])
>>> s
0    1.0
1    NaN
2    3.0
dtype: float64

>>> s.isnull()
0    False
1     True
2    False
dtype: bool

>>> ~s.isnull()
0     True
1    False
2     True
dtype: bool

>>> s.notnull()
0     True
1    False
2     True
dtype: bool

>>> ~s.notnull()
0    False
1     True
2    False
dtype: bool

>>> s = pd.Series([1.0, np.nan, 3.0])
>>> s
0    1.0
1    NaN
2    3.0
dtype: float64
>>>
>>> s.isna()
0    False
1     True
2    False
dtype: bool
>>>
>>> s.notna()
0     True
1    False
2     True
dtype: bool
>>>
>>> ~s.isna()
0     True
1    False
2     True
dtype: bool
>>>
>>> ~s.notna()
0    False
1     True
2    False
dtype: bool


Update
------
* Works with ``inplace=True`` parameter.

>>> s = pd.Series([1.0, None, None, 4.0, None, 6.0])
>>> s
0    1.0
1    NaN
2    NaN
3    4.0
4    NaN
5    6.0
dtype: float64

Fill NA - Scalar value:

>>> s.fillna(0.0)
0    1.0
1    0.0
2    0.0
3    4.0
4    0.0
5    6.0
dtype: float64

Forward Fill. ``ffill``: propagate last valid observation forward:

>>> s.ffill()
0    1.0
1    1.0
2    1.0
3    4.0
4    4.0
5    6.0
dtype: float64

Backward Fill. ``bfill``: use NEXT valid observation to fill gap:

>>> s.bfill()
0    1.0
1    4.0
2    4.0
3    4.0
4    6.0
5    6.0
dtype: float64

Interpolate. ``method: str``, default ``linear``, no ``inplace=True`` option:

>>> s.interpolate()
0    1.0
1    2.0
2    3.0
3    4.0
4    5.0
5    6.0
dtype: float64

Following method requires installation of ``scipy`` library:

>>> s.interpolate('nearest')
0    1.0
1    1.0
2    4.0
3    4.0
4    4.0
5    6.0
dtype: float64

Following method requires installation of ``scipy`` library:

>>> s.interpolate('polynomial', order=2)
0    1.0
1    2.0
2    3.0
3    4.0
4    5.0
5    6.0
dtype: float64

.. list-table:: Interpolation techniques
    :widths: 25, 75
    :header-rows: 1

    * - Method
      - Description

    * - ``linear``
      - Ignore the index and treat the values as equally spaced. This is the
        only method supported on MultiIndexes

    * - ``time``
      - Works on daily and higher resolution data to interpolate given
        length of interval

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


Drop
----
Drop Rows. Has ``inplace=True`` parameter:

>>> s = pd.Series([1.0, None, None, 4.0, None, 6.0])
>>> s
0    1.0
1    NaN
2    NaN
3    4.0
4    NaN
5    6.0
dtype: float64
>>>
>>> s.dropna()
0    1.0
3    4.0
5    6.0
dtype: float64


Conversion
----------
* If you have a ``DataFrame`` or ``Series`` using traditional types that have
  missing data represented using ``np.nan``

* There are convenience methods ``convert_dtypes()`` in ``Series`` and
  ``DataFrame`` that can convert data to use the newer dtypes for integers,
  strings and booleans

* This is especially helpful after reading in data sets when letting the
  readers such as ``read_csv()`` and ``read_excel()`` infer default dtypes.

>>> # doctest: +SKIP
... data = pd.read_csv('data/baseball.csv', index_col='id')
... data[data.columns[:10]].dtypes
player    object
year       int64
stint      int64
team      object
lg        object
g          int64
ab         int64
r          int64
h          int64
X2b        int64
dtype: object

>>> # doctest: +SKIP
... data = pd.read_csv('data/baseball.csv', index_col='id')
... data = data.convert_dtypes()
... data[data.columns[:10]].dtypes
player    string
year       Int64
stint      Int64
team      string
lg        string
g          Int64
ab         Int64
r          Int64
h          Int64
X2b        Int64
dtype: object


Assignments
-----------
.. literalinclude:: assignments/pandas_series_na_a.py
    :caption: :download:`Solution <assignments/pandas_series_na_a.py>`
    :end-before: # Solution
