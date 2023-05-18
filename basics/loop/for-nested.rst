Loop For Nested
===============
* Loop inside a loop
* Used to iterate over nested data


Recap
-----
>>> DATA = [1, 2, 3]
>>>
>>> for obj in DATA:
...     print(f'{obj=}')
obj=1
obj=2
obj=3

>>> DATA = [[1, 2, 3],
...         [4, 5, 6],
...         [7, 8, 9]]
>>>
>>>
>>> for obj in DATA:
...     print(f'{obj=}')
obj=[1, 2, 3]
obj=[4, 5, 6]
obj=[7, 8, 9]


Nested Loops
------------
You can have loop inside a loop:

>>> DATA = [[1, 2, 3],
...         [4, 5, 6],
...         [7, 8, 9]]
>>>
>>>
>>> for row in DATA:  # doctest: +NORMALIZE_WHITESPACE
...     for value in row:
...         print(f'{value}', end=' ')
...     print()
1 2 3
4 5 6
7 8 9


List of List
------------
* Matrix
* Suggested variable name: ``row``

>>> DATA = [[1, 2, 3],
...         [4, 5, 6],
...         [7, 8, 9]]
>>>
>>>
>>> for row in DATA:
...     a = row[0]
...     b = row[1]
...     c = row[2]
...     print(f'{a=} {b=} {c=}')
a=1 b=2 c=3
a=4 b=5 c=6
a=7 b=8 c=9


List of Pairs
-------------
>>> users = [
...     ('commander', 'Melissa Lewis'),
...     ('botanist', 'Mark Watney'),
...     ('pilot', 'Rick Martinez'),
... ]
>>>
>>>
>>> for user in users:
...     role = user[0]
...     name = user[1]
...     print (f'{role=}, {name=}')
role='commander', name='Melissa Lewis'
role='botanist', name='Mark Watney'
role='pilot', name='Rick Martinez'


List of Threes
--------------
>>> users = [
...     ('commander', 'Melissa', 'Lewis'),
...     ('botanist', 'Mark', 'Watney'),
...     ('pilot', 'Rick', 'Martinez'),
... ]
>>>
>>>
>>> for user in users:
...     role = user[0]
...     firstname = user[1]
...     lastname = user[2]
...     print (f'{role=}, {firstname=}, {lastname=}')
role='commander', firstname='Melissa', lastname='Lewis'
role='botanist', firstname='Mark', lastname='Watney'
role='pilot', firstname='Rick', lastname='Martinez'


List of Sequence
----------------
>>> DATA = [
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
... ]
>>>
>>>
>>> for row in DATA:
...     sepal_length = row[0]
...     sepal_width = row[1]
...     petal_length = row[2]
...     petal_width = row[3]
...     species = row[4]
...     total = sepal_length + sepal_width + petal_length + petal_width
...     print(f'{species} -> {total}')
setosa -> 10.2
versicolor -> 13.9
virginica -> 16.599999999999998

>>> DATA = [
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
... ]
>>>
>>>
>>> for row in DATA:
...     values = row[0:4]
...     species = row[4]
...     print(f'{species=}, {values=}')
species='setosa', values=(5.1, 3.5, 1.4, 0.2)
species='versicolor', values=(5.7, 2.8, 4.1, 1.3)
species='virginica', values=(6.3, 2.9, 5.6, 1.8)


Mixed
-----
Let's analyze the following example. We received data as follows:

>>> DATA = [('Mark', 'Watney'), 'Lewis', 69, 13.37, [True, None, False]]

The desired format should be:

.. code-block:: text

    Mark
    Watney
    Lewis
    69
    13.37
    True
    None
    False

How to convert ``DATA`` to desired format?

Iterating over ``list`` with scalar and vector values - simple loop:

>>> DATA = [('Mark', 'Watney'), 'Lewis', 69, 13.37, [True, None, False]]
>>>
>>> for current in DATA:
...     print(current)
('Mark', 'Watney')
Lewis
69
13.37
[True, None, False]

Iterating over ``list`` with scalar and vector values - nested loop:

>>> DATA = [('Mark', 'Watney'), 'Lewis', 69, 13.37, [True, None, False]]
>>>
>>> # doctest: +SKIP
... for current in DATA:
...     for element in current:
...         print(element)
Mark
Watney
W
a
t
n
e
y
Traceback (most recent call last):
TypeError: 'int' object is not iterable

Iterating over ``list`` with scalar and vector values - smart loop:

>>> DATA = [('Mark', 'Watney'), 'Lewis', 69, 13.37, [True, None, False]]
>>>
>>> for current in DATA:
...     if type(current) in (list, tuple, set):
...         for inside in current:
...             print(inside)
...     else:
...         print(current)
Mark
Watney
Lewis
69
13.37
True
None
False


Good Practices
--------------
* ``row`` - best for nested loops with sequence inside
* Conventions for rows and columns:

    * ``row`` - row (all elements)
    * ``column`` - current column element from ``row`` sequence
    * ``i`` - row number
    * ``j`` - column number
    * ``x`` - row number
    * ``y`` - column number
    * ``outer`` - for outer loop element
    * ``inner`` - for inner loop element

* Note that ``i`` may interfere with ``i`` used as loop counter


Use Case - 0x01
---------------
>>> for row in [1, 2, 3]:  # doctest: +NORMALIZE_WHITESPACE
...     print()
...
...     for column in ['A', 'B', 'C']:
...         print(f'{column}{row}', end=' ')
A1 B1 C1
A2 B2 C2
A3 B3 C3



Assignments
-----------
.. literalinclude:: assignments/loop_nested_a.py
    :caption: :download:`Solution <assignments/loop_nested_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_nested_b.py
    :caption: :download:`Solution <assignments/loop_nested_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_nested_c.py
    :caption: :download:`Solution <assignments/loop_nested_c.py>`
    :end-before: # Solution
