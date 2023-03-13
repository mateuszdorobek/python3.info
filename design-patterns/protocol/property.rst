Protocol Property
=================
* Disable attribute modification
* Logging value access
* Check boundary
* Raise exceptions such as ``ValueError`` or ``TypeError``
* Check argument type

SetUp:

>>> from dataclasses import dataclass
>>> from datetime import date

Definition:

>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     birthday: date
...
...     @property
...     def age(self):
...         diff = date.today() - self.birthday
...         years = diff.days / 365.25
...         return round(years, 1)

Usage:

>>> mark = Astronaut('Mark', 'Watney', birthday=date(1969, 7, 21))
>>> mark.age  # doctest: +SKIP
53.4

>>> mark.age = 40
Traceback (most recent call last):
AttributeError: property 'age' of 'Astronaut' object has no setter


Problem
-------
>>> class Point:
...     x: int
...
...     def get_x(self): pass
...     def set_x(self, newvalue): pass
...     def del_x(self): pass
>>>
>>>
>>> pt = Point()
>>> pt.set_x(1)

>>> class Point:
...     x: int
...     y: int
...
...     def get_x(self): pass
...     def set_x(self, newvalue): pass
...     def del_x(self): pass
...     def get_y(self): pass
...     def set_y(self, newvalue): pass
...     def del_y(self): pass
>>>
>>>
>>> pt = Point()
>>> pt.set_x(1)
>>> pt.set_y(1)

>>> class Point:
...     x: int
...     y: int
...     z: int
...
...     def get_x(self) -> int: pass
...     def get_x(self): pass
...     def set_x(self, newvalue): pass
...     def del_x(self): pass
...     def get_y(self): pass
...     def set_y(self, newvalue): pass
...     def del_y(self): pass
...     def get_z(self): pass
...     def set_z(self, newvalue): pass
...     def del_z(self): pass
>>>
>>>
>>> pt = Point()
>>> pt.set_x(1)
>>> pt.set_y(1)
>>> pt.set_z(1)


What if...
----------
>>> class Point:
...     x: int
...     y: int
...     z: int
...
...     def set_position(self, x, y, z):
...         self.x = x
...         self.y = y
...         self.z = z
>>>
>>> pt = Point()
>>> pt.set_position(1, 2, 3)

Works for point.
How about astronauts

>>> class Astronaut:
...     firstname: str
...     middlename: str
...     lastname: str
...
...     def set_name(self, name):
...         first, mid, last = name.split()
...         self.firstname = first
...         self.middlename = mid
...         self.lastname = last

Do everyone have a middle name?
Do everyone have first or lastname?


Solution
--------
>>> class Point:
...     x: int
...     y: int
...     z: int
>>>
>>>
>>> pt = Point()
>>> pt.x = 1
>>> pt.y = 2
>>> pt.z = 3

But what if we want to make validation:

>>> class Point:
...     x: int
...     y: int
...     z: int
...
...     def set_x(self, newvalue):
...         if newvalue > 0:
...             self.x = newvalue
...         else:
...             raise ValueError
...
...     def set_y(self, newvalue):
...         if newvalue > 0:
...             self.y = newvalue
...         else:
...             raise ValueError
...
...     def set_z(self, newvalue):
...         if newvalue > 0:
...             self.z = newvalue
...         else:
...             raise ValueError

We can refactor this code:

>>> class Point:
...     x: int
...     y: int
...     z: int
...
...     def _is_valid(self, value):
...         if newvalue > 0:
...             return value
...         else:
...             raise ValueError
...
...     def set_x(self, newvalue):
...         self.x = self._valid(newvalue)
...
...     def set_y(self, newvalue):
...         self.y = self._valid(newvalue)
...
...     def set_z(self, newvalue):
...         self.z = self._valid(newvalue)

But problem persist.

What if all parameters can have different ranges:

    - age between 0 and 130
    - height between 150 and 210
    - name first capital letter, then lowercased letters


Protocol
--------
* ``myattribute = property()`` - creates property
* ``@myattribute.getter`` - getter for attribute
* ``@myattribute.setter`` - setter for attribute
* ``@myattribute.deleter`` - deleter for attribute
* Method name must be the same as attribute name
* ``myattribute`` has to be ``property``
* ``@property`` - creates property and a getter

>>> class MyClass:
...     myattribute = property()
...
...     @myattribute.getter
...     def myattribute(self):
...         return ...
...
...     @myattribute.setter
...     def myattribute(self):
...         ...
...
...     @myattribute.deleter
...     def myattribute(self):
...         ...


Example
-------
* Kelvin is an absolute scale (no values below zero)

>>> class KelvinTemperature:
...     value: float
>>>
>>> t = KelvinTemperature()
>>> t.value = -2               # Should raise ValueError('Kelvin cannot be negative')

>>> class KelvinTemperature:
...     value: float
...
...     def __init__(self, initialvalue):
...         self.value = initialvalue
>>>
>>> t = KelvinTemperature(-1)   # Should raise ValueError('Kelvin cannot be negative')
>>> t.value = -2                # Should raise ValueError('Kelvin cannot be negative')

>>> class KelvinTemperature:
...     value: float
...
...     def __init__(self, initialvalue):
...         if initialvalue < 0:
...             raise ValueError('Negative Kelvin Temperature')
...         self.value = initialvalue
>>>
>>>
>>> t = KelvinTemperature(1)
>>> t.value = -1  # Should raise ValueError('Kelvin cannot be negative')

>>> class KelvinTemperature:
...     _value: float
...
...     def __init__(self, initialvalue):
...         self.set_value(initialvalue)
...
...     def set_value(self, newvalue):
...         if newvalue < 0:
...             raise ValueError('Negative Kelvin Temperature')
...         self._value = newvalue

>>> class KelvinTemperature:
...     _value: float
...     value = property()
...
...     def __init__(self, initialvalue):
...         self.value = initialvalue
...
...     @value.setter
...     def value(self, newvalue):
...         if newvalue < 0:
...             raise ValueError('Negative Kelvin Temperature')
...         self._value = newvalue


Use Case - 0x01
---------------
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self._firstname = firstname
...         self._lastname = lastname
...
...     @property
...     def name(self):
...         return f'{self._firstname} {self._lastname[0]}.'
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>> print(astro.name)
Mark W.


Use Case - 0x02
---------------
>>> class Astronaut:
...     name = property()
...
...     def __init__(self, firstname, lastname):
...         self._firstname = firstname
...         self._lastname = lastname
...
...     @name.getter
...     def name(self):
...         return f'{self._firstname} {self._lastname[0]}.'
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>> print(astro.name)
Mark W.


Use Case - 0x03
---------------
>>> class Temperature:
...     kelvin = property()
...     __value: float
...
...     def __init__(self, kelvin=None):
...         self.__value = kelvin
...
...     @kelvin.setter
...     def kelvin(self, newvalue):
...         if newvalue < 0:
...             raise ValueError('Negative Kelvin Temperature')
...         else:
...             self.__value = newvalue
>>>
>>>
>>> t = Temperature()
>>> t.kelvin = 10
>>> t.kelvin = -1
Traceback (most recent call last):
ValueError: Negative Kelvin Temperature


Attribute Access
----------------
* Java way: Setter and Getter
* Pythonic way: Properties, Reflection, Descriptors

Accessing class fields using setter and getter:

>>> class Astronaut:
...     def __init__(self, name=None):
...         self._name = name
...
...     def set_name(self, name):
...         self._name = name
...
...     def get_name(self):
...         return self._name
>>>
>>>
>>> astro = Astronaut()
>>> astro.set_name('Mark Watney')
>>> print(astro.get_name())
Mark Watney

Accessing class fields. Either put ``name`` as an argument for ``__init__()`` or create dynamic field in runtime:

>>> class Astronaut:
...     def __init__(self, name=None):
...         self.name = name
>>>
>>>
>>> astro = Astronaut()
>>> astro.name = 'Mark Watney'
>>> print(astro.name)
Mark Watney


Property class
--------------
* Property's arguments are method references ``get_name``, ``set_name``, ``del_name`` and a docstring
* Not recommended

>>> class Astronaut:
...     def __init__(self, name=None):
...         self._name = name
...
...     def get_name(self):
...         return self._name
...
...     def set_name(self, value):
...         self._name = value
...
...     def del_name(self):
...         del self._name
...
...     name = property(get_name, set_name, del_name, "I am the 'name' property.")


Property Descriptor
-------------------
* Prefer ``name = property()``

>>> class Astronaut:
...     name = property()
...
...     def __init__(self, name=None):
...         self._name = name
...
...     @name.getter
...     def name(self):
...         return self._name
...
...     @name.setter
...     def name(self, value):
...         self._name = value
...
...     @name.deleter
...     def name(self):
...         del self._name


Property Decorator
------------------
* Typically used when, there is only getter and no setter and deleter methods

>>> class Astronaut:
...     def __init__(self, name=None):
...         self._name = name
...
...     @property
...     def name(self):
...         return self._name
...
...     @name.setter
...     def name(self, value):
...         self._name = value
...
...     @name.deleter
...     def name(self):
...         del self._name


Use Case - 0x01
---------------
>>> class Astronaut:
...     def __init__(self):
...         self._name = None
...
...     def set_name(self, name):
...         self._name = name.title()
...
...     def get_name(self):
...         if self._name:
...             firstname, lastname = self._name.split()
...             return f'{firstname} {lastname[0]}.'
...
...     def del_name(self):
...         self._name = None
>>>
>>>
>>> astro = Astronaut()
>>>
>>> astro.set_name('MARK WaTNeY')
>>> print(astro.get_name())
Mark W.
>>>
>>> astro.del_name()
>>> print(astro.get_name())
None

>>> class Astronaut:
...     name = property()
...
...     def __init__(self):
...         self._name = None
...
...     @name.getter
...     def name(self):
...         if self._name:
...             firstname, lastname = self._name.split()
...             return f'{firstname} {lastname[0]}.'
...
...     @name.setter
...     def name(self, name):
...         self._name = name.title()
...
...     @name.deleter
...     def name(self):
...         self._name = None
>>>
>>>
>>> astro = Astronaut()
>>>
>>> astro.name = 'MARK WaTNeY'
>>> print(astro.name)
Mark W.
>>>
>>> del astro.name
>>> print(astro.name)
None


Use Case - 0x02
---------------
* Calculate age

>>> from dataclasses import dataclass
>>> from datetime import date
>>>
>>> DAY = 1
>>> YEAR = 365.25 * DAY
>>> TODAY = date(2000, 1, 1)  # date.today()
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     birthday: date
...
...     @property
...     def age(self):
...         age = TODAY - self.birthday
...         return round(age.days/YEAR, 1)
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney', date(1969, 7, 21))
>>> print(astro.age)
30.4


Use Case - 0x03
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
... class Astronaut:
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
>>> astro = Astronaut('Mark', 'Watney', date(1969, 7, 21))
>>> print(astro.age)
30.4


Use Case - 0x04
---------------
>>> class Temperature:
...     def __init__(self, initial_temperature):
...         self._protected = initial_temperature
...
...     @property
...     def value(self):
...         print('You are trying to access a value')
...         return self._protected
>>>
>>>
>>> t = Temperature(100)
>>>
>>> print(t.value)
You are trying to access a value
100

>>> class Temperature:
...     def __init__(self, initial_temperature):
...         self._protected = initial_temperature
...
...     @property
...     def value(self):
...         return self._protected
...
...     @value.setter
...     def value(self, new_value):
...         if new_value < 0.0:
...             raise ValueError('Kelvin Temperature cannot be negative')
...         else:
...             self._protected = new_value
>>>
>>>
>>> t = Temperature(100)
>>> t.value = -10
Traceback (most recent call last):
ValueError: Kelvin Temperature cannot be negative

>>> class Temperature:
...     def __init__(self, initial_temperature):
...         self._protected = initial_temperature
...
...     @property
...     def value(self):
...         return self._protected
...
...     @value.deleter
...     def value(self):
...         print('Resetting temperature')
...         self._protected = 0.0
>>>
>>>
>>> t = Temperature(100)
>>>
>>> del t.value
Resetting temperature
>>>
>>> print(t.value)
0.0


Use Case - 0x04
---------------
>>> class Astronaut:
...     name = property()
...     _name: str
...
...     def __init__(self, name):
...         self.name = name
...
...     @name.getter
...     def name(self):
...         return self._name
...
...     @name.setter
...     def name(self, new_name):
...         if any(letter in '0123456789' for letter in new_name):
...             raise ValueError('Name cannot have digits')
...         self._name = new_name
...
...     @name.deleter
...     def name(self):
...         self._name = None

>>> astro = Astronaut('Mark Watney')
>>> astro.name = 'Melissa Lewis'
>>> astro.name = 'Rick Martinez 1'
Traceback (most recent call last):
ValueError: Name cannot have digits

>>> astro = Astronaut('Mark Watney')
>>> astro = Astronaut('Rick Martinez 1')
Traceback (most recent call last):
ValueError: Name cannot have digits

>>> astro = Astronaut('Mark Watney')
>>> print(f'Name is: {astro.name}')
Name is: Mark Watney
>>>
>>> del astro.name
>>> print(f'Name is: {astro.name}')
Name is: None





Assignments
-----------
.. literalinclude:: assignments/protocol_property_a.py
    :caption: :download:`Solution <assignments/protocol_property_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/protocol_property_b.py
    :caption: :download:`Solution <assignments/protocol_property_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/protocol_property_c.py
    :caption: :download:`Solution <assignments/protocol_property_c.py>`
    :end-before: # Solution
