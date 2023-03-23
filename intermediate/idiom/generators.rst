Function Generator-Like
=======================
* It is not a generator
* Generator-like objects
* ``range(start, stop, step)``
* ``reversed(iterable)``
* ``enumerate(iterable, start=0)``
* ``zip(*iterable, strict=False)``
* ``map(func, iterable)``
* ``filter(func, iterable)``
* ``next(iterable)``
* ``iter(iterable)``


Range
-----
* ``range([start], <stop>, [step])``
* optional ``start``, inclusive, default: ``0``
* required ``stop``, exclusive
* optional ``step``, default: ``1``

``range()`` syntax:

>>> range(0,3)
range(0, 3)

>>> list(range(0,3))
[0, 1, 2]
>>>
>>> tuple(range(0,3))
(0, 1, 2)
>>>
>>> set(range(0,3))
{0, 1, 2}
>>>
>>> list(range(4,11,2))
[4, 6, 8, 10]


Reversed
--------
* ``reversed()`` - Return a reverse iterator over the values of the given sequence

>>> data = (1, 2, 3)
>>> list(reversed(data))
[3, 2, 1]


Enumerate
---------
* ``enumerate(*iterables)``

>>> months = ['January', 'February', 'March']
>>> result = enumerate(months)
>>>
>>> list(result)
[(0, 'January'), (1, 'February'), (2, 'March')]

>>> months = ['January', 'February', 'March']
>>> result = enumerate(months)
>>>
>>> dict(result)
{0: 'January', 1: 'February', 2: 'March'}

>>> months = ['January', 'February', 'March']
>>> result = enumerate(months, start=1)
>>>
>>> dict(result)
{1: 'January', 2: 'February', 3: 'March'}

>>> months = ['January', 'February', 'March']
>>> result = {f'{i:02}':month for i,month in enumerate(months, start=1)}
>>>
>>> print(result)
{'01': 'January', '02': 'February', '03': 'March'}


Zip
---
* ``zip(*iterables)``

>>> firstnames = ['Mark', 'Melissa', 'Rick']
>>> lastnames = ['Watney', 'Lewis', 'Martinez']
>>>
>>> list(zip(firstnames, lastnames))
[('Mark', 'Watney'), ('Melissa', 'Lewis'), ('Rick', 'Martinez')]

>>> firstnames = ['Mark', 'Melissa', 'Rick']
>>> lastnames = ['Watney', 'Lewis', 'Martinez']
>>>
>>> dict(zip(firstnames, lastnames))
{'Mark': 'Watney', 'Melissa': 'Lewis', 'Rick': 'Martinez'}

>>> roles = ['botanist', 'commander', 'pilot']
>>> names = ['Mark Watney', 'Melissa Lewis', 'Rick Martinez']
>>>
>>> dict(zip(roles, names))  # doctest: +NORMALIZE_WHITESPACE
{'botanist': 'Mark Watney',
 'commander': 'Melissa Lewis',
 'pilot': 'Rick Martinez'}

``zip()`` adjusts to the shortest:

>>> firstnames = ['Mark', 'Melissa']
>>> lastnames = ['Watney', 'Lewis', 'Martinez']
>>>
>>> list(zip(firstnames, lastnames))
[('Mark', 'Watney'), ('Melissa', 'Lewis')]

Three-way:

>>> roles = ['botanist', 'commander', 'pilot']
>>> firstnames = ['Mark', 'Melissa', 'Rick']
>>> lastnames = ['Watney', 'Lewis', 'Martinez']
>>>
>>> result = zip(roles, firstnames, lastnames)
>>>
>>>
>>> next(result)
('botanist', 'Mark', 'Watney')
>>>
>>> next(result)
('commander', 'Melissa', 'Lewis')
>>>
>>> next(result)
('pilot', 'Rick', 'Martinez')
>>>
>>> next(result)
Traceback (most recent call last):
StopIteration


Map
---
* Apply function to all elements of data
* ``map(callable, *iterables)``

>>> def square(x):
...     return x ** 2

>>> data = [1, 2, 3]
>>> result = map(square, data)
>>> list(result)
[1, 4, 9]


Filter
------
* ``filter(callable, *iterables)``

>>> def even(x):
...     return x % 2 == 0

>>> data = [0, 1, 2, 3, 4]
>>> result = filter(even, data)
>>> list (result)
[0, 2, 4]


Next
----
Range:

>>> result = range(0,5)
>>>
>>> next(result)
Traceback (most recent call last):
TypeError: 'range' object is not an iterator

Zip two-way:

>>> firstnames = ['Mark', 'Melissa', 'Rick']
>>> lastnames = ['Watney', 'Lewis', 'Martinez']
>>>
>>> result = zip(firstnames, lastnames)
>>>
>>>
>>> next(result)
('Mark', 'Watney')
>>>
>>> next(result)
('Melissa', 'Lewis')
>>>
>>> next(result)
('Rick', 'Martinez')
>>>
>>> next(result)
Traceback (most recent call last):
StopIteration

Enumerate:

>>> months = ['January', 'February', 'March']
>>> result = enumerate(months)
>>>
>>> next(result)
(0, 'January')
>>>
>>> next(result)
(1, 'February')
>>>
>>> next(result)
(2, 'March')
>>>
>>> next(result)
Traceback (most recent call last):
StopIteration

Zip n-way:

>>> roles = ['botanist', 'commander', 'pilot']
>>> firstnames = ['Mark', 'Melissa', 'Rick']
>>> lastnames = ['Watney', 'Lewis', 'Martinez']
>>>
>>> result = zip(roles, firstnames, lastnames)
>>>
>>>
>>> next(result)
('botanist', 'Mark', 'Watney')
>>>
>>> next(result)
('commander', 'Melissa', 'Lewis')
>>>
>>> next(result)
('pilot', 'Rick', 'Martinez')
>>>
>>> next(result)
Traceback (most recent call last):
StopIteration

Map:

>>> def square(x):
...     return x ** 2
>>>
>>> data = [1, 2, 3]
>>> result = map(square, data)
>>>
>>>
>>> next(result)
1
>>>
>>> next(result)
4
>>>
>>> next(result)
9
>>> next(result)
Traceback (most recent call last):
StopIteration

Filter:

>>> def even(x):
...     return x % 2 == 0
>>>
>>> data = [0, 1, 2, 3, 4]
>>> result = filter(even, data)
>>>
>>>
>>> next(result)
0
>>>
>>> next(result)
2
>>>
>>> next(result)
4
>>> next(result)
Traceback (most recent call last):
StopIteration


Iter
----
Range:

>>> for i in range(0,3):
...     print(i)
0
1
2

Enumerate:

>>> months = ['January', 'February', 'March']
>>>
>>> for i, month in enumerate(months, start=1):
...     print(f'{i=}, {month=}')
i=1, month='January'
i=2, month='February'
i=3, month='March'

Zip:

>>> roles = ['botanist', 'commander', 'pilot']
>>> names = ['Mark Watney', 'Melissa Lewis', 'Rick Martinez']
>>>
>>> for role, name in zip(roles, names):
...     print(f'{role=}, {name=}')
role='botanist', name='Mark Watney'
role='commander', name='Melissa Lewis'
role='pilot', name='Rick Martinez'


Generator Chain
---------------
* Function composition

>>> def square(x):
...     return x ** 2
>>>
>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> result = range(0,10)
>>> result = map(square, result)
>>> result = filter(even, result)
>>>
>>> for value in result:
...     print(value)
...     if value > 3:
...         break
0
4
>>>
>>> next(result)
16
>>>
>>> list(result)
[36, 64]


Itertools
---------
* Learn more at https://docs.python.org/3/library/itertools.html
* More information in `Itertools`
* ``itertools.count(start=0, step=1)``
* ``itertools.cycle(iterable)``
* ``itertools.repeat(object[, times])``
* ``itertools.accumulate(iterable[, func, *, initial=None])``
* ``itertools.chain(*iterables)``
* ``itertools.compress(data, selectors)``
* ``itertools.islice(iterable, start, stop[, step])``
* ``itertools.starmap(function, iterable)``
* ``itertools.product(*iterables, repeat=1)``
* ``itertools.permutations(iterable, r=None)``
* ``itertools.combinations(iterable, r)``
* ``itertools.combinations_with_replacement(iterable, r)``
* ``itertools.groupby(iterable, key=None)``


Use Case - 0x01
---------------
>>> def increment(x):
...     return x + 1
>>>
>>>
>>> data = [1, 2, 3, 4]
>>> result = map(increment, data)
>>>
>>> list(result)
[2, 3, 4, 5]


Use Case - 0x02
---------------
>>> def square(x):
...     return x ** 2
>>>
>>>
>>> data = [1, 2, 3]
>>> result = map(square, data)
>>>
>>> list(result)
[1, 4, 9]


Use Case - 0x03
---------------
>>> PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
...       'ł': 'l', 'ń': 'n', 'ó': 'o',
...       'ś': 's', 'ż': 'z', 'ź': 'z'}
>>>
>>>
>>> def translate(letter):
...     return PL.get(letter, letter)
>>>
>>>
>>> text = 'zażółć gęślą jaźń'
>>> result = map(translate, text)
>>>
>>> ''.join(result)
'zazolc gesla jazn'


Use Case - 0x04
---------------
>>> people = [
...     {'age': 21, 'name': 'Mark Watney'},
...     {'age': 25, 'name': 'Melissa Lewis'},
...     {'age': 18, 'name': 'Rick Martinez'}]
>>>
>>>
>>> def adult(person):
...     return person['age'] >= 21
>>>
>>>
>>> result = filter(adult, people)
>>>
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[{'age': 21, 'name': 'Mark Watney'},
 {'age': 25, 'name': 'Melissa Lewis'}]


Use Case - 0x05
---------------
>>> people = [
...     {'is_astronaut': False, 'name': 'Mark Watney'},
...     {'is_astronaut': True, 'name': 'Melissa Lewis'},
...     {'is_astronaut': True, 'name': 'Rick Martinez'}]
>>>
>>>
>>> def astronaut(person):
...     return person['is_astronaut']
>>>
>>>
>>> result = filter(astronaut, people)
>>>
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[{'is_astronaut': True, 'name': 'Melissa Lewis'},
 {'is_astronaut': True, 'name': 'Rick Martinez'}]


Use Case - 0x06
---------------
Sum stdin (standard input):

>>> import sys
>>>
>>> # doctest: +SKIP
... print(sum(map(int, sys.stdin)))

.. code-block:: console

    $ cat ~/.profile |grep addnum
    alias addnum='python -c"import sys; print(sum(map(int, sys.stdin)))"'


Assignments
-----------
.. literalinclude:: assignments/idiom_generators_a.py
    :caption: :download:`Solution <assignments/idiom_generators_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_generators_b.py
    :caption: :download:`Solution <assignments/idiom_generators_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_generators_c.py
    :caption: :download:`Solution <assignments/idiom_generators_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_generators_d.py
    :caption: :download:`Solution <assignments/idiom_generators_d.py>`
    :end-before: # Solution
