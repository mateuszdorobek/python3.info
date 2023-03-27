Idiom Range
===========
* Return sequence of numbers
* It is not a generator
* Generator (lazy evaluated)
* Built-in


Syntax
------
* ``range([start], <stop>, [step])``
* optional ``start``, inclusive, default: ``0``
* required ``stop``, exclusive,
* optional ``step``, default: ``1``


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
.. literalinclude:: assignments/idioms_range_a.py
    :caption: :download:`Solution <assignments/idioms_range_a.py>`
    :end-before: # Solution
