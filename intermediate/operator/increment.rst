Operator Increment
==================
* ``x += y`` - will call method "iadd" on object ``x`` (``x.__iadd__(y)``)
* ``x -= y`` - will call method "isub" on object ``x`` (``x.__isub__(y)``)
* ``x *= y`` - will call method "imul" on object ``x`` (``x.__imul__(y)``)
* ``x **= y`` - will call method "ipow" on object ``x`` (``x.__ipow__(y)``)
* ``x @= y`` - will call method "imatmul" on object ``x`` (``x.__imatmul__(y)``)
* ``x /= y`` - will call method "itruediv" on object ``x`` (``x.__itruediv__(y)``)
* ``x //= y`` - will call method "ifloordiv" on object ``x`` (``x.__ifloordiv__(y)``)
* ``x %= y`` - will call method "imod" on object ``x`` (``x.__imod__(y)``)

.. csv-table:: Numerical Operator Overload
    :header: "Operator", "Method"

    "``obj += other``",     "``obj.__iadd__(other)``"
    "``obj -= other``",     "``obj.__isub__(other)``"
    "``obj *= other``",     "``obj.__imul__(other)``"
    "``obj **= other``",    "``obj.__ipow__(other)``"
    "``obj @= other``",     "``obj.__imatmul__(other)``"
    "``obj /= other``",     "``obj.__itruediv__(other)``"
    "``obj //= other``",    "``obj.__ifloordiv__(other)``"
    "``obj %= other``",     "``obj.__imod__(other)``"


Memory
------
* ``tuple`` is immutable
* ``list`` is mutable
* ``tuple += tuple`` will generate new ``tuple``
* ``list += list`` will update old ``list``
* ``__iadd__()`` operator on ``tuple`` is different than on ``list``

>>> a = (1, 2, 3)
>>> id(a)  # doctest: +SKIP
4354672064
>>>
>>> a += (4, 5, 6)
>>> id(a)  # doctest: +SKIP
4360031872
>>>
>>> a
(1, 2, 3, 4, 5, 6)

>>> a = [1, 2, 3]
>>> id(a)  # doctest: +SKIP
4345884480
>>>
>>> a += [4, 5, 6]
>>> id(a)  # doctest: +SKIP
4345884480
>>>
>>> a
[1, 2, 3, 4, 5, 6]


SetUp
-----
>>> from dataclasses import dataclass, field


Syntax
------
>>> @dataclass
... class Vector:
...     x: int
...     y: int
...
...     def __iadd__(self, other): ...              # x += y    calls x.__iadd__(y)
...     def __isub__(self, other): ...              # x -= y    calls x.__isub__(y)
...     def __imul__(self, other): ...              # x *= y    calls x.__imul__(y)
...     def __ipow__(self, power, modulo=None): ... # x **= y   calls x.__ipow__(y)
...     def __imatmul__(self, other): ...           # x @= y    calls x.__imatmul__(y)
...     def __itruediv__(self, other): ...          # x /= y    calls x.__itruediv__(y)
...     def __ifloordiv__(self, other): ...         # x //= y   calls x.__ifloordiv__(y)
...     def __imod__(self, other): ...              # x %= y    calls x.__imod__(y)


Example
-------
>>> @dataclass
... class Vector:
...     x: int
...     y: int
...
...     def __iadd__(self, other):
...         self.x += other.x
...         self.y += other.y
...         return self
...
>>>
>>>
>>> a = Vector(x=1, y=2)
>>>
>>> a += Vector(x=10, y=20)
>>> print(a)
Vector(x=11, y=22)


Add vs Iadd
-----------
>>> @dataclass
... class Vector:
...     x: int
...     y: int
...
...     def __add__(self, other):
...         return Vector(
...             x = self.x + other.x,
...             y = self.y + other.y)
>>>
>>>
>>> a = Vector(x=1, y=2)
>>>
>>> id(a)  # doctest: +SKIP
4435911632
>>>
>>> a += Vector(x=10, y=20)
>>> id(a)  # doctest: +SKIP
4435972432
>>>
>>> print(a)
Vector(x=11, y=22)

>>> @dataclass
... class Vector:
...     x: int
...     y: int
...
...     def __iadd__(self, other):
...         self.x += other.x
...         self.y += other.y
...         return self
>>>
>>>
>>> a = Vector(x=1, y=2)
>>>
>>> id(a)  # doctest: +SKIP
4437201808
>>>
>>> a += Vector(x=10, y=20)
>>> id(a)  # doctest: +SKIP
4437201808
>>>
>>> print(a)
Vector(x=11, y=22)


Use Case - 0x01
---------------
Imports:

>>> from dataclasses import dataclass, field
>>> from pprint import pprint

Definition:

>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> @dataclass
... class Crew:
...     members: list[Astronaut] = field(default_factory=list)
...
...     def __iadd__(self, other):
...         self.members.append(other)
...         return self

Usage:

>>> ares3 = Crew()
>>> ares3 += Astronaut('Mark', 'Watney')
>>> ares3 += Astronaut('Melissa', 'Lewis')

>>> pprint(ares3)
Crew(members=[Astronaut(firstname='Mark', lastname='Watney'),
              Astronaut(firstname='Melissa', lastname='Lewis')])

>>> for member in ares3.members:
...     print(member)
Astronaut(firstname='Mark', lastname='Watney')
Astronaut(firstname='Melissa', lastname='Lewis')


Assignments
-----------
.. literalinclude:: assignments/operator_increment_a.py
    :caption: :download:`Solution <assignments/operator_increment_a.py>`
    :end-before: # Solution
