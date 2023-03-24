Function Scope
==============
* Values defined in function does not leak out
* Functions has access to global values
* Shadowing is when you define variable with name identical to the one
  from outer scope
* Shadowing in a function is valid only in a function
* After function return, the original value of a shadowed variable
  is restored
* ``global`` keyword allows modification of global variable
* Using ``global`` keyword is considered as a bad practice


Values Leaking
--------------
* Values defined in function does not leak out

>>> def login():
...     username = 'mwatney'
...     password = 'nasa'
>>>
>>>
>>> print(username)
Traceback (most recent call last):
NameError: name 'username' is not defined
>>>
>>> print(password)
Traceback (most recent call last):
NameError: name 'password' is not defined
>>>
>>>
>>> login()
>>>
>>> print(username)
Traceback (most recent call last):
NameError: name 'username' is not defined
>>>
>>> print(password)
Traceback (most recent call last):
NameError: name 'password' is not defined


Outer Scope
-----------
* Functions has access to global values

>>> user = ('Mark', 'Watney')
>>>
>>>
>>> def login():
...     print(user)
>>>
>>>
>>> print(user)
('Mark', 'Watney')
>>>
>>> login()
('Mark', 'Watney')
>>>
>>> print(user)
('Mark', 'Watney')


Shadowing
---------
* When variable in function has the same name as in outer scope
* Shadowing in a function is valid only in a function
* Shadowed variable will be deleted upon function return
* After function return, the original value of a shadowed variable
  is restored

>>> user = ('Mark', 'Watney')
>>>
>>>
>>> def login():
...     user = ('Melissa', 'Lewis')  # Shadows name 'user' from outer scope
...     print(user)
>>>
>>>
>>> print(user)
('Mark', 'Watney')
>>>
>>> login()
('Melissa', 'Lewis')
>>>
>>> print(user)
('Mark', 'Watney')


Global
------
* ``global`` keyword allows modification of global variable
* Using ``global`` keyword is considered as a bad practice

>>> user = ('Mark', 'Watney')
>>>
>>>
>>> def login():
...     global user
...     user = ('Melissa', 'Lewis')
...     print(user)
>>>
>>>
>>> print(user)
('Mark', 'Watney')
>>>
>>> login()
('Melissa', 'Lewis')
>>>
>>> print(user)
('Melissa', 'Lewis')


Global Scope
------------
>>> globals()   # doctest: +SKIP
{'__name__': '__main__',
 '__doc__': None,
 '__package__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__spec__': None,
 '__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>}

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> globals()  # doctest: +SKIP
{'__name__': '__main__',
 '__doc__': None,
 '__package__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__spec__': None,
 '__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 'firstname': 'Mark',
 'lastname': 'Watney'}

>>> def login():
...     pass
>>>
>>>
>>> globals()  # doctest: +SKIP +ELLIPSIS
{'__name__': '__main__',
 '__doc__': None,
 '__package__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__spec__': None,
 '__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 'login': <function __main__.login()>}


Local Scope
-----------
* Variables defined inside function
* Variables are not available from outside
* If outside the function, will return the same as ``globals()``

>>> locals()  # doctest: +SKIP
{'__name__': '__main__',
 '__doc__': None,
 '__package__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__spec__': None,
 '__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>}

>>> def login():
...     username = 'mwatney'
...     password = 'nasa'
...     print(locals())
>>>
>>>
>>> login()
{'username': 'mwatney', 'password': 'nasa'}

If outside the function, will return the same as ``globals()``:

>>> locals() == globals()
True
>>>
>>> locals() is globals()
True


Shadowing Global Scope
----------------------
* Defining variable with the same name as in outer scope
* Shadowed variable will be deleted upon function return

Shadowing of a global scope is used frequently in Mocks and Stubs.
This way, we can simulate user input. Note that Mocks and Stubs will
stay until the end of a program.

>>> def input(prompt):
...     return 'Mark Watney'
>>>
>>>
>>> name = input('Type your name: ')
>>> name
'Mark Watney'
>>>
>>> age = input('Type your age: ')
>>> age
'Mark Watney'

>>> from unittest.mock import MagicMock
>>> input = MagicMock(side_effect=['Mark Watney', '44'])
>>>
>>>
>>> name = input('Type your name: ')
>>> name
'Mark Watney'
>>>
>>> age = input('Type your age: ')
>>> age
'44'

To restore default behavior of ``input()`` function use:

>>> from builtins import input


Builtins
--------
>>> import builtins
>>>
>>> dir(builtins)   # doctest: +NORMALIZE_WHITESPACE
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError',
 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError',
 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError',
 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning',
 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None',
 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError',
 'OverflowError', 'PendingDeprecationWarning', 'PermissionError',
 'ProcessLookupError', 'RecursionError', 'ReferenceError',
 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__loader__', '__name__',
 '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii',
 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr',
 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr',
 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter',
 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash',
 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter',
 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min',
 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']


Use Case - 0x01
---------------
Simulate user input (for test automation)

>>> from unittest.mock import MagicMock
>>> input = MagicMock(side_effect=['lastname'])

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>>
>>> varname = input('Type variable name: ')   #input: 'lastname'
>>>
>>> globals()[varname]
'Watney'


Assignments
-----------
.. literalinclude:: assignments/function_scope_a.py
    :caption: :download:`Solution <assignments/function_scope_a.py>`
    :end-before: # Solution
