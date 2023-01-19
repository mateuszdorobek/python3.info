Operator Left
=============
* ``x + y`` - will call method "add" on object ``x`` (``x.__add__(y)``)
* ``x - y`` - will call method "sub" on object ``x`` (``x.__sub__(y)``)
* ``x * y`` - will call method "mul" on object ``x`` (``x.__mul__(y)``)
* ``x ** y`` - will call method "pow" on object ``x`` (``x.__pow__(y)``)
* ``x @ y`` - will call method "matmul" on object ``x`` (``x.__matmul__(y)``)
* ``x / y`` - will call method "truediv" on object ``x`` (``x.__truediv__(y)``)
* ``x // y`` - will call method "floordiv" on object ``x`` (``x.__floordiv__(y)``)
* ``x % y`` - will call method "mod" on object ``x`` (``x.__mod__(y)``)

.. csv-table:: Numerical Operator Overload
    :header: "Operator", "Method"

    "``obj + other``",     "``obj.__add__(other)``"
    "``obj - other``",     "``obj.__sub__(other)``"
    "``obj * other``",     "``obj.__mul__(other)``"
    "``obj ** other``",    "``obj.__pow__(other)``"
    "``obj @ other``",     "``obj.__matmul__(other)``"
    "``obj / other``",     "``obj.__truediv__(other)``"
    "``obj // other``",    "``obj.__floordiv__(other)``"
    "``obj % other``",     "``obj.__mod__(other)``"


SetUp
-----
>>> from dataclasses import dataclass
>>> from functools import reduce


Syntax
------
>>> @dataclass
... class Vector:
...     x: int
...     y: int
...
...     def __add__(self, other): ...               # x + y     calls x.__add__(y)
...     def __sub__(self, other): ...               # x - y     calls x.__sub__(y)
...     def __mul__(self, other): ...               # x * y     calls x.__mul__(y)
...     def __pow__(self, power, modulo=None): ...  # x ** y    calls x.__pow__(y)
...     def __matmul__(self, other): ...            # x @ y     calls x.__matmul__(y)
...     def __truediv__(self, other): ...           # x / y     calls x.__truediv__(y)
...     def __floordiv__(self, other): ...          # x // y    calls x.__floordiv__(y)
...     def __mod__(self, other): ...               # x % y     calls x.__mod__(y)


Example
-------
>>> @dataclass
... class Vector:
...     x: int
...     y: int
...
...     def __add__(self, other):
...         new_x = self.x + other.x
...         new_y = self.y + other.y
...         return Vector(new_x, new_y)
...
>>>
>>>
>>> a = Vector(x=1, y=2)
>>> b = Vector(x=3, y=4)
>>> c = Vector(x=5, y=6)
>>>
>>> (a+b) + c
Vector(x=9, y=12)


Use Case - 0x01
---------------
* Game

>>> hero @ Position(x=50, y=120)  # doctest: +SKIP
>>>
>>> hero['gold'] += dragon['gold']  # doctest: +SKIP


Use Case - 0x02
---------------
This is our function library.

Transformation functions (non-reducing) -
takes one argument and returns one value:

>>> def increment(x):
...     return x + 1
>>>
>>> def decrement(x):
...     return x - 1
>>>
>>> def square(x):
...     return x ** 2
>>>
>>> def cube(x):
...     return x ** 3

Reducing functions - takes two arguments returns one value:

>>> def add(x, y):
...     return x + y
>>>
>>> def sub(x, y):
...     return x - y
>>>
>>> def mul(x, y):
...     return x * x

We have data to compute:

>>> data = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9],
... ]

On this data, we want to apply the following transformations:

>>> transformations = [increment, square, decrement, cube]

We need to create apply function, which takes data and apply
the transformation:

>>> def apply(data, fn):
...     return map(fn, data)

Let's do it parallel. We will create three independent workers.
Each worker will get part of the data (one-third) and will apply
all the transformation (map) to their data subset.

>>> workerA = reduce(apply, transformations, data[0])  # [27, 512, 3375]
>>> workerB = reduce(apply, transformations, data[1])  # [13824, 42875, 110592]
>>> workerC = reduce(apply, transformations, data[2])  # [250047, 512000, 970299]

Note, that all workers will produce generators (maps).
We need to merge the results using ``reduce`` function,
but before that we need to evaluate maps to lists.

>>> def merge(x, y):
...     return list(x) + list(y)

>>> merged = reduce(merge, [workerA, workerB, workerC])
>>> result = reduce(add, merged)

>>> print(result)
1903551

>>> print(merged)
[27, 512, 3375, 13824, 42875, 110592, 250047, 512000, 970299]


Assignments
-----------
.. literalinclude:: assignments/operator_left_a.py
    :caption: :download:`Solution <assignments/operator_left_a.py>`
    :end-before: # Solution
