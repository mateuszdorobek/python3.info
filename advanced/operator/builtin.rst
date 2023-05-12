Operator Builtin
================
* ``abs()``
* ``bool()``
* ``complex()``
* ``del()``
* ``delattr()``
* ``dir()``
* ``divmod()``
* ``float()``
* ``getattr()``
* ``hash()``
* ``hex()``
* ``int()``
* ``iter()``
* ``len()``
* ``next()``
* ``oct()``
* ``pow()``
* ``reversed()``
* ``round()``
* ``setattr()``


About
-----
.. csv-table:: Builtin Functions Overload
    :header: "Function", "Method"

    "``abs(obj)``",                      "``obj.__abs__()``"
    "``bool(obj)``",                     "``obj.__bool__()``"
    "``complex(obj)``",                  "``obj.__complex__()``"
    "``del obj``",                       "``obj.__del__()``"
    "``delattr(obj, name)``",            "``obj.__delattr__(name)``"
    "``dir(obj)``",                      "``obj.__dir__()``"
    "``divmod(obj, other)``",            "``obj.__divmod__(other)``"
    "``float(obj)``",                    "``obj.__float__()``"
    "``getattr(obj, name, default)``",   "``obj.__getattr__(name, default)``"
    "``hash(obj)``",                     "``obj.__hash__()``"
    "``hex(obj)``",                      "``obj.__hex__()``"
    "``int(obj)``",                      "``obj.__int__()``"
    "``iter(obj)``",                     "``obj.__iter__()``"
    "``len(obj)``",                      "``obj.__len__()``"
    "``next(obj)``",                     "``obj.__next__()``"
    "``oct(obj)``",                      "``obj.__oct__()``"
    "``pow(obj)``",                      "``obj.__pow__()``"
    "``reversed(obj)``",                 "``obj.__reversed__()``"
    "``round(obj, ndigits)``",           "``obj.__round__(ndigits)``"
    "``setattr(obj, name)``",            "``obj.__setattr__(name)``"


Length
------
>>> data = [1, 2, 3]
>>>
>>> len(data)
3
>>>
>>> data.__len__()
3

This is because ``len(data)`` calls ``data.__len__()``.

>>> class User:
...     pass
...
>>>
>>> a = User()
>>>
>>> len(a)
Traceback (most recent call last):
TypeError: object of type 'User' has no len()

>>> class User:
...     def __len__(self):
...         return 69
>>>
>>>
>>> a = User()
>>>
>>> len(a)
69


Float
-----
>>> class User:
...     pass
...
>>>
>>> a = User()
>>>
>>> float(a)
Traceback (most recent call last):
TypeError: float() argument must be a string or a real number, not 'User'

>>> class User:
...     def __float__(self):
...         return 13.37
...
>>>
>>> a = User()
>>>
>>> float(a)
13.37


Abs
---
>>> from math import sqrt
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Vector:
...     x: int = 0
...     y: int = 0
...
...     def __abs__(self):
...         return sqrt(self.x**2 + self.y**2)
>>>
>>>
>>> abs(Vector(x=3, y=4))
5.0


Round
-----
>>> pi = 3.1415
>>>
>>> type(pi)
<class 'float'>
>>>
>>> round(pi, 2)
3.14
>>>
>>> float.__round__(pi, 2)
3.14


Use Case - 0x01
---------------
>>> class User:
...     def __float__(self) -> float:
...         return 1961.0
...
...     def __int__(self) -> int:
...         return 1969
...
...     def __len__(self) -> int:
...         return 170
...
...     def __str__(self) -> str:
...         return 'My name... José Jiménez'
...
...     def __repr__(self) -> str:
...         return f'User()'
>>>
>>>
>>> mark = User()
>>>
>>> float(mark)
1961.0
>>>
>>> int(mark)
1969
>>>
>>> len(mark)
170
>>>
>>> repr(mark)
'User()'
>>>
>>> str(mark)
'My name... José Jiménez'
>>>
>>> print(mark)
My name... José Jiménez
