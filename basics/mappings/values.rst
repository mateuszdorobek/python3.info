Mapping Values
==============
* Value can be any object


Basic Types
-----------
>>> data = {
...     'sepal_length': 5.8,
...     'sepal_width': 2.7,
...     'petal_length': 5.1,
...     'petal_width': 1.9,
... }


Sequence
--------
>>> data = {
...     'virginica': (5.8, 2.7, 5.1, 1.9),
...     'setosa': (5.1, 3.5, 1.4, 0.2),
...     'versicolor': (5.7, 2.8, 4.1, 1.3),
... }

>>> data = {
...     'virginica': [5.8, 2.7, 5.1, 1.9],
...     'setosa': [5.1, 3.5, 1.4, 0.2],
...     'versicolor': [5.7, 2.8, 4.1, 1.3],
... }

>>> data = {
...     'virginica': {5.8, 2.7, 5.1, 1.9},
...     'setosa': {5.1, 3.5, 1.4, 0.2},
...     'versicolor': {5.7, 2.8, 4.1, 1.3},
... }

>>> data = {
...     'virginica': [5.8, 2.7, 5.1, 1.9],
...     'setosa': (5.1, 3.5, 1.4, 0.2),
...     'versicolor': {5.7, 2.8, 4.1, 1.3},
... }


Mapping
-------
>>> data = {
...     'commander': {'firstname': 'Melissa', 'lastname': 'Lewis'},
...     'botanist': {'firstname': 'Mark', 'lastname': 'Watney'},
...     'pilot': {'firstname': 'Rick', 'lastname': 'Martinez'},
... }


Get Values
----------
In Python 2, the methods items(), keys() and values() used to "take a snapshot"
of the dictionary contents and return it as a list. It meant that if the
dictionary changed while you were iterating over the list, the contents in the
list would not change. In Python 3, these methods return a view object whose
contents change dynamically as the dictionary changes. Therefore, in order for
the behavior of iterations over the result of these methods to remain consistent
with previous versions, an additional call to list() has to be performed in
Python 3 to "take a snapshot" of the view object contents. [#Hamidi2017]_

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>>
>>> crew.values()
dict_values(['Melissa Lewis', 'Mark Watney', 'Rick Martinez'])
>>>
>>> list(crew.values())
['Melissa Lewis', 'Mark Watney', 'Rick Martinez']


References
----------
.. [#Hamidi2017] Frédéric Hamidi. Why does Python 3 need dict.items to be wrapped with list()? Retrieved: 2021-02-28. URL: https://stackoverflow.com/a/17695716


.. todo:: Assignments
