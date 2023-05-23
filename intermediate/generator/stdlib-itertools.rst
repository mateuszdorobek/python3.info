Generator Itertools
===================


Itertools
---------
* Learn more at https://docs.python.org/library/itertools.html
* More information in `Itertools`
* ``from itertools import *``
* ``count(start=0, step=1)``
* ``cycle(iterable)``
* ``repeat(object[, times])``
* ``accumulate(iterable[, func, *, initial=None])``
* ``chain(*iterables)``
* ``compress(data, selectors)``
* ``islice(iterable, start, stop[, step])``
* ``starmap(function, iterable)``
* ``product(*iterables, repeat=1)``
* ``permutations(iterable, r=None)``
* ``combinations(iterable, r)``
* ``combinations_with_replacement(iterable, r)``
* ``groupby(iterable, key=None)``


Itertools Count
---------------
* ``itertools.count(start=0, step=1)``

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


Itertools Cycle
---------------
* ``itertools.cycle(iterable)``

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


Itertools Repeat
----------------
* ``itertools.repeat(object[, times])``

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


Itertools Accumulate
--------------------
* ``itertools.accumulate(iterable[, func, *, initial=None])``

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


Itertools Chain
---------------
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


Itertools Compress
------------------
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


Itertools ISlice
----------------
* ``itertools.islice(iterable, start, stop[, step])``

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


Itertools Starmap
-----------------
* ``itertools.starmap(function, iterable)``

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


Itertools Product
-----------------
* ``itertools.product(*iterables, repeat=1)``

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


Itertools Permutations
----------------------
* ``itertools.permutations(iterable, r=None)``

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


Itertools Combinations
----------------------
* ``itertools.combinations(iterable, r)``

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


Itertools Combinations With Replacement
---------------------------------------
* ``itertools.combinations_with_replacement(iterable, r)``

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


Itertools GroupBy
-----------------
* ``itertools.groupby(iterable, key=None)``
* Make an iterator that returns consecutive keys and groups from the
  iterable. Generally, the iterable needs to already be sorted on the same
  key function. The operation of groupby() is similar to the uniq filter
  in Unix. It generates a break or new group every time the value of the
  key function changes. That behavior differs from SQL's GROUP BY which
  aggregates common elements regardless of their input order:

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


Use Case - 0x01
---------------
>>> from itertools import product
>>> from pprint import pprint

>>> filenames = ['file1.txt', 'file2.txt']
>>> modes = ['r', 'w', 'a']
>>> encodings = ['utf-8', None, 'latin-1']

>>> result = product(filenames, modes, encodings)
>>> pprint(list(result))
[('file1.txt', 'r', 'utf-8'),
 ('file1.txt', 'r', None),
 ('file1.txt', 'r', 'latin-1'),
 ('file1.txt', 'w', 'utf-8'),
 ('file1.txt', 'w', None),
 ('file1.txt', 'w', 'latin-1'),
 ('file1.txt', 'a', 'utf-8'),
 ('file1.txt', 'a', None),
 ('file1.txt', 'a', 'latin-1'),
 ('file2.txt', 'r', 'utf-8'),
 ('file2.txt', 'r', None),
 ('file2.txt', 'r', 'latin-1'),
 ('file2.txt', 'w', 'utf-8'),
 ('file2.txt', 'w', None),
 ('file2.txt', 'w', 'latin-1'),
 ('file2.txt', 'a', 'utf-8'),
 ('file2.txt', 'a', None),
 ('file2.txt', 'a', 'latin-1')]

* https://docs.python.org/3/library/unittest.html#distinguishing-test-iterations-using-subtests

.. code-block:: python

    class NumbersTest(unittest.TestCase):

        def test_even(self):
            """
            Test that numbers between 0 and 5 are all even.
            """
            for i in range(0, 6):
                with self.subTest(i=i):
                    self.assertEqual(i % 2, 0)


Use Case - 0x02
---------------
>>> from itertools import permutations
>>>
>>>
>>> actions = ['press play', 'press stop', 'press eject', 'press rewind']
>>>
>>> result = permutations(actions)
>>> pprint(list(result))
[('press play', 'press stop', 'press eject', 'press rewind'),
 ('press play', 'press stop', 'press rewind', 'press eject'),
 ('press play', 'press eject', 'press stop', 'press rewind'),
 ('press play', 'press eject', 'press rewind', 'press stop'),
 ('press play', 'press rewind', 'press stop', 'press eject'),
 ('press play', 'press rewind', 'press eject', 'press stop'),
 ('press stop', 'press play', 'press eject', 'press rewind'),
 ('press stop', 'press play', 'press rewind', 'press eject'),
 ('press stop', 'press eject', 'press play', 'press rewind'),
 ('press stop', 'press eject', 'press rewind', 'press play'),
 ('press stop', 'press rewind', 'press play', 'press eject'),
 ('press stop', 'press rewind', 'press eject', 'press play'),
 ('press eject', 'press play', 'press stop', 'press rewind'),
 ('press eject', 'press play', 'press rewind', 'press stop'),
 ('press eject', 'press stop', 'press play', 'press rewind'),
 ('press eject', 'press stop', 'press rewind', 'press play'),
 ('press eject', 'press rewind', 'press play', 'press stop'),
 ('press eject', 'press rewind', 'press stop', 'press play'),
 ('press rewind', 'press play', 'press stop', 'press eject'),
 ('press rewind', 'press play', 'press eject', 'press stop'),
 ('press rewind', 'press stop', 'press play', 'press eject'),
 ('press rewind', 'press stop', 'press eject', 'press play'),
 ('press rewind', 'press eject', 'press play', 'press stop'),
 ('press rewind', 'press eject', 'press stop', 'press play')]

* https://docs.python.org/3/library/unittest.html#distinguishing-test-iterations-using-subtests

.. code-block:: python

    class NumbersTest(unittest.TestCase):

        def test_even(self):
            """
            Test that numbers between 0 and 5 are all even.
            """
            for i in range(0, 6):
                with self.subTest(i=i):
                    self.assertEqual(i % 2, 0)


Use Case - 0x03
---------------
>>> from itertools import combinations
>>>
>>>
>>> colors = ['red', 'orange', 'yellow', 'green', 'blue']
>>>
>>> result = combinations(colors, 3)
>>> pprint(list(result))
[('red', 'orange', 'yellow'),
 ('red', 'orange', 'green'),
 ('red', 'orange', 'blue'),
 ('red', 'yellow', 'green'),
 ('red', 'yellow', 'blue'),
 ('red', 'green', 'blue'),
 ('orange', 'yellow', 'green'),
 ('orange', 'yellow', 'blue'),
 ('orange', 'green', 'blue'),
 ('yellow', 'green', 'blue')]

* https://docs.python.org/3/library/unittest.html#distinguishing-test-iterations-using-subtests

.. code-block:: python

    class NumbersTest(unittest.TestCase):

        def test_even(self):
            """
            Test that numbers between 0 and 5 are all even.
            """
            for i in range(0, 6):
                with self.subTest(i=i):
                    self.assertEqual(i % 2, 0)

Use Case - 0x04
---------------
>>> from itertools import chain
>>>
>>>
>>> def powerset(iterable):
...     """
...     >>> powerset ([1,2,31])
...     () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
...     """
...     s = list(iterable)
...     return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))
...
>>>
>>> users = ['Mark', 'Melissa', 'Rick', 'Alex']
>>>
>>> result = powerset(users)
>>> pprint(list(result))
[(),
 ('Mark',),
 ('Melissa',),
 ('Rick',),
 ('Alex',),
 ('Mark', 'Melissa'),
 ('Mark', 'Rick'),
 ('Mark', 'Alex'),
 ('Melissa', 'Rick'),
 ('Melissa', 'Alex'),
 ('Rick', 'Alex'),
 ('Mark', 'Melissa', 'Rick'),
 ('Mark', 'Melissa', 'Alex'),
 ('Mark', 'Rick', 'Alex'),
 ('Melissa', 'Rick', 'Alex'),
 ('Mark', 'Melissa', 'Rick', 'Alex')]


Use Case - 0x05
---------------
>>> from itertools import starmap
>>> from dataclasses import dataclass
>>>
>>>
>>> DATA = [
...     ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
... ]
>>>
>>>
>>> @dataclass
... class Iris:
...     sl: float
...     sw: float
...     pl: float
...     pw: float
...     species: str
...
...     def save(self):
...         return 'success'

>>> result = starmap(Iris, DATA[1:])
>>>
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[Iris(sl=5.8, sw=2.7, pl=5.1, pw=1.9, species='virginica'),
 Iris(sl=5.1, sw=3.5, pl=1.4, pw=0.2, species='setosa'),
 Iris(sl=5.7, sw=2.8, pl=4.1, pw=1.3, species='versicolor'),
 Iris(sl=6.3, sw=2.9, pl=5.6, pw=1.8, species='virginica'),
 Iris(sl=6.4, sw=3.2, pl=4.5, pw=1.5, species='versicolor'),
 Iris(sl=4.7, sw=3.2, pl=1.3, pw=0.2, species='setosa')]

>>> result = starmap(Iris, DATA[1:])
>>> result = map(Iris.save, result)
>>>
>>> list(result)
['success', 'success', 'success', 'success', 'success', 'success']

>>> for iris in starmap(Iris, DATA[1:]):
...     print(f'Saving to database...', end=' ')
...     result = iris.save()
...     print(result)
...
Saving to database... success
Saving to database... success
Saving to database... success
Saving to database... success
Saving to database... success
Saving to database... success


Use Case - 0x06
---------------
>>> from unittest import TestCase
>>> from itertools import permutations
>>>
>>>
>>> def click(button1, button2, button3, button4):
...     return ...
>>>
>>>
>>> class PayerTest(TestCase):
...     def test_buttons(self):
...         buttons = ['play', 'stop', 'rev', 'fwd']
...         for order in permutations(buttons):
...             with self.subTest(order):
...                 result = click(*order)
...                 self.assertEqual(result, ...)


Use Case - 0x07
---------------
>>> from unittest import TestCase
>>> from itertools import product
>>>
>>>
>>> def parse(encoding, delimiter, lineterminator):
...     return ...
>>>
>>>
>>> class ParserTest(TestCase):
...     def test_parse(self):
...         encoding = ['utf-8', 'cp1250', 'iso-8859-2', 'utf-16', 'utf-32']
...         delimiter = [',', ';']
...         lineterminator = ['\n', '\r\n']
...         for option in product(encoding, delimiter, lineterminator):
...             with self.subTest(option):
...                 result = parse(*option)
...                 self.assertEqual(result, ...)


Assignments
-----------
.. literalinclude:: assignments/generator_itertools_a.py
    :caption: :download:`Solution <assignments/generator_itertools_a.py>`
    :end-before: # Solution
