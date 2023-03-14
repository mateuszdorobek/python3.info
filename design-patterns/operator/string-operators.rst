Operator String Operators
=========================
* ``+`` - add
* ``-`` - sub
* ``*`` - mul
* ``%`` - mod
* ``+=`` - iadd
* ``-=`` - isub
* ``*=`` - imul
* ``%=`` - imod


About
-----
.. csv-table:: String Operator Overload
    :header: "Operator", "Method"

    "``obj + other``",        "``obj.__add__(other)``"
    "``obj - other``",        "``obj.__sub__(other)``"
    "``obj * other``",        "``obj.__mul__(other)``"
    "``obj % other``",        "``obj.__mod__(other)``"

    "``obj += other``",       "``obj.__iadd__(other)``"
    "``obj -= other``",       "``obj.__isub__(other)``"
    "``obj *= other``",       "``obj.__imul__(other)``"
    "``obj %= other``",       "``obj.__imod__(other)``"


Mod
---
* ``%`` (``__mod__``) operator behavior for ``int`` and ``str``:

>>> 13 % 4
1
>>>
>>> '13' % '4'
Traceback (most recent call last):
TypeError: not all arguments converted during string formatting

>>> pi = 3.1514
>>>
>>>
>>> 'String: %s' % pi
'String: 3.1514'
>>>
>>> 'Double: %d' % pi
'Double: 3'
>>>
>>> 'Float: %f' % pi
'Float: 3.151400'

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>>
>>> 'Hello %s' % firstname
'Hello Mark'
>>>
>>> 'Hello %s %s' % (firstname, lastname)
'Hello Mark Watney'
>>>
>>> 'Hello %(fname)s %(lname)s' % {'fname': firstname, 'lname': lastname}
'Hello Mark Watney'

>>> text = 'Hello %s'
>>> text %= 'Mark Watney'
>>>
>>> print(text)
Hello Mark Watney

>>> class Str:
...     def __mod__(self, other):
...         """str substitute"""
...
...         if type(other) is str:
...             ...
...         if type(other) is tuple:
...             ...
...         if type(other) is dict:
...             ...

Note, that using ``%s``, ``%d``, ``%f`` is currently deprecated in favor
of ``f'...'`` string formatting. More information in `Builtin Printing`
