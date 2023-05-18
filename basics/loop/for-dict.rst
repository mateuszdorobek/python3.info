Loop For Dict
=============
* Since Python 3.7: ``dict`` keeps order
* Before Python 3.7: ``dict`` order is not ensured!!


Iterate
-------
* By default ``dict`` iterates over keys
* Suggested variable name: ``key``

>>> DATA = {'sepal_length': 5.1,
...         'sepal_width': 3.5,
...         'petal_length': 1.4,
...         'petal_width': 0.2,
...         'species': 'setosa'}
>>>
>>> for obj in DATA:
...     print(obj)
sepal_length
sepal_width
petal_length
petal_width
species


Iterate Keys
------------
* Suggested variable name: ``key``

>>> DATA = {'sepal_length': 5.1,
...         'sepal_width': 3.5,
...         'petal_length': 1.4,
...         'petal_width': 0.2,
...         'species': 'setosa'}
>>>
>>> list(DATA.keys())
['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
>>>
>>> for obj in DATA.keys():
...     print(obj)
sepal_length
sepal_width
petal_length
petal_width
species


Iterate Values
--------------
* Suggested variable name: ``value``

>>> DATA = {'sepal_length': 5.1,
...         'sepal_width': 3.5,
...         'petal_length': 1.4,
...         'petal_width': 0.2,
...         'species': 'setosa'}
>>>
>>> list(DATA.values())
[5.1, 3.5, 1.4, 0.2, 'setosa']
>>>
>>> for obj in DATA.values():
...     print(obj)
5.1
3.5
1.4
0.2
setosa


Iterate Key-Value Pairs
-----------------------
* Suggested variable name: ``key``, ``value``

Getting pair: ``key``, ``value`` from ``dict`` items:

>>> DATA = {'sepal_length': 5.1,
...         'sepal_width': 3.5,
...         'petal_length': 1.4,
...         'petal_width': 0.2,
...         'species': 'setosa'}
>>>
>>>
>>> list(DATA.items())  # doctest: +NORMALIZE_WHITESPACE
[('sepal_length', 5.1),
 ('sepal_width', 3.5),
 ('petal_length', 1.4),
 ('petal_width', 0.2),
 ('species', 'setosa')]
>>>
>>> for key, value in DATA.items():
...     print(key, '->', value)
sepal_length -> 5.1
sepal_width -> 3.5
petal_length -> 1.4
petal_width -> 0.2
species -> setosa


List of Dicts
-------------
Unpacking ``list`` of ``dict``:

>>> DATA = [
...     {'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2, 'species': 'setosa'},
...     {'sepal_length': 5.7, 'sepal_width': 2.8, 'petal_length': 4.1, 'petal_width': 1.3, 'species': 'versicolor'},
...     {'sepal_length': 6.3, 'sepal_width': 2.9, 'petal_length': 5.6, 'petal_width': 1.8, 'species': 'virginica'},
... ]
>>>
>>> for row in DATA:
...     sepal_length = row['sepal_length']
...     species = row['species']
...     print(f'{species} -> {sepal_length}')
setosa -> 5.1
versicolor -> 5.7
virginica -> 6.3


Generate with Range
-------------------
* ``range()``
* Pythonic way is to use ``zip()``
* Don't use ``len(range(...))`` - it evaluates generator

Create ``dict`` from two ``list``:

>>> header = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
>>> data = [5.1, 3.5, 1.4, 0.2, 'setosa']
>>> result = {}
>>>
>>> for i in range(len(header)):
...     key = header[i]
...     value = data[i]
...     result[key] = value
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.1,
 'sepal_width': 3.5,
 'petal_length': 1.4,
 'petal_width': 0.2,
 'species': 'setosa'}


Generate with Enumerate
-----------------------
* ``enumerate()``
* ``_`` regular variable name (not a special syntax)
* ``_`` by convention is used when variable will not be referenced

Create ``dict`` from two ``list``:

>>> header = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
>>> data = [5.1, 3.5, 1.4, 0.2, 'setosa']
>>> result = {}
>>>
>>> for i, key in enumerate(header):
...     result[key] = data[i]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.1,
 'sepal_width': 3.5,
 'petal_length': 1.4,
 'petal_width': 0.2,
 'species': 'setosa'}


Generate with Zip
-----------------
* ``zip()``
* The most Pythonic way

>>> header = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
>>> data = [5.1, 3.5, 1.4, 0.2, 'setosa']
>>> result = {}
>>>
>>> for key, value in zip(header, data):
...     result[key] = value
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.1,
 'sepal_width': 3.5,
 'petal_length': 1.4,
 'petal_width': 0.2,
 'species': 'setosa'}

>>> header = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
>>> data = [5.1, 3.5, 1.4, 0.2, 'setosa']
>>> result = dict(zip(header, data))
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.1,
 'sepal_width': 3.5,
 'petal_length': 1.4,
 'petal_width': 0.2,
 'species': 'setosa'}


Assignments
-----------
.. literalinclude:: assignments/loop_dict_a.py
    :caption: :download:`Solution <assignments/loop_dict_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_dict_b.py
    :caption: :download:`Solution <assignments/loop_dict_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_dict_c.py
    :caption: :download:`Solution <assignments/loop_dict_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_dict_d.py
    :caption: :download:`Solution <assignments/loop_dict_d.py>`
    :end-before: # Solution
