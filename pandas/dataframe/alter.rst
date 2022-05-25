DataFrame Alter
===============
* ``pd.date_range('1999-12-30', periods=7)``
* ``df['not-existing'] = 1``
* ``df['not-existing'] = range(0,10)``
* ``df['not-existing'] = np.arange(0,10)``
* ``.transpose()``
* ``.drop(columns=[...])``
* ``.drop(index=[...])``
* ``.drop_duplicates()``


SetUp
-----
>>> import pandas as pd
>>> import numpy as np


Add Rows and Columns
--------------------
Add Column:

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

>>> df['X'] = ['a', 'b', 'c']
>>> df
    A   B   C  X
0  10  20  30  a
1  11  21  31  b
2  12  22  32  c

>>> df['X'] = ['a', 'b']
Traceback (most recent call last):
ValueError: Length of values (2) does not match length of index (3)

>>> df['X'] = ['a', 'b', 'c', 'd']
Traceback (most recent call last):
ValueError: Length of values (4) does not match length of index (3)

>>> df['Z'] = np.arange(3.0)
>>> df
    A   B   C  X    Z
0  10  20  30  a  0.0
1  11  21  31  b  1.0
2  12  22  32  c  2.0


Drop Rows and Columns
---------------------
* Works with ``inplace=True``

Drop Column:

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

>>> df.drop('A', axis='columns')
    B   C
0  20  30
1  21  31
2  22  32

>>> df.drop(columns='A')
    B   C
0  20  30
1  21  31
2  22  32

>>> df.drop(columns=['A', 'B'])
    C
0  30
1  31
2  32

Drop Row:

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

>>> df.drop(1)
    A   B   C
0  10  20  30
2  12  22  32

>>> df.drop([0, 2])
    A   B   C
1  11  21  31

>>> rows = df[:2].index
>>> df.drop(rows)
    A   B   C
2  12  22  32

Drop from Timeseries:

>>> np.random.seed(0)
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

>>> df.drop('1999-12-30')
             Morning      Noon   Evening  Midnight
1999-12-31  1.867558 -0.977278  0.950088 -0.151357
2000-01-01 -0.103219  0.410599  0.144044  1.454274
2000-01-02  0.761038  0.121675  0.443863  0.333674
2000-01-03  1.494079 -0.205158  0.313068 -0.854096
2000-01-04 -2.552990  0.653619  0.864436 -0.742165
2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Transpose
---------
* ``df.transpose()`` or ``df.T``
* ``df.transpose()`` is preferred

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
>>> df.transpose()
    0   1   2
A  10  11  12
B  20  21  22
C  30  31  32
>>>
>>> df.T
    0   1   2
A  10  11  12
B  20  21  22
C  30  31  32

>>> df = pd.DataFrame({
...     'A': [10, 11, 12],
...     'B': [20, 21, 22],
...     'C': [30, 31, 32]})
>>>
>>> x = df['A']         # will select column A
>>> x = df['B']         # will select column B
>>> x = df['C']         # will select column C
>>>
>>> x = df.A            # will select column A
>>> x = df.B            # will select column B
>>> x = df.C            # will select column C
>>>
>>> x = df.T            # will transpose data
>>> x = df.transpose()  # will transpose data

>>> df = pd.DataFrame({
...     'R': [10, 11, 12],
...     'S': [20, 21, 22],
...     'T': [30, 31, 32]})
>>>
>>> x = df['R']         # will select column R
>>> x = df['S']         # will select column S
>>> x = df['T']         # will select column T
>>>
>>> x = df.R            # will select column R
>>> x = df.S            # will select column S
>>> x = df.T            # will transpose data
>>>
>>> x = df.transpose()  # will transpose data


.. todo:: Assignments
