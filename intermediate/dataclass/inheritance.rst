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
... class Account:
...     firstname: str
...     lastname: str
>>>
>>>
>>> @dataclass
... class User(Account):
...     role: str = 'user'

Will generate:

>>> class User:
...     firstname: str
...     lastname: str
...     role: str = 'user'
...
...     def __init__(self,
...                  firstname: str,
...                  lastname: str,
...                  role: str = 'user'):
...
...         self.firstname = firstname
...         self.lastname = lastname
...         self.role = role


Post Init
---------
When a child class define ``__post_init__()`` method it will overwrite
this method from a parent class:

>>> @dataclass
... class Account:
...     firstname: str
...     lastname: str
...
...     def __post_init__(self):
...         print('Account post init')
>>>
>>>
>>> @dataclass
... class User(Account):
...     role: str = 'user'
...
...     def __post_init__(self):
...         print('User post init')
>>>
>>>
>>> mark = User('Mark', 'Watney')
User post init


Super
-----
Using ``super()`` allows a child class to call ``__post_init__()`` from
a superclass. Note that all the parameters are already assigned, no need
to pass them like for ``__init__()`` function.

>>> @dataclass
... class Account:
...     firstname: str
...     lastname: str
...
...     def __post_init__(self):
...         print('Account post init')
>>>
>>>
>>> @dataclass
... class User(Account):
...     role: str = 'user'
...
...     def __post_init__(self):
...         super().__post_init__()
...         print('User post init')
>>>
>>>
>>> mark = User('Mark', 'Watney')
Account post init
User post init
