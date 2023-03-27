Idiom Range
===========
* Return sequence of numbers
* It is not a generator
* Generator (lazy evaluated)
* ``range([start], <stop>, [step])``
* optional ``start``, inclusive, default: ``0``
* required ``stop``, exclusive,
* optional ``step``, default: ``1``

>>> from inspect import isgeneratorfunction, isgenerator
>>>
>>>
>>> isgeneratorfunction(range)
False
>>>
>>> result = range(0,5)
>>> isgenerator(result)
False


Example
-------
>>> range(0,3)
range(0, 3)

>>> list(range(0,3))
[0, 1, 2]

>>> tuple(range(0,3))
(0, 1, 2)

>>> set(range(0,3))
{0, 1, 2}

>>> list(range(4,11,2))
[4, 6, 8, 10]


Problem
-------
>>> i = 0
>>> result = []
>>>
>>> while i < 3:
...     result.append(i)
...     i += 1
>>>
>>> result
[0, 1, 2]


Solution
--------
>>> result = range(0,3)
>>>
>>> list(result)
[0, 1, 2]


Lazy Evaluation
---------------
>>> for i in range(0,3):
...     print(i)
0
1
2


Itertools
---------
* Learn more at https://docs.python.org/3/library/itertools.html
* More information in `Itertools`
* ``itertools.count(start=0, step=1)``

>>> from itertools import count
>>>
>>>
>>> result = count(3, 2)
>>>
>>> next(result)
3
>>> next(result)
5
>>> next(result)
7


Assignments
-----------
.. literalinclude:: assignments/idiom_range_a.py
    :caption: :download:`Solution <assignments/idiom_range_a.py>`
    :end-before: # Solution
