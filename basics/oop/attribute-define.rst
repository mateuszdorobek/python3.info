OOP Attribute Define
====================
* Attribute Annotation is optional, but a good practice


No Attribute Definition
-----------------------
>>> class User:
...     pass


Basic Types
-----------
>>> class User:
...     firstname: str
...     lastname: str
...     age: int


Union
-----
>>> class User:
...     firstname: str
...     lastname: str
...     age: int | float


Optional
--------
>>> class User:
...     firstname: str
...     lastname: str
...     age: int | float
...     height: float | None
...     weight: float | None


Sequences
---------
* Since Python 3.9 you can use ``list[str]``
* Before Python 3.9 use ``list`` without specifying type of elements inside

>>> class User:
...     firstname: str
...     lastname: str
...     age: int
...     groups: list[str]


Relation One to One
-------------------
>>> class Group:
...     gid: int
...     name: int
>>>
>>>
>>> class User:
...     firstname: str
...     lastname: str
...     group: Group


Relation One to Many
--------------------
>>> class Group:
...     gid: int
...     name: str
>>>
>>>
>>> class User:
...     firstname: str
...     lastname: str
...     groups: list[Group]


Example
-------
>>> class User:
...     firstname: str
...     lastname: str
...     email: str
...     active: bool
...     age: int | float
...     height: float | None
...     weight: float | None
...     groups: list[str] | None
...     friends: list['User'] | None


Good Practices
--------------
* ``snake_case`` name convention
* Attributes should be defined only in ``__init__()`` method
* More information in `OOP Init Method`


Use Case - 0x01
---------------
>>> class Point:
...     x: int
...     y: int
...     z: int


Use Case - 0x02
---------------
>>> class Date:
...     year: int
...     month: int
...     day: int


Use Case - 0x03
---------------
>>> class Laptop:
...     cpu: str
...     ram: str
...     ssd: str


Use Case - 0x04
---------------
>>> class Iris:
...     features: list[float]
...     label: str


Use Case - 0x05
---------------
>>> class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str


Use Case - 0x06
---------------
>>> from datetime import date
>>> from typing import Literal
>>>
>>>
>>> class Address:
...     type: Literal['home', 'work']
...     street: str
...     house: str
...     apartment: str
...     post_code: str
...     city: str
...     region: str
...     country: str
>>>
>>>
>>> class PhoneNumber:
...     type: Literal['home', 'work', 'mobile']
...     number: str
>>>
>>>
>>> class Person:
...     firstname: str
...     lastname: str
...     age: int | float
...     born: date
...     gender: Literal['male', 'female']
...     height: float | None
...     weight: float | None
...     education: list[str] | None
...     job: str | None
...     addresses: list[Address] | None
...     emails: list[str] | None
...     phones: PhoneNumber | None
...     friends: list['Person'] | None


Assignments
-----------
.. literalinclude:: assignments/oop_attribute_define_a.py
    :caption: :download:`Solution <assignments/oop_attribute_define_a.py>`
    :end-before: # Solution
