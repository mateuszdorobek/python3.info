Dataclass About
===============
* Used for easier class definition
* Since Python 3.7: :pep:`557` -- Data Classes
* This are not static fields!
* Dataclasses require Type Annotations

New style classes:

>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname

Dataclasses:

>>> from dataclasses import dataclass
>>>
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str


SetUp
-----
>>> from dataclasses import dataclass


Problem
-------
>>> class User:
...     firstname: str
...     lastname: str
...
...     def __init__(self, firstname: str, lastname: str) -> None:
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __str__(self) -> str:
...         return f'{self.firstname} {self.lastname}'
...
...     def __repr__(self):
...         clsname = self.__class__.__name__
...         firstname = self.firstname
...         lastname = self.lastname
...         return f'{clsname}({firstname=}, {lastname=})'
...
...     def __eq__(self, other):
...         return self.__class__ is other.__class__ \
...            and self.firstname == other.firstname \
...            and self.lastname == other.lastname

To add field `middlename: str` we need to make change in 7 different places:

>>> class User:
...     firstname: str
...     middlename: str  # 1
...     lastname: str
...
...     def __init__(self, firstname: str, middlename: str, lastname: str) -> None:  # 2
...         self.firstname = firstname
...         self.middlename = middlename  # 3
...         self.lastname = lastname
...
...     def __str__(self) -> str:
...         return f'{self.firstname} {self.middlename} {self.lastname}'  # 4
...
...     def __repr__(self):
...         clsname = self.__class__.__name__
...         firstname = self.firstname
...         middlename = self.middlename  # 5
...         lastname = self.lastname
...         return f'{clsname}({firstname=}, {middlename=}, {lastname=})'  # 6
...
...     def __eq__(self, other):
...         return (
...             self.__class__ is other.__class__ and
...             self.firstname == other.firstname and
...             self.middlename == other.middlename and  # 7
...             self.lastname == other.lastname
...         )


Solution
--------
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str

To add field `middlename: str` we need to make change in 1 place:

>>> @dataclass
... class User:
...     firstname: str
...     middlename: str  # 1
...     lastname: str


Use Case - 0x01
---------------
>>> from dataclasses import dataclass
>>> from datetime import date
>>> from typing import Literal, Self
>>>
>>>
>>> @dataclass
... class Group:
...     gid: int
...     name: str
>>>
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     email: str
...     username: str
...     password: str
...     birthday: date | None = None
...     height: int | float | None = None
...     weight: int | float | None = None
...     role: Literal['admin', 'user', 'guest'] = 'user'
...     friends: list[Self] | None = None
...     groups: list[Group] | None = None


Use Case - 0x02
---------------
>>> from dataclasses import dataclass
>>> from itertools import starmap
>>>
>>>
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
... ]
>>>
>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str
>>>
>>> result = starmap(Iris, DATA[1:])
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[Iris(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9, species='virginica'),
 Iris(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species='setosa'),
 Iris(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3, species='versicolor'),
 Iris(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8, species='virginica'),
 Iris(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5, species='versicolor'),
 Iris(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2, species='setosa')]

