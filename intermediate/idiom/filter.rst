Idiom Filter
============
* ``filter(callable, *iterables)``
* Select elements from sequence
* Generator (lazy evaluated)
* required ``callable`` - Function
* required ``iterables`` - 1 or many sequence or iterator objects

>>> def even(x):
...     return x % 2 == 0
>>>
>>> result = (x for x in range(0,5) if even(x))
>>> result = filter(even, range(0,5))


Not-a-Generator
---------------
>>> from inspect import isgeneratorfunction, isgenerator
>>>
>>>
>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> isgeneratorfunction(filter)
False
>>>
>>> result = filter(even, [1,2,3])
>>> isgenerator(result)
False


Problem
-------
Plain code:

>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> DATA = [1, 2, 3, 4, 5, 6]
>>> result = []
>>>
>>> for x in DATA:
...     if even(x):
...         result.append(x)
>>>
>>> print(result)
[2, 4, 6]

Comprehension:

>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> DATA = [1, 2, 3, 4, 5, 6]
>>> result = [x for x in DATA if even(x)]
>>>
>>> print(result)
[2, 4, 6]


Solution
--------
>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> DATA = [1, 2, 3, 4, 5, 6]
>>> result = filter(even, DATA)
>>>
>>> list(result)
[2, 4, 6]


Lazy Evaluation
---------------
>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> DATA = [1, 2, 3, 4, 5, 6]
>>> result = filter(even, DATA)
>>>
>>> next(result)
2
>>> next(result)
4
>>> next(result)
6
>>> next(result)
Traceback (most recent call last):
StopIteration


Performance
-----------
>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> data = [1, 2, 3, 4, 5, 6]

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = [x for x in data if even(x)]
1.11 µs ± 139 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = list(filter(even, data))
921 ns ± 112 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)


Use Case - 0x01
---------------
>>> users = [
...     {'age': 41, 'username': 'mwatney'},
...     {'age': 40, 'username': 'mlewis'},
...     {'age': 39, 'username': 'rmartinez'},
...     {'age': 40, 'username': 'avogel'},
...     {'age': 29, 'username': 'bjohanssen'},
...     {'age': 36, 'username': 'cbeck'},
... ]

>>> def above40(user):
...     return user['age'] >= 40
>>>
>>> def under40(user):
...     return user['age'] < 40

>>> result = filter(above40, users)
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[{'age': 41, 'username': 'mwatney'},
 {'age': 40, 'username': 'mlewis'},
 {'age': 40, 'username': 'avogel'}]

>>> result = filter(under40, users)
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[{'age': 39, 'username': 'rmartinez'},
 {'age': 29, 'username': 'bjohanssen'},
 {'age': 36, 'username': 'cbeck'}]


Use Case - 0x02
---------------
>>> users = [
...     {'is_admin': False, 'name': 'Mark Watney'},
...     {'is_admin': True,  'name': 'Melissa Lewis'},
...     {'is_admin': False, 'name': 'Rick Martinez'},
...     {'is_admin': False, 'name': 'Alex Vogel'},
...     {'is_admin': True,  'name': 'Beth Johanssen'},
...     {'is_admin': False, 'name': 'Chris Beck'},
... ]
>>>
>>>
>>> def admin(user):
...     return user['is_admin'] is True
>>>
>>>
>>> result = filter(admin, users)
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[{'is_admin': True, 'name': 'Melissa Lewis'},
 {'is_admin': True, 'name': 'Beth Johanssen'}]


Use Case - 0x03
---------------
>>> users = [
...     'mwatney',
...     'mlewis',
...     'rmartinez',
...     'avogel',
...     'bjohanssen',
...     'cbeck',
... ]
>>>
>>> admins = [
...     'mlewis',
...     'bjohanssen',
... ]
>>>
>>>
>>> def is_admin(user):
...     return user in admins
>>>
>>>
>>> result = filter(is_admin, users)
>>> list(result)
['mlewis', 'bjohanssen']


Use Case - 0x04
---------------
>>> class User:
...     firstname: str
...     lastname: str
...     groups: list[str]
...
...     def __init__(self, firstname, lastname, groups):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.groups = groups
...
...     def __repr__(self):
...         return f'{self.firstname}'
...
>>> DATABASE = [
...     User('Mark', 'Watney', groups=['user', 'staff']),
...     User('Melissa', 'Lewis', groups=['user', 'staff', 'admin']),
...     User('Rick', 'Martinez', groups=['user', 'staff']),
...     User('Alex', 'Vogel', groups=['user']),
...     User('Beth', 'Johanssen', groups=['user', 'staff', 'admin']),
...     User('Chris', 'Beck', groups=['user', 'staff']),
... ]

>>> def is_user(user: User) -> bool:
...     return 'user' in user.groups
>>>
>>> def is_staff(user: User) -> bool:
...     return 'staff' in user.groups
>>>
>>> def is_admin(user: User) -> bool:
...     return 'admin' in user.groups

>>> users = filter(is_user, DATABASE)
>>> staff = filter(is_staff, DATABASE)
>>> admins = filter(is_admin, DATABASE)

>>> list(users)
[Mark, Melissa, Rick, Alex, Beth, Chris]
>>>
>>> list(staff)
[Mark, Melissa, Rick, Beth, Chris]
>>>
>>> list(admins)
[Melissa, Beth]


Assignments
-----------
.. literalinclude:: assignments/idiom_filter_a.py
    :caption: :download:`Solution <assignments/idiom_filter_a.py>`
    :end-before: # Solution
