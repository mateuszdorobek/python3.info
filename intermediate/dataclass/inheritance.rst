Dataclass Inheritance
=====================
* Dataclasses can inherit from other classes
* Superclass not necessarily has to be dataclass
* If parent is dataclass the init will be joined
  (all parameters from parent and child will be set)


SetUp
-----
>>> from dataclasses import dataclass


Inheritance
-----------
>>> @dataclass
... class Person:
...     firstname: str
...     lastname: str
...     job: str = 'unemployed'
>>>
>>>
>>> @dataclass
... class Astronaut(Person):
...     job: str = 'astronaut'
...     agency: str = 'NASA'

Will generate:

>>> class Astronaut:
...     firstname: str
...     lastname: str
...     job: str = 'astronaut'
...     agency: str = 'NASA'
...
...     def __init__(self,
...                  firstname: str,
...                  lastname: str,
...                  job: str = 'astronaut',
...                  agency: str = 'NASA'):
...
...         self.firstname = firstname
...         self.lastname = lastname
...         self.job = job
...         self.agency = agency


Post Init
---------
When a child class define ``__post_init__()`` method it will overwrite
this method from a parent class:

>>> @dataclass
... class Person:
...     firstname: str
...     lastname: str
...
...     def __post_init__(self):
...         print('Person post init')
>>>
>>>
>>> @dataclass
... class Astronaut(Person):
...     job: str = 'astronaut'
...
...     def __post_init__(self):
...         print('Astronaut post init')
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
Astronaut post init


Super
-----
Using ``super()`` allows a child class to call ``__post_init__()`` from
a superclass. Note that all the parameters are already assigned, no need
to pass them like for ``__init__()`` function.

>>> @dataclass
... class Person:
...     firstname: str
...     lastname: str
...
...     def __post_init__(self):
...         print('Person post init')
>>>
>>>
>>> @dataclass
... class Astronaut(Person):
...     job: str = 'astronaut'
...
...     def __post_init__(self):
...         super().__post_init__()
...         print('Astronaut post init')
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
Person post init
Astronaut post init
