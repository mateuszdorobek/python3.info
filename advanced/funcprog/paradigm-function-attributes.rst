FuncProg Function Attributes
============================

>>> def add(a, b):
...     return a + b
>>>
>>>
>>> type(add)
<class 'function'>


Name
----
* ``function.__name__``
* ``function.__qualname__``

>>> def add(a, b):
...     return a + b

>>> add.__name__
'add'

>>> add.__qualname__
'add'


Type
----
* ``type(function)``
* ``function.__class__``
* ``function.__class__.__name__``
* ``function.__class__.__qualname__``
* ``function.__class__.__text_signature__``

>>> def add(a, b):
...     return a + b

>>> type(add)
<class 'function'>

add.__class__
<class 'function'>

>>> add.__class__.__name__
'function'

>>> add.__class__.__qualname__
'function'


Annotations
-----------
>>> def add(a: int, b: int) -> int:
...     return a + b

>>> add.__annotations__
{'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}


Signature
---------
>>> from inspect import signature

>>> def add(a, b):
...     return a + b
>>>
>>>
>>> signature(add)
<Signature (a, b)>

>>> def add(a: int, b: int) -> int:
...     return a + b
>>>
>>>
>>> signature(add)
<Signature (a: int, b: int) -> int>


Doc
---
* ``help(function)``
* ``function.__doc__``

>>> def add(a: int, b: int) -> int:
...     """
...     Function adds two numbers (int|float)
...     """
...     return a + b

>>> add.__doc__
'\n    Function adds two numbers (int|float)\n    '

>>> help(add)
Help on function add in module __main__:
<BLANKLINE>
add(a: int, b: int) -> int
    Function adds two numbers (int|float)
<BLANKLINE>


Call
----
* ``callable(function)``
* ``function()``
* ``function.__call__()``

>>> def add(a, b):
...     return a + b

>>> callable(add)
True

>>> add(1, 2)
3

>>> add.__call__(1,2)
3


Setattr, Getattr
----------------
>>> def hello():
...     pass
>>>
>>>
>>> hello.firstname = 'Mark'
>>> hello.lastname = 'Watney'
>>>
>>> print(f'Hello {hello.firstname} {hello.lastname}')
Hello Mark Watney

>>> def hello():
...     return f'Hello {hello.firstname} {hello.lastname}'
>>>
>>>
>>> hello.firstname = 'Mark'
>>> hello.lastname = 'Watney'
>>>
>>> hello()
'Hello Mark Watney'


Function Code
-------------
>>> def add(a, b):
...     return a + b
>>>
>>>
>>> add.__code__.co_varnames
('a', 'b')
>>>
>>> dir(add.__code__)  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
[...,
 'co_argcount',
 'co_cellvars',
 'co_code',
 'co_consts',
 'co_exceptiontable',
 'co_filename',
 'co_firstlineno',
 'co_flags',
 'co_freevars',
 'co_kwonlyargcount',
 'co_lines',
 'co_linetable',
 'co_lnotab',
 'co_name',
 'co_names',
 'co_nlocals',
 'co_positions',
 'co_posonlyargcount',
 'co_qualname',
 'co_stacksize',
 'co_varnames',
 'replace']


Use Case - 0x01
---------------
>>> def hello():
...     if not hello.disabled:
...         print('My name... José Jiménez')
...     else:
...         raise PermissionError
>>>
>>>
>>> hello.disabled = False
>>> hello()
My name... José Jiménez
>>>
>>> hello.disabled = True
>>> hello()
Traceback (most recent call last):
PermissionError


Use Case - 0x02
---------------
>>> def add(a, b):
...     return a + b
>>>
>>>
>>> add(1, 2)
3
>>>
>>> add(1, 2)
3
>>>
>>> add(1, 2)
3

>>> def add(a, b):
...     if not hasattr(add, '_cache'):
...         setattr(add, '_cache', {})
...     if (a,b) in add._cache:
...         print('Found in cache; fetching...')
...         return add._cache[a,b]
...     else:
...         print('Not in cache; computing and updating cache...')
...         add._cache[a,b] = result = a + b
...         return result
>>>
>>>
>>> add(1, 2)
Not in cache; computing and updating cache...
3
>>>
>>> add(1, 2)
Found in cache; fetching...
3
>>>
>>> add(1, 2)
Found in cache; fetching...
3


Use Case - 0x03
---------------
>>> def add(a, b):
...     cache = getattr(add, '__cache__', {})
...     if (a,b) not in cache:
...         cache[(a,b)] = a + b
...         setattr(add, '__cache__', cache)
...     return cache[(a,b)]
>>>
>>>
>>> add(1,2)
3
>>>
>>> add(3,2)
5
>>>
>>> add(3,5)
8
>>>
>>> add  # doctest: +ELLIPSIS
<function add at 0x...>
>>>
>>> add.__cache__
{(1, 2): 3, (3, 2): 5, (3, 5): 8}


Use Case - 0x04
---------------
>>> def factorial(n):
...     if not hasattr(factorial, 'cache'):
...         factorial.cache = {0: 1}
...     if n not in factorial.cache:
...         factorial.cache[n] = n * factorial(n-1)
...     return factorial.cache[n]
>>>
>>>
>>> factorial(10)
3628800
>>>
>>> factorial.cache  # doctest: +NORMALIZE_WHITESPACE
{0: 1,
 1: 1,
 2: 2,
 3: 6,
 4: 24,
 5: 120,
 6: 720,
 7: 5040,
 8: 40320,
 9: 362880,
 10: 3628800}

