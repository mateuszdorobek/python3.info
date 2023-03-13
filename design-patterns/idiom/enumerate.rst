Enumerate
=========
* Enumerate sequences
* Generator (lazy evaluated)
* Built-in


Syntax
------
* ``enumerate(*iterables)``
* required ``*iterables`` - 1 or many sequences or iterator object


Problem
-------
>>> months = ['January', 'February', 'March']
>>> result = []
>>>
>>> i = 0
>>>
>>> for month in months:
...     result.append((i, month))
...     i += 1
>>>
>>> result
[(0, 'January'), (1, 'February'), (2, 'March')]


Solution
--------
>>> months = ['January', 'February', 'March']
>>> result = enumerate(months)
>>>
>>> list(result)
[(0, 'January'), (1, 'February'), (2, 'March')]


Lazy Evaluation
---------------
>>> months = ['January', 'February', 'March']
>>> result = enumerate(months)
>>>
>>> next(result)
(0, 'January')
>>> next(result)
(1, 'February')
>>> next(result)
(2, 'March')
>>> next(result)
Traceback (most recent call last):
StopIteration


Dict Conversion
---------------
>>> months = ['January', 'February', 'March']
>>> result = enumerate(months)
>>>
>>> dict(result)
{0: 'January', 1: 'February', 2: 'March'}

>>> months = ['January', 'February', 'March']
>>> result = enumerate(months, start=1)
>>>
>>> dict(result)
{1: 'January', 2: 'February', 3: 'March'}

>>> months = ['January', 'February', 'March']
>>> result = {f'{i:02}':month for i,month in enumerate(months, start=1)}
>>>
>>> print(result)
{'01': 'January', '02': 'February', '03': 'March'}


Using in a Loop
---------------
>>> months = ['January', 'February', 'March']
>>>
>>> for i, month in enumerate(months, start=1):
...     print(f'{i} -> {month}')
1 -> January
2 -> February
3 -> March


Assignments
-----------
.. todo:: Assignments
