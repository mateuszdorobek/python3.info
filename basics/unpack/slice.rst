Unpack Slice
============
* Slice argument must be ``int`` (positive, negative or zero)
* Positive Index starts with ``0``
* Negative index starts with ``-1``


Slice Forwards
--------------
* ``sequence[start:stop]``

>>> data = 'abcde'
>>> data[0:3]
'abc'

>>> data = 'abcde'
>>> data[2:5]
'cde'


Slice Defaults
--------------
* ``sequence[start:stop]``
* ``start`` defaults to ``0``
* ``stop`` defaults to ``len(sequence)``

>>> data = 'abcde'
>>> data[:3]
'abc'

>>> data = 'abcde'
>>> data[3:]
'de'

>>> data = 'abcde'
>>> data[:]
'abcde'


Slice Backwards
---------------
* Negative index starts from the end and go right to left

>>> data = 'abcde'
>>> data[-3:-1]
'cd'

>>> data = 'abcde'
>>> data[-3:]
'cde'

>>> data = 'abcde'
>>> data[0:-3]
'ab'

>>> data = 'abcde'
>>> data[:-3]
'ab'

>>> data = 'abcde'
>>> data[-3:0]
''


Step Forward
------------
* Every ``n``-th element
* ``sequence[start:stop:step]``
* ``start`` defaults to ``0``
* ``stop`` defaults to ``len(sequence)``
* ``step`` defaults to ``1``


>>> data = 'abcde'
>>> data[::1]
'abcde'

>>> data = 'abcde'
>>> data[::2]
'ace'

>>> data = 'abcde'
>>> data[::3]
'ad'

>>> data = 'abcde'
>>> data[1:4:2]
'bd'


Step Backward
-------------
* Every ``n``-th element
* ``sequence[start:stop:step]``
* ``start`` defaults to ``0``
* ``stop`` defaults to ``len(sequence)``
* ``step`` defaults to ``1``

>>> data = 'abcde'
>>> data[::-1]
'edcba'

>>> data = 'abcde'
>>> data[::-2]
'eca'

>>> data = 'abcde'
>>> data[::-3]
'eb'

>>> data = 'abcde'
>>> data[4:1:-2]
'ec'


Slice Errors
------------
>>> data = 'abcde'
>>> data[::0]
Traceback (most recent call last):
ValueError: slice step cannot be zero

>>> data = 'abcde'
>>> data[::1.0]
Traceback (most recent call last):
TypeError: slice indices must be integers or None or have an __index__ method


Out of Range
------------
>>> data = 'abcde'
>>> data[:100]
'abcde'

>>> data = 'abcde'
>>> data[100:]
''


Slice str
---------
>>> data = 'abcde'
>>>
>>>
>>> data[0:3]
'abc'
>>> data[3:5]
'de'
>>> data[:3]
'abc'
>>> data[3:]
'de'
>>> data[::1]
'abcde'
>>> data[::-1]
'edcba'
>>> data[::2]
'ace'
>>> data[::-2]
'eca'
>>> data[1::2]
'bd'
>>> data[1:4:2]
'bd'


Slice tuple
-----------
>>> data = ('a', 'b', 'c', 'd', 'e')
>>>
>>>
>>> data[0:3]
('a', 'b', 'c')
>>> data[3:5]
('d', 'e')
>>> data[:3]
('a', 'b', 'c')
>>> data[3:]
('d', 'e')
>>> data[::2]
('a', 'c', 'e')
>>> data[::-1]
('e', 'd', 'c', 'b', 'a')
>>> data[1::2]
('b', 'd')
>>> data[1:4:2]
('b', 'd')

Slice list
----------
>>> data = ['a', 'b', 'c', 'd', 'e']
>>>
>>>
>>> data[0:3]
['a', 'b', 'c']
>>> data[3:5]
['d', 'e']
>>> data[:3]
['a', 'b', 'c']
>>> data[3:]
['d', 'e']
>>> data[::2]
['a', 'c', 'e']
>>> data[::-1]
['e', 'd', 'c', 'b', 'a']
>>> data[1::2]
['b', 'd']
>>> data[1:4:2]
['b', 'd']


Slice set
---------
Slicing ``set`` is not possible:

>>> data = {'a', 'b', 'c', 'd', 'e'}
>>>
>>> data[:3]
Traceback (most recent call last):
TypeError: 'set' object is not subscriptable


Nested Sequences
----------------
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
>>> DATA[1:]  # doctest: +NORMALIZE_WHITESPACE
[(5.8, 2.7, 5.1, 1.9, 'virginica'),
 (5.1, 3.5, 1.4, 0.2, 'setosa'),
 (5.7, 2.8, 4.1, 1.3, 'versicolor'),
 (6.3, 2.9, 5.6, 1.8, 'virginica'),
 (6.4, 3.2, 4.5, 1.5, 'versicolor'),
 (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>> DATA[-3:]  # doctest: +NORMALIZE_WHITESPACE
[(6.3, 2.9, 5.6, 1.8, 'virginica'),
 (6.4, 3.2, 4.5, 1.5, 'versicolor'),
 (4.7, 3.2, 1.3, 0.2, 'setosa')]


Column Selection
----------------
Column selection unfortunately does not work on ``list``:

>>> data = [[1, 2, 3],
...         [4, 5, 6],
...         [7, 8, 9]]
...
>>> data[:]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>>
>>> data[:, 1]
Traceback (most recent call last):
TypeError: list indices must be integers or slices, not tuple
>>>
>>> data[:][1]
[4, 5, 6]

However this syntax is valid in `numpy` and `pandas`.


Index Arithmetic
----------------
>>> text = 'We choose to go to the Moon!'
>>> first = 23
>>> last = 28
>>> step = 2
>>>
>>> text[first:last]
'Moon!'
>>> text[first:last-1]
'Moon'
>>> text[first:last:step]
'Mo!'
>>> text[first:last-1:step]
'Mo'


Slice Function
--------------
* Every ``n``-th element
* ``sequence[start:stop:step]``
* ``start`` defaults to ``0``
* ``stop`` defaults to ``len(sequence)``
* ``step`` defaults to ``1``

>>> text = 'We choose to go to the Moon!'
>>>
>>> q = slice(23, 27)
>>> text[q]
'Moon'
>>>
>>> q = slice(None, 9)
>>> text[q]
'We choose'
>>>
>>> q = slice(23, None)
>>> text[q]
'Moon!'
>>>
>>> q = slice(23, None, 2)
>>> text[q]
'Mo!'
>>>
>>> q = slice(None, None, 2)
>>> text[q]
'W hoet ot h on'


Use Case - 0x01
---------------
>>> from pprint import pprint
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
>>> pprint(DATA[1:])
[(5.8, 2.7, 5.1, 1.9, 'virginica'),
 (5.1, 3.5, 1.4, 0.2, 'setosa'),
 (5.7, 2.8, 4.1, 1.3, 'versicolor'),
 (6.3, 2.9, 5.6, 1.8, 'virginica'),
 (6.4, 3.2, 4.5, 1.5, 'versicolor'),
 (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>> pprint(DATA[1::2])
[(5.8, 2.7, 5.1, 1.9, 'virginica'),
 (5.7, 2.8, 4.1, 1.3, 'versicolor'),
 (6.4, 3.2, 4.5, 1.5, 'versicolor')]
>>>
>>> pprint(DATA[1::-2])
[(5.8, 2.7, 5.1, 1.9, 'virginica')]
>>>
>>> pprint(DATA[:1:-2])
[(4.7, 3.2, 1.3, 0.2, 'setosa'),
 (6.3, 2.9, 5.6, 1.8, 'virginica'),
 (5.1, 3.5, 1.4, 0.2, 'setosa')]
>>>
>>> pprint(DATA[:-5:-2])
[(4.7, 3.2, 1.3, 0.2, 'setosa'), (6.3, 2.9, 5.6, 1.8, 'virginica')]
>>>
>>> pprint(DATA[1:-5:-2])
[]


Use Case - 0x02
---------------
>>> data = [[1, 2, 3],
...         [4, 5, 6],
...         [7, 8, 9]]
...
>>> data[::2]  # doctest: +NORMALIZE_WHITESPACE
[[1, 2, 3],
 [7, 8, 9]]
>>>
>>> data[::2][1]
[7, 8, 9]
>>>
>>> data[::2][:1]
[[1, 2, 3]]
>>>
>>> data[::2][1][1:]
[8, 9]


Use Case - 0x03
---------------
>>> text = 'We choose to go to the Moon!'
>>> word = 'Moon'
>>>
>>>
>>> start = text.find(word)
>>> stop = start + len(word)
>>>
>>> text[start:stop]
'Moon'
>>>
>>> text[:start]
'We choose to go to the '
>>>
>>> text[stop:]
'!'
>>>
>>> text[:start] + text[stop:]
'We choose to go to the !'


Assignments
-----------
.. literalinclude:: assignments/unpack_slice_a.py
    :caption: :download:`Solution <assignments/unpack_slice_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/unpack_slice_b.py
    :caption: :download:`Solution <assignments/unpack_slice_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/unpack_slice_c.py
    :caption: :download:`Solution <assignments/unpack_slice_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/unpack_slice_d.py
    :caption: :download:`Solution <assignments/unpack_slice_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/unpack_slice_e.py
    :caption: :download:`Solution <assignments/unpack_slice_e.py>`
    :end-before: # Solution
