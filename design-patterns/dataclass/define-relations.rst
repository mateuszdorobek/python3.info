Dataclass Define Nested
=======================


SetUp
-----
>>> from dataclasses import dataclass
>>> from typing import Self


Relation to Objects
-------------------
>>> @dataclass
... class Mission:
...     year: int
...     name: str
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[Mission]

>>> astro = Astronaut('Mark', 'Watney', missions=[
...     Mission(1973, 'Apollo 18'),
...     Mission(2012, 'STS-136'),
...     Mission(2035, 'Ares 3')])

>>> astro  # doctest: +NORMALIZE_WHITESPACE
Astronaut(firstname='Mark', lastname='Watney',
          missions=[Mission(year=1973, name='Apollo 18'),
                    Mission(year=2012, name='STS-136'),
                    Mission(year=2035, name='Ares 3')])


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
... class Astronaut:
...     firstname: str
...     lastname: str
...     friends: list[Self] = None

Use:

>>> astro = Astronaut('Mark', 'Watney', friends=[
...     Astronaut('Melissa', 'Lewis'),
...     Astronaut('Rick', 'Martinez'),
...     Astronaut('Beth', 'Johanssen'),
...     Astronaut('Chris', 'Beck'),
...     Astronaut('Alex', 'Vogel')])

>>> astro  # doctest: +NORMALIZE_WHITESPACE
Astronaut(firstname='Mark', lastname='Watney',
          friends=[Astronaut(firstname='Melissa', lastname='Lewis', friends=None),
                   Astronaut(firstname='Rick', lastname='Martinez', friends=None),
                   Astronaut(firstname='Beth', lastname='Johanssen', friends=None),
                   Astronaut(firstname='Chris', lastname='Beck', friends=None),
                   Astronaut(firstname='Alex', lastname='Vogel', friends=None)])


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
