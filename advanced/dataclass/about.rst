Dataclass About
===============
* Used for easier class definition
* Since Python 3.7: :pep:`557` -- Data Classes
* This are not static fields!
* Dataclasses require Type Annotations

SetUp:

>>> from dataclasses import dataclass

Class:

>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname

Dataclass:

>>> @dataclass
... class User:
...     firstname: str
...     lastname: str


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
>>> from dataclasses import dataclass, field, asdict
>>> from datetime import date, time, datetime, timezone, timedelta
>>> from pprint import pprint
>>> from typing import ClassVar
>>> import pickle
>>>
>>>
>>> @dataclass
... class Group:
...     gid: int
...     name: str
>>>
>>>
>>> @dataclass(frozen=True)
... class User:
...     firstname: str
...     lastname: str
...     email: str | None = None
...     born: date | None = None
...     height: int | float | None = field(default=None, metadata={'unit': 'cm', 'min': 156, 'max': 210})
...     weight: int | float | None = field(default=None, metadata={'unit': 'kg', 'min': 50, 'max': 90})
...     groups: list[Group] = field(default_factory=list)
...     account_type: str = field(default='user', metadata={'choices': ['guest', 'user', 'admin']})
...     account_created: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
...     account_modified: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
...     account_lastlogin: datetime | None = None
...     account_expiration: timedelta | None = None
...     AGE_MIN: ClassVar[int] = 30
...     AGE_MAX: ClassVar[int] = 50

>>> mark = User(
...     firstname='Mark',
...     lastname='Watney',
...     email='mwatney@nasa.gov',
...     born=date(1969, 4, 12),
...     height=178.0,
...     weight=75.5,
...     groups=[Group(gid=1, name='users'), Group(gid=2, name='staff')],
...     account_type='user',
...     account_created=datetime(1969, 7, 21, 2, 56, 15, 0, tzinfo=timezone.utc),
...     account_modified=datetime(1969, 7, 21, 2, 56, 15, 0, tzinfo=timezone.utc),
...     account_lastlogin=None,
...     account_expiration=None,
... )


Use Case - 0x03
---------------
>>> from dataclasses import dataclass
>>> from itertools import starmap
>>>
>>>
>>> DATA = [
...     ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
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
