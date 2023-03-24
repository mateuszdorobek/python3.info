OOP Stringify About
===================
* ``str()``
* ``repr()``


SetUp
-----
>>> import datetime
>>>
>>> date = datetime.date(1969, 7, 21)


Str
---
>>> str(date)
'1969-07-21'

>>> print(date)
1969-07-21


Repr
----
>>> repr(date)
'datetime.date(1969, 7, 21)'

>>> date
datetime.date(1969, 7, 21)


Memory Address
--------------
>>> class User:
...     pass
...
>>> mark = User()

Printing ``user`` will display memory address of an object:

>>> print(mark)  # doctest: +SKIP
<__main__.User object at 0x1064f0f90>

CPython implementation of ``id()`` builtin function will return
the same memory address of an object, but in decimal form.
You can convert this to the hexadecimal form using ``hex()`` function.

>>> id(mark)  # doctest: +SKIP
4400811920
>>>
>>> hex(id(mark))  # doctest: +SKIP
'0x1064f0f90'
