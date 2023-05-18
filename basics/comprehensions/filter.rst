Comprehension Filter
====================


Recap
-----
>>> result = []
>>>
>>> for x in range(0,5):
...     if x % 2 == 0:
...         result.append(x)
>>>
>>> print(result)
[0, 2, 4]


Syntax
------
>>> # doctest: +SKIP
... result = [<RETURN> for <VARIABLE> in <ITERABLE> if <CONDITION>]


Example
-------
>>> result = [x for x in range(0,5) if x%2==0]
>>>
>>> print(result)
[0, 2, 4]


Filter list[tuple]
------------------
>>> DATA = [
...     ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
... ]
>>>
>>>
>>> [row for row in DATA[1:] if row[-1] == 'setosa']
[(5.1, 3.5, 1.4, 0.2, 'setosa'), (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>> [features for *features,label in DATA[1:] if label == 'setosa']
[[5.1, 3.5, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]]
>>>
>>> [X for *X,y in DATA[1:] if y == 'setosa']
[[5.1, 3.5, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]]


Filter list[dict]
-----------------
>>> users = [
...     {'is_admin': True,  'name': 'Melissa Lewis'},
...     {'is_admin': True,  'name': 'Mark Watney'},
...     {'is_admin': False, 'name': 'Rick Martinez'},
...     {'is_admin': True,  'name': 'Alex Vogel'},
... ]
>>>
>>>
>>> admins = []
>>>
>>> for user in users:
...     if user['is_admin']:
...         admins.append(user['name'])
>>>
>>> print(admins)
['Melissa Lewis', 'Mark Watney', 'Alex Vogel']

>>> users = [
...     {'is_admin': True,  'name': 'Melissa Lewis'},
...     {'is_admin': True,  'name': 'Mark Watney'},
...     {'is_admin': False, 'name': 'Rick Martinez'},
...     {'is_admin': True,  'name': 'Alex Vogel'},
... ]
>>>
>>>
>>> admins = [user['name']
...           for user in users
...           if user['is_admin']]
>>>
>>> print(admins)
['Melissa Lewis', 'Mark Watney', 'Alex Vogel']


Good Practices
--------------
>>> result = [pow(x, 2) for x in range(0, 5) if x % 2 == 0]

>>> result = [pow(x,2) for x in range(0,5) if x%2==0]

>>> result = [pow(x,2)
...           for x in range(0,5)
...               if x % 2 == 0]

>>> result = [pow(x,2)
...           for x in range(0,5)
...           if x % 2 == 0]


Assignments
-----------
.. literalinclude:: assignments/comprehension_filter_a.py
    :caption: :download:`Solution <assignments/comprehension_filter_a.py>`
    :end-before: # Solution
