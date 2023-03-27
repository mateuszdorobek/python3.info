Idiom Map
=========
* Map (convert) elements in sequence
* Generator (lazy evaluated)
* Built-in


Syntax
------
* ``map(callable, *iterables)``
* required ``callable`` - Function
* required ``iterables`` - 1 or many sequence or iterator objects

>>> result = (float(x) for x in range(0,5))
>>> print(list(result))
[0.0, 1.0, 2.0, 3.0, 4.0]

>>> result = map(float, range(0,5))
>>> print(list(result))
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
>>> DATA = [(1,2), (3,4)]
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
>>> import requests
>>>
>>> url = 'https://python.astrotech.io/_static/iris-dirty.csv'
>>>
>>> data = requests.get(url).text
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
>>> # doctest: +SKIP
... import pandas as pd
...
...
... DATA = 'https://python.astrotech.io/_static/phones-pl.csv'
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


Use Case - 0x08
---------------
>>> from functools import reduce
>>> from operator import add
>>>
>>>
>>> def even(x):
...     return x % 2 == 0
>>>
>>> def positive(x):
...     return x > 0
>>>
>>> def non_negative(x):
...     return x >= 0
>>>
>>> def square(x):
...     return x ** 2
>>>
>>> def add1(x):
...     return x + 1
>>>
>>> def minus1(x):
...     return x + 1

>>> data = range(0, 1024)
>>> data = filter(even, data)
>>> data = filter(positive, data)
>>> data = filter(non_negative, data)
>>> data = map(square, data)
>>> data = map(add1, data)
>>> data = map(minus1, data)
>>> result = reduce(add, data)
>>>
>>> result
178434046

>>> filters = [
...     even,
...     positive,
...     non_negative,
... ]
>>>
>>> maps = [
...     square,
...     add1,
...     minus1,
... ]
>>>
>>> def apply(data, fn):
...     return map(fn, data)
>>>
>>>
>>> data = range(0, 1024)
>>> data = reduce(apply, filters, data)
>>> data = reduce(apply, maps, data)
>>> result = reduce(add, data)
>>>
>>> result
3072


Assignments
-----------
.. todo:: Assignments
