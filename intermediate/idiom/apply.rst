Idiom Apply
===========

>>> def square(x):
...     return x ** 2
>>>
>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> result = range(0,10)
>>> result = map(square, result)
>>> result = filter(even, result)
>>>
>>> for value in result:
...     print(value)
...     if value > 3:
...         break
0
4
>>>
>>> next(result)
16
>>>
>>> list(result)
[36, 64]


Assignments
-----------
.. literalinclude:: assignments/idiom_apply_a.py
    :caption: :download:`Solution <assignments/idiom_apply_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_apply_b.py
    :caption: :download:`Solution <assignments/idiom_apply_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_apply_c.py
    :caption: :download:`Solution <assignments/idiom_apply_c.py>`
    :end-before: # Solution
