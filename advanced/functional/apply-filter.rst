Functional Filter
=================
* ``filter(callable, *iterables)``
* Select elements from sequence
* Generator (lazy evaluated)
* required ``callable`` - Function
* required ``iterables`` - 1 or many sequence or iterator objects

The filter function in Python is a built-in function that allows you to
filter out elements from a given iterable based on a specified condition. It
takes two arguments: a function that returns a Boolean value and an iterable
(such as a list, tuple, or set) that you want to filter.

The function is applied to each element in the iterable, and only those
elements for which the function returns True are included in the result. The
filtered elements are returned as an iterator, which can be converted to a
list or other iterable if desired.

Here's an example of using the filter function to filter out even numbers
from a list:

>>> data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>>
>>> def is_odd(n):
...     return n % 2 != 0
>>>
>>> result = filter(is_odd, data)
>>> list(result)
[1, 3, 5, 7, 9]

In this example, the ``is_odd`` function returns ``True`` for odd numbers
and ``False`` for even numbers. The ``filter`` function is used to apply
this function to each element in the ``numbers`` list and return only those
elements for which ``is_odd`` returns ``True``. The resulting list contains
only the odd numbers from the original list.

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
...     {'age': 41, 'username': 'mwatney'},
...     {'age': 40, 'username': 'mlewis'},
...     {'age': 39, 'username': 'rmartinez'},
...     {'age': 40, 'username': 'avogel'},
...     {'age': 29, 'username': 'bjohanssen'},
...     {'age': 36, 'username': 'cbeck'},
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
