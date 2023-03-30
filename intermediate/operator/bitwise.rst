Operator Bitwise
================
* ``&`` - and
* ``|`` - or
* ``^`` - xor
* ``&=`` - iand
* ``|=`` - ior
* ``^=`` - ixor
* ``<<`` - lshift
* ``>>`` - rshift
* ``<<=`` - ilshift
* ``>>=`` - irshift


About
-----
.. csv-table:: Boolean Operator Overload
    :header: "Operator", "Method"

    "``obj & other``",     "``obj.__and__(other)``"
    "``obj | other``",     "``obj.__or__(other)``"
    "``obj ^ other``",     "``obj.__xor__(other)``"

    "``obj &= other``",    "``obj.__iand__(other)``"
    "``obj |= other``",    "``obj.__ior__(other)``"
    "``obj ^= other``",    "``obj.__ixor__(other)``"

    "``obj << other``",    "``obj.__lshift__(other)``"
    "``obj >> other``",    "``obj.__rshift__(other)``"
    "``obj <<= other``",   "``obj.__ilshift__(other)``"
    "``obj >>= other``",   "``obj.__irshift__(other)``"


Example
-------
>>> True + True
2

>>> True & True
True


AND - Conjunction
-----------------
.. code-block:: text

    1 & 1 = 1
    1 & 0 = 0
    0 & 1 = 0
    0 & 0 = 0

>>> True & True
True
>>>
>>> True & False
False
>>>
>>> False &  True
False
>>>
>>> False &  False
False


OR - Alternative
----------------
.. code-block:: text

    1 | 1 = 1
    1 | 0 = 1
    0 | 1 = 1
    0 | 0 = 0

>>> True | True
True
>>>
>>> True | False
True
>>>
>>> False | True
True
>>>
>>> False | False
False


XOR - Exclusive Alternative
---------------------------
.. code-block:: text

    1 ^ 1 = 0
    1 ^ 0 = 1
    0 ^ 1 = 1
    0 ^ 0 = 0

>>> True ^ True
False
>>>
>>> True ^ False
True
>>>
>>> False ^ True
True
>>>
>>> False ^ False
False


Bool
----
>>> a = True
>>> b = False

>>> a & b
False

>>> a ^ b
True

>>> a | b
True


Set
---
>>> a = {1,2,3}
>>> b = {2,3,4}

>>> a & b
{2, 3}

>>> a ^ b
{1, 4}

>>> a | b
{1, 2, 3, 4}


Dict
----
>>> a = {'commander': 'Melissa Lewis', 'botanist': 'Mark Watney'}
>>> b = {'pilot': 'Rick Martinez', 'chemist': 'Alex Vogel'}

>>> a & b
Traceback (most recent call last):
TypeError: unsupported operand type(s) for &: 'dict' and 'dict'

>>> a ^ b
Traceback (most recent call last):
TypeError: unsupported operand type(s) for ^: 'dict' and 'dict'

>>> a | b  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'pilot': 'Rick Martinez',
 'chemist': 'Alex Vogel'}

>>> a |= b
>>>
>>> a  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'pilot': 'Rick Martinez',
 'chemist': 'Alex Vogel'}
>>>
>>> b
{'pilot': 'Rick Martinez', 'chemist': 'Alex Vogel'}


Dictionary Update
-----------------
>>> x = {'a':1, 'b':2, 'c':3}
>>> y = {'d':4, 'e':5}
>>>
>>> x | y
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
>>>
>>> x |= y
>>> x
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

>>> old_crew = {'commander': 'Melissa Lewis',
...             'botanist': 'Mark Watney'}
>>>
>>> new_crew = {'chemist': 'Alex Vogel',
...             'pilot': 'Rick Martinez'}
>>>
>>>
>>> old_crew | new_crew  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'chemist': 'Alex Vogel',
 'pilot': 'Rick Martinez'}

>>> old_crew
{'commander': 'Melissa Lewis', 'botanist': 'Mark Watney'}
>>>
>>> new_crew
{'chemist': 'Alex Vogel', 'pilot': 'Rick Martinez'}
>>>
>>>
>>> crew = old_crew | new_crew
>>> crew  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'chemist': 'Alex Vogel',
 'pilot': 'Rick Martinez'}

>>> old_crew |= new_crew
>>> old_crew  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'chemist': 'Alex Vogel',
 'pilot': 'Rick Martinez'}

>>> class dict:
...     def __or__(self, other):
...         return {**self, **other}
...
...     def __ior__(self, other):
...         self.update(other)
...         return self


Use Case - 0x01
---------------
* XOR as pow
* Excel uses ``^`` to rise number to the power of a second number

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Number:
...     value: int
...
...     def __xor__(self, other):
...         return Number(self.value ** other.value)
>>>
>>>
>>> a = Number(2)
>>> b = Number(4)
>>>
>>> a ^ b
Number(value=16)


Use Case - 0x02
---------------
* Game

>>> hero >> Direction(left=10, up=20)  # doctest: +SKIP


Use Case - 0x03
---------------
* Numpy

>>> import numpy as np

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> a > 2
array([[False, False,  True],
       [ True,  True,  True],
       [ True,  True,  True]])
>>>
>>> (a>2) & (a<7)
array([[False, False,  True],
       [ True,  True,  True],
       [False, False, False]])
>>>
>>> (a>2) & (a<7) | (a>3)
array([[False, False,  True],
       [ True,  True,  True],
       [ True,  True,  True]])

Python understands this:

>>> ~( (a>2) & (a<7) | (a>3) )
array([[ True,  True, False],
       [False, False, False],
       [False, False, False]])

As as chained calls of the following methods:

>>> a.__gt__(2).__and__(a.__lt__(7)).__or__(a.__gt__(3)).__invert__()
array([[ True,  True, False],
       [False, False, False],
       [False, False, False]])


Use Case - 0x05
---------------
* Talk - Sebastiaan Zeeff: Demystifying Python's Internals: Diving into CPython by implementing... https://www.youtube.com/watch?v=HYKGZunmF50
* Łukasz Langa - Life Is Better Painted Black, or: How to Stop Worrying and Embrace Auto-Formatting https://www.youtube.com/watch?v=esZLCuWs_2Y
* https://docs.influxdata.com/influxdb/v2.0/query-data/get-started/query-influxdb/

>>> def upper(text):
...     return str.upper(text)
>>>
>>> def lower(text):
...     return str.lower(text)
>>>
>>> def capitalize(text):
...     return str.capitalize(text)

Let's make a transformation:

>>> name = 'Mark Watney'
>>> upper(name)
'MARK WATNEY'

What if we have a pipe operator to do that?

>>> name = 'Mark Watney'
>>> name |> upper  # doctest: +SKIP
Traceback (most recent call last):
SyntaxError: invalid syntax

Why? Because we can chain multiple pipe operations:

>>> name = 'Mark Watney'
>>> name |> upper |> lower |> capitalize
Traceback (most recent call last):
SyntaxError: invalid syntax


.. todo:: Assignment: lshift overload, position move
.. todo:: Assignment: rshift overload, damage take
