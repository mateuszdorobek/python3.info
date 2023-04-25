Operator Arithmetic About
=========================
* Operator Overload
* Operator Overload is the Pythonic way
* Operator Overload allows readable syntax
* Operator Overload allows simpler operations
* All examples in this chapter uses ``dataclasses`` for you to focus on the important code, not boilerplate code just to make it works


SetUp
-----
>>> from dataclasses import dataclass


Operators
---------
* Source: https://github.com/python/cpython/blob/main/Grammar/python.gram#L695
* Comparison: ``==``, ``!=``, ``<=``, ``<``, ``>=``, ``>``, ``not in``, ``in``, ``is not``, ``is``
* Bitwise: ``|``, ``^``, ``&``, ``<<``, ``>>``
* Arithmetic: ``+``, ``-``, ``*``, ``/``, ``//``, ``%``, ``@``, ``**``, ``~``


Recap
-----
>>> a = int(1)
>>> b = int(2)
>>> a + b
3

>>> a = float(1.0)
>>> b = float(2.0)
>>> a + b
3.0

>>> a = str('1')
>>> b = str('2')
>>> a + b
'12'

>>> a = list([1])
>>> b = list([2])
>>> a + b
[1, 2]

>>> a = tuple((1,))
>>> b = tuple((2,))
>>> a + b
(1, 2)


Problem
-------
* ``dataclass`` is used to generate ``__init__()`` and ``__repr__()``
* ``dataclass`` does not have any influence on addition

>>> @dataclass
... class Vector:
...     x: int
...     y: int
>>>
>>>
>>> a = Vector(x=1, y=2)
>>> b = Vector(x=2, y=3)
>>> a + b
Traceback (most recent call last):
TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'


Solution
--------
>>> @dataclass
... class Vector:
...     x: int = 0
...     y: int = 0
...
...     def __add__(self, other):
...         new_x = self.x + other.x
...         new_y = self.y + other.y
...         return Vector(new_x, new_y)
>>>
>>>
>>> a = Vector(x=1, y=2)
>>> b = Vector(x=2, y=3)
>>> a + b
Vector(x=3, y=5)


Further Reading
---------------
* https://docs.python.org/reference/datamodel.html#emulating-numeric-types
* https://docs.python.org/library/operator.html
