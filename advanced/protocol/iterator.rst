Protocol Iterator
=================
* Used for iterating in a ``for`` loop
* ``__iter__(self) -> self``
* ``__next__(self) -> raise StopIteration``
* ``iter(obj)`` -> ``obj.__iter__()``
* ``next(obj)`` -> ``obj.__next__()``

/gpt describe iterator protocol in Python
The iterator protocol is a Python protocol that defines the rules for
implementing an iterator object. An iterator is an object that produces a
sequence of values, one at a time, and can be used in a ``for`` loop or other
iteration contexts.

The iterator protocol consists of two methods:

1. ``__iter__()``: This method returns the iterator object itself.
It is called when the ``iter()`` function is called on an iterable
object, such as a list or tuple.

2. ``__next__()``: This method returns the next value in the sequence.
It is called when the ``next()`` function is called on the iterator object.

Here's an example of implementing an iterator object that produces a
sequence of Fibonacci numbers:

>>> class Fibonacci:
...     def __init__(self):
...         self.prev = 0
...         self.curr = 1
...
...     def __iter__(self):
...         return self
...
...     def __next__(self):
...         value = self.curr
...         self.curr += self.prev
...         self.prev = value
...         return value
>>>
>>> # Use the Fibonacci iterator in a for loop
>>> fibonacci = Fibonacci()
>>> for i in range(10):
...     print(next(fibonacci))
1
1
2
3
5
8
13
21
34
55

In this example, the ``Fibonacci`` class implements the iterator protocol
by defining the ``__iter__()`` and ``__next__()`` methods. The ``__iter__()``
method returns the iterator object itself, and the ``__next__()`` method
returns the next Fibonacci number in the sequence.

The ``Fibonacci`` iterator can be used in a ``for`` loop or other iteration
contexts by calling the ``next()`` function on the iterator object. In this
example, the ``Fibonacci`` iterator is used to produce the first 10 Fibonacci
numbers.

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
>>> class Group:
...     def __init__(self, name):
...         self.name = name
...         self.members = []
...
...     def add(self, user):
...         self.members.append(user)
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
>>> admins = Group('admins')
>>> admins.add('mwatney')
>>> admins.add('mlewis')
>>> admins.add('rmartinez')
>>>
>>> for admin in admins:
...     print(admin)
mwatney
mlewis
rmartinez


Loop and Iterators
------------------
For loop:

>>> DATA = [1, 2, 3]
>>>
>>> for x in DATA:
...     print(x)
1
2
3

Intuitive implementation of the ``for`` loop:

>>> DATA = [1, 2, 3]
>>> current = iter(DATA)
>>>
>>> try:
...     x = next(current)
...     print(x)
...
...     x = next(current)
...     print(x)
...
...     x = next(current)
...     print(x)
...
...     x = next(current)
...     print(x)
... except StopIteration:
...     pass
1
2
3

Intuitive implementation of the ``for`` loop:

>>> DATA = [1, 2, 3]
>>> current = DATA.__iter__()
>>>
>>> try:
...     x = current.__next__()
...     print(x)
...
...     x = current.__next__()
...     print(x)
...
...     x = current.__next__()
...     print(x)
...
...     x = current.__next__()
...     print(x)
... except StopIteration:
...     pass
1
2
3


Use Case - 0x01
---------------
>>> class Crew:
...     def __init__(self):
...         self.members = []
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


Use Case - 0x02
---------------

Use Case - 0x01
---------------
Iterator implementation:

>>> class Parking:
...     def __init__(self):
...         self._parked_cars = []
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


Assignments
-----------
.. literalinclude:: assignments/protocol_iterator_a.py
    :caption: :download:`Solution <assignments/protocol_iterator_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/protocol_iterator_b.py
    :caption: :download:`Solution <assignments/protocol_iterator_b.py>`
    :end-before: # Solution
