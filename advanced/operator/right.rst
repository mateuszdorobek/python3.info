Operator Right
==============
* ``x + y`` - if method "add" on object ``x`` fails, then call "radd" on object ``y`` (``y.__radd__(x)``)
* ``x - y`` - if method "sub" on object ``x`` fails, then call "rsub" on object ``y`` (``y.__rsub__(x)``)
* ``x * y`` - if method "mul" on object ``x`` fails, then call "rmul" on object ``y`` (``y.__rmul__(x)``)
* ``x ** y`` - if method "pow" on object ``x`` fails, then call "rpow" on object ``y`` (``y.__rpow__(x)``)
* ``x @ y`` - if method "matmul" on object ``x`` fails, then call "rmatmul" on object ``y`` (``y.__rmatmul__(x)``)
* ``x / y`` - if method "truediv" on object ``x`` fails, then call "rtruediv" on object ``y`` (``y.__rtruediv__(x)``)
* ``x // y`` - if method "floordiv" on object ``x`` fails, then call "rfloordiv" on object ``y`` (``y.__rfloordiv__(x)``)
* ``x % y`` - if method "mod" on object ``x`` fails, then call "rmod" on object ``y`` (``y.__rmod__(x)``)

.. csv-table:: Numerical Operator Overload
    :header: "Operator", "Method"

    "``obj + other``",     "``other.__radd__(obj)``"
    "``obj - other``",     "``other.__rsub__(obj)``"
    "``obj * other``",     "``other.__rmul__(obj)``"
    "``obj ** other``",    "``other.__rpow__(obj)``"
    "``obj @ other``",     "``other.__rmatmul__(obj)``"
    "``obj / other``",     "``other.__rtruediv__(obj)``"
    "``obj // other``",    "``other.__rfloordiv__(obj)``"
    "``obj % other``",     "``other.__rmod__(obj)``"


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
...     def __radd__(self, other): ...              # x + y     if fails, then calls y.__radd__(x)
...     def __rsub__(self, other): ...              # x - y     if fails, then calls y.__rsub__(x)
...     def __rmul__(self, other): ...              # x * y     if fails, then calls y.__rmul__(x)
...     def __rpow__(self, power, modulo=None): ... # x ** y    if fails, then calls y.__rpow__(x)
...     def __rmatmul__(self, other): ...           # x @ y     if fails, then calls y.__rmatmul__(x)
...     def __rtruediv__(self, other): ...          # x / y     if fails, then calls y.__rtruediv__(x)
...     def __rfloordiv__(self, other): ...         # x // y    if fails, then calls y.__rfloordiv__(x)
...     def __rmod__(self, other): ...              # x % y     if fails, then calls y.__rmod__(x)


Left Operation
--------------
>>> class Left:
...     def __add__(self, other):
...         return 'left'
>>>
>>> class Right:
...     pass

Left operation:

>>> Left() + Right()   # left.__add__(right)
'left'

What if ``Right`` class does not define ``__add__`` attribute?

>>> Right() + Left()    # right.__add__(left)
Traceback (most recent call last):
TypeError: unsupported operand type(s) for +: 'Right' and 'Left'


Example
-------
>>> class Left:
...     def __add__(self, other):
...         return 'left'
...
...     def __radd__(self, other):
...         return 'left too'
>>>
>>>
>>> class Right:
...     pass

Left operation:

>>> Left() + Right()   # left.__add__(right)
'left'

What if ``Right`` class does not define ``__add__`` attribute?
Python will search for ``__radd__`` attribute in ``Right`` class:

>>> Right() + Left()     # Right.__add__(left) -> error -> # left.__radd__(right)
'left too'


Both
----
>>> class Left:
...     def __add__(self, other):
...         return 'left'
...
...     def __radd__(self, other):
...         return 'left too'
>>>
>>>
>>> class Right:
...     def __add__(self, other):
...         return 'right'
>>>
>>>
>>> Left() + Right()    # left.__add__(right)
'left'
>>>
>>> Right() + Left()    # right.__add__(left)
'right'


Example
-------
>>> a = 1
>>> b = 2
>>>
>>>
>>> a - b
-1
>>>
>>> a.__sub__(b)
-1
>>> b.__rsub__(a)
-1
>>>
>>>
>>> b - a
1
>>>
>>> b.__sub__(a)
1
>>> a.__rsub__(b)
1

Use Case
--------
>>> import numpy as np
>>>
>>>
>>> mylist = [1, 2, 3]
>>> myarr = np.array([4,5,6])
>>>
>>>
>>> myarr + mylist
array([5, 7, 9])
>>>
>>>
>>> mylist + myarr
array([5, 7, 9])
>>>
>>>
>>> mylist.__add__(myarr)
Traceback (most recent call last):
TypeError: can only concatenate list (not "numpy.ndarray") to list
>>>
>>> myarr.__radd__(mylist)
array([5, 7, 9])

>>> class ndarray:
...     def __add__(self, other):
...         if isinstance(other, list):
...             other = np.array(other)
...         if isinstance(other, np.array):
...             ...
...
...     def __radd__(self, other):
...         if isinstance(other, list):
...             other = np.array(other)
...         if isinstance(other, np.array):
...             ...


Use Case - 0x01
---------------
* Game

>>> hero @ Position(x=50, y=120)  # doctest: +SKIP
>>>
>>> hero['gold'] += dragon['gold']  # doctest: +SKIP


Use Case - 0x02
---------------
>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> @dataclass
... class Crew:
...     members: list[Astronaut] = field(default_factory=list)
...
...     def __iadd__(self, other):
...         self.members.append(other)
...         return self
>>>
>>>
>>> ares3 = Crew()
>>> ares3 += Astronaut('Mark', 'Watney')
>>> ares3 += Astronaut('Melissa', 'Lewis')
>>>
>>> print(ares3)
Crew(members=[Astronaut(firstname='Mark', lastname='Watney'), Astronaut(firstname='Melissa', lastname='Lewis')])
>>>
>>> for member in ares3.members:
...     print(member)
Astronaut(firstname='Mark', lastname='Watney')
Astronaut(firstname='Melissa', lastname='Lewis')


Use Case - 0x03
---------------
>>> a = np.array([1, 2, 3])
>>> b = [4, 5, 6]
>>>
>>> a
array([1, 2, 3])
>>>
>>> b
[4, 5, 6]

>>> a + b
array([5, 7, 9])
>>>
>>> a.__add__(b)
array([5, 7, 9])

>>> b + a
array([5, 7, 9])
>>>
>>> b.__add__(a)
Traceback (most recent call last):
TypeError: can only concatenate list (not "numpy.ndarray") to list

>>> a.__radd__(b)
array([5, 7, 9])


Use Case - 0x04
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
