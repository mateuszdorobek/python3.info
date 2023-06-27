Array Getitem
=============
>>> class ndarray:
...     def __getitem__(self, item):
...         if type(item) == int:
...             ...
...         if type(item) == list:
...             ...
...         if type(item) == tuple:
...             ...
...         if type(item) == slice:
...             ...


Index int
---------
* ``int``, example: ``0`` or ``1``


Index slice
-----------
* ``slice``, example: ``1:3`` or ``:3`` or ``1:3:2``


Index list
----------
* ``list[int]``, example: ``[0, 1]``
* ``list[bool]``, example: ``[True, False, True]``


Index tuple[int, T]
-------------------
* ``tuple[int, int]``, example: ``0, 0``
* ``tuple[int, list[int]]``, example: ``1, [1,2]``
* ``tuple[int, list[bool]]``, example: ``1, [True, False, True]``
* ``tuple[int, slice]``, example: ``1, 0:2``


Index tuple[slice, T]
---------------------
* ``tuple[slice, int]``, example: ``1:3, 0``
* ``tuple[slice, list[int]]``, example: ``1:3, [1,2]``
* ``tuple[slice, list[bool]]``, example: ``1:3, [True, False, True]``
* ``tuple[slice, slice]``, example: ``1:3, 0:2``


Index tuple[list[int], T]
-------------------------
* ``tuple[list[int], int]``, example: ``[0,1], 0``
* ``tuple[list[int], list[int]]``, example: ``[0,1], [1,2]``
* ``tuple[list[int], list[bool]]``, example: ``[0,1], [True, False, True]``
* ``tuple[list[int], slice]``, example: ``[0,1], 0:2``


Index tuple[list[bool], T]
--------------------------
* ``tuple[list[bool], int]``, example: ``[True, False, True], 0``
* ``tuple[list[bool], list[int]]``, example: ``[True, False, True], [1,2]``
* ``tuple[list[bool], list[bool]]``, example: ``[True, False, True], [True, False, True]``
* ``tuple[list[bool], slice]``, example: ``[True, False, True], 0:2``


SetUp
-----
>>> import numpy as np


Example
-------
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> a[ 0 ]  # int
array([1, 2, 3])
>>>
>>> a[ [0,2] ]  # list[int]
array([[1, 2, 3],
       [7, 8, 9]])
>>>
>>> a[ [True,False,True] ]  # list[bool]
array([[1, 2, 3],
       [7, 8, 9]])

.. todo:: Split chapters GetItem and Slice by __getitem__ argument type.



Index
-----
>>> a = np.array([1, 2, 3])
>>>
>>>
>>> a.flat[0]
1
>>> a.flat[1]
2
>>> a.flat[2]
3
>>> a.flat[4]
Traceback (most recent call last):
IndexError: index 4 is out of bounds for axis 0 with size 3

Flat:

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a.flat[0]
1
>>> a.flat[1]
2
>>> a.flat[2]
3
>>> a.flat[3]
4
>>> a.flat[4]
5
>>> a.flat[5]
6

Multidimensional:

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a[0][0]
1
>>> a[0][1]
2
>>> a[0][2]
3
>>> a[1][0]
4
>>> a[1][1]
5
>>> a[1][2]
6
>>> a[2]
Traceback (most recent call last):
IndexError: index 2 is out of bounds for axis 0 with size 2
>>>
>>> a[-1][-1]
6
>>> a[-3]
Traceback (most recent call last):
IndexError: index -3 is out of bounds for axis 0 with size 2
>>>
>>> a[0,0]
1
>>> a[0,1]
2
>>> a[0,2]
3
>>> a[1,0]
4
>>> a[1,1]
5
>>> a[1,2]
6


Selecting items
---------------
1-dimensional Array:

>>> a = np.array([1, 2, 3])
>>>
>>> a[0]
1
>>> a[1]
2
>>> a[2]
3
>>> a[3]
Traceback (most recent call last):
IndexError: index 3 is out of bounds for axis 0 with size 3
>>> a[-1]
3

2-dimensional Array:

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a[0]
array([1, 2, 3])
>>> a[1]
array([4, 5, 6])
>>> a[2]
Traceback (most recent call last):
IndexError: index 2 is out of bounds for axis 0 with size 2
>>>
>>> a[0,0]
1
>>> a[0,1]
2
>>> a[0,2]
3
>>>
>>> a[1,0]
4
>>> a[1,1]
5
>>> a[1,2]
6
>>>
>>> a[2,0]
Traceback (most recent call last):
IndexError: index 2 is out of bounds for axis 0 with size 2

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> a[0]
array([1, 2, 3])
>>> a[1]
array([4, 5, 6])
>>> a[2]
array([7, 8, 9])
>>>
>>> a[0,0]
1
>>> a[0,1]
2
>>> a[0,2]
3
>>>
>>> a[1,0]
4
>>> a[1,1]
5
>>> a[1,2]
6
>>>
>>> a[2,0]
7
>>> a[2,1]
8
>>> a[2,2]
9

3-dimensional Array:

>>> a = np.array([[[ 1,  2,  3],
...                [ 4,  5,  6],
...                [ 5,  6,  7]],
...               [[11, 22, 33],
...                [44, 55, 66],
...                [77, 88, 99]]])
>>>
>>> a[0,0,0]
1
>>> a[0,0,1]
2
>>> a[0,0,2]
3
>>> a[0,0,3]
Traceback (most recent call last):
IndexError: index 3 is out of bounds for axis 2 with size 3
>>>
>>> a[0,1,2]
6
>>> a[0,2,1]
6
>>> a[2,1,0]
Traceback (most recent call last):
IndexError: index 2 is out of bounds for axis 0 with size 2


Substituting items
------------------
1-dimensional Array:

* Will type cast values to ``np.ndarray.dtype``

>>> a = np.array([1, 2, 3])
>>>
>>> a[0] = 99
>>> a
array([99,  2,  3])
>>>
>>> a[-1] = 11
>>> a
array([99,  2, 11])

>>> a = np.array([1, 2, 3], float)
>>>
>>> a[0] = 99.9
>>> a
array([99.9,  2. ,  3. ])
>>>
>>> a[-1] = 11.1
>>> a
array([99.9,  2. , 11.1])

>>> a = np.array([1, 2, 3], int)
>>>
>>> a[0] = 99.9
>>> a
array([99,  2,  3])
>>>
>>> a[-1] = 11.1
>>> a
array([99,  2, 11])

2-dimensional Array:

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a[0,0] = 99
>>> a
array([[99,  2,  3],
       [ 4,  5,  6]])
>>>
>>> a[1,2] = 11
>>> a
array([[99,  2,  3],
       [ 4,  5, 11]])


Multi-indexing
--------------
>>> a = np.array([1, 2, 3])
>>>
>>> a[0], a[2], a[-1]
(1, 3, 3)
>>>
>>> a[[0, 2, -1]]
array([1, 3, 3])
>>>
>>> a[[True, False, True]]
array([1, 3])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> a[[0,1]]
array([[1, 2, 3],
       [4, 5, 6]])
>>>
>>> a[[0,2,-1]]
array([[1, 2, 3],
       [7, 8, 9],
       [7, 8, 9]])
>>>
>>> a[[True, False, True]]
array([[1, 2, 3],
       [7, 8, 9]])


Assignments
-----------
.. literalinclude:: assignments/numpy_getitem_a.py
    :caption: :download:`Solution <assignments/numpy_getitem_a.py>`
    :end-before: # Solution
