Sequence Tuple
==============


Important
---------
* Immutable - cannot add, modify or remove items


Syntax
------
Defining ``tuple()`` is more explicit, however empty tuple with ``()`` is used
more often and it's also faster:

>>> data = ()
>>> data = tuple()

Can store elements of any type:

>>> data = (1, 2, 3)
>>> data = (1.1, 2.2, 3.3)
>>> data = (True, False)
>>> data = ('a', 'b', 'c')
>>> data = ('a', 1, 2.2, True, None)


Type Casting
------------
Builtin function ``tuple()`` converts argument to ``tuple``

>>> data = 'abcd'
>>> tuple(data)
('a', 'b', 'c', 'd')

>>> data = ['a', 'b', 'c', 'd']
>>> tuple(data)
('a', 'b', 'c', 'd')

>>> data = ('a', 'b', 'c', 'd')
>>> tuple(data)
('a', 'b', 'c', 'd')

>>> tuple('a', 'b', 'c', 'd')
Traceback (most recent call last):
TypeError: tuple expected at most 1 argument, got 4


Optional Brackets
-----------------
Brackets are optional, but it's a good practice to always write them:

>>> data = (1, 2, 3)
>>> data = 1, 2, 3

Single element ``tuple`` require comma at the end (**important!**):

>>> data = (1,)
>>> type(data)
<class 'tuple'>

>>> data = (1)
>>> type(data)
<class 'int'>

Comma after last element of multi value tuple is optional:

>>> data = (1, 2)
>>> type(data)
<class 'tuple'>

>>> data = (1, 2,)
>>> type(data)
<class 'tuple'>


Tuple or Int, Float, Str
------------------------
>>> x = 1           # int
>>> x = 1.          # float
>>> x = 1,          # tuple

>>> x = (1)         # int
>>> x = (1.)        # float
>>> x = (1,)        # tuple

>>> x = 'one'       # str
>>> x = 'one',      # tuple
>>> x = 'one'.
Traceback (most recent call last):
SyntaxError: invalid syntax

>>> x = (12)        # int
>>> x = (1.2)       # float
>>> x = (1,2)       # tuple
>>> x = 1.,1.       # tuple
>>> x = 1.,.1       # tuple
>>> x = .1,1.       # tuple


Index
-----
>>> colors = ('red', 'green', 'blue')
>>> colors.index('red')
0


Count
-----
>>> colors = ('red', 'green', 'blue', 'red', 'blue')
>>> colors.count('red')
2


Sort
----
>>> data = (3, 1, 2)
>>> tuple(sorted(data))
(1, 2, 3)


Reversed
--------
>>> data = (1, 2, 3)
>>> tuple(reversed(data))
(3, 2, 1)


Length
------
>>> data = (1, 2, 3)
>>> len(data)
3


Built-in Functions
------------------
* ``min()`` - Minimal value
* ``max()`` - Maximal value
* ``sum()`` - Sum of elements
* ``len()`` - Length of a list
* ``all()`` - All values are ``True``
* ``any()`` - Any values is ``True``

List with numeric values:

>>> data = (3, 1, 2)
>>>
>>> len(data)
3
>>> min(data)
1
>>> max(data)
3
>>> sum(data)
6

List with string values:

>>> data = ('a', 'c', 'b')
>>>
>>> len(data)
3
>>> min(data)
'a'
>>> max(data)
'c'
>>> sum(data)
Traceback (most recent call last):
TypeError: unsupported operand type(s) for +: 'int' and 'str'


List with boolean values:

>>> data = (True, False, True)
>>>
>>> any(data)
True
>>> all(data)
False


Memory
------
.. figure:: img/memory-tuple.png

    Memory representation for ``tuple``


Assignments
-----------
.. literalinclude:: assignments/sequence_tuple_a.py
    :caption: :download:`Solution <assignments/sequence_tuple_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_tuple_b.py
    :caption: :download:`Solution <assignments/sequence_tuple_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_tuple_c.py
    :caption: :download:`Solution <assignments/sequence_tuple_c.py>`
    :end-before: # Solution
