Operator Arithmetic About
=========================
* Operator Overload
* Operator Overload is the Pythonic way
* Operator Overload allows readable syntax
* Operator Overload allows simpler operations
* All examples in this chapter uses ``dataclasses`` for you to focus on the important code, not boilerplate code just to make it works


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


Problem
-------
>>> class Vector:
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
>>>
>>>
>>> a = Vector(1,2)
>>> b = Vector(2,3)
>>> a + b
Traceback (most recent call last):
TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'


Solution
--------
>>> class Vector:
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
>>>
>>>
>>> Vector(x=1, y=2) + Vector(x=3, y=4)
Traceback (most recent call last):
TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'


Dataclasses
-----------
>>> from dataclasses import dataclass

>>> @dataclass
... class Vector:
...     x: int
...     b: int
>>>
>>>
>>> a = Vector(1,2)
>>> b = Vector(2,3)
>>> a + b
Traceback (most recent call last):
TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'

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
>>> Vector(x=1, y=2) + Vector(x=3, y=4)
Vector(x=4, y=6)
>>>
>>> Vector(x=1, y=2) + Vector(x=3, y=4) + Vector(x=5, y=6)
Vector(x=9, y=12)


Further Reading
---------------
* https://docs.python.org/reference/datamodel.html#emulating-numeric-types
* https://docs.python.org/library/operator.html
