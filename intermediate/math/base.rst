Math Base
=========


Binary
------
* Base 2
* Allowed: 0, 1
* Prefix: ``0b...``

>>> data = 0b1000101
>>> print(data)
69

>>> int('0b1000101', base=2)
69
>>>
>>> int('1000101', base=2)
69

>>> bin(69)
'0b1000101'

>>> int(1000101, base=2)
Traceback (most recent call last):
TypeError: int() can't convert non-string with explicit base
>>>
>>> bin('69')
Traceback (most recent call last):
TypeError: 'str' object cannot be interpreted as an integer


Octal
-----
* Base 8
* Allowed: 0, 1, 2, 3, 4, 5, 6, 7
* Prefix: ``0o...``

>>> data = 0o105
>>> print(data)
69

>>> int('0o105', base=8)
69
>>>
>>> int('105', base=8)
69

>>> oct(69)
'0o105'

>>> int(0o105, base=8)
Traceback (most recent call last):
TypeError: int() can't convert non-string with explicit base
>>>
>>> int(105, base=8)
Traceback (most recent call last):
TypeError: int() can't convert non-string with explicit base


Decimal
-------
* Base 10
* Allowed: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

>>> data = 69
>>> print(data)
69

>>> int('69', base=10)
69

>>> int(69, base=10)
Traceback (most recent call last):
TypeError: int() can't convert non-string with explicit base


Hexadecimal
-----------
* Base 16
* Allowed: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f, A, B, C, D, E, F
* Prefix: ``0x...``

>>> data = 0x45
>>> print(data)
69

>>> int('45', base=16)
69
>>>
>>> int('0x45', base=16)
69

>>> hex(69)
'0x45'

Other examples:

>>> int('100', base=16)
256
>>>
>>> int('0x69', base=16)
105
>>>
>>> int('0x3C', base=16)
60


Errors
------
>>> data = 'abc'
>>>
>>> int(data, base=10)
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: 'abc'
>>>
>>>
>>> int(data, base=16)
2748
>>>
>>> import string
>>> string.hexdigits
'0123456789abcdefABCDEF'


Assignments
===========
.. todo:: assignments with bin()
.. todo:: assignments with hex()
.. todo:: assignments with oct()
