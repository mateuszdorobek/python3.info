Array Create
============


SetUp
-----
>>> import numpy as np


Example
-------
* ``ndarray`` - n-dimensional array

>>> a = np.array([1, 2, 3])
>>>
>>> type(a)
<class 'numpy.ndarray'>


From List
---------
>>> data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> np.array(data)
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


From Range
----------


data = range(0, 10)
np.array(data)
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

data
range(0, 10)
list(data)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


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


Performance
-----------
* Python 3.11.4

Pure Python:

>>> # doctest: +SKIP
... %%timeit -n 1000 -r 1000
... data = range(0, 10)
... result = list(data)
279 ns ± 102 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> # doctest: +SKIP
... %%timeit -n 1000 -r 1000
... result = [x for x in range(0, 10)]
520 ns ± 201 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

Python + Numpy:

>>> # doctest: +SKIP
... %%timeit -n 1000 -r 1000
... data = range(0, 10)
... result = np.array(data)
2.34 µs ± 249 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> # doctest: +SKIP
... %%timeit -n 1000 -r 1000
... result = np.array(range(0, 10))
2.46 µs ± 359 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

Pure Numpy:

>>> # doctest: +SKIP
... %%timeit -n 1000 -r 1000
... result = np.arange(0, 10)
559 ns ± 189 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)


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
