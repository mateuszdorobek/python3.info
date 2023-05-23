Typing Iterable
===============
* Before Python 3.9 you need ``from typing import List, Tuple, Set, Frozenset``
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections


Tuple
-----
Declaration:

>>> data: tuple
>>>
>>> data: tuple[int]
>>> data: tuple[float]
>>> data: tuple[bool]
>>> data: tuple[str]
>>>
>>> data: tuple[int, ...]
>>> data: tuple[float, ...]
>>> data: tuple[bool, ...]
>>> data: tuple[str, ...]

Empty:

>>> data: tuple
>>> data = ()

>>> data: tuple
>>> data = tuple()

>>> data: tuple = ()
>>> data: tuple = tuple()

Generic:

>>> data: tuple = (1, 2, 3)
>>> data: tuple = (1.1, 2.2, 3.3)
>>> data: tuple = ('a', 'b', 'c')

Strict:

>>> data: tuple[int, int, int] = (1, 2, 3)
>>> data: tuple[float, float, float] = (1.1, 2.2, 3.3)
>>> data: tuple[str, str, str] = ('a', 'b', 'c')
>>> data: tuple[str, int, float] = ('a', 2, 3.3)

Repeating:

>>> data: tuple[int, ...] = (1, 2, 3)
>>> data: tuple[float, ...] = (1.1, 2.2, 3.3)
>>> data: tuple[str, ...] = ('a', 'b', 'c')

Examples:

>>> data: tuple[str,str,int] = ('Mark', 'Watney', 40)
>>> data: tuple[float,float,float,float,str] = (5.1, 3.5, 1.4, 0.2, 'setosa')


List
----
Declaration:

>>> data: list
>>>
>>> data: list[int]
>>> data: list[float]
>>> data: list[bool]
>>> data: list[str]

Empty:

>>> data: list = []
>>> data: list = list()

Generic:

>>> data: list = [1, 2, 3]
>>> data: list = [1.1, 2.2, 3.3]
>>> data: list = ['a', 'b', 'c']

Strict and Repeating:

>>> data: list[int] = [1, 2, 3]
>>> data: list[float] = [1.1, 2.2, 3.3]
>>> data: list[str] = ['a', 'b', 'c']

Unions:

>>> data: list[int|float] = [1, 2, 3.3, 4.4]
>>> data: list[int|float|str] = [1, 2, 3.3, 4.0, 'a', 'b']


Set
---
Declaration:

>>> data: set
>>>
>>> data: set[int]
>>> data: set[float]
>>> data: set[bool]
>>> data: set[str]

Empty:

>>> data: set = set()

Generic:

>>> data: set = {1, 2, 3}
>>> data: set = {1.1, 2.2, 3.3}
>>> data: set = {'a', 'b', 'c'}

Strict and Repeating:

>>> data: set[int] = {1, 2, 3}
>>> data: set[float] = {1.1, 2.2, 3.3}
>>> data: set[str] = {'a', 'b', 'c'}

Unions:

>>> data: set[int|float] = {1, 2, 3.3, 4.4}
>>> data: set[int|float|str] = {1, 2, 3.3, 4.0, 'a', 'b'}


Frozenset
---------
Declaration:

>>> data: frozenset
>>>
>>> data: frozenset[int]
>>> data: frozenset[float]
>>> data: frozenset[bool]
>>> data: frozenset[str]

Empty:

>>> data: frozenset = frozenset()

Generic:

>>> data: frozenset = frozenset({1, 2, 3})
>>> data: frozenset = frozenset({1.1, 2.2, 3.3})
>>> data: frozenset = frozenset({'a', 'b', 'c'})

Strict and Repeating:

>>> data: frozenset[int] = frozenset({1, 2, 3})
>>> data: frozenset[float] = frozenset({1.1, 2.2, 3.3})
>>> data: frozenset[str] = frozenset({'a', 'b', 'c'})

Unions:

>>> data: frozenset[int|float] = frozenset({1, 2, 3.3, 4.4})
>>> data: frozenset[int|float|str] = frozenset({1, 2, 3.3, 4.0, 'a', 'b'})


Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`


References
----------
.. [#pyDocTyping] https://docs.python.org/3/library/typing.html#module-contents


Assignments
-----------
.. literalinclude:: assignments/typing_iterable_a.py
    :caption: :download:`Solution <assignments/typing_iterable_a.py>`
    :end-before: # Solution
