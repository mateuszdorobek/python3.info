Series Attributes
=================


SetUp
-----
>>> import pandas as pd
>>>
>>> data = pd.Series(['a', 'b', 'c'])


Size
----
>>> data.size
3


NDim
----
* Number of Dimensions

>>> data.ndim
1


Shape
-----
>>> data.shape
(3,)


Index
-----
* More information in `Pandas Series Index`

>>> data
0    a
1    b
2    c
dtype: object

>>> data.index
RangeIndex(start=0, stop=3, step=1)


Values
------
>>> data.values
array(['a', 'b', 'c'], dtype=object)


Assignments
-----------
.. literalinclude:: assignments/pandas_series_attributes_a.py
    :caption: :download:`Solution <assignments/pandas_series_attributes_a.py>`
    :end-before: # Solution
