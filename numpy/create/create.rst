Array Create
============


SetUp
-----
>>> import numpy as np


Declare
-------
1-dimensional Array:

>>> np.array([1, 2, 3])
array([1, 2, 3])
>>>
>>> np.array([1.0, 2.0, 3.0])
array([1., 2., 3.])
>>>
>>> np.array([1.1, 2.2, 3.3])
array([1.1, 2.2, 3.3])
>>>
>>> np.array([1, 2, 3], float)
array([1., 2., 3.])
>>>
>>> np.array([1, 2, 3], dtype=float)
array([1., 2., 3.])

2-dimensional Array:

>>> np.array([[1, 2, 3],
...           [4, 5, 6],
...           [7, 8, 9]])
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

3-dimensional Array:

>>> np.array([[[1, 2, 3],
...            [4, 5, 6],
...            [7, 8, 9]],
...
...           [[1, 2, 3],
...            [4, 5, 6],
...            [7, 8, 9]]])
...
array([[[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]],
<BLANKLINE>
       [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]])

.. figure:: img/numpy-create-cake.png

    Multi layer cake as an analog for n-dim array [#CAKE]_


Stringify
---------
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> str(a)
'[[1 2 3]\n [4 5 6]\n [7 8 9]]'
>>>
>>> print(a)
[[1 2 3]
 [4 5 6]
 [7 8 9]]
>>>
>>> repr(a)
'array([[1, 2, 3],\n       [4, 5, 6],\n       [7, 8, 9]])'
>>>
>>> a
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>>
>>> print(repr(a))
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])


Recap
-----
>>> a = np.array([1, 2, 3])
>>> b = np.array(range(0, 10))


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
