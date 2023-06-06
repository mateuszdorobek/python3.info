Idiom Reduce
============
* Reduce sequence using function
* Built-in

>>> 1 + 2
3

>>> 1 + 2 + 3 + 4
10


Syntax
------
* ``functools.reduce(function, iterable[, initializer])``
* required ``callable`` - Function
* required ``iterable`` - Sequence or iterator object
* https://docs.python.org/library/functools.html


Problem
-------
>>> def add(x, y):
...     return x + y
>>>
>>>
>>> DATA = [1, 2, 3, 4]
>>> result = 0
>>>
>>> for element in DATA:
...     result = add(result, element)
>>>
>>> print(result)
10


Solution
--------
>>> from functools import reduce
>>>
>>>
>>> def add(x, y):
...     return x + y
>>>
>>>
>>> DATA = [1, 2, 3, 4]
>>>
>>> reduce(add, DATA)
10


Rationale
---------
* https://docs.python.org/library/operator.html

>>> from functools import reduce
>>> from operator import mul
>>>
>>>
>>> DATA = [1, 2, 3, 4]
>>>
>>> reduce(mul, DATA)
24

>>> from functools import reduce
>>>
>>>
>>> DATA = [1, 2, 3, 4]
>>>
>>> reduce(min, DATA)
1
>>> reduce(max, DATA)
4


Map Reduce
----------
* https://dask.org

.. figure:: img/idiom-reduce-mapreduce.gif


Assignments
-----------
.. literalinclude:: assignments/idiom_reduce_a.py
    :caption: :download:`Solution <assignments/idiom_reduce_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_reduce_b.py
    :caption: :download:`Solution <assignments/idiom_reduce_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_reduce_c.py
    :caption: :download:`Solution <assignments/idiom_reduce_c.py>`
    :end-before: # Solution
