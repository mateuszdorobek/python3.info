Dataclass Define Nested
=======================


SetUp
-----
>>> from dataclasses import dataclass
>>> from typing import Self


Relation to Objects
-------------------
>>> @dataclass
... class Group:
...     gid: int
...     name: str
>>>
>>>
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     groups: list[Group]

Usage:

>>> mark = User('Mark', 'Watney', groups=[
...     Group(gid=1, name='users'),
...     Group(gid=2, name='staff'),
...     Group(gid=3, name='admins')])


Relation to Self
----------------
* Note, that there are ``None`` default friends
* Using an empty list ``[]`` as a default value will not work
* ``Self`` is available since Python 3.11
* We will cover this topic later

Import:

>>> from typing import Self

Define class:

>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     friends: list[Self] = None

Use:

>>> mark = User('Mark', 'Watney', friends=[
...     User('Melissa', 'Lewis'),
...     User('Rick', 'Martinez'),
...     User('Beth', 'Johanssen'),
...     User('Chris', 'Beck'),
...     User('Alex', 'Vogel')])


Assignments
-----------
.. literalinclude:: assignments/dataclass_define_relations_a.py
    :caption: :download:`Solution <assignments/dataclass_define_relations_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/dataclass_define_relations_b.py
    :caption: :download:`Solution <assignments/dataclass_define_relations_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/dataclass_define_relations_c.py
    :caption: :download:`Solution <assignments/dataclass_define_relations_c.py>`
    :end-before: # Solution
