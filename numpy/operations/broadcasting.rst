Array Broadcasting
==================

.. glossary::

    Vector
    Broadcasting
    Matrix Multiplication


SetUp
-----
>>> import numpy as np


Broadcasting Rules
------------------
* Source [#NumpyBroadcastingRules]_

#. Operations between multiple array objects are first checked for proper
   shape match

#. Mathematical operators (``+``, ``-``, ``*``, ``/``, ``exp``, ``log``, ...)
   apply element by element, on values

#. Reduction operations (``mean``, ``std``, ``skew``, ``kurt``, ``sum``,
   ``prod``, ...) apply to whole array, unless an axis is specified

#. Missing values propagate, unless explicitly ignored (``nanmean``,
   ``nansum``, ...)


Addition
--------
>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> b = np.array([[4, 5, 6], [7, 8, 9]])
>>> c = np.array([1, 2, 3])
>>> d = np.array([4, 5])
>>>
>>> a + a
array([[ 2,  4,  6],
       [ 8, 10, 12]])
>>>
>>> a + b
array([[ 5,  7,  9],
       [11, 13, 15]])
>>>
>>> a + c
array([[2, 4, 6],
       [5, 7, 9]])
>>>
>>> a + d  # doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
ValueError: operands could not be broadcast together with shapes (2,3) (2,)


Subtraction
-----------
>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> b = np.array([[4, 5, 6], [7, 8, 9]])
>>> c = np.array([1, 2, 3])
>>> d = np.array([4, 5])
>>>
>>> a - a
array([[0, 0, 0],
       [0, 0, 0]])
>>>
>>> a - b
array([[-3, -3, -3],
       [-3, -3, -3]])
>>>
>>> a - c
array([[0, 0, 0],
       [3, 3, 3]])
>>>
>>> a - d  # doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
ValueError: operands could not be broadcast together with shapes (2,3) (2,)


True Division
-------------
>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> b = np.array([[4, 5, 6], [7, 8, 9]])
>>> c = np.array([1, 2, 3])
>>> d = np.array([4, 5])
>>>
>>> a / a
array([[1., 1., 1.],
       [1., 1., 1.]])
>>>
>>> a / b
array([[0.25      , 0.4       , 0.5       ],
       [0.57142857, 0.625     , 0.66666667]])
>>>
>>> a / c
array([[1. , 1. , 1. ],
       [4. , 2.5, 2. ]])
>>>
>>> a / d  # doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
ValueError: operands could not be broadcast together with shapes (2,3) (2,)


Floor Division
--------------
>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> b = np.array([[4, 5, 6], [7, 8, 9]])
>>> c = np.array([1, 2, 3])
>>> d = np.array([4, 5])
>>>
>>> a // a
array([[1, 1, 1],
       [1, 1, 1]])
>>>
>>> a // b
array([[0, 0, 0],
       [0, 0, 0]])
>>>
>>> a // c
array([[1, 1, 1],
       [4, 2, 2]])
>>>
>>> a // d  # doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
ValueError: operands could not be broadcast together with shapes (2,3) (2,)


Modulo
------
>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> b = np.array([[4, 5, 6], [7, 8, 9]])
>>> c = np.array([1, 2, 3])
>>> d = np.array([4, 5])
>>>
>>> a % a
array([[0, 0, 0],
       [0, 0, 0]])
>>>
>>> a % b
array([[1, 2, 3],
       [4, 5, 6]])
>>>
>>> a % c
array([[0, 0, 0],
       [0, 1, 0]])
>>>
>>> a % d  # doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
ValueError: operands could not be broadcast together with shapes (2,3) (2,)


Power
-----
>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> b = np.array([[4, 5, 6], [7, 8, 9]])
>>> c = np.array([1, 2, 3])
>>> d = np.array([4, 5])
>>>
>>> a ** a
array([[    1,     4,    27],
       [  256,  3125, 46656]])
>>>
>>> a ** b
array([[       1,       32,      729],
       [   16384,   390625, 10077696]])
>>>
>>> a ** c
array([[  1,   4,  27],
       [  4,  25, 216]])
>>>
>>> a ** d  # doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
ValueError: operands could not be broadcast together with shapes (2,3) (2,)


Root
----
>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> b = np.array([[4, 5, 6], [7, 8, 9]])
>>> c = np.array([1, 2, 3])
>>> d = np.array([4, 5])
>>>
>>> a ** (1/a)
array([[1.        , 1.41421356, 1.44224957],
       [1.41421356, 1.37972966, 1.34800615]])
>>>
>>> a ** (1/b)
array([[1.        , 1.14869835, 1.20093696],
       [1.21901365, 1.22284454, 1.22028494]])
>>>
>>> a ** (1/c)
array([[1.        , 1.41421356, 1.44224957],
       [4.        , 2.23606798, 1.81712059]])
>>>
>>> a ** (1/d)  # doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
ValueError: operands could not be broadcast together with shapes (2,3) (2,)


Array Multiplication
--------------------
* Multiplication ``*`` remains elementwise
* Does not correspond to matrix multiplication

>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> b = np.array([[4, 5, 6], [7, 8, 9]])
>>> c = np.array([1, 2, 3])
>>> d = np.array([4, 5])
>>>
>>> a * a
array([[ 1,  4,  9],
       [16, 25, 36]])
>>>
>>> a * b
array([[ 4, 10, 18],
       [28, 40, 54]])
>>>
>>> a * c
array([[ 1,  4,  9],
       [ 4, 10, 18]])
>>>
>>> a * d  # doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
ValueError: operands could not be broadcast together with shapes (2,3) (2,)


Matrix Multiplication
---------------------
.. figure:: img/arithmetic-matmul.gif

.. figure:: img/arithmetic-matmul.jpg

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> b = np.array([[1, 2],
...               [3, 4],
...               [5, 6]])
>>>
>>> a @ b
array([[22, 28],
       [49, 64]])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> b = np.array([[4, 5, 6],
...               [7, 8, 9]])
>>>
>>> a @ b  # doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 2 is different from 3)


Dot
---
* ``np.dot()``
* If either a or b is 0-D (scalar), it is equivalent to ``multiply`` and using ``numpy.multiply(a, b)`` or ``a * b`` is preferred.
* If both a and b are 1-D arrays, it is inner product of vectors (without complex conjugation).
* If both a and b are 2-D arrays, it is matrix multiplication, but using ``matmul`` or ``a @ b`` is preferred.
* If a is an N-D array and b is a 1-D array, it is a sum product over the last axis of a and b.
* If a is an N-D array and b is an M-D array (where ``M>=2``), it is a sum product over the last axis of a and the second-to-last axis of b: ``dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])``

>>> a = np.array([1, 2, 3], float)
>>> b = np.array([0, 1, 1], float)
>>>
>>> np.dot(a, b)
5.0

>>> a = np.array([[0, 1], [2, 3]], float)
>>> b = np.array([2, 3], float)
>>> c = np.array([[1, 1], [4, 0]], float)
>>>
>>> np.dot(b, a)
array([ 6., 11.])
>>>
>>> np.dot(a, b)
array([ 3., 13.])
>>>
>>> np.dot(a, c)
array([[ 4.,  0.],
       [14.,  2.]])
>>>
>>> np.dot(c, a)
array([[2., 4.],
       [0., 4.]])

References
----------
.. [#NumpyBroadcastingRules] Alex Chabot-Leclerc. Introduction to Numerical Computing with NumPy: Broadcasting Rules. Year: 2019. Retrieved: 2019-11-31. URL: https://youtu.be/ZB7BZMhfPgk?t=5142


Assignments
-----------
.. literalinclude:: assignments/numpy_broadcasting_a.py
    :caption: :download:`Solution <assignments/numpy_broadcasting_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_broadcasting_b.py
    :caption: :download:`Solution <assignments/numpy_broadcasting_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_broadcasting_c.py
    :caption: :download:`Solution <assignments/numpy_broadcasting_c.py>`
    :end-before: # Solution
