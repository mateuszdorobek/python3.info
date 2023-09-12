OOP Property Decorator
======================
* Disable attribute modification
* Logging value access

In Python, ``@property`` is a built-in decorator that allows you to define a
method as a read-only property of a class. This means that the method can be
accessed like an attribute, without needing to call it as a method. The
``@property`` decorator is used to define a getter method for a property.
The getter method should have the same name as the property, and it should
return the value of the property.

Here's an example of using the ``@property`` decorator to define a read-only
property of a class:

>>> class MyClass:
...     def __init__(self, x):
...         self._x = x
...
...     @property
...     def x(self):
...         return self._x
>>>
>>> # Create an instance of MyClass
>>> obj = MyClass(10)
>>>
>>> # Access the property like an attribute
>>> print(obj.x)
10

In this example, the ``MyClass`` class defines a private attribute ``_x``
and a getter method ``x()`` decorated with the ``@property`` decorator.
The ``x()`` method returns the value of the ``_x`` attribute.

The ``obj.x`` expression accesses the ``x`` property of the ``obj`` instance
of ``MyClass``, which calls the ``x()`` method to retrieve the value of the
``_x`` attribute. Note that the ``_x`` attribute is private and cannot be
accessed directly from outside the class.


SetUp
-----
>>> from dataclasses import dataclass
>>> from datetime import date


Example
-------
>>> class Point:
...     x: int
...     y: int
...     z: int
...
...     def get_position(self):
...         return self.x, self.y, self.z
>>>
>>>
>>> pt = Point()
>>> pt.x = 1
>>> pt.y = 2
>>> pt.z = 3
>>>
>>> print(pt.get_position())
(1, 2, 3)

>>> class Point:
...     x: int
...     y: int
...     z: int
...
...     @property
...     def position(self):
...         return self.x, self.y, self.z
>>>
>>>
>>> pt = Point()
>>> pt.x = 1
>>> pt.y = 2
>>> pt.z = 3
>>>
>>> print(pt.position)
(1, 2, 3)


Use Case - 0x01
---------------
>>> YEAR = 365.25
>>>
>>> class User:
...     def __init__(self, firstname, lastname, birthday):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.birthday = birthday
...
...     @property
...     def age(self):
...         days = (date.today() - self.birthday).days
...         return int(days/YEAR)
>>>
>>>
>>> mark = User('Mark', 'Watney', birthday=date(1969, 7, 21))
>>> mark.age  # doctest: +SKIP
53


Use Case - 0x02
---------------
>>> class User:
...     def __init__(self, firstname, lastname):
...         self._firstname = firstname
...         self._lastname = lastname
...
...     @property
...     def name(self):
...         return f'{self._firstname} {self._lastname[0]}.'
>>>
>>>
>>> mark = User('Mark', 'Watney')
>>> print(mark.name)
Mark W.


Use Case - 0x04
---------------
* Cached Property

>>> from dataclasses import dataclass, field
>>> from datetime import date
>>>
>>> YEAR = 365.25
>>> TODAY = date(2000, 1, 1)
>>>
>>>
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     date_of_birth: date
...     __cache: dict = field(default_factory=dict)
...
...     @property
...     def age(self):
...         if 'age' not in self.__cache:
...             age = (TODAY - self.date_of_birth).days / YEAR
...             self.__cache['age'] = round(age, 1)
...         return self.__cache['age']
>>>
>>>
>>> mark = User('Mark', 'Watney', date(1969, 7, 21))
>>> print(mark.age)
30.4


Use Case - 0x08
---------------
>>> import logging
>>>
>>>
>>> class User:
...     def __init__(self, username, password):
...         self._username = username
...         self._password = password
...
...     @property
...     def username(self):
...         logging.warning("User's username was accessed")
...         return self._username
...
...     @property
...     def password(self):
...         logging.warning("User's password was accessed")
...         return self._password
>>>
>>>
>>> mark = User(username='mwatney', password='Ares3')
>>>
>>> print(mark.password)
Ares3


Assignments
-----------
.. literalinclude:: assignments/oop_attribute_property_decorator_a.py
    :caption: :download:`Solution <assignments/oop_property_decorator_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_attribute_property_decorator_b.py
    :caption: :download:`Solution <assignments/oop_property_decorator_b.py>`
    :end-before: # Solution
