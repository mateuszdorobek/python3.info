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

>>> class User:
...     def __init__(self, name, groups=[]):
...         self.name = name
...         self.groups = groups
>>>
>>>
>>> mark = User('Mark Watney')
>>> melissa = User('Melissa Lewis')
>>>
>>> mark.groups.append('user')
>>> mark.groups.append('staff')
>>> mark.groups.append('admin')
>>>
>>> print(f'Name: {mark.name}, Missions: {mark.groups}')
Name: Mark Watney, Missions: ['user', 'staff', 'admin']
>>>
>>> print(f'Name: {melissa.name}, Missions: {melissa.groups}')
Name: Melissa Lewis, Missions: ['user', 'staff', 'admin']

>>> class User:
...     def __init__(self, name, groups=None):
...         self.name = name
...         self.groups = groups if groups else []
>>>
>>>
>>> mark = User('Mark Watney')
>>> melissa = User('Melissa Lewis')
>>>
>>> mark.groups.append('user')
>>> mark.groups.append('staff')
>>> mark.groups.append('admin')
>>>
>>> print(f'Name: {mark.name}, Missions: {mark.groups}')
Name: Mark Watney, Missions: ['user', 'staff', 'admin']
>>>
>>> print(f'Name: {melissa.name}, Missions: {melissa.groups}')
Name: Melissa Lewis, Missions: []


List of Strings
---------------
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     groups: list[str] = field(default_factory=list)
>>>
>>>
>>> mark = User('Mark', 'Watney')
>>> print(mark)
User(firstname='Mark', lastname='Watney', groups=[])


List of Objects
---------------
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
...     groups: list[Group] = field(default_factory=list)
>>>
>>>
>>> mark = User('Mark', 'Watney')
>>> print(mark)
User(firstname='Mark', lastname='Watney', groups=[])


Dict
----
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     groups: dict[int,str] = field(default_factory=dict)
>>>
>>>
>>> mark = User('Mark', 'Watney')
>>> print(mark)
User(firstname='Mark', lastname='Watney', groups={})


Default Values
--------------
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     groups: list[str] = field(default_factory=lambda: ['user', 'staff', 'admins'])
>>>
>>>
>>> mark = User('Mark', 'Watney')
>>> print(mark)
User(firstname='Mark', lastname='Watney', groups=['user', 'staff', 'admins'])
