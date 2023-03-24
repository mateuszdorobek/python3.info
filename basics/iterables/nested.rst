Iterable Nested
===============
* Iterable is an object
* Iterable element is an object too
* Therefore an element of a Iterable could be another sequence
* There is no limit how nested it could be

>>> obj = 1
>>>
>>> data = [obj, obj, obj]
>>> data
[1, 1, 1]

>>> obj = [1, 2, 3]
>>>
>>> data = [obj, obj, obj]
>>> data  # doctest: +NORMALIZE_WHITESPACE
[[1, 2, 3],
 [1, 2, 3],
 [1, 2, 3]]


What is an Object?
------------------
* Basic types are objects
* Sequences are objects too
* Everything is an object

>>> int.mro()
[<class 'int'>, <class 'object'>]

>>> float.mro()
[<class 'float'>, <class 'object'>]

>>> bool.mro()
[<class 'bool'>, <class 'int'>, <class 'object'>]

>>> type(None).mro()
[<class 'NoneType'>, <class 'object'>]

>>> tuple.mro()
[<class 'tuple'>, <class 'object'>]

>>> list.mro()
[<class 'list'>, <class 'object'>]

>>> set.mro()
[<class 'set'>, <class 'object'>]


List of Lists
-------------
Also known as multidimensional lists or matrix.

Readability differs depending on whitespaces:

>>> a = [[1,2,3],[4,5,6],[7,8,9]]

>>> b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

>>> c = [[1,2,3], [4,5,6], [7,8,9]]

>>> d = [
...      [1, 2, 3],
...      [4, 5, 6],
...      [7, 8, 9],
... ]

>>> e = [
...      [1, 2, 3],
...      [4, 5, 6],
...      [7, 8, 9]]

>>> f = [[1, 2, 3],
...      [4, 5, 6],
...      [7, 8, 9],
... ]

>>> g = [[1, 2, 3],
...      [4, 5, 6],
...      [7, 8, 9]]


List of Tuples
--------------
Readability differs depending on whitespaces:

>>> data = [(4.7, 3.2, 1.3, 0.2, 'setosa'),
...         (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...         (7.6, 3.0, 6.6, 2.1, 'virginica')]

>>> data = [
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica')]

>>> data = [
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica'),
... ]


Many Types
----------
Readability differs depending on whitespaces:

>>> data = [
...     [1, 2],
...     (3, 4, 5, 6),
...     {7, 8, 9, 10, 11}]

>>> data = [
...     [1, 2],
...     (3, 4, 5, 6),
...     {7, 8, 9, 10, 11}
... ]

>>> data = [[1, 2],
...         (3, 4, 5, 6),
...         {7, 8, 9, 10, 11}]

Content could be both basic types and sequences:

>>> data = [
...     1,
...     1.5,
...     True,
...     None,
...     [1, 2],
...     (3, 4, 5, 6),
...     {7, 8, 9, 10, 11},
... ]


Length
------
>>> data = [[1, 2, 3],
...         [4, 5, 6],
...         [7, 8, 9]]
>>>
>>> len(data)
3
>>> len(data[0])
3

>>> data = [
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica'),
... ]
>>>
>>> len(data)
3
>>> len(data[0])
5

>>> data = [
...     1,
...     1.5,
...     True,
...     None,
...     [1, 2],
...     (3, 4, 5, 6),
...     {7, 8, 9, 10, 11},
... ]
>>>
>>> len(data)
7
>>>
>>> len(data[0])
Traceback (most recent call last):
TypeError: object of type 'int' has no len()
>>>
>>> len(data[1])
Traceback (most recent call last):
TypeError: object of type 'float' has no len()
>>>
>>> len(data[2])
Traceback (most recent call last):
TypeError: object of type 'bool' has no len()
>>>
>>> len(data[3])
Traceback (most recent call last):
TypeError: object of type 'NoneType' has no len()
>>>
>>> len(data[4])
2
>>>
>>> len(data[5])
4
>>>
>>> len(data[6])
5

Append vs Extend
----------------
>>> data = [1,2,3]
>>> data.extend([4,5,6])
>>>
>>> data
[1, 2, 3, 4, 5, 6]

>>> data = [1,2,3]
>>> data.append([4,5,6])
>>>
>>> data
[1, 2, 3, [4, 5, 6]]

Append elements using ``list.append()``:

>>> data = [
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica')]
>>>
>>> row = (4.9, 2.5, 4.5, 1.7, 'virginica')
>>>
>>> data.append(row)
>>> data  # doctest: +NORMALIZE_WHITESPACE
[(4.7, 3.2, 1.3, 0.2, 'setosa'),
 (7.0, 3.2, 4.7, 1.4, 'versicolor'),
 (7.6, 3.0, 6.6, 2.1, 'virginica'),
 (4.9, 2.5, 4.5, 1.7, 'virginica')]

Append elements using ``list.extend()``:

>>> data = [
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica')]
>>>
>>> row = (4.9, 2.5, 4.5, 1.7, 'virginica')
>>>
>>> data.extend(row)
>>> data  # doctest: +NORMALIZE_WHITESPACE
[(4.7, 3.2, 1.3, 0.2, 'setosa'),
 (7.0, 3.2, 4.7, 1.4, 'versicolor'),
 (7.6, 3.0, 6.6, 2.1, 'virginica'),
 4.9,
 2.5,
 4.5,
 1.7,
 'virginica']

Length:

>>> data = [
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica')]
>>>
>>> len(data)
3
>>> len(data[0])
5


Use Case - 0x01
---------------
One dimensional (1D) structure - vector:

>>> from pprint import pprint

>>> obj1 = 1
>>> obj2 = 2
>>> obj3 = 3
>>>
>>> data = [obj1, obj2, obj3]
>>>
>>> pprint(data, width=20)
[1, 2, 3]

Two dimensional (2D) structure - matrix:

>>> obj1 = [1, 2, 3]
>>> obj2 = [4, 5, 6]
>>> obj3 = [7, 8, 9]
>>>
>>> data = [obj1, obj2, obj3]
>>>
>>> pprint(data, width=20)
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

Three dimensional (3D) structure - tensor:

>>> obj1 = [[1,2,3], [4,5,6], [7,8,9]]
>>> obj2 = [[10,20,30], [40,50,60], [70,80,90]]
>>> obj3 = [[100,200,300], [400,500,600], [700,800,900]]
>>>
>>> data = [obj1, obj2, obj3]
>>>
>>> pprint(data, width=20)
[[[1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]],
 [[10, 20, 30],
  [40, 50, 60],
  [70, 80, 90]],
 [[100, 200, 300],
  [400, 500, 600],
  [700, 800, 900]]]


Assignments
-----------
.. literalinclude:: assignments/sequence_nested_a.py
    :caption: :download:`Solution <assignments/sequence_nested_a.py>`
    :end-before: # Solution
