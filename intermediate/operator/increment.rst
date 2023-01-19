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

>>> x = [1, 2, 3]
>>> id(x)  # doctest: +SKIP
4343115776
>>>
>>> x += [4, 5, 6]
>>> id(x)  # doctest: +SKIP
4343115776

SetUp
-----
>>> from dataclasses import dataclass


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
>>> b = Vector(x=3, y=4)
>>> c = Vector(x=5, y=6)
>>>
>>>
>>> a += Vector(x=10, y=20)
>>> print(a)
Vector(x=11, y=22)


Use Case - 0x01
---------------
>>> from dataclasses import dataclass, field
>>>
>>>
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
>>>
>>>
>>> ares3 = Crew()
>>> ares3 += Astronaut('Mark', 'Watney')
>>> ares3 += Astronaut('Melissa', 'Lewis')
>>>
>>> print(ares3)
Crew(members=[Astronaut(firstname='Mark', lastname='Watney'), Astronaut(firstname='Melissa', lastname='Lewis')])
>>>
>>> for member in ares3.members:
...     print(member)
Astronaut(firstname='Mark', lastname='Watney')
Astronaut(firstname='Melissa', lastname='Lewis')


Assignments
-----------
.. literalinclude:: assignments/operator_increment_a.py
    :caption: :download:`Solution <assignments/operator_increment_a.py>`
    :end-before: # Solution
