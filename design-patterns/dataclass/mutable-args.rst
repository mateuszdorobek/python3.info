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
>>> watney = Astronaut('Mark Watney')
>>> lewis = Astronaut('Melissa Lewis')
>>>
>>> watney.missions.append('Ares 1')
>>> watney.missions.append('Ares 2')
>>> watney.missions.append('Ares 3')
>>>
>>> print(f'Name: {watney.name}, Missions: {watney.missions}')
Name: Mark Watney, Missions: ['Ares 1', 'Ares 2', 'Ares 3']
>>>
>>> print(f'Name: {lewis.name}, Missions: {lewis.missions}')
Name: Melissa Lewis, Missions: ['Ares 1', 'Ares 2', 'Ares 3']

>>> class Astronaut:
...     def __init__(self, name, missions=None):
...         self.name = name
...         self.missions = missions if missions else []
>>>
>>>
>>> watney = Astronaut('Mark Watney')
>>> lewis = Astronaut('Melissa Lewis')
>>>
>>> watney.missions.append('Ares 1')
>>> watney.missions.append('Ares 2')
>>> watney.missions.append('Ares 3')
>>>
>>> print(f'Name: {watney.name}, Missions: {watney.missions}')
Name: Mark Watney, Missions: ['Ares 1', 'Ares 2', 'Ares 3']
>>>
>>> print(f'Name: {lewis.name}, Missions: {lewis.missions}')
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
>>> astro = Astronaut('Mark', 'Watney')
>>> print(astro)
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
>>> astro = Astronaut('Mark', 'Watney')
>>> print(astro)
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
>>> astro = Astronaut('Mark', 'Watney')
>>> print(astro)
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
>>> astro = Astronaut('Mark', 'Watney')
>>> print(astro)
Astronaut(firstname='Mark', lastname='Watney', groups=['astronauts', 'managers'])
