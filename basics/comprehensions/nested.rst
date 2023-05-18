Comprehension Nested
====================


Syntax
------
.. code-block:: python

    result = [<RETURN> for <VARIABLE> in <ITERABLE> for <VARIABLE> in <ITERABLE>]

.. code-block:: python

    result = [<RETURN>
              for <VARIABLE> in <ITERABLE>
              for <VARIABLE> in <ITERABLE>]


Example
-------
>>> DATA = {
...     6: ['Doctorate', 'Prof-school'],
...     5: ['Masters', 'Bachelor', 'Engineer'],
...     4: ['HS-grad'],
...     3: ['Junior High'],
...     2: ['Primary School'],
...     1: ['Kindergarten']}
>>>
>>>
>>> result = {}
>>> for lvl, titles in DATA.items():
...     for title in titles:
...         result[title] = lvl
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'Doctorate': 6,
 'Prof-school': 6,
 'Masters': 5,
 'Bachelor': 5,
 'Engineer': 5,
 'HS-grad': 4,
 'Junior High': 3,
 'Primary School': 2,
 'Kindergarten': 1}

>>> DATA = {
...     6: ['Doctorate', 'Prof-school'],
...     5: ['Masters', 'Bachelor', 'Engineer'],
...     4: ['HS-grad'],
...     3: ['Junior High'],
...     2: ['Primary School'],
...     1: ['Kindergarten']}
>>>
>>>
>>> result = {title: lvl
...           for lvl, titles in DATA.items()
...           for title in titles}
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'Doctorate': 6,
 'Prof-school': 6,
 'Masters': 5,
 'Bachelor': 5,
 'Engineer': 5,
 'HS-grad': 4,
 'Junior High': 3,
 'Primary School': 2,
 'Kindergarten': 1}


Microbenchmark
--------------
>>> DATA = {
...     6: ['Doctorate', 'Prof-school'],
...     5: ['Masters', 'Bachelor', 'Engineer'],
...     4: ['HS-grad'],
...     3: ['Junior High'],
...     2: ['Primary School'],
...     1: ['Kindergarten'],
... }

>>> # %%timeit -r 1000 -n 1000
>>> result = {title: lvl
...           for lvl, titles in DATA.items()
...           for title in titles}
>>> # 2.22 µs ± 138 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)

>>> # %%timeit -r 1000 -n 1000
>>> result = {t:l for l,ts in DATA.items() for t in ts}
>>> # 2.22 µs ± 181 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)

>>> # %%timeit -r 1000 -n 1000
>>> result = {}
>>> for lvl, titles in DATA.items():
...     for title in titles:
...         result[title] = lvl
>>> # 2.24 µs ± 152 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)


Nested
------
>>> DATA = [
...     ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
... ]
>>>
>>>
>>> result = '\n'.join(','.join(str(x) for x in row) for row in DATA)
>>>
>>> print(result)
sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor
6.3,2.9,5.6,1.8,virginica
6.4,3.2,4.5,1.5,versicolor
4.7,3.2,1.3,0.2,setosa


Hybrid Solution
---------------
>>> DATA = [
...     ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
... ]
>>>
>>>
>>> data = []
>>>
>>> for row in DATA:
...     line = ','.join(str(x) for x in row)
...     data.append(line)
>>>
>>> result = '\n'.join(data)
>>>
>>> print(result)
sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor
6.3,2.9,5.6,1.8,virginica
6.4,3.2,4.5,1.5,versicolor
4.7,3.2,1.3,0.2,setosa


Code Readability
----------------
>>> # doctest: +SKIP
... result = [user | dict(addresses)
...           for user in json.loads(DATA)
...             for i, address in enumerate(user.pop('addresses'), start=1)
...                 if (columns := [f'{key}{i}' for key in address.keys()])
...                     and (addresses := zip(columns, address.values()))]

>>> # doctest: +SKIP
... result = [user | dict(addresses)
...           for user in json.loads(DATA)
...           for i, address in enumerate(user.pop('addresses'), start=1)
...           if (columns := [f'{key}{i}' for key in address.keys()])
...           and (addresses := zip(columns, address.values()))]


Assignments
-----------
.. literalinclude:: assignments/comprehension_nested_a.py
    :caption: :download:`Solution <assignments/comprehension_nested_a.py>`
    :end-before: # Solution
