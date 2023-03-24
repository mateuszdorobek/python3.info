Generator Expression
====================
* ``(x for x in range(0,5))``
* Used only once

>>> (x for x in range(0,5))  # doctest: +ELLIPSIS
<generator object <genexpr> at 0x...>


Examples
--------
>>> data = list(x for x in range(0,5))      # list comprehension
>>> data = tuple(x for x in range(0,5))     # tuple comprehension
>>> data = set(x for x in range(0,5))       # set comprehension
>>> data = dict((x,x) for x in range(0,5))  # dict comprehension

>>> data = [x for x in range(0,5)]          # list comprehension
>>> data = (x for x in range(0,5))          # generator expression
>>> data = {x for x in range(0,5)}          # set comprehension
>>> data = {x:x for x in range(0,5)}        # dict comprehension


Why Round Brackets?
-------------------
>>> 1+2 * 3
7
>>>
>>> (1+2) * 3
9

>>> 1
1
>>>
>>> (1)
1

>>> 1, 2
(1, 2)
>>>
>>> (1, 2)
(1, 2)


Lazy vs Greedy
--------------
* Comprehensions executes instantly
* Generator expression executes lazily

>>> data = [x for x in range(0,10)]
>>>
>>> print(data)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> data = (x for x in range(0,10))
>>>
>>> print(data)  # doctest: +ELLIPSIS
<generator object <genexpr> at 0x...>


Generate
--------
>>> result = (x for x in range(0,5))
>>>
>>> next(result)
0
>>> next(result)
1
>>> next(result)
2
>>> next(result)
3
>>> next(result)
4
>>> next(result)
Traceback (most recent call last):
StopIteration


Evaluate
--------
>>> result = (x for x in range(0,5))
>>>
>>> list(result)
[0, 1, 2, 3, 4]

>>> list(x for x in range(0,5))
[0, 1, 2, 3, 4]


Comparison
----------
Comprehension:

>>> data = [x for x in range(0,10)]
>>>
>>> for x in data:  # doctest: +NORMALIZE_WHITESPACE
...     print(x, end=' ')
...     if x == 3:
...         break
0 1 2 3
>>>
>>> for x in data:  # doctest: +NORMALIZE_WHITESPACE
...     print(x, end=' ')
...     if x == 6:
...         break
0 1 2 3 4 5 6
>>>
>>> print(list(data))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> print(list(data))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Generator Expressions:

>>> data = (x for x in range(0,10))
>>>
>>> for x in data:  # doctest: +NORMALIZE_WHITESPACE
...     print(x, end=' ')
...     if x == 3:
...         break
0 1 2 3
>>>
>>> for x in data:  # doctest: +NORMALIZE_WHITESPACE
...     print(x, end=' ')
...     if x == 6:
...         break
4 5 6
>>>
>>> print(list(data))
[7, 8, 9]
>>>
>>> print(list(data))
[]


Use Case - 0x01
---------------
* Comparison

>>> [x for x in range(0,100)]  # doctest: +NORMALIZE_WHITESPACE
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

>>> list(x for x in range(0,100))  # doctest: +NORMALIZE_WHITESPACE
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

>>> (x for x in range(0,100))  # doctest: +ELLIPSIS
<generator object <genexpr> at 0x...>

>>> result = (x for x in range(0,100))
>>>
>>> next(result)
0
>>> next(result)
1
>>> next(result)
2
>>> del result


Use Case - 0x01
---------------
* Sum

>>> sum([1,2,3])
6

>>> sum([x for x in range(0,5)])
10

>>> sum(x for x in range(0,5))
10


.. todo:: Assignments
