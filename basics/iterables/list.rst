Iterable List
=============
* Mutable - can add, remove, and modify items
* Stores elements of any type

CPython's lists are really variable-length arrays, not Lisp-style linked
lists. The implementation uses a contiguous array of references to other
objects, and keeps a pointer to this array and the array's length in a list
head structure.

This makes indexing a list ``data[i]`` an operation whose cost is independent
of the size of the list or the value of the index.

When items are appended or inserted, the array of references is resized.
Some cleverness is applied to improve the performance of appending items
repeatedly; when the array must be grown, some extra space is allocated
so the next few times don't require an actual resize.


Syntax
------
* ``data = []`` - empty list
* ``data = [1, 2.2, 'abc']`` - list with values
* ``data = []`` is faster than ``data = list()``

Defining empty list with ``[]`` is used more often, but ``list()`` is more
explicit:

>>> data = list()
>>> data = []

Comma after last element is optional:

>>> data = [1]
>>> data = [1,]

Can store elements of any types:

>>> data = [1, 2, 3]
>>> data = [1.1, 2.2, 3.3]
>>> data = [True, False]
>>> data = ['a', 'b', 'c']
>>> data = ['a', 1, 2.2, True, None]

Brackets are required

>>> data = [1, 2, 3]

Performance:

>>> %%timeit -r 10_000 -n 10_000  # doctest: +SKIP
... data = list()
...
53.8 ns ± 8.15 ns per loop (mean ± std. dev. of 10000 runs, 10,000 loops each)
>>>
>>>
>>> %%timeit -r 10_000 -n 10_000  # doctest: +SKIP
... data = []
...
23.9 ns ± 4.23 ns per loop (mean ± std. dev. of 10000 runs, 10,000 loops each)


Type Conversion
---------------
* ``list()`` converts argument to ``list``
* Takes one iterable as an argument
* Multiple arguments are not allowed

Builtin function ``list()`` converts argument to ``list``

>>> text = 'hello'
>>> list(text)
['h', 'e', 'l', 'l', 'o']

>>> colors = ['red', 'green', 'blue']
>>> list(colors)
['red', 'green', 'blue']

>>> colors = ('red', 'green', 'blue')
>>> list(colors)
['red', 'green', 'blue']

>>> list('red', 'green', 'blue')
Traceback (most recent call last):
TypeError: list expected at most 1 argument, got 3


Get Item
--------
* Returns a value at given index
* Note, that Python start counting at zero (zero based indexing)
* Raises ``IndexError`` if the index is out of range
* More information in `Iterable GetItem`
* More information in `Iterable Slice`

>>> colors = ['red', 'green', 'blue']
>>>
>>> colors[0]
'red'
>>> colors[1]
'green'
>>> colors[2]
'blue'


Set Item
--------
>>> colors = ['red', 'green', 'blue']
>>> colors[0] = 'black'
>>>
>>> print(colors)
['black', 'green', 'blue']

>>> colors = ['red', 'green', 'blue']
>>> colors[4] = 'black'
Traceback (most recent call last):
IndexError: list assignment index out of range


Del Item
--------
>>> colors = ['red', 'green', 'blue']
>>> del colors[2]
>>>
>>> print(colors)
['red', 'green']

>>> colors = ['red', 'green', 'blue']
>>> result = colors.pop()
>>>
>>> colors
['red', 'green']
>>> result
'blue'


Append
------
* ``list + list`` - add
* ``list += list`` - increment add
* ``list.extend()`` - extend
* ``list.append()`` - append
* ``O(1)`` complexity

Add:

>>> colors = ['red', 'green', 'blue']
>>> result = colors + ['black']
>>>
>>> print(colors)
['red', 'green', 'blue']
>>>
>>> print(result)
['red', 'green', 'blue', 'black']

Increment Add:

>>> colors = ['red', 'green', 'blue']
>>> colors += ['black']
>>>
>>> print(colors)
['red', 'green', 'blue', 'black']

Extend:

>>> colors = ['red', 'green', 'blue']
>>> colors.extend(['black', 'white'])
>>>
>>> print(colors)
['red', 'green', 'blue', 'black', 'white']

Append:
>>> colors = ['red', 'green', 'blue']
>>> colors.append(['black', 'white'])
>>>
>>> print(colors)
['red', 'green', 'blue', ['black', 'white']]

Errors:

>>> colors + 'black'
Traceback (most recent call last):
TypeError: can only concatenate list (not "str") to list

>>> colors = ['red', 'green', 'blue']
>>> colors += 'black'
>>>
>>> print(colors)
['red', 'green', 'blue', 'b', 'l', 'a', 'c', 'k']


Insert
------
* ``list.insert(idx, object)``
* Insert object at specific position
* ``O(n)`` complexity

>>> colors = ['red', 'green', 'blue']
>>> colors.insert(0, 'black')
>>>
>>> print(colors)
['black', 'red', 'green', 'blue']

>>> colors = ['red', 'green', 'blue']
>>> colors.insert(1, 'black')
>>>
>>> print(colors)
['red', 'black', 'green', 'blue']


Sort
----
* ``sorted()`` - returns new sorted list, but does not modify the original
* ``list.sort()`` - sorts list and returns ``None``

Why doesn't list.sort() return the sorted list? [#PyDocListSort]_

In situations where performance matters, making a copy of the list just to sort it would be wasteful. Therefore, list.sort() sorts the list in place. In order to remind you of that fact, it does not return the sorted list. This way, you won't be fooled into accidentally overwriting a list when you need a sorted copy but also need to keep the unsorted version around.

If you want to return a new list, use the built-in sorted() function instead. This function creates a new list from a provided iterable, sorts it and returns it. For example, here's how to iterate over the keys of a dictionary in sorted order

Timsort is a hybrid stable sorting algorithm, derived from merge sort and
insertion sort, designed to perform well on many kinds of real-world data.
It was implemented by Tim Peters in 2002 for use in the Python programming
language. The algorithm finds subsequences of the data that are already
ordered (runs) and uses them to sort the remainder more efficiently. This
is done by merging runs until certain criteria are fulfilled. Timsort has
been Python's standard sorting algorithm since version 2.3. It is also used
to sort arrays of non-primitive type in Java SE 7, on the Android platform,
in GNU Octave, on V8, Swift, and Rust. [#timsort]_

* Worst-case performance: :math:`O(n\log{n})`
* Best-case performance: :math:`O(n)`
* Average performance: :math:`O(n\log{n})`
* Worst-case space complexity: :math:`O(n)`

* ``sorted()`` - Returns sorted list, do not modify the original
* ``list.sort()`` - Changes object permanently, returns ``None``

Return sorted values without modifying a list:

>>> values = [3, 1, 2]
>>>
>>> sorted(values)
[1, 2, 3]
>>>
>>> sorted(values, reverse=True)
[3, 2, 1]

Permanent sorting with list modification (note that ``list.sort()`` modifies
values, and returns ``None``, not values):

>>> values = [3, 1, 2]
>>>
>>> values.sort()
>>> values
[1, 2, 3]
>>>
>>> values.sort(reverse=True)
>>> values
[3, 2, 1]

You can also use ``list.sort()`` and/or ``sorted()`` with ``str``. It will
sort strings according to Unicode (UTF-8) value, that is ASCII table for
latin alphabet and Unicode for extended encoding. This kind of sorting is
called lexicographic order.

>>> colors = ['red', 'green', 'blue']
>>>
>>> sorted(colors)
['blue', 'green', 'red']


Reverse
-------
* ``reversed()``
* ``list.reverse()``

>>> colors = ['red', 'green', 'blue']
>>> colors.reverse()
>>> colors
['blue', 'green', 'red']

>>> colors = ['red', 'green', 'blue']
>>> result = reversed(colors)
>>>
>>> list(result)
['blue', 'green', 'red']

Why?:

>>> colors = ['red', 'green', 'blue']
>>> result = reversed(colors)
>>>
>>> result  # doctest: +ELLIPSIS
<list_reverseiterator object at 0x...>
>>>
>>> next(result)
'blue'
>>> next(result)
'green'
>>> next(result)
'red'
>>> next(result)
Traceback (most recent call last):
StopIteration


Index
-----
* ``list.index()`` - position at which something is in the list
* Note, that Python start counting at zero (zero based indexing)
* Raises ``ValueError`` if the value is not present

>>> colors = ['red', 'green', 'blue']
>>> result = colors.index('blue')
>>>
>>> print(result)
2


Count
-----
* ``list.count()`` - number of occurrences of value

>>> colors = ['red', 'green', 'blue', 'red', 'blue', 'red']
>>> result = colors.count('red')
>>>
>>> print(result)
3


Method Chaining
---------------
>>> colors = ['red', 'green', 'blue']
>>> colors.sort()
>>> colors.append('black')
>>>
>>> print(colors)
['blue', 'green', 'red', 'black']

>>> colors = ['red', 'green', 'blue']
>>>
>>> colors.sort().append('black')
Traceback (most recent call last):
AttributeError: 'NoneType' object has no attribute 'append'


Built-in Functions
------------------
* ``min()`` - Minimal value
* ``max()`` - Maximal value
* ``sum()`` - Sum of elements
* ``len()`` - Length of a list
* ``all()`` - All values are ``True``
* ``any()`` - Any values is ``True``

List with numeric values:

>>> data = [3, 1, 2]
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

>>> data = ['a', 'c', 'b']
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

>>> data = [True, False, True]
>>>
>>> any(data)
True
>>> all(data)
False


Memory
------
.. figure:: img/memory-list.png

    Memory representation for ``list``


Shallow Copy vs Deep Copy
-------------------------
* Shallow Copy (by reference) - identifiers are pointing to the same object in memory
* Deep Copy - identifiers are pointing to distinct objects
* Shallow Copy is faster and requires less memory (no duplicated objects)
* Deep Copy is slower and requires twice sa much memory, but is safe for modification

Shallow Copy:

>>> a = ['red', 'green', 'blue']
>>> b = a
>>>
>>> a.append('black')
>>>
>>> a
['red', 'green', 'blue', 'black']
>>> b
['red', 'green', 'blue', 'black']
>>>
>>> id(a)  # doctest: +SKIP
4417433984
>>> id(b)  # doctest: +SKIP
4417433984

Deep Copy:

>>> a = ['red', 'green', 'blue']
>>> b = a.copy()
>>>
>>> a.append('black')
>>>
>>> a
['red', 'green', 'blue', 'black']
>>> b
['red', 'green', 'blue']
>>>
>>> id(first)  # doctest: +SKIP
4391796976
>>> id(second)  # doctest: +SKIP
4391797008


Recap
-----
* Mutable - can add, remove, and modify items
* Stores elements of any type
* Extensible and flexible


References
----------
.. [#timsort] https://en.wikipedia.org/wiki/Timsort

.. [#PyDocList] van Rossum, G. et al. How are lists implemented in CPython? Year: 2022. Retrieved: 2022-09-25. URL: https://docs.python.org/3/faq/design.html#how-are-lists-implemented-in-cpython

.. [#PyDocListSort] van Rossum, G. et al. Why doesn't list.sort() return the sorted list? Year: 2022. Retrieved: 2022-09-25. URL: https://docs.python.org/3/faq/design.html#why-doesn-t-list-sort-return-the-sorted-list



Assignments
-----------
.. literalinclude:: assignments/sequence_list_a.py
    :caption: :download:`Solution <assignments/sequence_list_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_list_b.py
    :caption: :download:`Solution <assignments/sequence_list_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_list_c.py
    :caption: :download:`Solution <assignments/sequence_list_c.py>`
    :end-before: # Solution
