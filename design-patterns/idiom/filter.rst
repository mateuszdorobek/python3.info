Filter
======
* Select elements from sequence
* Generator (lazy evaluated)
* Built-in

Syntax:

    * ``filter(callable, *iterables)``
    * required ``callable`` - Function
    * required ``iterables`` - 1 or many sequence or iterator objects

>>> def even(x):
...     return x % 2 == 0
>>>
>>> result = (x for x in range(0,5) if even(x))
>>> result = filter(even, range(0,5))

>>> result = (x for x in range(0,5) if x%2==0)
>>> result = filter(lambda x: x%2==0, range(0,5))


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
>>> # %%timeit -r 10 -n 100_000
>>> # result = (x for x in range(0,5) if x%2==0)
>>> # 490 ns ± 44 ns per loop (mean ± std. dev. of 10 runs, 100000 loops each)

>>> # %%timeit -r 10 -n 100_000
>>> # result = filter(lambda x: x%2==0, range(0,5))
>>> # 384 ns ± 34.2 ns per loop (mean ± std. dev. of 10 runs, 100000 loops each)


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
.. literalinclude:: assignments/idioms_filter_a.py
    :caption: :download:`Solution <assignments/idioms_filter_a.py>`
    :end-before: # Solution
