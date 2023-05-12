Dataclass Mutable Attrs
=======================
* problem with ``dict``, ``list``, ``set``
* You should not set mutable objects as a default function argument
* ``field()`` creates new empty ``list`` for each object
* It does not reuse reference
* Discussion: https://github.com/ericvsmith/dataclasses/issues/3


SetUp
-----
>>> from dataclasses import dataclass, field


Problem
-------
Note, You should not set mutable objects as a default function argument.
More information in `Argument Mutability`. This is how all dynamically typed
languages work (including PHP, Ruby, Perl etc).

>>> class Astronaut:
...     def __init__(self, name, missions=[]):
...         self.name = name
...         self.missions = missions
>>>
>>>
>>> mark = Astronaut('Mark Watney')
>>> melissa = Astronaut('Melissa Lewis')
>>>
>>> mark.missions.append('Ares 1')
>>> mark.missions.append('Ares 2')
>>> mark.missions.append('Ares 3')
>>>
>>> print(f'Name: {mark.name}, Missions: {mark.missions}')
Name: Mark Watney, Missions: ['Ares 1', 'Ares 2', 'Ares 3']
>>>
>>> print(f'Name: {melissa.name}, Missions: {melissa.missions}')
Name: Melissa Lewis, Missions: ['Ares 1', 'Ares 2', 'Ares 3']

>>> class Astronaut:
...     def __init__(self, name, missions=None):
...         self.name = name
...         self.missions = missions if missions else []
>>>
>>>
>>> mark = Astronaut('Mark Watney')
>>> melissa = Astronaut('Melissa Lewis')
>>>
>>> mark.missions.append('Ares 1')
>>> mark.missions.append('Ares 2')
>>> mark.missions.append('Ares 3')
>>>
>>> print(f'Name: {mark.name}, Missions: {mark.missions}')
Name: Mark Watney, Missions: ['Ares 1', 'Ares 2', 'Ares 3']
>>>
>>> print(f'Name: {melissa.name}, Missions: {melissa.missions}')
Name: Melissa Lewis, Missions: []


List of Strings
---------------
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[str] = field(default_factory=list)
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>> print(mark)
Astronaut(firstname='Mark', lastname='Watney', missions=[])


List of Objects
---------------
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
...     missions: list[Mission] = field(default_factory=list)
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>> print(mark)
Astronaut(firstname='Mark', lastname='Watney', missions=[])


Dict
----
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: dict[int,str] = field(default_factory=dict)
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>> print(mark)
Astronaut(firstname='Mark', lastname='Watney', missions={})


Default Values
--------------
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     groups: list[str] = field(default_factory=lambda: ['astronauts', 'managers'])
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>> print(mark)
Astronaut(firstname='Mark', lastname='Watney', groups=['astronauts', 'managers'])
