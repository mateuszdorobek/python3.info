Comprehension List
==================


Syntax
------
Short syntax:

>>> [x for x in range(0,5)]
[0, 1, 2, 3, 4]

Long Syntax:

>>> list(x for x in range(0,5))
[0, 1, 2, 3, 4]


Microbenchmark
--------------
>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = []
... for x in range(0,5):
...     result.append(x)
...
457 ns ± 69.4 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = [x for x in range(0,5)]
...
411 ns ± 76.6 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)


Manipulate Numbers
------------------
>>> [x+1 for x in range(0,5)]
[1, 2, 3, 4, 5]
>>>
>>> [x+10 for x in range(0,5)]
[10, 11, 12, 13, 14]

>>> [x*x for x in range(1,5)]
[1, 4, 9, 16]
>>>
>>> [x*(x+1) for x in range(1,5)]
[2, 6, 12, 20]

>>> [x**2 for x in range(0,5)]
[0, 1, 4, 9, 16]
>>>
>>> [x**3 for x in range(0,5)]
[0, 1, 8, 27, 64]
>>>
>>> [2**x for x in range(0,5)]
[1, 2, 4, 8, 16]
>>>
>>> [3**x for x in range(0,5)]
[1, 3, 9, 27, 81]

>>> [1/x for x in range(0,5)]
Traceback (most recent call last):
ZeroDivisionError: division by zero
>>>
>>> [1/x for x in range(1,5)]
[1.0, 0.5, 0.3333333333333333, 0.25]


Manipulate Strings
------------------
>>> DATA = ['a', 'b', 'c']
>>>
>>> ','.join(DATA)
'a,b,c'
>>>
>>> ','.join(x for x in DATA)
'a,b,c'
>>>
>>> ','.join(x.upper() for x in DATA)
'A,B,C'


Type Conversion
---------------
>>> DATA = [1, 2, 3]
>>>
>>> [float(x) for x in DATA]
[1.0, 2.0, 3.0]

Method ``str.join()`` requires all arguments to be strings. If your data
has other types in it, such as ``int`` in the following examples, method
will fail. You can convert those values to string using comprehension.

>>> DATA = [1, 2, 3]
>>>
>>> ','.join(DATA)
Traceback (most recent call last):
TypeError: sequence item 0: expected str instance, int found
>>>
>>> ','.join(str(x) for x in DATA)
'1,2,3'


Slice Sequences
---------------
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> [row for row in DATA]  # doctest: +NORMALIZE_WHITESPACE
[('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
 (5.8, 2.7, 5.1, 1.9, 'virginica'),
 (5.1, 3.5, 1.4, 0.2, 'setosa'),
 (5.7, 2.8, 4.1, 1.3, 'versicolor'),
 (6.3, 2.9, 5.6, 1.8, 'virginica'),
 (6.4, 3.2, 4.5, 1.5, 'versicolor'),
 (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>> [row for row in DATA[1:]]  # doctest: +NORMALIZE_WHITESPACE
[(5.8, 2.7, 5.1, 1.9, 'virginica'),
 (5.1, 3.5, 1.4, 0.2, 'setosa'),
 (5.7, 2.8, 4.1, 1.3, 'versicolor'),
 (6.3, 2.9, 5.6, 1.8, 'virginica'),
 (6.4, 3.2, 4.5, 1.5, 'versicolor'),
 (4.7, 3.2, 1.3, 0.2, 'setosa')]


Slice Data in Sequences
-----------------------
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> [row[-1] for row in DATA[1:]]
['virginica', 'setosa', 'versicolor', 'virginica', 'versicolor', 'setosa']
>>>
>>> [row[0:4] for row in DATA[1:]]  # doctest: +NORMALIZE_WHITESPACE
[(5.8, 2.7, 5.1, 1.9),
 (5.1, 3.5, 1.4, 0.2),
 (5.7, 2.8, 4.1, 1.3),
 (6.3, 2.9, 5.6, 1.8),
 (6.4, 3.2, 4.5, 1.5),
 (4.7, 3.2, 1.3, 0.2)]


Unpack Sequences
----------------
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> [features for *features,label in DATA[1:]]  # doctest: +NORMALIZE_WHITESPACE
[[5.8, 2.7, 5.1, 1.9],
 [5.1, 3.5, 1.4, 0.2],
 [5.7, 2.8, 4.1, 1.3],
 [6.3, 2.9, 5.6, 1.8],
 [6.4, 3.2, 4.5, 1.5],
 [4.7, 3.2, 1.3, 0.2]]
>>>
>>> [X for *X,y in DATA[1:]]  # doctest: +NORMALIZE_WHITESPACE
[[5.8, 2.7, 5.1, 1.9],
 [5.1, 3.5, 1.4, 0.2],
 [5.7, 2.8, 4.1, 1.3],
 [6.3, 2.9, 5.6, 1.8],
 [6.4, 3.2, 4.5, 1.5],
 [4.7, 3.2, 1.3, 0.2]]

>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> [label for *features,label in DATA[1:]]
['virginica', 'setosa', 'versicolor', 'virginica', 'versicolor', 'setosa']
>>>
>>> [y for *X,y in DATA[1:]]
['virginica', 'setosa', 'versicolor', 'virginica', 'versicolor', 'setosa']


Use Case - 0x01
---------------
* Increment

>>> [x+1 for x in range(0,5)]
[1, 2, 3, 4, 5]


Use Case - 0x02
---------------
* Decrement

>>> [x-1 for x in range(0,5)]
[-1, 0, 1, 2, 3]


Use Case - 0x03
---------------
* Sum

>>> sum(x for x in range(0,5))
10


Use Case - 0x04
---------------
* Even or Odd

>>> [x for x in range(0,5)]
[0, 1, 2, 3, 4]

>>> [x%2==0 for x in range(0,5)]
[True, False, True, False, True]


Assignments
-----------
.. literalinclude:: assignments/comprehension_list_a.py
    :caption: :download:`Solution <assignments/comprehension_list_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/comprehension_list_b.py
    :caption: :download:`Solution <assignments/comprehension_list_b.py>`
    :end-before: # Solution
