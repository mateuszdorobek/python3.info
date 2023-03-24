Comprehension Set
=================


Syntax
------
Short Syntax:

>>> {x+10 for x in range(0, 5)}
{10, 11, 12, 13, 14}

Long Syntax:

>>> set(x+10 for x in range(0, 5))
{10, 11, 12, 13, 14}


Use Case - 0x01
---------------
* Unique

>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor')]

>>> result = {row[-1] for row in DATA[1:]}
>>>
>>> sorted(result)
['setosa', 'versicolor', 'virginica']
>>>
>>> dict(enumerate(sorted(result)))
{0: 'setosa', 1: 'versicolor', 2: 'virginica'}


Use Case - 0x02
---------------
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]

>>> result = {y for *X,y in DATA[1:]}
>>>
>>> sorted(result)
['setosa', 'versicolor', 'virginica']
>>>
>>> result = dict(enumerate(sorted(result)))
>>> result
{0: 'setosa', 1: 'versicolor', 2: 'virginica'}

.. todo:: Assignments
