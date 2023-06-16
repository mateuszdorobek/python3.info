Operator Module
===============
* ``operator.add()``
* ``operator.sub()``
* ``operator.mul()``
* ``operator.truediv()``
* ``operator.floordiv()``
* ``operator.mod()``
* ``operator.pow()``
* ``operator.matmul()``
* ``operator.neg()``
* ``operator.pos()``
* ``operator.invert()``

The operator module in Python provides a set of functions that correspond to
the built-in operators in Python. These functions can be used to perform
operations on data types such as numbers, strings, and lists.

The module contains functions for arithmetic operations such as addition,
subtraction, multiplication, and division, as well as functions for logical
operations such as AND, OR, NOT, and XOR. It also includes functions for
comparison operations such as less than, greater than, equal to, and not
equal to.

One of the main benefits of using the operator module is that it allows you
to perform operations on objects that may not support the corresponding
operator. For example, you can use the ``operator.add()`` function to add two
lists together, even though the ``+`` operator is not supported for lists.

Overall, the operator module provides a convenient way to perform operations
in Python and can be particularly useful in functional programming.


Operator Module - AND
---------------------
.. code-block:: text

    1 & 1 = 1
    1 & 0 = 0
    0 & 1 = 0
    0 & 0 = 0

>>> from operator import and_
>>>
>>>
>>> and_(True, True)
True
>>> and_(True, False)
False
>>> and_(False, True)
False
>>> and_(False, False)
False


Operator Module - OR
--------------------
.. code-block:: text

    1 | 1 = 1
    1 | 0 = 1
    0 | 1 = 1
    0 | 0 = 0

>>> from operator import or_
>>>
>>>
>>> or_(True, True)
True
>>> or_(True, False)
True
>>> or_(False, True)
True
>>> or_(False, False)
False


Operator Module - XOR
---------------------
.. code-block:: text

    1 ^ 1 = 0
    1 ^ 0 = 1
    0 ^ 1 = 1
    0 ^ 0 = 0

>>> from operator import xor
>>>
>>>
>>> xor(True, True)
False
>>> xor(True, False)
True
>>> xor(False, True)
True
>>> xor(False, False)
False



Reduce
------
>>> from functools import reduce
>>>
>>> data = [1, 2, 3, 4]

>>> def add(x, y):
...     return x + y
>>>
>>> def sub(x, y):
...     return x - y
>>>
>>> def mul(x, y):
...     return x * y
>>>
>>>
>>> reduce(add, data)
10
>>> reduce(sub, data)
-8
>>> reduce(mul, data)
24

>>> reduce(lambda x,y: x+y, data)
10
>>> reduce(lambda x,y: x-y, data)
-8
>>> reduce(lambda x,y: x*y, data)
24

>>> from operator import add, sub, mul
>>>
>>> reduce(add, data)
10
>>> reduce(sub, data)
-8
>>> reduce(mul, data)
24


Methodcaller
------------
>>> from operator import methodcaller
>>>
>>> colors = ['red', 'green', 'blue']

>>> result = filter(lambda x: x.startswith('r'), colors)
>>> list(result)
['red']

>>> result = filter(methodcaller('startswith', 'r'), colors)
>>> list(result)
['red']


Reduce
------
>>> from functools import reduce
>>> from operator import add

>>> data = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9],
... ]

>>> result = 0
>>>
>>> for row in data:
...     for digit in row:
...         result += digit
>>>
>>> print(result)
45

>>> sum(data[0])
6
>>>
>>> sum(data[1])
15
>>>
>>> sum(data[2])
24
>>>
>>>
>>> sum(data[0]) + sum(data[1]) + sum(data[2])
45

>>> reduce(add, data[0])
6
>>>
>>> reduce(add, data[1])
15
>>>
>>> reduce(add, data[2])
24
>>>
>>>
>>> reduce(add, [
...     reduce(add, data[0]),
...     reduce(add, data[1]),
...     reduce(add, data[2]),
... ])
45


Map-Reduce
----------
>>> from functools import reduce
>>> from itertools import starmap
>>> from operator import add, sub, mul

>>> def square(x):
...     return x ** 2
>>>
>>> def cube(x):
...     return x ** 3
>>>
>>> def apply(data, fn):
...     return map(fn, data)

>>> data = [1, 2, 3, 4]
>>> funcs = [square, cube]
>>>
>>> result = reduce(apply, funcs, data)
>>> list(result)
[1, 64, 729, 4096]
>>>
>>> result = reduce(apply, funcs, data)
>>> reduce(add, result)
4890

>>> data = [1, 2, 3, 4]
>>> funcs = [add, sub, mul]
>>>
>>> result = [reduce(fn,data) for fn in funcs]
>>> reduce(add, result)
26
>>>
>>> result = map(lambda fn: reduce(fn,data), funcs)
>>> reduce(add, result)
26

>>> data = [1, 2, 3, 4]
>>> funcs = [
...     (add, data),
...     (sub, data),
...     (mul, data),
... ]
>>>
>>> result = starmap(reduce, funcs)
>>> reduce(add, result)
26

>>> data = [1, 2, 3, 4]
>>> result = starmap(reduce, [
...     (add, data),
...     (sub, data),
...     (mul, data)])
>>>
>>> reduce(add, result)
26
