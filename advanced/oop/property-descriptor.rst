OOP Property Descriptor
=======================
* Disable attribute modification
* Logging value access
* Check boundary
* Raise exceptions such as ``ValueError`` or ``TypeError``
* Check argument type

In Python you can also define a setter method for a property using the
``@propertyname.setter`` decorator. The setter method should have the same
name as the property, followed by ``.setter``, and it should take a single
parameter that represents the new value of the property.

Here's an example of using the ``@propertyname.setter`` decorator to define a
read-write property of a class:

>>> class MyClass:
...     x = property()
...
...     @x.getter
...     def x(self):
...         return self._x
...
...     @x.setter
...     def x(self, value):
...         self._x = value
>>>
>>> # Create an instance of MyClass
>>> obj = MyClass()
>>>
>>> # Change the value of the property
>>> obj.x = 1
>>>
>>> # Access the property like an attribute
>>> print(obj.x)
1

In this example, the ``MyClass`` class defines a ``x = property()``,
private attribute ``_x``.

The ``@x.getter`` decorator defines a getter method for the ``x`` property.
The ``x()`` method returns the value of the ``_x`` attribute.

The ``@x.setter`` decorator defines a setter method for the ``x`` property.
The ``x()`` method takes a single parameter ``value`` that represents the new
value of the ``_x`` attribute.

The ``obj.x = 1`` expression calls the ``x()`` setter method to set the value
of the ``_x`` attribute to 1. The ``obj.x`` expression calls the ``x()``
getter method to retrieve the new value of the ``_x`` attribute.


SetUp
-----
>>> from dataclasses import dataclass
>>> from datetime import date


Setter and Getter Methods
-------------------------
* Not only Java, but C++ and many others too

>>> class Point:
...     _x: int
...     _y: int
...     _z: int
...
...     def set_x(self, value):
...         self._x = value
...
...     def get_x(self):
...         return self._x
...
...     def set_y(self, value):
...         self._y = value
...
...     def get_y(self):
...         return self._y
...
...     def set_z(self, value):
...         self._z = value
...
...     def get_z(self):
...         return self._z

End-users code:

>>> pt = Point()
>>>
>>> pt.set_x(1)
>>> pt.set_y(2)
>>> pt.set_z(3)
>>>
>>> print(pt.get_x(), pt.get_y(), pt.get_z())
1 2 3

Let's introduce feature, that z-axis cannot be negative (value below 0).
Although we cannot change previously defined API (methods). If we change API
it will break our end-users code and we don't want that. However we can
change our class code without any problem.

Not a big of a deal. We already have placeholders to inject such validation.
What was previously considered as an overhead, eventually gave us future proof.
Very good!

But this is the Java way...

>>> class Point:
...     _x: int
...     _y: int
...     _z: int
...
...     def set_x(self, value):
...         self._x = value
...
...     def get_x(self):
...         return self._x
...
...     def set_y(self, value):
...         self._y = value
...
...     def get_y(self):
...         return self._y
...
...     def set_z(self, value):
...         if value < 0:
...             raise ValueError('Value cannot be negative')
...         self._z = value
...
...     def get_z(self):
...         return self._z

End-users code is left unchanged:

>>> pt = Point()
>>>
>>> pt.set_x(1)
>>> pt.set_y(2)
>>> pt.set_z(3)
>>>
>>> print(pt.get_x(), pt.get_y(), pt.get_z())
1 2 3

And new feature is working:

>>> pt.set_z(-1)
Traceback (most recent call last):
ValueError: Value cannot be negative


Pythonic Way
------------
>>> class Point:
...     x: int
...     y: int
...     z: int

End-user's code:

>>> pt = Point()
>>> pt.x = 1
>>> pt.y = 2
>>> pt.z = 3
>>> print(pt.x, pt.y, pt.z)
1 2 3

Let's introduce the same feature, that z-axis cannot be negative.
And still we cannot change previously defined API (methods).

Woops, we don't have placeholders to inject such validation. We previously
considered this as an overhead and we removed it. We are not future proof.

However in Python, you have properties, which is exactly for that reason.

>>> class Point:
...     x: int
...     y: int
...     z = property()
...
...     @z.getter
...     def z(self):
...         return self._z
...
...     @z.setter
...     def z(self, value):
...         if value < 0:
...             raise ValueError('Value cannot be negative')
...         self._z = value

End-users code is left unchanged:

>>> pt = Point()
>>> pt.x = 1
>>> pt.y = 2
>>> pt.z = 3
>>> print(pt.x, pt.y, pt.z)
1 2 3

And new feature is working:

>>> pt.z = -1
Traceback (most recent call last):
ValueError: Value cannot be negative


Encapsulation
-------------
Defining setter, getter and deleter methods for each property is not
a valid way to do an encapsulation. In Java there is Project Lombok
which can generate setters and getters for your fields automatically
and you can overwrite only those which need to be overwritten. But,
this not a sustainable solution and it requires a 3rd-party library
installation as dependency.

Setter and getter way:

>>> class Point:
...     _x: int
...     _y: int
...     _z: int
...
...     def set_x(self, value):
...         self._x = value
...
...     def get_x(self):
...         return self._x
...
...     def set_y(self, value):
...         self._y = value
...
...     def get_y(self):
...         return self._y
...
...     def set_z(self, value):
...         self._z = value
...
...     def get_z(self):
...         return self._z
>>>
>>>
>>> pt = Point()
>>> pt.set_x(1)
>>> pt.set_y(2)
>>> pt.set_z(3)
>>> print(pt.get_x(), pt.get_y(), pt.get_z())
1 2 3

Python properties way:

>>> class Point:
...     x = property()
...     y = property()
...     z = property()
...
...     @x.setter
...     def x(self, value):
...         if value < 0:
...             raise ValueError
...         self._x = value
...
...     @x.getter
...     def x(self):
...         return self._x
...
...     @y.setter
...     def y(self, value):
...         if value < 0:
...             raise ValueError
...         self._y = value
...
...     @y.getter
...     def y(self):
...         return self._y
...
...     @z.setter
...     def z(self, value):
...         if value < 0:
...             raise ValueError
...         self._z = value
...
...     @z.getter
...     def z(self):
...         return self._z
>>>
>>>
>>> pt = Point()
>>> pt.x = 1
>>> pt.y = 2
>>> pt.z = 3
>>> print(pt.x, pt.y, pt.z)
1 2 3

Real encapsulation is about something else. It is about creating an
abstraction over your implementation in order to be allowed to change
it in future.

>>> class Point:
...     _x: int
...     _y: int
...     _z: int
...
...     def set_position(self, x, y, z):
...         self._x = x
...         self._y = y
...         self._z = z
...
...     def get_position(self):
...         return self._x, self._y, self._z
>>>
>>>
>>> pt = Point()
>>> pt.set_position(1, 2, 3)
>>> print(pt.get_position())
(1, 2, 3)

Now, I can change from 2D to 3D without a big of a hassle.


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


Property class
--------------
* Property's arguments are method references ``get_name``, ``set_name``, ``del_name`` and a docstring
* Not recommended

>>> class User:
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

>>> class User:
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

>>> class User:
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
>>> class User:
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
>>> mark = User()
>>>
>>> mark.set_name('MARK WaTNeY')
>>> print(mark.get_name())
Mark W.
>>>
>>> mark.del_name()
>>> print(mark.get_name())
None

>>> class User:
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
>>> mark = User()
>>>
>>> mark.name = 'MARK WaTNeY'
>>> print(mark.name)
Mark W.
>>>
>>> del mark.name
>>> print(mark.name)
None


Use Case - 0x02
---------------
>>> class User:
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

>>> mark = User('Mark Watney')
>>> mark.name = 'Melissa Lewis'
>>> mark.name = 'Rick Martinez 1'
Traceback (most recent call last):
ValueError: Name cannot have digits

>>> mark = User('Mark Watney')
>>> mark = User('Rick Martinez 1')
Traceback (most recent call last):
ValueError: Name cannot have digits

>>> mark = User('Mark Watney')
>>> print(f'Name is: {mark.name}')
Name is: Mark Watney
>>>
>>> del mark.name
>>> print(f'Name is: {mark.name}')
Name is: None


Use Case - 0x06
---------------
* Kelvin is an absolute scale (no values below zero)

>>> class KelvinTemperature:
...     value: float
>>>
>>> t = KelvinTemperature()
>>> t.value = -1  # Should raise ValueError('Kelvin cannot be negative')

>>> class KelvinTemperature:
...     value = property()
...
...     @value.setter
...     def value(self, newvalue):
...         if newvalue < 0:
...             raise ValueError('Negative Kelvin Temperature')
...         self._value = newvalue
>>>
>>>
>>> t = KelvinTemperature()

This will pass:

>>> t.value = 1

This will raise an exception:

>>> t.value = -1
Traceback (most recent call last):
ValueError: Negative Kelvin Temperature


Assignments
-----------
.. literalinclude:: assignments/oop_attribute_property_descriptor_a.py
    :caption: :download:`Solution <assignments/oop_property_descriptor_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_attribute_property_descriptor_b.py
    :caption: :download:`Solution <assignments/oop_property_descriptor_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_attribute_property_descriptor_c.py
    :caption: :download:`Solution <assignments/oop_property_descriptor_c.py>`
    :end-before: # Solution
