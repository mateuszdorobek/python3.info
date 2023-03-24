OOP Init Validation
===================


Validation
----------
>>> class User:
...     firstname: str
...     lastname: str
...     age: int
...
...     def __init__(self, firstname, lastname, age):
...         if age < 13:
...             raise ValueError('User too young')
...         self.firstname = firstname
...         self.lastname = lastname
...         self.age = age

>>> mark = User('Mark', 'Watney', age=30)

>>> mark = User('Mark', 'Watney', age=10)
Traceback (most recent call last):
ValueError: User too young


ClassVar
--------
* Type annotations - those are not fields, only optional information
* Instance variables (dynamic) - can change
* Class variables (static) - should not change
* Class variable name should be capitalized
* Class variable should not be initialized in ``__init__()``

Type annotations:

>>> class User:
...     firstname: str
...     lastname: str

Instance variables:

>>> class User:
...     def __init__(self, firstname, lastname, age):
...         self.firstname = firstname
...         self.lastname = lastname

Class variables:

>>> class User:
...     firstname: str = 'Mark'
...     lastname: str = 'Watney'

Example:

>>> class User:
...     firstname: str
...     lastname: str
...     age: int
...
...     AGE_MIN: int = 30
...     AGE_MAX: int = 50
...
...     def __init__(self, firstname, lastname, age):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.age = age


Use Case - 0x01
---------------
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     age: int
...
...     def __init__(self, firstname, lastname='asd', age=0):
...         if not 30 <= age < 50:
...             raise ValueError('Astronauts are selected between age of 30-50 years')
...         self.firstname = firstname
...         self.lastname = lastname
...         self.age = age
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney', age=40)
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}
>>>
>>> mark = Astronaut('Mark', 'Watney', age=60)
Traceback (most recent call last):
ValueError: Astronauts are selected between age of 30-50 years


Use Case - 0x02
---------------
* Those are static attributes
* Usefully for string configuration values
* Do not modify those values later in a code (keep them constant / final)
* More information in `OOP Static Attributes`.

>>> class Astronaut:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: int = 30
...     AGE_MAX: int = 50
...
...     def __init__(self, firstname, lastname='asd', age=0):
...         if not self.AGE_MIN <= age < self.AGE_MAX:
...             raise ValueError('Astronauts are selected between age of 30-50 years')
...         self.firstname = firstname
...         self.lastname = lastname
...         self.age = age
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney', age=40)
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}
>>>
>>> mark = Astronaut('Mark', 'Watney', age=60)
Traceback (most recent call last):
ValueError: Astronauts are selected between age of 30-50 years


Use Case - 0x03
---------------
>>> class Point:
...     x: int
...     y: int
...
...     def __init__(self, x, y):
...         if x < 0 or y < 0:
...             raise ValueError('Coordinate cannot be negative')
...         self.x = x
...         self.y = y
>>>
>>>
>>> point1 = Point(x=1, y=2)
>>> vars(point1)
{'x': 1, 'y': 2}
>>>
>>> point2 = Point(x=-1, y=-2)
Traceback (most recent call last):
ValueError: Coordinate cannot be negative


Use Case - 0x04
---------------
>>> class Kelvin:
...     ABSOLUTE_ZERO = 0.0
...     value: float
...
...     def __init__(self, value):
...         if value < self.ABSOLUTE_ZERO:
...             raise ValueError('Temperature must be greater than 0')
...         self.value = value
>>>
>>>
>>> t1 = Kelvin(273.15)
>>> print(t1.value)
273.15
>>>
>>> t2 = Kelvin(-300)
Traceback (most recent call last):
ValueError: Temperature must be greater than 0


Use Case - 0x05
---------------
* Boundaries

>>> class Point:
...     x: int
...     y: int
...
...     def __init__(self, x, y):
...         if not 0 <= x < 1024:
...             raise ValueError(f'{x} is out of boundary')
...         if not 0 <= y < 1024:
...             raise ValueError(f'{y} is out of boundary')
...         self.x = x
...         self.y = y
>>>
>>>
>>> point1 = Point(x=-10, y=1)
Traceback (most recent call last):
ValueError: -10 is out of boundary


Use Case - 0x06
---------------
* Parametrized Boundaries

>>> class Point:
...     X_MIN: int = 0
...     X_MAX: int = 1024
...     Y_MIN: int = 0
...     Y_MAX: int = 1024
...
...     x: int
...     y: int
...
...     def __init__(self, x: int, y: int):
...         if not self.X_MIN <= x < self.X_MAX:
...             raise ValueError(f'{x=} is out of boundary {self.X_MIN}, {self.X_MAX}')
...         if not self.Y_MIN <= y < self.Y_MAX:
...             raise ValueError(f'{y=} is out of boundary {self.Y_MIN}, {self.Y_MAX}')
...         self.x = x
...         self.y = y
>>>
>>>
>>> point1 = Point(x=-10, y=1)
Traceback (most recent call last):
ValueError: x=-10 is out of boundary 0, 1024
