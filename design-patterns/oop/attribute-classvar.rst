OOP Attribute ClassVar
======================
* Class Variables
* Instance Variables
* Type Annotations


Class Variables
---------------
* Fields defined on a class
* Must have default values
* Share state
* Also known as 'static attributes'

Class variables are defined on a class:

>>> class Astronaut:
...     pass
>>>
>>>
>>> Astronaut.firstname = 'Mark'
>>> Astronaut.lastname = 'Watney'

Class variables are defined in a class:

>>> class Astronaut:
...     firstname = 'Mark'
...     lastname = 'Watney'


Instance Variables
------------------
* Fields defined on an instance
* Do not share state (unless mutable argument in method signature)
* By convention initialized in ``__init__()``
* Also known as 'dynamic attributes'

Instance variables are defined on an instance:

>>> class Astronaut:
...     pass
>>>
>>>
>>> mark = Astronaut()
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'

Instance variables are defined in init:

>>> class Astronaut:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'

Instance variables with variable values:

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname


Class and Instance Variables
----------------------------
Class and instance variables defined in code:

>>> class Astronaut:
...     pass
>>>
>>>
>>> Astronaut.firstname = 'Mark'
>>> Astronaut.lastname = 'Watney'
>>>
>>> melissa = Astronaut()
>>> melissa.firstname = 'Melissa'
>>> melissa.lastname = 'Lewis'

Class and instance variables defined in class:

>>> class Astronaut:
...     firstname = 'Mark'
...     lastname = 'Watney'
...
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'

Note, the last example makes not meaningful sense. Instance variables
will shadow class variables.


Type Annotations
----------------
Type annotations are not variable definition:

>>> x: int
>>>
>>> print(x)
Traceback (most recent call last):
NameError: name 'x' is not defined

Type annotations will only tell, that if there will be an identifier
with name ``x`` then it should be an ``int``:

>>> x: int
>>> x = 1
>>>
>>> print(x)
1

Typically it is written in shorter form:

>>> x: int = 1
>>>
>>> print(x)
1

These are not attributes at all (sic!). These are type annotations only,
and they do not exist before initialization in a code:

>>> class Astronaut:
...     firstname: str
...     lastname: str

Class variables with type annotations:

>>> class Astronaut:
...     firstname: str = 'Mark'
...     lastname: str = 'Watney'

Class variables with proper type annotations:

>>> from typing import ClassVar
>>>
>>>
>>> class Astronaut:
...     firstname: ClassVar[str] = 'Mark'
...     lastname: ClassVar[str] = 'Watney'

Instance variables with type annotations:

>>> class Astronaut:
...     firstname: str
...     lastname: str
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname


Dataclasses
-----------
* Dataclass uses class variables notation to create instance fields
* Dataclass do not validate type annotations, unless ``ClassVar``

>>> from dataclasses import dataclass
>>> from typing import ClassVar

Instance variables:

>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str

Instance variables with default values:

>>> @dataclass
... class Astronaut:
...     firstname: str = 'Mark'
...     lastname: str = 'Watney'

Class variables must have default values:

>>> @dataclass
... class Astronaut:
...     firstname: ClassVar[str] = 'Mark'
...     lastname: ClassVar[str] = 'Watney'


Class vs. Instance Variables
----------------------------
Lets define a class with class variable:

>>> class Astronaut:
...     agency = 'NASA'

Lets create three instances of ``Astronaut`` class:

>>> mark = Astronaut()
>>> melissa = Astronaut()
>>> rick = Astronaut()

We will print ``agency`` field:

>>> print(mark.agency)
NASA
>>>
>>> print(melissa.agency)
NASA
>>>
>>> print(rick.agency)
NASA
>>>
>>> print(Astronaut.agency)
NASA

Lets change field on a class and print ``agency`` field:

>>> Astronaut.agency = 'ESA'
>>>
>>>
>>> print(mark.agency)
ESA
>>>
>>> print(melissa.agency)
ESA
>>>
>>> print(rick.agency)
ESA
>>>
>>> print(Astronaut.agency)
ESA

Lets change field on an instance and print ``agency`` field:

>>> mark.agency = 'POLSA'
>>>
>>>
>>> print(mark.agency)
POLSA
>>>
>>> print(melissa.agency)
ESA
>>>
>>> print(rick.agency)
ESA
>>>
>>> print(Astronaut.agency)
ESA

Note, that the class which defined instance variable shadowed
the class variable.

Lets change field on a class and print ``agency`` field:

>>> Astronaut.agency = 'NASA'
>>>
>>>
>>> print(mark.agency)
POLSA
>>>
>>> print(melissa.agency)
NASA
>>>
>>> print(rick.agency)
NASA
>>>
>>> print(Astronaut.agency)
NASA

Lets delete field from an instance and print ``agency`` field:

>>> del mark.agency
>>>
>>>
>>> print(mark.agency)
NASA
>>>
>>> print(melissa.agency)
NASA
>>>
>>> print(rick.agency)
NASA
>>>
>>> print(Astronaut.agency)
NASA


Mechanism
---------
* ``vars(obj)`` is will return ``obj.__dict__``

>>> class Astronaut:
...     firstname = 'Mark'
...     lastname = 'Watney'
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> mark = Astronaut('Melissa', 'Lewis')
>>>
>>> vars(mark)
{'firstname': 'Melissa', 'lastname': 'Lewis'}
>>>
>>> vars(Astronaut)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
mappingproxy({'__module__': '__main__',
              'firstname': 'Mark',
              'lastname': 'Watney',
              '__init__': <function Astronaut.__init__ at 0x...>,
              '__dict__': <attribute '__dict__' of 'Astronaut' objects>,
              '__weakref__': <attribute '__weakref__' of 'Astronaut' objects>,
              '__doc__': None})


Use Case - 0x01
---------------
>>> from typing import ClassVar
>>>
>>>
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: ClassVar[int] = 30
...     AGE_MAX: ClassVar[int] = 50


Use Case - 0x02
---------------
>>> from typing import ClassVar
>>>
>>>
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: ClassVar[int] = 30
...     AGE_MAX: ClassVar[int] = 50
...
...     def __init__(self, firstname, lastname, age):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.age = age
...
...         if not self.AGE_MIN <= self.age < self.AGE_MAX:
...             raise ValueError('age is invalid')


Use Case - 0x03
---------------
>>> from dataclasses import dataclass
>>> from typing import ClassVar
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: ClassVar[int] = 30
...     AGE_MAX: ClassVar[int] = 50
...
...     def __post_init__(self):
...         if not self.AGE_MIN <= self.age < self.AGE_MAX:
...             raise ValueError('age is invalid')


Assignments
-----------
.. todo:: Assignments
