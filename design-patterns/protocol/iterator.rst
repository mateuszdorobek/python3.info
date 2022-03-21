Protocol Iterator
=================


Important
---------
* Used for iterating in a ``for`` loop


Protocol
--------
* ``__iter__(self) -> self``
* ``__next__(self) -> raise StopIteration``
* ``iter(obj)`` -> ``obj.__iter__()``
* ``next(obj)`` -> ``obj.__next__()``


>>> class Iterator:
...     def __iter__(self):
...         self._current = 0
...         return self
...
...     def __next__(self):
...         if self._current >= len(self.values):
...             raise StopIteration
...         element = self.values[self._current]
...         self._current += 1
...         return element


Example
-------
>>> class Crew:
...     def __init__(self):
...         self.members = list()
...
...     def __iadd__(self, other):
...         self.members.append(other)
...         return self
...
...     def __iter__(self):
...         self._current = 0
...         return self
...
...     def __next__(self):
...         if self._current >= len(self.members):
...             raise StopIteration
...         result = self.members[self._current]
...         self._current += 1
...         return result
>>>
>>>
>>> crew = Crew()
>>> crew += 'Mark Watney'
>>> crew += 'Jose Jimenez'
>>> crew += 'Melissa Lewis'
>>>
>>> for member in crew:
...     print(member)
Mark Watney
Jose Jimenez
Melissa Lewis


Loop and Iterators
------------------
For loop:

>>> DATA = [1, 2, 3]
>>>
>>> for current in DATA:
...     print(current)
1
2
3

Intuitive implementation of the ``for`` loop:

>>> DATA = [1, 2, 3]
>>> iterator = iter(DATA)
>>>
>>> try:
...     current = next(iterator)
...     print(current)
...
...     current = next(iterator)
...     print(current)
...
...     current = next(iterator)
...     print(current)
...
...     current = next(iterator)
...     print(current)
... except StopIteration:
...     pass
1
2
3

Intuitive implementation of the ``for`` loop:

>>> DATA = [1, 2, 3]
>>> iterator = DATA.__iter__()
>>>
>>> try:
...     current = iterator.__next__()
...     print(current)
...
...     current = iterator.__next__()
...     print(current)
...
...     current = iterator.__next__()
...     print(current)
...
...     current = iterator.__next__()
...     print(current)
... except StopIteration:
...     pass
1
2
3


Built-in Type Iteration
-----------------------
Iterating ``str``:

>>> for character in 'hello':
...     print(character)
h
e
l
l
o

Iterating sequences:

>>> for number in [1, 2, 3]:
...     print(number)
1
2
3

Iterating ``dict``:

>>> DATA = {'a': 1, 'b': 2, 'c': 3}
>>>
>>> for element in DATA:
...     print(element)
a
b
c

Iterating ``dict``:

>>> for key, value in DATA.items():
...     print(f'{key} -> {value}')
a -> 1
b -> 2
c -> 3

Iterating nested sequences:

>>> for key, value in [('a',1), ('b',2), ('c',3)]:
...     print(f'{key} -> {value}')
a -> 1
b -> 2
c -> 3


Use Case - 0x01
---------------
Iterator implementation:

>>> class Parking:
...     def __init__(self):
...         self._parked_cars = list()
...
...     def park(self, car):
...         self._parked_cars.append(car)
...
...     def __iter__(self):
...         self._current = 0
...         return self
...
...     def __next__(self):
...         if self._current >= len(self._parked_cars):
...             raise StopIteration
...         element = self._parked_cars[self._current]
...         self._current += 1
...         return element
>>>
>>>
>>> parking = Parking()
>>> parking.park('Mercedes')
>>> parking.park('Maluch')
>>> parking.park('Toyota')
>>>
>>> for car in parking:
...     print(car)
Mercedes
Maluch
Toyota


Standard Library Itertools
--------------------------
``itertools.count(start=0, step=1)``:

>>> from itertools import count
>>>
>>>
>>> data = count(3, 2)
>>>
>>> next(data)
3
>>> next(data)
5
>>> next(data)
7

``itertools.cycle(iterable)``:

>>> from itertools import cycle
>>>
>>>
>>> data = cycle(['white', 'gray'])
>>>
>>> next(data)
'white'
>>> next(data)
'gray'
>>> next(data)
'white'
>>> next(data)
'gray'


``itertools.cycle(iterable)``:

>>> from itertools import cycle
>>>
>>>
>>> for i, status in enumerate(cycle(['even', 'odd'])):  # doctest + SKIP
...     print(i, status)
...     if i == 3:
...         break
0 even
1 odd
2 even
3 odd

``itertools.repeat(object[, times])``:

>>> from itertools import repeat
>>>
>>>
>>> data = repeat('Beetlejuice', 3)
>>>
>>> next(data)
'Beetlejuice'
>>> next(data)
'Beetlejuice'
>>> next(data)
'Beetlejuice'
>>> next(data)
Traceback (most recent call last):
StopIteration

``itertools.accumulate(iterable[, func, *, initial=None])``:

>>> from itertools import accumulate
>>>
>>>
>>> data = accumulate([1, 2, 3, 4])
>>>
>>> next(data)
1
>>> next(data)
3
>>> next(data)
6
>>> next(data)
10
>>> next(data)
Traceback (most recent call last):
StopIteration

``itertools.chain(*iterables)``:

>>> from itertools import chain
>>>
>>>
>>> keys = ['a', 'b', 'c']
>>> values = [1, 2, 3]
>>>
>>> for x in chain(keys, values):
...     print(x)
a
b
c
1
2
3

``itertools.chain(*iterables)``:

>>> from itertools import chain
>>>
>>>
>>> class Iterator:
...     def __iter__(self):
...         self._current = 0
...         return self
...
...     def __next__(self):
...         if self._current >= len(self.values):
...             raise StopIteration
...         element = self.values[self._current]
...         self._current += 1
...         return element
>>>
>>>
>>> class Character(Iterator):
...     def __init__(self, *values):
...         self.values = values
>>>
>>>
>>> class Number(Iterator):
...     def __init__(self, *values):
...         self.values = values
>>>
>>>
>>> chars = Character('a', 'b', 'c')
>>> nums = Number(1, 2, 3)
>>> data = chain(chars, nums)
>>> next(data)
'a'
>>> next(data)
'b'
>>> next(data)
'c'
>>> next(data)
1
>>> next(data)
2
>>> next(data)
3

``itertools.compress(data, selectors)``:

>>> from itertools import compress
>>>
>>>
>>> # data = compress('ABCDEF', [1,0,1,0,1,1])
>>> data = compress('ABCDEF', [True, False, True, False, True, True])
>>>
>>> next(data)
'A'
>>> next(data)
'C'
>>> next(data)
'E'
>>> next(data)
'F'
>>> next(data)
Traceback (most recent call last):
StopIteration

``itertools.islice(iterable, start, stop[, step])``:

>>> from itertools import islice
>>>
>>>
>>> data = islice('ABCDEFG', 2, 6, 2 )
>>>
>>> next(data)
'C'
>>> next(data)
'E'
>>> next(data)
Traceback (most recent call last):
StopIteration

``itertools.starmap(function, iterable)``:

>>> from itertools import starmap
>>>
>>>
>>> data = starmap(pow, [(2,5), (3,2), (10,3)])
>>>
>>> next(data)
32
>>> next(data)
9
>>> next(data)
1000
>>> next(data)
Traceback (most recent call last):
StopIteration

``itertools.product(*iterables, repeat=1)``:

>>> from itertools import product
>>>
>>>
>>> data = product(['a', 'b', 'c'], [1,2])
>>>
>>> next(data)
('a', 1)
>>> next(data)
('a', 2)
>>> next(data)
('b', 1)
>>> next(data)
('b', 2)
>>> next(data)
('c', 1)
>>> next(data)
('c', 2)
>>> next(data)
Traceback (most recent call last):
StopIteration

``itertools.permutations(iterable, r=None)``:

>>> from itertools import permutations
>>>
>>>
>>> data = permutations([1,2,3])
>>>
>>> next(data)
(1, 2, 3)
>>> next(data)
(1, 3, 2)
>>> next(data)
(2, 1, 3)
>>> next(data)
(2, 3, 1)
>>> next(data)
(3, 1, 2)
>>> next(data)
(3, 2, 1)
>>> next(data)
Traceback (most recent call last):
StopIteration

``itertools.combinations(iterable, r)``:

>>> from itertools import combinations
>>>
>>>
>>> data = combinations([1, 2, 3, 4], 2)
>>>
>>> next(data)
(1, 2)
>>> next(data)
(1, 3)
>>> next(data)
(1, 4)
>>> next(data)
(2, 3)
>>> next(data)
(2, 4)
>>> next(data)
(3, 4)
>>> next(data)
Traceback (most recent call last):
StopIteration

``itertools.combinations_with_replacement(iterable, r)``:

>>> from itertools import combinations_with_replacement
>>>
>>>
>>> data = combinations_with_replacement([1,2,3], 2)
>>>
>>> next(data)
(1, 1)
>>> next(data)
(1, 2)
>>> next(data)
(1, 3)
>>> next(data)
(2, 2)
>>> next(data)
(2, 3)
>>> next(data)
(3, 3)
>>> next(data)
Traceback (most recent call last):
StopIteration

``itertools.groupby(iterable, key=None)``. Make an iterator that returns consecutive keys and groups from the iterable. Generally, the iterable needs to already be sorted on the same key function. The operation of groupby() is similar to the uniq filter in Unix. It generates a break or new group every time the value of the key function changes. That behavior differs from SQL's GROUP BY which aggregates common elements regardless of their input order:

>>> from itertools import groupby
>>>
>>>
>>> data = groupby('AAAABBBCCDAABBB')
>>>
>>> next(data)  # doctest: +ELLIPSIS
('A', <itertools._grouper object at 0x...>)
>>> next(data)  # doctest: +ELLIPSIS
('B', <itertools._grouper object at 0x...>)
>>> next(data)  # doctest: +ELLIPSIS
('C', <itertools._grouper object at 0x...>)
>>> next(data)  # doctest: +ELLIPSIS
('D', <itertools._grouper object at 0x...>)
>>> next(data)  # doctest: +ELLIPSIS
('A', <itertools._grouper object at 0x...>)
>>> next(data)  # doctest: +ELLIPSIS
('B', <itertools._grouper object at 0x...>)
>>> next(data)
Traceback (most recent call last):
StopIteration
>>> [k for k, g in groupby('AAAABBBCCDAABBB')]
['A', 'B', 'C', 'D', 'A', 'B']
>>> [list(g) for k, g in groupby('AAAABBBCCD')]
[['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D']]


Assignments
-----------
.. literalinclude:: assignments/protocol_iterator_a.py
    :caption: :download:`Solution <assignments/protocol_iterator_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/protocol_iterator_b.py
    :caption: :download:`Solution <assignments/protocol_iterator_b.py>`
    :end-before: # Solution
