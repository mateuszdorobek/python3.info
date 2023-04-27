Idiom Enumerate
===============
* Enumerate sequences
* Built-in generator like (lazy evaluated)
* ``enumerate(*iterables)``
* required ``*iterables`` - 1 or many sequences or iterator object
* Return an enumerate object
* The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.


>>> from inspect import isgeneratorfunction, isgenerator
>>>
>>>
>>> isgeneratorfunction(enumerate)
False
>>> result = enumerate(['a', 'b', 'c'])
>>> isgenerator(result)
False


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
.. literalinclude:: assignments/idiom_enumerate_a.py
    :caption: :download:`Solution <assignments/idiom_enumerate_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_enumerate_b.py
    :caption: :download:`Solution <assignments/idiom_enumerate_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_enumerate_c.py
    :caption: :download:`Solution <assignments/idiom_enumerate_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_enumerate_d.py
    :caption: :download:`Solution <assignments/idiom_enumerate_d.py>`
    :end-before: # Solution
