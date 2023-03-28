Dataclass Define Special
========================


SetUp
-----
>>> from dataclasses import dataclass, field
>>> from typing import Literal, Final


Union Fields
------------
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     age: int | float


Optional Fields
---------------
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     age: int | None = None


Literal Field
-------------
Import:

>>> from typing import Literal

Define class:

>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     role: Literal['users', 'staff', 'admins']


ClassVar Fields
---------------
* ``from typing import ClassVar``
* Defines static field

One of two places where ``dataclass()`` actually inspects the type of a
field is to determine if a field is a class variable as defined in PEP 526.
It does this by checking if the type of the field is ``typing.ClassVar``.
If a field is a ``ClassVar``, it is excluded from consideration as a field
and is ignored by the dataclass mechanisms. Such ``ClassVar`` pseudo-fields
are not returned by the module-level ``fields()`` function.

Import:

>>> from typing import ClassVar

Define Class:

>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: ClassVar[int] = 30
...     AGE_MAX: ClassVar[int] = 50

Note, that those fields will not be displayed in repr or while printing.

>>> User('Mark', 'Watney', age=40)
User(firstname='Mark', lastname='Watney', age=40)


Keyword Arguments Only
----------------------
* Since Python 3.10
* ``from dataclasses import KW_ONLY``

Any fields after a pseudo-field with the type of ``KW_ONLY`` are marked
as keyword-only fields. Note that a pseudo-field of type ``KW_ONLY`` is
otherwise completely ignored. This includes the name of such a field.
By convention, a name of ``_`` is used for a ``KW_ONLY`` field.

Import:

>>> from dataclasses import KW_ONLY

Define class:

>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     _: KW_ONLY
...     age: int
...     height: float
...     weight: float

>>> User('Mark', 'Watney', age=40, height=185.0, weight=75.5)
User(firstname='Mark', lastname='Watney', age=40, height=185.0, weight=75.5)

>>> mark = User('Mark', 'Watney', 40, height=185.0, weight=75.5)
Traceback (most recent call last):
TypeError: User.__init__() takes 3 positional arguments but 4 positional arguments (and 2 keyword-only arguments) were given

>>> mark = User('Mark', 'Watney', 40, 185.0, weight=75.5)
Traceback (most recent call last):
TypeError: User.__init__() takes 3 positional arguments but 5 positional arguments (and 1 keyword-only argument) were given

>>> mark = User('Mark', 'Watney', 40, 185.0, 75.5)
Traceback (most recent call last):
TypeError: User.__init__() takes 3 positional arguments but 6 were given


Assignments
-----------
.. todo:: Assignments
