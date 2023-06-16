Functional Map
==============
* Map (convert) elements in sequence
* Generator (lazy evaluated)
* ``map(callable, *iterables)``
* required ``callable`` - Function
* required ``iterables`` - 1 or many sequence or iterator objects

The ``map()`` function in Python is a built-in function that applies a given
function to each element of an iterable (such as a list, tuple, or set) and
returns a new iterable with the results. It takes two arguments: a function
and an iterable.

The function is applied to each element in the iterable, and the results
are collected into a new iterable. The resulting iterable can be converted
to a list, tuple, or set if desired.

Here's an example of using the ``map()`` function to square each number
in a list:

>>> data = [1, 2, 3, 4, 5]
>>>
>>> def square(n):
...     return n ** 2
>>>
>>> result = map(square, data)
>>> list(result)
[1, 4, 9, 16, 25]

In this example, the ``square`` function is applied to each element in the
``numbers`` list using the ``map()`` function. The resulting iterable contains
the squared values of each element in the original list. The ``list()``
function is used to convert the iterable to a list.

>>> from inspect import isgeneratorfunction, isgenerator
>>>
>>>
>>> isgeneratorfunction(map)
False
>>>
>>> result = map(float, [1,2,3])
>>> isgenerator(result)
False


Example
-------
>>> result = (float(x) for x in range(0,5))
>>>
>>> list(result)
[0.0, 1.0, 2.0, 3.0, 4.0]

>>> result = map(float, range(0,5))
>>>
>>> list(result)
[0.0, 1.0, 2.0, 3.0, 4.0]


Problem
-------
>>> data = [1, 2, 3]
>>> result = []
>>>
>>> for x in data:
...     result.append(float(x))
>>>
>>> print(result)
[1.0, 2.0, 3.0]


Solution
--------
>>> data = [1, 2, 3]
>>> result = map(float, data)
>>>
>>> list(result)
[1.0, 2.0, 3.0]


Lazy Evaluation
---------------
>>> data = [1, 2, 3]
>>> result = map(float, data)
>>>
>>> next(result)
1.0
>>> next(result)
2.0
>>> next(result)
3.0
>>> next(result)
Traceback (most recent call last):
StopIteration


Multi Parameters
----------------
>>> def myfunc(x):
...     return sum(x)
>>>
>>>
>>> DATA = [
...     (1,2),
...     (3,4),
... ]
>>>
>>> result = map(myfunc, DATA)
>>> print(list(result))
[3, 7]


Starmap
-------
>>> from itertools import starmap
>>>
>>>
>>> DATA = [
...     (3.1415, 3),
...     (2.71828, 2)]
>>>
>>> result = starmap(round, DATA)  # round(number=3.1415, ndigits=2)
>>> print(list(result))
[3.142, 2.72]


Partial
-------
>>> from functools import partial
>>>
>>>
>>> myround = partial(round, ndigits=1)
>>> DATA = [1.111, 2.222, 3.333]
>>>
>>> result = map(myround, DATA)  # round(number=1.111, ndigits=1)
>>> print(list(result))
[1.1, 2.2, 3.3]


Performance
-----------
>>> def even(x):
...     return x % 2 == 0

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = [float(x) for x in data if even(x)]
1.9 µs ± 206 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = list(map(float, filter(parzysta, data)))
1.66 µs ± 175 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)



Use Case - 0x01
---------------
Built-in functions:

>>> DATA = [1, 2, 3]
>>> result = map(float, DATA)
>>>
>>> tuple(map(float, DATA))
(1.0, 2.0, 3.0)

>>> DATA = [1, 2, 3]
>>> result = map(float, DATA)
>>>
>>> set(map(float, DATA))
{1.0, 2.0, 3.0}

>>> DATA = [1, 2, 3]
>>> result = (float(x) for x in DATA)
>>>
>>> list(result)
[1.0, 2.0, 3.0]

>>> DATA = [1.1, 2.2, 3.3]
>>> result = map(round, DATA)
>>>
>>> list(result)
[1, 2, 3]


Use Case - 0x02
---------------
>>> def square(x):
...     return x ** 2
>>>
>>>
>>> DATA = [1, 2, 3]
>>> result = map(square, DATA)
>>>
>>> list(result)
[1, 4, 9]


Use Case - 0x03
---------------
>>> def increment(x):
...     return x + 1
>>>
>>>
>>> DATA = [1, 2, 3, 4]
>>> result = map(increment, DATA)
>>>
>>> list(result)
[2, 3, 4, 5]


Use Case - 0x04
---------------
>>> def translate(letter):
...     return PL.get(letter, letter)
>>>
>>>
>>> DATA = 'zażółć gęślą jaźń'
>>> PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
...       'ł': 'l', 'ń': 'n', 'ó': 'o',
...       'ś': 's', 'ż': 'z', 'ź': 'z'}
>>>
>>> result = map(translate, DATA)
>>> ''.join(result)
'zazolc gesla jazn'


Use Case - 0x05
---------------
Standard input:

>>> import sys
>>>
>>> # doctest: +SKIP
... print(sum(map(int, sys.stdin)))

.. code-block:: console

    $ cat ~/.profile |grep addnum
    alias addnum='python -c"import sys; print(sum(map(int, sys.stdin)))"'


Use Case - 0x06
---------------
>>> import httpx
>>>
>>> url = 'https://python3.info/_static/iris-dirty.csv'
>>>
>>> data = httpx.get(url).text
>>> header, *rows = data.splitlines()
>>> nrows, nfeatures, *class_labels = header.strip().split(',')
>>> label_encoder = dict(enumerate(class_labels))

>>> result = []
>>> for row in rows:
...     *features, species = row.strip().split(',')
...     features = map(float, features)
...     species = label_encoder[int(species)]
...     row = tuple(features) + (species,)
...     result.append(row)

>>> def decode(row):
...     *features, species = row.strip().split(',')
...     features = map(float, features)
...     species = label_encoder[int(species)]
...     return tuple(features) + (species,)
>>>
>>> result = map(decode, rows)

>>> def decode(row):
...     *features, species = row.strip().split(',')
...     features = map(float, features)
...     species = label_encoder[int(species)]
...     return tuple(features) + (species,)
>>>
>>> with open('/tmp/myfile.csv') as file:  # doctest: +SKIP
...     header = file.readline()
...     for line in map(decode, file):
...         print(line)


Use Case - 0x07
---------------
SetUp:

>>> from doctest import testmod as run_tests

Data [#ghSklearnIris]_:

>>> DATA = """150,4,setosa,versicolor,virginica
... 5.1,3.5,1.4,0.2,0
... 7.0,3.2,4.7,1.4,1
... 6.3,3.3,6.0,2.5,2
... 4.9,3.0,1.4,0.2,0
... 6.4,3.2,4.5,1.5,1
... 5.8,2.7,5.1,1.9,2"""

Definition:

>>> def get_labelencoder(header: str) -> dict[int, str]:
...     """
...     >>> get_labelencoder('150,4,setosa,versicolor,virginica')
...     {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
...     """
...     nrows, nfeatures, *class_labels = header.split(',')
...     return dict(enumerate(class_labels))
>>>
>>> run_tests()  # doctest: +SKIP
TestResults(failed=0, attempted=1)

>>> def get_data(line: str) -> tuple:
...     """
...     >>> convert('5.1,3.5,1.4,0.2,0')
...     (5.1, 3.5, 1.4, 0.2, 'setosa')
...     >>> convert('7.0,3.2,4.7,1.4,1')
...     (7.0, 3.2, 4.7, 1.4, 'versicolor')
...     >>> convert('6.3,3.3,6.0,2.5,2')
...     (6.3, 3.3, 6.0, 2.5, 'virginica')
...     """
...     *values, species = line.split(',')
...     values = map(float, values)
...     species = label_encoder[int(species)]
...     return tuple(values) + (species,)
>>>
>>> run_tests()  # doctest: +SKIP
TestResults(failed=0, attempted=3)

>>> header, *lines = DATA.splitlines()
>>> label_encoder = get_labelencoder(header)
>>> result = map(get_data, lines)

>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[(5.1, 3.5, 1.4, 0.2, 'setosa'),
 (7.0, 3.2, 4.7, 1.4, 'versicolor'),
 (6.3, 3.3, 6.0, 2.5, 'virginica'),
 (4.9, 3.0, 1.4, 0.2, 'setosa'),
 (6.4, 3.2, 4.5, 1.5, 'versicolor'),
 (5.8, 2.7, 5.1, 1.9, 'virginica')]


Use Case - 0x08
---------------
>>> # doctest: +SKIP
... import pandas as pd
...
...
... DATA = 'https://python3.info/_static/phones-pl.csv'
...
... result = (
...     pd
...     .read_csv(DATA, parse_dates=['datetime'])
...     .set_index('datetime', drop=True)
...     .drop(columns=['id'])
...     .loc['2000-01-01':'2000-03-01']
...     .query('item == "sms"')
...     .groupby(['period','item'])
...     .agg(
...         duration_count = ('duration', 'count'),
...         duration_sum = ('duration', 'sum'),
...         duration_median = ('duration', 'median'),
...         duration_mean = ('duration', 'mean'),
...         duration_std = ('duration', 'std'),
...         duration_var = ('duration', 'var'),
...         value = ('duration', lambda column: column.mean().astype(int))
...     )
... )


References
----------
.. [#ghSklearnIris] Scikit-learn Contributors. Iris Dataset. Year: 2022. Retrieved: 2022-12-19. URL:  https://raw.githubusercontent.com/scikit-learn/scikit-learn/main/sklearn/datasets/data/iris.csv


Assignments
-----------
.. literalinclude:: assignments/idiom_applymap_a.py
    :caption: :download:`Solution <assignments/idiom_applymap_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_applymap_b.py
    :caption: :download:`Solution <assignments/idiom_applymap_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_applymap_c.py
    :caption: :download:`Solution <assignments/idiom_applymap_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_applymap_d.py
    :caption: :download:`Solution <assignments/idiom_applymap_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_applymap_e.py
    :caption: :download:`Solution <assignments/idiom_applymap_e.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_applymap_f.py
    :caption: :download:`Solution <assignments/idiom_applymap_f.py>`
    :end-before: # Solution
