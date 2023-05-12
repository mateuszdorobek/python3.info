Functional Filter
=================
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
>>>
>>> result = (x for x in range(0,5) if x%2==0)
>>> result = filter(lambda x: x%2==0, range(0,5))


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
...     {'age': 41,  'username': 'mwatney'},
...     {'age': 40,  'username': 'mlewis'},
...     {'age': 39,  'username': 'rmartinez'},
...     {'age': 40, 'username': 'avogel'},
...     {'age': 29,  'username': 'bjohanssen'},
...     {'age': 36,  'username': 'cbeck'},
... ]

>>> def above40(person):
...     return person['age'] >= 40
>>>
>>> def under40(person):
...     return person['age'] < 40

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
...     {'is_staff': True,  'username': 'mwatney'},
...     {'is_staff': True,  'username': 'mlewis'},
...     {'is_staff': True,  'username': 'rmartinez'},
...     {'is_staff': False, 'username': 'avogel'},
...     {'is_staff': True,  'username': 'bjohanssen'},
...     {'is_staff': True,  'username': 'cbeck'},
... ]
>>>
>>>
>>> def can_login(user):
...     return user['is_staff']
>>>
>>>
>>> staff = filter(can_login, users)
>>> list(staff)  # doctest: +NORMALIZE_WHITESPACE
[{'is_staff': True, 'username': 'mwatney'},
 {'is_staff': True, 'username': 'mlewis'},
 {'is_staff': True, 'username': 'rmartinez'},
 {'is_staff': True, 'username': 'bjohanssen'},
 {'is_staff': True, 'username': 'cbeck'}]


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
>>> staff = [
...     'mwatney',
...     'mlewis',
...     'ptwardowski',
...     'jjimenez',
... ]
>>>
>>>
>>> def can_login(user):
...     return user in staff
>>>
>>>
>>> result = filter(can_login, users)
>>> list(result)
['mwatney', 'mlewis']


Assignments
-----------
.. literalinclude:: assignments/idiom_applyfilter_a.py
    :caption: :download:`Solution <assignments/idiom_applyfilter_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_applyfilter_a.py
    :caption: :download:`Solution <assignments/idiom_applyfilter_a.py>`
    :end-before: # Solution
