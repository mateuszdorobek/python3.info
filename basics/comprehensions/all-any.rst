Comprehension All, Any
======================


Any
---
>>> any(x for x in range(0,5))
True

>>> users = [{'is_admin': False, 'name': 'Mark Watney'},
...          {'is_admin': True,  'name': 'Melissa Lewis'},
...          {'is_admin': False, 'name': 'Rick Martinez'},
...          {'is_admin': False, 'name': 'Alex Vogel'},
...          {'is_admin': True,  'name': 'Beth Johanssen'},
...          {'is_admin': False, 'name': 'Chris Beck'}]
>>>
>>>
>>> if any(user['is_admin'] for user in users):
...     print('At least one user is admin')
... else:
...     print('There are no admins')
At least one user is admin


All
---
>>> all(x for x in range(0,5))
False

>>> users = [{'is_admin': False, 'name': 'Mark Watney'},
...          {'is_admin': True,  'name': 'Melissa Lewis'},
...          {'is_admin': False, 'name': 'Rick Martinez'},
...          {'is_admin': False, 'name': 'Alex Vogel'},
...          {'is_admin': True,  'name': 'Beth Johanssen'},
...          {'is_admin': False, 'name': 'Chris Beck'}]
>>>
>>>
>>> if all(user['is_admin'] for user in users):
...     print('Everyone has admin permissions')
... else:
...     print('Not everyone is admin')
Not everyone is admin

>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor')]
>>>
>>>
>>> all(observation > 1.0
...     for *features, label in DATA[1:]
...     for observation in features
...     if isinstance(observation, float))
False



.. todo:: Assignments
