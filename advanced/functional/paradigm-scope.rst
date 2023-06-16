Functional Scope
================
* Values defined in function does not leak out
* Functions has access to global values
* Shadowing is when you define variable with name identical to the one
  from outer scope
* Shadowing in a function is valid only in a function
* After function return, the original value of a shadowed variable
  is restored
* ``global`` keyword allows modification of global variable
* Using ``global`` keyword is considered as a bad practice

In Python, a function scope refers to the area of a program where a variable
is accessible. A variable's scope is determined by where it is defined in
the program.

When a variable is defined inside a function, it has local scope, which
means that it can only be accessed within that function. Local variables are
destroyed when the function returns.

Here's an example of using local variables in Python:

>>> def my_function():
...     x = 10
...     print(x)
>>>
>>> my_function()
10
>>> print(x)
Traceback (most recent call last):
NameError: name 'x' is not defined

In this example, the ``x`` variable is defined inside the ``my_function()``
function. It has local scope and can only be accessed within the function.
When the function is called, it prints the value of ``x``. When the function
returns, the ``x`` variable is destroyed.

If we try to access the `x` variable outside the function, we get a
``NameError`` because the variable is not defined in the global scope.

Variables defined outside of any function have global scope, which means
that they can be accessed from anywhere in the program. Global variables are
not destroyed when a function returns.

Here's an example of using global variables in Python:

>>> x = 10
>>>
>>> def my_function():
...     print(x)
>>>
>>> my_function()
10
>>> print(x)
10

In this example, the ``x`` variable is defined outside of any function and has
global scope. It can be accessed from within the ``my_function()`` function
and from outside the function. When the function is called, it prints the
value of ``x``. When the program ends, the ``x`` variable is not destroyed
because it has global scope.

Using function scope helps to keep variables organized and prevent naming
conflicts between different parts of a program.


Values Leaking
--------------
* Values defined in function does not leak out

>>> def run(a, b=1):
...     c = 2
>>>
>>>
>>> print(a)
Traceback (most recent call last):
NameError: name 'a' is not defined
>>>
>>> print(b)
Traceback (most recent call last):
NameError: name 'b' is not defined
>>>
>>> print(c)
Traceback (most recent call last):
NameError: name 'c' is not defined
>>>
>>> run(0)
>>>
>>> print(a)
Traceback (most recent call last):
NameError: name 'a' is not defined
>>>
>>> print(b)
Traceback (most recent call last):
NameError: name 'b' is not defined
>>>
>>> print(c)
Traceback (most recent call last):
NameError: name 'c' is not defined


Outer Scope
-----------
* Functions has access to global values

>>> data = [1, 2, 3]
>>>
>>>
>>> def run():
...     print(data)
>>>
>>>
>>> print(data)
[1, 2, 3]
>>>
>>> run()
[1, 2, 3]
>>>
>>> print(data)
[1, 2, 3]


Shadowing
---------
* When variable in function has the same name as in outer scope
* Shadowing in a function is valid only in a function
* Shadowed variable will be deleted upon function return
* After function return, the original value of a shadowed variable
  is restored

>>> data = [1, 2, 3]
>>>
>>>
>>> def run():
...     data = [10, 20, 30]  # Shadows name 'data' from outer scope
...     print(data)
>>>
>>>
>>> print(data)
[1, 2, 3]
>>>
>>> run()
[10, 20, 30]
>>>
>>> print(data)
[1, 2, 3]


Global
------
* ``global`` keyword allows modification of global variable
* Using ``global`` keyword is considered as a bad practice

>>> data = [1, 2, 3]
>>>
>>>
>>> def run():
...     global data
...     data = [10, 20, 30]
...     print(data)
>>>
>>>
>>> print(data)
[1, 2, 3]
>>>
>>> run()
[10, 20, 30]
>>>
>>> print(data)
[10, 20, 30]


Nonlocal
--------
* Python nonlocal keyword is used to reference a variable in the nearest scope

The nonlocal keyword won't work on local or global variables and therefore
must be used to reference variables in another scope except the global and
local one. The nonlocal keyword is used in nested functions to reference a
variable in the parent function. [#nonlocal]_

>>> data = [1, 2, 3]
>>>
>>> def run():
...     data = [10, 20, 30]
...     def main():
...         data += [40, 50, 60]
...         print(data)
...     main()
...
...
>>> run()
Traceback (most recent call last):
UnboundLocalError: cannot access local variable 'data' where it is not associated with a value

>>> data = [1, 2, 3]
>>>
>>> def run():
...     data = [10, 20, 30]
...     def main():
...         nonlocal data
...         data += [40, 50, 60]
...         print(data)
...     main()
...
...
>>> run()
[10, 20, 30, 40, 50, 60]


This does not work with non-nested functions:

>>> data = 1
>>>
>>> def run():
...     data += 1
...     print(data)
...
>>>
>>> run()
Traceback (most recent call last):
UnboundLocalError: cannot access local variable 'data' where it is not associated with a value

>>> def run():
...     nonlocal data
...     data += 1
...     print(data)
Traceback (most recent call last):
SyntaxError: no binding for nonlocal 'data' found


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

>>> class User:
...    pass
>>>
>>> mark = User()
>>>
>>> globals()  # doctest: +SKIP +ELLIPSIS
{'__name__': '__main__',
 '__doc__': None,
 '__package__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__spec__': None,
 '__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 'User': <class '__main__.User'>,
 'mark': <__main__.User object at 0x...>}


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

>>> def echo():
...     a = 1
...     print(locals())
>>>
>>>
>>> echo()
{'a': 1}

>>> def echo(a, b=2):
...     c = 3
...     print(locals())
>>>
>>>
>>> echo(1)
{'a': 1, 'b': 2, 'c': 3}

If outside the function, will return the same as ``globals()``:

>>> locals() == globals()
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


Use Case - 0x02
---------------
>>> class Iris:
...     def __init__(self, sl, sw, pl, pw):
...         ...
>>>
>>> class Setosa(Iris):
...     pass
>>>
>>> class Virginica(Iris):
...     pass
>>>
>>> class Versicolor(Iris):
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
 'Setosa': <class '__main__.Setosa'>,
 'Virginica': <class '__main__.Virginica'>,
 'Versicolor': <class '__main__.Versicolor'>}

>>> *measurement, species = (5.1, 3.5, 1.4, 0.2, 'Setosa')
>>> cls = globals()[species]
>>> cls(*measurement)  # doctest: +ELLIPSIS
<__main__.Setosa object at 0x...>


References
----------
.. [#nonlocal] Satyam00so. Python nonlocal Keyword. Year: 2022. Retrieved: 2022-07-28, URL: https://www.geeksforgeeks.org/python-nonlocal-keyword/


Assignments
-----------
.. literalinclude:: assignments/functional_scope_a.py
    :caption: :download:`Solution <assignments/functional_scope_a.py>`
    :end-before: # Solution
