Mapping Generate
================


Recap
-----
Pair:

>>> data = ('commander', 'Melissa Lewis')

List of pairs:

>>> data = [
...     ('commander', 'Melissa Lewis'),
...     ('botanist', 'Mark Watney'),
...     ('pilot', 'Rick Martinez'),
... ]


List of Pairs
-------------
>>> data = [
...     ('commander', 'Melissa Lewis'),
...     ('botanist', 'Mark Watney'),
...     ('pilot', 'Rick Martinez')
... ]
>>>
>>> dict(data)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
  'botanist': 'Mark Watney',
  'pilot': 'Rick Martinez'}


Enumerate
---------
SetUp:

>>> crew = ['Melissa Lewis', 'Mark Watney', 'Rick Martinez']

Function ``enumerate`` will create a list of pairs:

>>> result = enumerate(crew)
>>>
>>> next(result)
(0, 'Melissa Lewis')
>>>
>>> next(result)
(1, 'Mark Watney')
>>>
>>> next(result)
(2, 'Rick Martinez')
>>>
>>> next(result)
Traceback (most recent call last):
StopIteration

Evaluate enumerate object to list instantly:

>>> list(enumerate(crew))  # doctest: +NORMALIZE_WHITESPACE
[(0, 'Melissa Lewis'),
 (1, 'Mark Watney'),
 (2, 'Rick Martinez')]

Evaluate enumerate object to dict instantly:

>>> dict(enumerate(crew))  # doctest: +NORMALIZE_WHITESPACE
{0: 'Melissa Lewis',
 1: 'Mark Watney',
 2: 'Rick Martinez'}


Zip
---
SetUp:

>>> roles = ['commander', 'botanist', 'pilot']
>>> crew = ['Melissa Lewis', 'Mark Watney', 'Rick Martinez']

Function ``zip`` will create a list of pairs:

>>> result = zip(roles, crew)
>>>
>>> next(result)
('commander', 'Melissa Lewis')
>>>
>>> next(result)
('botanist', 'Mark Watney')
>>>
>>> next(result)
('pilot', 'Rick Martinez')
>>>
>>> next(result)
Traceback (most recent call last):
StopIteration

Evaluate zip object to list instantly:

>>> list(zip(roles, crew))  # doctest: +NORMALIZE_WHITESPACE
[('commander', 'Melissa Lewis'),
 ('botanist', 'Mark Watney'),
 ('pilot', 'Rick Martinez')]

Evaluate zip object to dict instantly:

>>> dict(zip(roles, crew))  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'pilot': 'Rick Martinez'}


Use Case - 0x01
---------------
>>> months = ['January', 'February', 'March', 'April']
>>>
>>>
>>> dict(enumerate(months))
{0: 'January', 1: 'February', 2: 'March', 3: 'April'}
>>>
>>> dict(enumerate(months, start=1))
{1: 'January', 2: 'February', 3: 'March', 4: 'April'}


Use Case - 0x02
---------------
>>> DATA = """10, 4, virginica, setosa, versicolor
... 5.8, 2.7, 5.1, 1.9, 0
... 5.1, 3.5, 1.4, 0.2, 1
... 5.7, 2.8, 4.1, 1.3, 2
... 6.3, 2.9, 5.6, 1.8, 0
... 6.4, 3.2, 4.5, 1.5, 2
... 4.7, 3.2, 1.3, 0.2, 1
... 7.0, 3.2, 4.7, 1.4, 2
... 7.6, 3.0, 6.6, 2.1, 0
... 4.9, 3.0, 1.4, 0.2, 1
... 4.9, 2.5, 4.5, 1.7, 0"""

>>> header, *rows = DATA.splitlines()
>>> nrows, nfeatures, *class_labels = header.split(', ')
>>> label_encoder = dict(enumerate(class_labels))

>>> nrows
'10'
>>>
>>> nfeatures
'4'
>>>
>>> class_labels
['virginica', 'setosa', 'versicolor']
>>>
>>> label_encoder
{0: 'virginica', 1: 'setosa', 2: 'versicolor'}

>>> label_encoder[0]
'virginica'
>>>
>>> label_encoder[1]
'setosa'
>>>
>>> label_encoder[2]
'versicolor'


Use Case - 0x03
---------------
SetUp:

>>> roles = ['commander', 'botanist', 'pilot']
>>> crew = [('Melissa', 'Lewis'), ('Mark', 'Watney'), ('Rick', 'Martinez')]

>>> result = zip(roles, crew)
>>>
>>> next(result)
('commander', ('Melissa', 'Lewis'))
>>>
>>> next(result)
('botanist', ('Mark', 'Watney'))
>>>
>>> next(result)
('pilot', ('Rick', 'Martinez'))
>>>
>>> next(result)
Traceback (most recent call last):
StopIteration

Evaluate zip object to list instantly:

>>> list(zip(roles, crew))  # doctest: +NORMALIZE_WHITESPACE
[('commander', ('Melissa', 'Lewis')),
 ('botanist', ('Mark', 'Watney')),
 ('pilot', ('Rick', 'Martinez'))]

Evaluate zip object to dict instantly:

>>> dict(zip(roles, crew))  # doctest: +NORMALIZE_WHITESPACE
{'commander': ('Melissa', 'Lewis'),
 'botanist': ('Mark', 'Watney'),
 'pilot': ('Rick', 'Martinez')}


Assignments
-----------
.. literalinclude:: assignments/mapping_generate_a.py
    :caption: :download:`Solution <assignments/mapping_generate_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/mapping_generate_b.py
    :caption: :download:`Solution <assignments/mapping_generate_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/mapping_generate_c.py
    :caption: :download:`Solution <assignments/mapping_generate_c.py>`
    :end-before: # Solution
