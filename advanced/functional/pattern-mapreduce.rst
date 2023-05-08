Functional Pattern MapReduce
============================
* split-apply-combine strategy

Apply function of two arguments cumulatively to the items of iterable, from
left to right, so as to reduce the iterable to a single value. For example,
``reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])`` calculates
``((((1+2)+3)+4)+5)``. The left argument, x, is the accumulated value and
the right argument, y, is the update value from the iterable. If the
optional initializer is present, it is placed before the items of the
iterable in the calculation, and serves as a default when the iterable is
empty. If initializer is not given and iterable contains only one item, the
first item is returned.

.. figure:: img/functional-map-reduce.gif

    Computational graph for map-reduce. [#dask]_


SetUp
-----
>>> from functools import reduce


Pattern
-------
>>> class MapReduce:
...     def __init__(self, values):
...         self.values = values
...
...     def filter(self, fn):
...          self.values = filter(fn, self.values)
...          return self
...
...     def map(self, fn):
...         self.values = map(fn, self.values)
...         return self
...
...     def reduce(self, fn):
...         return reduce(fn, self.values)


Usage
-----
>>> DATA = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> result = (
...     MapReduce(DATA)
...     .map(lambda x: x ** 2)
...     .map(lambda x: x / 2)
...     .map(lambda x: x + 2)
...     .map(lambda x: round(x, 2))
...     .map(lambda x: int(x))
...     .filter(lambda x: x > 10)
...     .reduce(lambda x,y: x + y)
... )
>>>
>>> result
136


Use Case - 0x01
---------------
>>> def even(x):
...     return x % 2 == 0
>>>
>>> def positive(x):
...     return x > 0
>>>
>>> def non_negative(x):
...     return x >= 0
>>>
>>> def square(x):
...     return x ** 2
>>>
>>> def increment(x):
...     return x + 1
>>>
>>> def decrement(x):
...     return x + 1

>>> from functools import reduce
>>> from operator import add
>>>
>>> data = range(0, 1024)
>>> data = filter(even, data)
>>> data = filter(positive, data)
>>> data = filter(non_negative, data)
>>> data = map(square, data)
>>> data = map(increment, data)
>>> data = map(decrement, data)
>>> result = reduce(add, data)
>>>
>>> result
178434046


Use Case - 0x02
---------------
>>> def even(x):
...     return x % 2 == 0
>>>
>>> def positive(x):
...     return x > 0
>>>
>>> def non_negative(x):
...     return x >= 0
>>>
>>> def square(x):
...     return x ** 2
>>>
>>> def increment(x):
...     return x + 1
>>>
>>> def decrement(x):
...     return x + 1

>>> filters = [
...     even,
...     positive,
...     non_negative,
... ]
>>>
>>> maps = [
...     square,
...     increment,
...     decrement,
... ]
>>>
>>> def apply(data, fn):
...     return map(fn, data)

>>> from functools import reduce
>>> from operator import add
>>>
>>> data = range(0, 1024)
>>> data = reduce(apply, filters, data)
>>> data = reduce(apply, maps, data)
>>> result = reduce(add, data)
>>>
>>> result
3072


Use Case - 0x03
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
