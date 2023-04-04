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
>>> people = [
...     {'age': 21, 'name': 'Pan Twardowski'},
...     {'age': 25, 'name': 'Mark Watney'},
...     {'age': 18, 'name': 'Melissa Lewis'}]
>>>
>>>
>>> def adult(person):
...     return person['age'] >= 21
>>>
>>>
>>> result = filter(adult, people)
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[{'age': 21, 'name': 'Pan Twardowski'},
 {'age': 25, 'name': 'Mark Watney'}]


Use Case - 0x02
---------------
>>> people = [
...     {'is_astronaut': False, 'name': 'Pan Twardowski'},
...     {'is_astronaut': True, 'name': 'Mark Watney'},
...     {'is_astronaut': True, 'name': 'Melissa Lewis'}]
>>>
>>>
>>> def astronaut(person):
...     return person['is_astronaut']
>>>
>>>
>>> result = filter(astronaut, people)
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[{'is_astronaut': True, 'name': 'Mark Watney'},
 {'is_astronaut': True, 'name': 'Melissa Lewis'}]


Use Case - 0x03
---------------
>>> astronauts = ['Mark Watney', 'Melissa Lewis']
>>> people = ['Mark Watney', 'Melissa Lewis', 'Jimenez']
>>>
>>>
>>> def is_astronaut(person):
...     return person in astronauts
>>>
>>>
>>> result = filter(is_astronaut, people)
>>> list(result)
['Mark Watney', 'Melissa Lewis']


Assignments
-----------
.. literalinclude:: assignments/idiom_filter_a.py
    :caption: :download:`Solution <assignments/idiom_filter_a.py>`
    :end-before: # Solution
