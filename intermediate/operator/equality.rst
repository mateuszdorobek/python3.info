Operator Comparison
===================
* ``in`` - contains


SetUp
-----
>>> from functools import reduce


About
-----
.. csv-table:: Comparison Operator Overload
    :header: "Operator", "Method"

    "``obj == other``",   "``obj.__eq__(other)``"
    "``obj != other``",   "``obj.__ne__(other)``"


Object Equality
---------------
* When you compare objects with the same fields from two different classes
* Always remember to compare classes
* This way you avoid bug, when both has the same fields and values
* Eq Works at Both Sides

>>> class Fruit:
...     def __init__(self, name):
...         self.name = name
>>>
>>>
>>> a = Fruit('Apple')
>>> b = Fruit('Apple')
>>>
>>> a == b
False

>>> class Fruit:
...     def __init__(self, name):
...         self.name = name
...
...     def __eq__(self, other):
...         return self.name == other.name
>>>
>>>
>>> a = Fruit('Apple')
>>> b = Fruit('Apple')
>>>
>>> a == b
True

>>> class Fruit:
...     def __init__(self, name):
...         self.name = name
...
...     def __eq__(self, other):
...         return self.name == other.name
>>>
>>>
>>> class Company:
...     def __init__(self, name):
...         self.name = name
>>>
>>>
>>> a = Fruit('Apple')
>>> b = Fruit('Apple')
>>> c = Company('Apple')
>>>
>>> a == b
True
>>>
>>> a == c
True

>>> class Fruit:
...     def __init__(self, name):
...         self.name = name
...
...     def __eq__(self, other):
...         return self.__class__ is other.__class__ \
...            and self.name == other.name
>>>
>>>
>>> class Company:
...     def __init__(self, name):
...         self.name = name
>>>
>>>
>>> a = Fruit('Apple')
>>> b = Fruit('Apple')
>>> c = Company('Apple')
>>>
>>> a == b
True
>>>
>>> a == c
False

Eq Works at Both Sides:

>>> class Fruit:
...     def __init__(self, name):
...         self.name = name
>>>
>>>
>>> class Company:
...     def __init__(self, name):
...         self.name = name
...
...     def __eq__(self, other):
...         return self.__class__ is other.__class__ \
...            and self.name == other.name
>>>
>>>
>>> a = Fruit('Apple')
>>> b = Fruit('Apple')
>>> c = Company('Apple')
>>>
>>> a == b
False
>>>
>>> a == c
False
