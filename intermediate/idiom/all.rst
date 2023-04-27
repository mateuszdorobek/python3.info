Idiom All
=========
* Return True if all elements of the iterable are true (or if the iterable is empty).
* Built-in (evaluated)

>>> DATA = [True, False, True]
>>>
>>> all(DATA)
False


Solution
--------
>>> def all(iterable):
...     if not iterable:
...         return False
...     for element in iterable:
...         if not element:
...             return False
...     return True


Use Case - 0x01
---------------
>>> all(x for x in range(0,5))
False


Use Case - 0x02
---------------
>>> USERS = [
...     {'is_admin': True,  'name': 'Mark Watney'},
...     {'is_admin': True,  'name': 'Melisa Lewis'},
...     {'is_admin': False, 'name': 'Rick Martinez'},
...     {'is_admin': True,  'name': 'Alex Vogel'},
...     {'is_admin': False, 'name': 'Beth Johanssen'},
...     {'is_admin': False, 'name': 'Chris Beck'},
... ]
>>>
>>>
>>> if all(user['is_admin'] for user in USERS):
...     print('Everyone is admin')
... else:
...     print('Not everyone is admin')
Not everyone is admin


Use Case - 0x03
---------------
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
>>> all(value > 1.0
...     for *values, species in DATA[1:]
...     for value in values
...     if isinstance(value, float))
False


Performance
-----------
.. todo:: cleanup

Setup:

>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
... ]

>>> %%timeit -n 1000 -r 1000  # doctest: +SKIP
... result = []
... for row in DATA[1:]:
...     for value in row:
...         if isinstance(value, float):
...             result.append(value >= 1.0)
... result = all(result)
5.24 µs ± 591 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> %%timeit -n 1000 -r 1000  # doctest: +SKIP
... result = True
... for row in DATA[1:]:
...     for value in row:
...         if isinstance(value, float):
...             if not value >= 1.0:
...                 result = False
...                 break
...     if not result:
...         break
1.49 µs ± 596 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> %%timeit -n 1000 -r 1000  # doctest: +SKIP
... result = all(value >= 1.0
...              for row in DATA[1:]
...              for value in row
...              if isinstance(value, float))
1.55 µs ± 436 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> %%timeit -n 1000 -r 1000  # doctest: +SKIP
... result = all(value >= 1.0 for row in DATA[1:] for value in row if isinstance(value, float))
1.51 µs ± 396 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> %%timeit -n 1000 -r 1000  # doctest: +SKIP
... result = all(y >= 1.0 for x in DATA[1:] for y in x if isinstance(y, float))
1.53 µs ± 433 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> %%timeit -n 1000 -r 1000  # doctest: +SKIP
... result = all(x >= 1.0 for X in DATA[1:] for x in X if isinstance(x, float))
1.57 µs ± 437 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
