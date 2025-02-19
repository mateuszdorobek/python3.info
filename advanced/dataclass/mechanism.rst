Dataclass Mechanism
===================


SetUp
-----
>>> from dataclasses import dataclass


Input
-----
>>> @dataclass
... class ShoppingCartItem:
...     name: str
...     unit_price: float
...     quantity: int = 0
...
...     def total_cost(self) -> float:
...         return self.unit_price * self.quantity


Output
------
>>> class ShoppingCartItem:
...     name: str
...     unit_price: float
...     quantity: int
...
...     def total_cost(self) -> float:
...         return self.unit_price * self.quantity
...
...     ## All code below is added by dataclass
...
...     def __init__(self, name: str, unit_price: float,
...                  quantity: int = 0) -> None:
...         self.name = name
...         self.unit_price = unit_price
...         self.quantity = quantity
...
...     def __repr__(self):
...         return f'ShoppingCartItem(name={self.name!r}, ' \
...                f'unit_price={self.unit_price!r}, ' \
...                f'quantity={self.quantity!r})'
...
...     def __eq__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                 == (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __ne__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                 != (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __lt__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                  < (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __le__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                 <= (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __gt__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                  > (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __ge__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                 >= (other.name, other.unit_price, other.quantity)
...         return NotImplemented


Use Case - 0x01
---------------
``class``:

>>> from dataclasses import dataclass
>>> from datetime import date
>>> from typing import ClassVar, Literal, Self
>>>
>>>
>>> class Group:
...    gid: int
...    name: str
...
...    def __init__(self, gid: int, name: str):
...        self.name = name
...        self.gid = gid
>>>
>>>
>>> class User:
...     firstname: str
...     lastname: str
...     birthday: date
...     age: int | None = None
...     height: float | None = None
...     weight: float | None = None
...     roles: Literal['user', 'staff', 'admin'] = 'admin'
...     friends: list[Self] | None = None
...     groups: list[Group] | None = None
...     rank: str | None = None
...     previous_job: str | None = None
...     experience: list[str] | None = None
...     AGE_MIN: ClassVar[int] = 27
...     AGE_MAX: ClassVar[int] = 50
...     WEIGHT_MIN: ClassVar[int] = 50
...     WEIGHT_MAX: ClassVar[int] = 90
...     HEIGHT_MIN: ClassVar[int] = 156
...     HEIGHT_MAX: ClassVar[int] = 210
...
...     def __init__(self,
...                  firstname: str,
...                  lastname: str,
...                  birthday: date,
...                  age: int | None = None,
...                  height: float | None = None,
...                  weight: float | None = None,
...                  agency: Literal['NASA', 'ESA'] = 'NASA',
...                  friends: list['User'] | None = None,
...                  groups: list[Group] | None = None,
...                  rank: str | None = None,
...                  previous_job: str | None = None,
...                  experience: list[str] | None = None):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.birthday = birthday
...         self.age = age
...         self.height = height
...         self.weight = weight
...         self.agency = agency
...         self.friends = friends
...         self.groups = groups
...         self.rank = rank
...         self.previous_job = previous_job
...         self.experience = experience
...
...     def __self__(self):
...         return self.repr()
...
...     def __repr__(self):
...         return (
...             f"{self.__class__.__name__}("
...             f"firstname='{self.firstname}'"
...             f"lastname='{self.lastname}'"
...             f"birthday={self.birthday}"
...             f"age={self.age}"
...             f"height={self.height}"
...             f"weight={self.weight}"
...             f"agency='{self.agency}'"
...             f"friends={self.friends}"
...             f"groups={self.groups}"
...             f"rank='{self.rank}'"
...             f"previous_job='{self.previous_job}'"
...             f"experience={self.experience}"
...             f")")
...
...     def __eq__(self, other):
...         return (self.__class__ is other.__class__
...            and self.firstname == other.firstname
...            and self.lastname == other.lastname
...            and self.birthday == other.birthday
...            and self.age == other.age
...            and self.height == other.height
...            and self.weight == other.weight
...            and self.agency == other.agency
...            and self.friends == other.friends
...            and self.groups == other.groups
...            and self.rank == other.rank
...            and self.previous_job == other.previous
...            and self.experience == other.experience)

``dataclass``:

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
...     birthday: date
...     age: int | None = None
...     height: float | None = None
...     weight: float | None = None
...     agency: Literal['NASA', 'ESA'] = 'NASA'
...     friends: list['User'] | None = None
...     groups: list[Group] | None = None
...     rank: str | None = None
...     previous_job: str | None = None
...     experience: list[str] | None = None
...     AGE_MIN: ClassVar[int] = 27
...     AGE_MAX: ClassVar[int] = 50
...     WEIGHT_MIN: ClassVar[int] = 50
...     WEIGHT_MAX: ClassVar[int] = 90
...     HEIGHT_MIN: ClassVar[int] = 156
...     HEIGHT_MAX: ClassVar[int] = 210
