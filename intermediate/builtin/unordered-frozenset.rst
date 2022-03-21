Sequence Frozenset
==================


Important
---------
* Only unique values
* Immutable - cannot add, modify or remove items
* Can store elements of any **hashable** types
* Has all ``set`` methods such as ``.intersect()``, ``.subset()`` ``.union()``, etc.
* One solid block in memory
* Frozenset is unordered data structure and do not record element position
* Do not support getitem and slice


Definition
----------
Defining only with ``frozenset()`` - no short syntax:

>>> data = frozenset()

Comma after last element of a one element frozenset is optional:

>>> data = frozenset({1})
>>> data = frozenset({1,})

Brackets inside are required:

>>> data = frozenset({1})
>>> data = frozenset({1, 2, 3})
>>> data = frozenset({1.1, 2.2, 3.3})
>>> data = frozenset({True, False})
>>> data = frozenset({'a', 'b', 'c'})
>>> data = frozenset({'a', 1, 2.2, True, None})


Type Casting
------------
Builtin function ``frozenset()`` converts argument to ``frozenset``

>>> data = 'abcd'
>>> frozenset(data) == frozenset({'a', 'b', 'c', 'd'})
True

>>> data = ['a', 'b', 'c', 'd']
>>> frozenset(data) == frozenset({'a', 'b', 'c', 'd'})
True

>>> data = ('a', 'b', 'c', 'd')
>>> frozenset(data) == frozenset({'a', 'b', 'c', 'd'})
True

>>> data = {'a', 'b', 'c', 'd'}
>>> frozenset(data) == frozenset({'a', 'b', 'c', 'd'})
True

>>> data = frozenset({'a', 'b', 'c', 'd'})
>>> frozenset(data) == frozenset({'a', 'b', 'c', 'd'})
True

>>> data = [1, 2, 3, [4, 5]]
>>> frozenset(data)
Traceback (most recent call last):
TypeError: unhashable type: 'list'

>>> data = [1, 2, 3, (4, 5)]
>>> frozenset(data) == frozenset({(4, 5), 1, 2, 3})
True


Assignments
-----------
.. literalinclude:: assignments/sequence_frozenset_a.py
    :caption: :download:`Solution <assignments/sequence_frozenset_a.py>`
    :end-before: # Solution
