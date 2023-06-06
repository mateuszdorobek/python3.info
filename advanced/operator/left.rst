Operator Left
=============
* ``x + y`` - will call method "add" on object ``x`` (``x.__add__(y)``)
* ``x - y`` - will call method "sub" on object ``x`` (``x.__sub__(y)``)
* ``x * y`` - will call method "mul" on object ``x`` (``x.__mul__(y)``)
* ``x ** y`` - will call method "pow" on object ``x`` (``x.__pow__(y)``)
* ``x @ y`` - will call method "matmul" on object ``x`` (``x.__matmul__(y)``)
* ``x / y`` - will call method "truediv" on object ``x`` (``x.__truediv__(y)``)
* ``x // y`` - will call method "floordiv" on object ``x`` (``x.__floordiv__(y)``)
* ``x % y`` - will call method "mod" on object ``x`` (``x.__mod__(y)``)

.. csv-table:: Numerical Operator Overload
    :header: "Operator", "Method"

    "``obj + other``",     "``obj.__add__(other)``"
    "``obj - other``",     "``obj.__sub__(other)``"
    "``obj * other``",     "``obj.__mul__(other)``"
    "``obj ** other``",    "``obj.__pow__(other)``"
    "``obj @ other``",     "``obj.__matmul__(other)``"
    "``obj / other``",     "``obj.__truediv__(other)``"
    "``obj // other``",    "``obj.__floordiv__(other)``"
    "``obj % other``",     "``obj.__mod__(other)``"


Memory
------
* ``tuple`` is immutable
* ``list`` is mutable
* ``tuple + tuple`` will generate new ``tuple``
* ``list + list`` will generate new ``list``
* ``__add__()`` operator on ``tuple`` is the same as on ``list``

>>> a = [1, 2, 3]
>>> id(a)  # doctest: +SKIP
4354839104
>>>
>>> a = a + [4, 5, 6]
>>> id(a)  # doctest: +SKIP
4358229056
>>>
>>> a
[1, 2, 3, 4, 5, 6]

>>> a = (1, 2, 3)
>>> id(a)  # doctest: +SKIP
4359020416
>>>
>>> a = a + (4, 5, 6)
>>> id(a)  # doctest: +SKIP
4360038688
>>>
>>> a
(1, 2, 3, 4, 5, 6)


Example
-------
>>> from dataclasses import dataclass
>>>
>>> @dataclass
... class Vector:
...     x: int
...     y: int
...
...     def __add__(self, other):
...         new_x = self.x + other.x
...         new_y = self.y + other.y
...         return Vector(new_x, new_y)
>>>
>>>
>>> a = Vector(x=1, y=2)
>>> b = Vector(x=3, y=4)
>>> c = Vector(x=5, y=6)
>>>
>>> (a+b) + c
Vector(x=9, y=12)


Use Case - 0x01
---------------
>>> hero @ Position(x=50, y=120)  # doctest: +SKIP


Assignments
-----------
.. literalinclude:: assignments/operator_left_a.py
    :caption: :download:`Solution <assignments/operator_left_a.py>`
    :end-before: # Solution

.. todo:: Assignment: add overload, add health
.. todo:: Assignment: sub overload, subtract health
.. todo:: Assignment: sub overload, subtract health
.. todo:: Assignment: matmul overload, Position() set
