Exception About
===============
* Used when error occurs
* You can catch exception and handles erroneous situation
* If file does not exists
* If no permissions to read file
* If function argument is invalid type (ie. ``int('one')``)
* If value is incorrect (ie. negative Kelvin temperature)
* If network or database connection could not be established


AttributeError
--------------
* Attribute reference or assignment fails

>>> name = 'Mark'
>>> name.append('Watney')
Traceback (most recent call last):
AttributeError: 'str' object has no attribute 'append'


IndexError
----------
* Sequence subscript is out of range

>>> DATA = ['a', 'b', 'c']
>>> DATA[100]
Traceback (most recent call last):
IndexError: list index out of range


IsADirectoryError
-----------------
* Trying to open directory instead of file

>>> open('/tmp')
Traceback (most recent call last):
IsADirectoryError: [Errno 21] Is a directory: '/tmp'


FileNotFoundError
-----------------
* File does not exists

>>> open('notexisting.txt')
Traceback (most recent call last):
FileNotFoundError: [Errno 2] No such file or directory: 'notexisting.txt'


KeyError
--------
* Dictionary key is not found

>>> DATA = {'a': 1, 'b': 2}
>>> DATA['x']
Traceback (most recent call last):
KeyError: 'x'


ModuleNotFoundError
-------------------
* Module could not be located

>>> import math
>>> import match
Traceback (most recent call last):
ModuleNotFoundError: No module named 'match'

Note, that this exception is also raised when you don't have this module
installed. Such as while importing ``pandas`` or ``numpy`` without installing
it first.


NameError
---------
* Local or global name is not found

>>> print(firstname)
Traceback (most recent call last):
NameError: name 'firstname' is not defined


SyntaxError
-----------
* Parser encounters a syntax error

>>> if True
...     print('Yes')
Traceback (most recent call last):
SyntaxError: expected ':'


IndentationError
----------------
* Syntax errors related to incorrect indentation

>>> if True:
...     print('Hello!')
...      print('My name...')
...     print('José Jiménez')
Traceback (most recent call last):
IndentationError: unexpected indent


TypeError
---------
* Operation or function is applied to an object of inappropriate type

>>> 42 + 'a'
Traceback (most recent call last):
TypeError: unsupported operand type(s) for +: 'int' and 'str'

>>> 'a' + 42
Traceback (most recent call last):
TypeError: can only concatenate str (not "int") to str

>>> a = ['a', 'b', 'c']
>>>
>>> a[1]
'b'
>>>
>>> a[1.0]
Traceback (most recent call last):
TypeError: list indices must be integers or slices, not float

>>> a, b = 1
Traceback (most recent call last):
TypeError: cannot unpack non-iterable int object


ValueError
----------
* Argument has an invalid value

>>> a, b, c = 1, 2
Traceback (most recent call last):
ValueError: not enough values to unpack (expected 3, got 2)

>>> a, b = 1, 2, 3
Traceback (most recent call last):
ValueError: too many values to unpack (expected 2)

>>> float('one')
Traceback (most recent call last):
ValueError: could not convert string to float: 'one'

>>> int('one')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: 'one'
