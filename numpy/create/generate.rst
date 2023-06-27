Array Generate
==============


SetUp
-----
>>> import numpy as np


Zeros
-----
>>> np.zeros((2, 3))
array([[0., 0., 0.],
       [0., 0., 0.]])
>>>
>>> np.zeros(shape=(2, 3))
array([[0., 0., 0.],
       [0., 0., 0.]])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> np.zeros_like(a)
array([[0, 0, 0],
       [0, 0, 0]])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]], float)
>>>
>>> np.zeros_like(a)
array([[0., 0., 0.],
       [0., 0., 0.]])


Ones
----
>>> np.ones((3, 2))
array([[1., 1.],
       [1., 1.],
       [1., 1.]])
>>>
>>> np.ones(shape=(3, 2))
array([[1., 1.],
       [1., 1.],
       [1., 1.]])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> np.ones_like(a)
array([[1, 1, 1],
       [1, 1, 1]])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]], float)
>>>
>>> np.ones_like(a)
array([[1., 1., 1.],
       [1., 1., 1.]])


Empty
-----
* Garbage from memory
* Will reuse previous if given shape was already created

>>> np.empty((3,4))  # doctest: +SKIP
array([[ 2.31584178e+077,  1.29073692e-231,  2.96439388e-323, 0.00000000e+000],
      [-2.32034891e+077,  2.68678047e+154,  2.18018101e-314, 2.18022275e-314],
      [ 0.00000000e+000,  2.18023445e-314,  1.38338381e-322, 9.03690495e-309]])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> np.empty((2,3))
array([[1., 2., 3.],
       [4., 5., 6.]])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> np.empty_like(a)
array([[1, 2, 3],
       [4, 5, 6]])


Full
----
>>> np.full((2, 2), np.inf)
array([[inf, inf],
       [inf, inf]])
>>>
>>> np.full((2, 2), 10)
array([[10, 10],
       [10, 10]])


Identity
--------
>>> np.identity(2)
array([[1., 0.],
       [0., 1.]])
>>>
>>> np.identity(3)
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
>>>
>>> np.identity(4, int)
array([[1, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 1, 0],
       [0, 0, 0, 1]])


Recap
-----
>>> a = np.zeros(shape=(2,3))
>>> b = np.zeros_like(a)
>>> c = np.ones(shape=(2,3))
>>> d = np.ones_like(a)
>>> e = np.empty(shape=(2,3))
>>> f = np.empty_like(a)
>>> g = np.full(shape=(2, 2), fill_value=np.nan)
>>> h = np.full_like(a, np.nan)
>>> i = np.identity(4)


References
----------
.. [#CAKE] https://i.ytimg.com/vi/iCOhz07Ng6g/maxresdefault.jpg


Assignments
-----------
.. literalinclude:: assignments/numpy_create_a.py
    :caption: :download:`Solution <assignments/numpy_create_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_create_b.py
    :caption: :download:`Solution <assignments/numpy_create_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_create_c.py
    :caption: :download:`Solution <assignments/numpy_create_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_create_d.py
    :caption: :download:`Solution <assignments/numpy_create_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_create_e.py
    :caption: :download:`Solution <assignments/numpy_create_e.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_create_f.py
    :caption: :download:`Solution <assignments/numpy_create_f.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_create_g.py
    :caption: :download:`Solution <assignments/numpy_create_g.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_create_h.py
    :caption: :download:`Solution <assignments/numpy_create_h.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_create_i.py
    :caption: :download:`Solution <assignments/numpy_create_i.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_create_j.py
    :caption: :download:`Solution <assignments/numpy_create_j.py>`
    :end-before: # Solution
