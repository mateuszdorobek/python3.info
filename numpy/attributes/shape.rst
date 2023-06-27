Array Shape
===========
* Any shape operation changes only ``np.ndarray.shape`` and ``np.ndarray.strides`` and does not touch data

.. figure:: img/numpy-shape-1d.png
.. figure:: img/numpy-shape-2d.png
.. figure:: img/numpy-shape-3d.png
.. figure:: img/numpy-shape-4d.png


SetUp
-----
>>> import numpy as np


Recap
-----
>>> obj = [1, 2, 3]
>>>
>>> len(obj)
3

>>> obj1 = [1, 2, 3]
>>> obj2 = [4, 5, 6]
>>>
>>> len([obj1, obj2])
2
>>> len([ [1,2,3], [4,5,6] ])
2
>>> len([[1,2,3],
...      [4,5,6]])
2

>>> obj1 = [1, 2, 3]
>>> obj2 = [4, 5, 6]
>>> obj3 = [7, 8, 9]
>>> obj4 = [10, 11, 12]
>>>
>>> len([ [obj1, obj2], [obj3, obj4] ])
2
>>> len([[obj1, obj2],
...      [obj3, obj4]])
2


Shape
-----
1-dimensional:

>>> a = np.array([1, 2, 3])
>>> a.shape
(3,)

2-dimensional:

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>> a.shape
(2, 3)

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>> a.shape
(3, 3)

3-dimensional:

>>> a = np.array([[[ 1,  2,  3],
...                [ 4,  5,  6],
...                [ 5,  6,  7]],
...               [[11, 22, 33],
...                [44, 55, 66],
...                [77, 88, 99]]])
>>> a.shape
(2, 3, 3)


Reshape
-------
* Returns new array
* Does not modify inplace
* ``a.reshape(1, 2)`` is equivalent to ``a.reshape((1, 2))``

>>> a = np.array([1, 2, 3])
>>>
>>> a.reshape(1, 3)
array([[1, 2, 3]])
>>>
>>> a.reshape(3, 1)
array([[1],
       [2],
       [3]])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a.reshape(3, 2)
array([[1, 2],
       [3, 4],
       [5, 6]])
>>>
>>> a.reshape(1, 6)
array([[1, 2, 3, 4, 5, 6]])
>>>
>>> a.reshape(6, 1)
array([[1],
       [2],
       [3],
       [4],
       [5],
       [6]])
>>>
>>> a.reshape(5, 2)
Traceback (most recent call last):
ValueError: cannot reshape array of size 6 into shape (5,2)

>>> a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
>>>
>>> a.reshape(2, 4)
array([[1, 2, 3, 4],
       [5, 6, 7, 8]])
>>>
>>> a.reshape(2, 4, 1)
array([[[1],
        [2],
        [3],
        [4]],
<BLANKLINE>
       [[5],
        [6],
        [7],
        [8]]])
>>>
>>> a.reshape(2, 2, 2)
array([[[1, 2],
        [3, 4]],
<BLANKLINE>
       [[5, 6],
        [7, 8]]])
>>>
>>> a.reshape(1, 2, 4)
array([[[1, 2, 3, 4],
        [5, 6, 7, 8]]])
>>>
>>> a.reshape(4, 2, 1)
array([[[1],
        [2]],
<BLANKLINE>
       [[3],
        [4]],
<BLANKLINE>
       [[5],
        [6]],
<BLANKLINE>
       [[7],
        [8]]])
>>>
>>> a.reshape(1, 8, 1)
array([[[1],
        [2],
        [3],
        [4],
        [5],
        [6],
        [7],
        [8]]])
>>>
>>> a.reshape(2, 3, 1)
Traceback (most recent call last):
ValueError: cannot reshape array of size 8 into shape (2,3,1)


Flatten
-------
* Returns new array (makes memory copy - expensive)
* Does not modify inplace

>>> a = np.array([1, 2, 3])
>>>
>>> a.flatten()
array([1, 2, 3])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> a.flatten()
array([1, 2, 3, 4, 5, 6, 7, 8, 9])

>>> a = np.array([[[ 1,  2,  3],
...                [ 4,  5,  6],
...                [ 5,  6,  7]],
...
...               [[11, 22, 33],
...                [44, 55, 66],
...                [77, 88, 99]]])
>>>
>>> a.flatten()  # doctest: +NORMALIZE_WHITESPACE
array([ 1,  2,  3,  4,  5,  6,  5,  6,  7, 11, 22, 33, 44, 55, 66, 77, 88, 99])


Ravel
-----
* Ravel is the same as Flatten but returns a reference (or view) of the array if possible (i.e. memory is contiguous)
* Otherwise returns new array (makes memory copy)

>>> a = np.array([1, 2, 3])
>>>
>>> a.ravel()
array([1, 2, 3])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> a.ravel()
array([1, 2, 3, 4, 5, 6, 7, 8, 9])

>>> a = np.array([[[ 1,  2,  3],
...                [ 4,  5,  6],
...                [ 5,  6,  7]],
...
...               [[11, 22, 33],
...                [44, 55, 66],
...                [77, 88, 99]]])
>>>
>>>
>>> a.ravel()  # doctest: +NORMALIZE_WHITESPACE
array([ 1,  2,  3,  4,  5,  6,  5,  6,  7, 11, 22, 33, 44, 55, 66, 77, 88, 99])


Flatten vs Ravel
----------------
>>> a = np.array([1, 2, 3])
>>> b = a.ravel()
>>> c = a.flatten()

>>> a[0] = 99

>>> a  # original
array([99,  2,  3])
>>>
>>> b  # flatten
array([99,  2,  3])
>>>
>>> c  # ravel
array([1, 2, 3])


Recap
-----
.. figure:: img/array-shape-ravel-vs-flatten.png


Assignments
-----------
.. literalinclude:: assignments/numpy_shape_a.py
    :caption: :download:`Solution <assignments/numpy_shape_a.py>`
    :end-before: # Solution
