Case Study: Unique Keys
=======================


Prepare
-------
Setup code used for all examples:

>>> DATA = [
...     {'sepal_length': 5.1, 'sepal_width': 3.5, 'species': 'setosa'},
...     {'petal_length': 4.1, 'petal_width': 1.3, 'species': 'versicolor'},
...     {'sepal_length': 6.3, 'petal_width': 1.8, 'species': 'virginica'},
...     {'sepal_length': 5.0, 'petal_width': 0.2, 'species': 'setosa'},
...     {'sepal_width': 2.8, 'petal_length': 4.1, 'species': 'versicolor'},
...     {'sepal_width': 2.9, 'petal_width': 1.8, 'species': 'virginica'},
... ]


List Append If
--------------
Append if object not in the list:

>>> #%%timeit -r 1000 -n 10_000
>>> result = []
>>> for row in DATA:
...     for key in row.keys():
...         if key not in result:
...             result.append(key)  # doctest: +SKIP
2.16 µs ± 26.5 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


List Append
-----------
Append to list and deduplicate at the end:

>>> #%%timeit -r 1000 -n 10_000
>>> result = []
>>> for row in DATA:
...     for key in row.keys():
...         result.append(key)
>>> result = set(result)  # doctest: +SKIP
2.5 µs ± 32.9 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


Set Add
-------
>>> ##%%timeit -r 1000 -n 10_000
>>> result = set()
>>> for row in DATA:
...     for key in row.keys():
...         result.add(key)  # doctest: +SKIP
2.12 µs ± 32.4 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)

Set Update
----------
>>> #%%timeit -r 1000 -n 10_000
>>> result = set()
>>> for row in DATA:
...     result.update(row.keys())  # doctest: +SKIP
1.57 µs ± 26.7 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


Set Comprehension
-----------------
>>> #%%timeit -r 1000 -n 10_000
>>> result = set(key
...     for record in DATA
...         for key in record.keys())  # doctest: +SKIP
2.06 µs ± 79.7 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


Set Comprehension Add
---------------------
* Add to Set Comprehension.
* Code appends generator object not values, this is why it is so fast!:

>>> #%%timeit -r 1000 -n 10_000
>>> result = set()
>>> result.add(key
...     for record in DATA
...        for key in record.keys())  # doctest: +SKIP
447 ns ± 9.52 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)

Set Comprehension Update
------------------------
Update Set Comprehension:

>>> #%%timeit -r 1000 -n 10_000
>>> result = set()
>>> result.update(tuple(x.keys()) for x in DATA)  # doctest: +SKIP
2.06 µs ± 45.9 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


Set Comprehension Update
------------------------
>>> #%%timeit -r 1000 -n 10_000
>>> result = set()
>>> for row in DATA:
...     result.update(row)  # doctest: +SKIP


Set Comprehension Update Tuple
------------------------------
>>> #%%timeit -r 1000 -n 10_000
>>> result = set()
>>> for row in DATA:
...     result.update(tuple(row))  # doctest: +SKIP
2.09 µs ± 16.1 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


Set Comprehension Update List
-----------------------------
>>> #%%timeit -r 1000 -n 10_000
>>> result = set()
>>> for row in DATA:
...     result.update(list(row))  # doctest: +SKIP
2.33 µs ± 30.2 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


Set Comprehension Update Set
----------------------------
>>> #%%timeit -r 1000 -n 10_000
>>> result = set()
>>> for row in DATA:
...     result.update(set(row))  # doctest: +SKIP
1.71 µs ± 54 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)
