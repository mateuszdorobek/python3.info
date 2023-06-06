Idiom Zip
=========
* Combine two sequences
* Generator (lazy evaluated)
* ``zip(*iterables, strict=False)``
* required ``*iterables`` - 1 or many sequences or iterator object
* Iterate over several iterables in parallel, producing tuples with an item from each one.

The ``zip`` object yields n-length tuples, where n is the number of iterables
passed as positional arguments to ``zip()``. The i-th element in every tuple
comes from the i-th iterable argument to ``zip()``.  This continues until the
shortest argument is exhausted. If strict is true and one of the arguments is
exhausted before the others, raise a ``ValueError``. [#pydoczip]_

>>> from inspect import isgeneratorfunction, isgenerator
>>>
>>>
>>> isgeneratorfunction(zip)
False
>>>
>>> result = zip(['a','b','c'], [1,2,3])
>>> isgenerator(result)
False


Problem
-------
>>> firstnames = ['Mark', 'Melissa', 'Alex']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>> result = []
>>> length = min(len(firstnames), len(lastnames))
>>> i = 0
>>>
>>> while i < length:
...     pair = (firstnames[i], lastnames[i])
...     result.append(pair)
...     i += 1
>>>
>>> result
[('Mark', 'Watney'), ('Melissa', 'Lewis'), ('Alex', 'Vogel')]

>>> firstnames = ['Mark', 'Melissa', 'Alex']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>> result = []
>>>
>>> for i in range(min(len(firstnames), len(lastnames))):
...     pair = (firstnames[i], lastnames[i])
...     result.append(pair)
>>>
>>> result
[('Mark', 'Watney'), ('Melissa', 'Lewis'), ('Alex', 'Vogel')]


Solution
--------
>>> firstnames = ['Mark', 'Melissa', 'Alex']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>> result = zip(firstnames, lastnames)
>>>
>>> list(result)
[('Mark', 'Watney'), ('Melissa', 'Lewis'), ('Alex', 'Vogel')]


Lazy Evaluation
---------------
>>> firstnames = ['Mark', 'Melissa', 'Alex']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>> result = zip(firstnames, lastnames)
>>>
>>> next(result)
('Mark', 'Watney')
>>> next(result)
('Melissa', 'Lewis')
>>> next(result)
('Alex', 'Vogel')
>>> next(result)
Traceback (most recent call last):
StopIteration


Generate Dict
-------------
>>> firstnames = ['Mark', 'Melissa', 'Alex']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>> result = zip(firstnames, lastnames)
>>>
>>> dict(result)
{'Mark': 'Watney', 'Melissa': 'Lewis', 'Alex': 'Vogel'}

>>> roles = ['botanist', 'commander', 'chemist']
>>> names = ['Mark Watney', 'Melissa Lewis', 'Alex Vogel']
>>>
>>> dict(zip(roles, names))  # doctest: +NORMALIZE_WHITESPACE
{'botanist': 'Mark Watney',
 'commander': 'Melissa Lewis',
 'chemist': 'Alex Vogel'}


Adjusts to the Shortest
-----------------------
* ``zip()`` adjusts to the shortest

>>> firstnames = ['Mark', 'Melissa']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>> result = zip(firstnames, lastnames)
>>>
>>> list(result)
[('Mark', 'Watney'), ('Melissa', 'Lewis')]


Adjust to the Longest
---------------------
* ``itertools.zip_longest(iter1 [,iter2 [...]], [fillvalue=None]) --> zip_longest object``

>>> from itertools import zip_longest
>>>
>>>
>>> firstnames = ['Mark', 'Melissa']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>>
>>> list(zip_longest(firstnames, lastnames))
[('Mark', 'Watney'), ('Melissa', 'Lewis'), (None, 'Vogel')]
>>> list(zip_longest(firstnames, lastnames, fillvalue=''))
[('Mark', 'Watney'), ('Melissa', 'Lewis'), ('', 'Vogel')]


Three-way merge
---------------
>>> roles = ['botanist', 'commander', 'chemist']
>>> firstnames = ['Mark', 'Melissa', 'Alex']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>> result = zip(roles, firstnames, lastnames)
>>>
>>> next(result)
('botanist', 'Mark', 'Watney')
>>> next(result)
('commander', 'Melissa', 'Lewis')
>>> next(result)
('chemist', 'Alex', 'Vogel')
>>> next(result)
Traceback (most recent call last):
StopIteration


In For Loop
-----------
>>> roles = ['botanist', 'commander', 'chemist']
>>> names = ['Mark Watney', 'Melissa Lewis', 'Alex Vogel']
>>>
>>> for role, name in zip(roles, names):
...     print(f'{role} -> {name}')
botanist -> Mark Watney
commander -> Melissa Lewis
chemist -> Alex Vogel


Unzip
-----
>>> firstnames = ['Mark', 'Melissa', 'Alex']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>>
>>> list(zip(firstnames, lastnames))
[('Mark', 'Watney'), ('Melissa', 'Lewis'), ('Alex', 'Vogel')]
>>>
>>> fname, lname = zip(*zip(firstnames, lastnames))
>>>
>>> print(fname)
('Mark', 'Melissa', 'Alex')
>>> print(lname)
('Watney', 'Lewis', 'Vogel')


Strict
------
* ``zip(*iterables, strict=False)``
* Since Python 3.10: :pep:`618` -- Add Optional Length-Checking To zip [#pep618]_
* Source [#pydoczip]_

``zip()`` adjusts to the shortest:

>>> firstnames = ['Mark', 'Melissa']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>> result = zip(firstnames, lastnames)
>>>
>>> list(result)
[('Mark', 'Watney'), ('Melissa', 'Lewis')]

``zip()`` is often used in cases where the iterables are assumed to be of equal length.
In such cases, it's recommended to use the ``strict=True`` option.
Its output is the same as regular ``zip()``

>>> firstnames = ['Mark', 'Melissa', 'Alex']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>> result = zip(firstnames, lastnames, strict=True)  # doctest: +SKIP
>>>
>>> list(result)  # doctest: +SKIP
[('Mark', 'Watney'), ('Melissa', 'Lewis'), ('Alex', 'Vogel')]

Unlike the default behavior, it checks that the lengths of iterables are identical, raising a ``ValueError`` if they aren't:

>>> firstnames = ['Mark', 'Melissa']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>>
>>> result = zip(firstnames, lastnames, strict=True)  # doctest: +SKIP
Traceback (most recent call last):
ValueError: zip() argument 2 is longer than argument 1

Without the ``strict=True`` argument, any bug that results in iterables of different lengths will be silenced, possibly manifesting as a hard-to-find bug in another part of the program.


Zip Longest
-----------
SetUp:

>>> from itertools import zip_longest
>>>
>>> firstnames = ['Mark', 'Melissa']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']

Usage:

>>> result = zip_longest(firstnames, lastnames)
>>> list(result)
[('Mark', 'Watney'), ('Melissa', 'Lewis'), (None, 'Vogel')]

>>> result = zip_longest(firstnames, lastnames, fillvalue='n/a')
>>>
>>> list(result)
[('Mark', 'Watney'), ('Melissa', 'Lewis'), ('n/a', 'Vogel')]


Use Case - 0x01
---------------
>>> for user, address, order in zip(users, addresses, orders):  # doctest: +SKIP
...    print(f'Get {user} orders... {order}')


References
----------
.. [#pep618] https://www.python.org/dev/peps/pep-0618/
.. [#pydoczip] Python Core Developers. Built-in Functions. Year: 2022. Retrieved: 2022-06-28. URL: https://docs.python.org/3/library/functions.html#zip


Assignments
-----------
.. literalinclude:: assignments/idiom_zip_a.py
    :caption: :download:`Solution <assignments/idiom_zip_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_zip_b.py
    :caption: :download:`Solution <assignments/idiom_zip_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_zip_c.py
    :caption: :download:`Solution <assignments/idiom_zip_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_zip_d.py
    :caption: :download:`Solution <assignments/idiom_zip_d.py>`
    :end-before: # Solution
