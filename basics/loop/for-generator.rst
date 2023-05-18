Loop For Generator
==================


Range
-----
* ``range(start, stop, step)``
* ``start`` is inclusive, default: ``0``
* ``stop`` is exclusive, required
* ``step`` default: ``1``

>>> range(0, 5)
range(0, 5)

>>> list(range(5))
[0, 1, 2, 3, 4]

>>> list(range(0, 5))
[0, 1, 2, 3, 4]

>>> list(range(0, 5, 1))
[0, 1, 2, 3, 4]

>>> list(range(0, 5, 2))
[0, 2, 4]

Loops with ``range``:

>>> for i in range(0, 3):
...     print(i)
0
1
2

Loops with ``range``:

>>> for number in range(4, 11, 2):
...     print(number)
4
6
8
10


Enumerate
---------
* Pythonic way
* Preferred over ``i=0`` and ``i+=1`` for every iteration
* ``enumerate()`` will return ``counter`` and ``value`` for every iteration

>>> DATA = ['a', 'b', 'c']
>>> result = enumerate(DATA)
>>>
>>> next(result)
(0, 'a')
>>> next(result)
(1, 'b')
>>> next(result)
(2, 'c')
>>> next(result)
Traceback (most recent call last):
StopIteration

``enumerate()`` will return ``counter`` and ``value`` for every iteration:

>>> DATA = ['a', 'b', 'c']
>>>
>>> for i, letter in enumerate(DATA):
...     print(f'{i} -> {letter}')
0 -> a
1 -> b
2 -> c

``enumerate()`` can start with custom number:

>>> DATA = ['a', 'b', 'c']
>>>
>>> for i, letter in enumerate(DATA, start=5):
...     print(f'{i} -> {letter}')
5 -> a
6 -> b
7 -> c

>>> DATA = [
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
... ]
>>>
>>> for i, row in enumerate(DATA):
...     print(f'{i} -> {row}')
0 -> (5.1, 3.5, 1.4, 0.2, 'setosa')
1 -> (5.7, 2.8, 4.1, 1.3, 'versicolor')
2 -> (6.3, 2.9, 5.6, 1.8, 'virginica')


Zip
---
>>> roles = ['commander', 'botanist', 'chemist']
>>> crew = ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']
>>> result = zip(roles, crew)
>>>
>>> next(result)
('commander', 'Melissa Lewis')
>>> next(result)
('botanist', 'Mark Watney')
>>> next(result)
('chemist', 'Alex Vogel')
>>> next(result)
Traceback (most recent call last):
StopIteration

>>> roles = ['commander', 'botanist', 'chemist']
>>> crew = ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']
>>>
>>> for role, name in zip(roles, crew):
...     print(f'{role} -> {name}')
commander -> Melissa Lewis
botanist -> Mark Watney
chemist -> Alex Vogel
