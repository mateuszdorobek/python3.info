Operator Reflection
===================
* When accessing an attribute
* ``setattr(obj, attrname, value) -> None``
* ``delattr(obj, attrname) -> None``
* ``getattr(obj, attrname, default) -> Any``
* ``hasattr(obj, attrname) -> bool``
* ``__setattr__(self, attrname, value) -> None``
* ``__delattr__(self, attrname) -> None``
* ``__getattribute__(self, attrname) -> Any``
* ``__getattr__(self, attrname) -> Any``

Reflection is the ability of a program to examine and modify its own
structure and behavior at runtime. In Python, reflection is supported
through a number of built-in functions and modules.

The ``inspect`` module provides a set of functions for introspecting Python
objects, such as classes, functions, and modules. These functions can be
used to examine the attributes, methods, and source code of an object, as
well as its inheritance hierarchy and type information.

Here's an example of using the ``inspect`` module to examine the attributes
and methods of a class:

>>> import inspect
>>>
>>> class MyClass:
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
...
...     def my_method(self, z):
...         return self.x + self.y + z
>>>
>>> # Use inspect to examine the attributes and methods of MyClass
>>> print(inspect.getmembers(MyClass))  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
[('__class__', <class 'type'>),
 ('__delattr__', <slot wrapper '__delattr__' of 'object' objects>),
 ('__dict__', mappingproxy({'__module__': '__main__',
                            '__init__': <function MyClass.__init__ at 0x...>,
                            'my_method': <function MyClass.my_method at 0x...>,
                            '__dict__': <attribute '__dict__' of 'MyClass' objects>,
                            '__weakref__': <attribute '__weakref__' of 'MyClass' objects>,
                            '__doc__': None})),
 ('__dir__', <method '__dir__' of 'object' objects>),
 ('__doc__', None),
 ('__eq__', <slot wrapper '__eq__' of 'object' objects>),
 ('__format__', <method '__format__' of 'object' objects>),
 ('__ge__', <slot wrapper '__ge__' of 'object' objects>),
 ('__getattribute__', <slot wrapper '__getattribute__' of 'object' objects>),
 ('__getstate__', <method '__getstate__' of 'object' objects>),
 ('__gt__', <slot wrapper '__gt__' of 'object' objects>),
 ('__hash__', <slot wrapper '__hash__' of 'object' objects>),
 ('__init__', <function MyClass.__init__ at 0x...>),
 ('__init_subclass__', <built-in method __init_subclass__ of type object at 0x...>),
 ('__le__', <slot wrapper '__le__' of 'object' objects>),
 ('__lt__', <slot wrapper '__lt__' of 'object' objects>),
 ('__module__', '__main__'),
 ('__ne__', <slot wrapper '__ne__' of 'object' objects>),
 ('__new__', <built-in method __new__ of type object at 0x...>),
 ('__reduce__', <method '__reduce__' of 'object' objects>),
 ('__reduce_ex__', <method '__reduce_ex__' of 'object' objects>),
 ('__repr__', <slot wrapper '__repr__' of 'object' objects>),
 ('__setattr__', <slot wrapper '__setattr__' of 'object' objects>),
 ('__sizeof__', <method '__sizeof__' of 'object' objects>),
 ('__str__', <slot wrapper '__str__' of 'object' objects>),
 ('__subclasshook__', <built-in method __subclasshook__ of type object at 0x...>),
 ('__weakref__', <attribute '__weakref__' of 'MyClass' objects>),
 ('my_method', <function MyClass.my_method at 0x...>)]

In this example, the ``getmembers()`` function from the ``inspect`` module
is used to examine the attributes and methods of the ``MyClass`` class.
The output shows a list of tuples, where each tuple contains the name
and value of an attribute or method of the class.

Another way to use reflection in Python is through the ``getattr()`` and
``setattr()`` built-in functions. These functions allow you to get and set
attributes of an object dynamically at runtime, based on their name.

Here's an example of using ``getattr()`` and ``setattr()`` to get and set
attributes of an object:

>>> class MyClass:
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
>>>
>>> # Create an instance of MyClass
>>> obj = MyClass(1, 2)
>>>
>>> # Use getattr to get the value of an attribute dynamically
>>> x_value = getattr(obj, 'x')
>>> print(x_value)
1
>>>
>>> # Use setattr to set the value of an attribute dynamically
>>> setattr(obj, 'y', 3)
>>> print(obj.y)
3


In this example, ``getattr()`` is used to get the value of the ``x`` attribute
of the ``obj`` instance of ``MyClass``, and ``setattr()`` is used to set the
value of the ``y`` attribute of ``obj`` to 3.

Protocol:

>>> class Reflection:
...
...     def __setattr__(self, attrname, value):
...         ...
...
...     def __delattr__(self, attrname):
...         ...
...
...     def __getattribute__(self, attrname):
...         ...
...
...     def __getattr__(self, attrname):
...         ...


Problem
-------
>>> class Point:
...     x = property()
...     y = property()
...     z = property()
...
...     @x.setter
...     def x(self, value):
...         if value < 0:
...             raise ValueError('Coordinate cannot be negative')
...         self._x = value
...
...     @x.getter
...     def x(self):
...         return self._x
...
...     @y.setter
...     def y(self, value):
...         if value < 0:
...             raise ValueError('Coordinate cannot be negative')
...         self._y = value
...
...     @y.getter
...     def y(self):
...         return self._y
...
...     @z.setter
...     def z(self, value):
...         if value < 0:
...             raise ValueError('Coordinate cannot be negative')
...         self._z = value
...
...     @z.getter
...     def z(self):
...         return self._z

>>> pt = Point()
>>> pt.x = 1
>>> pt.y = 2
>>> pt.z = 3
>>>
>>> pt.x = -1
Traceback (most recent call last):
ValueError: Coordinate cannot be negative
>>>
>>> pt.y = -2
Traceback (most recent call last):
ValueError: Coordinate cannot be negative
>>>
>>> pt.z = -3
Traceback (most recent call last):
ValueError: Coordinate cannot be negative


Set Attribute
-------------
* Called when trying to set attribute to a value
* Typing ``obj.attrname = value``
* Will call ``setattr(obj, attrname, value)``
* Which triggers ``obj.__setattr__(attrname, value)``

>>> class Point:
...     x: int
...     y: int
...     z: int
...
...     def __setattr__(self, attrname, value):
...         if value < 0:
...             raise ValueError('Coordinate cannot be negative')
...         super().__setattr__(attrname, value)

>>> pt = Point()
>>> pt.x = 1
>>> pt.y = 2
>>> pt.z = 3

>>> pt.x = -1
Traceback (most recent call last):
ValueError: Coordinate cannot be negative
>>>
>>> pt.y = -2
Traceback (most recent call last):
ValueError: Coordinate cannot be negative
>>>
>>> pt.z = -3
Traceback (most recent call last):
ValueError: Coordinate cannot be negative

This is because, when you do: ``pt.x = 1`` Python will call
``setattr(pt, 'x', 1)`` for you, which triggers ``pt.__setattr__('x', 1)``.

>>> pt = Point()
>>> pt.x = 1
>>> pt.x
1

>>> pt = Point()
>>> setattr(pt, 'x', 1)
>>> pt.x
1

>>> pt = Point()
>>> pt.__setattr__('x', 1)
>>> pt.x
1


Delete Attribute
----------------
* Called when trying to delete attribute
* Typing ``del obj.attrname``
* Will call ``delattr(obj, attrname)``
* Which triggers ``mark.__delattr__(name)``

>>> class Point:
...     x: int
...     y: int
...     z: int
...
...     def __delattr__(self, attrname):
...         self.__setattr__(attrname, 0)

>>> pt = Point()
>>> pt.x = 1
>>> pt.y = 2
>>> pt.z = 3

>>> del pt.x, pt.y, pt.z
>>> pt.x, pt.y, pt.z
(0, 0, 0)

>>> del pt.x
>>> pt.x
0

>>> delattr(pt, 'x')
>>> pt.x
0

>>> pt.__delattr__('x')
>>> pt.x
0


Get Attribute If Exists
-----------------------
* Called for every time, when you want to access any attribute
* Before even checking if this attribute exists
* If attribute is not found, then raises ``AttributeError`` and calls ``__getattr__()``
* Typing ``obj.attrname``
* Will call ``getattr(obj, attrname)``
* Which triggers ``obj.__getattribute__(attrname)``
* If ok: then return value
* If error: then call ``obj.__getattr__(attrname)``

>>> class Point:
...     x: int
...     y: int
...     z: int
...
...     def __getattribute__(self, attrname):
...         if attrname == 'y':
...             raise PermissionError(f'Attribute {attrname} access is forbidden')
...         return super().__getattribute__(attrname)

>>> pt = Point()
>>> pt.x = 1
>>> pt.y = 2
>>> pt.z = 3

>>> pt.x
1

>>> pt.y
Traceback (most recent call last):
PermissionError: Attribute y access is forbidden


Get Attribute If Missing
------------------------
* Called whenever you request an attribute that hasn't already been defined
* It will not execute, when attribute already exist
* Implementing a fallback for missing attributes

>>> class Point:
...     x: int
...     y: int
...     z: int
...
...     def __getattr__(self, attrname):
...         print(f'Attribute {attrname} does not exist')
...         super().__setattr__(attrname, 0)
...         print(f'Attribute {attrname} initialized with value 0')

>>> pt = Point()

>>> vars(pt)
{}

>>> pt.x
Attribute x does not exist
Attribute x initialized with value 0
>>>
>>> pt.x
0

>>> vars(pt)
{'x': 0}


Has Attribute
-------------
* Check if object has attribute
* There is no ``__hasattr__()`` method
* Calling ``hasattr(obj, attrname)``
* Will call ``__getattribute__()`` and checks if raises ``AttributeError``
* If no exception, then return ``True``
* If exception, then call ``__getattr__()`` and check
* If ``__getattr__()`` succeeds then return ``True``
* If ``__getattr__()`` fail then return ``False``

>>> class Point:
...     x: int
...     y: int
...     z: int

>>> pt = Point()
>>> pt.x = 1
>>> pt.y = 2

>>> hasattr(pt, 'x')
True
>>>
>>> hasattr(pt, 'y')
True
>>>
>>> hasattr(pt, 'z')
False
>>>
>>> hasattr(pt, 'other')
False


Use Case - 0x01
---------------
>>> class Point:
...     x: int
...     y: int
...     z: int
...
...     def __setattr__(self, attrname, value):
...         if attrname not in ('x', 'y', 'z'):
...             raise NameError('You can set only x, y, z attributes')
...         if type(value) not in (int,float):
...             raise TypeError('Attribute value must be int or float')
...         if value < 0:
...             raise ValueError('Attribute value cannot be negative')
...         return super().__setattr__(attrname, value)

>>> pt = Point()
>>> pt.x = 1
>>> pt.y = 2
>>> pt.z = 3
>>>
>>> pt.x = -1
Traceback (most recent call last):
ValueError: Attribute value cannot be negative
>>>
>>> pt.x = 'one'
Traceback (most recent call last):
TypeError: Attribute value must be int or float
>>>
>>> pt.notexisting = 1
Traceback (most recent call last):
NameError: You can set only x, y, z attributes


Use Case - 0x02
---------------
* Get Attribute Both

>>> class Point:
...     x: int
...     y: int
...     z: int
...
...     def __getattribute__(self, attrname):
...         if attrname == 'y':
...             raise PermissionError('Attribute y access is forbidden')
...         return super().__getattribute__(attrname)
...
...     def __getattr__(self, attrname):
...         print(f'Attribute {attrname} does not exist')
...         super().__setattr__(attrname, 0)
...         print(f'Attribute {attrname} initialized with value 0')

>>> pt = Point()
>>>
>>> pt.x = 1
>>> pt.y = 2
>>>
>>> vars(pt)
{'x': 1, 'y': 2}

>>> pt.x
1

>>> pt.y
Traceback (most recent call last):
PermissionError: Attribute y access is forbidden

>>> pt.z
Attribute z does not exist
Attribute z initialized with value 0
>>>
>>> pt.z
0

>>> vars(pt)
{'x': 1, 'y': 2, 'z': 0}


Use Case - 0x03
---------------
>>> class User:
...     def __setattr__(self, attrname, value):
...         if attrname.startswith('_'):
...             raise PermissionError('Field is protected')
...         else:
...             return super().__setattr__(attrname, value)
>>>
>>>
>>> mark = User()
>>> mark.name = 'Mark Watney'
>>> print(mark.name)
Mark Watney
>>>
>>> mark._salary = 1000
Traceback (most recent call last):
PermissionError: Field is protected


Use Case - 0x04
---------------
>>> class User:
...     def __delattr__(self, attrname):
...         if attrname.startswith('_'):
...             raise PermissionError('Field is protected')
...         else:
...             return super().__delattr__(attrname)
>>>
>>>
>>> mark = User()
>>> mark.name = 'Mark Watney'
>>> mark._salary = 1000
>>>
>>> del mark.name
>>> del mark._salary
Traceback (most recent call last):
PermissionError: Field is protected


Use Case - 0x05
---------------
>>> class User:
...     def __getattribute__(self, attrname):
...         if attrname.startswith('_'):
...             raise PermissionError('Field is protected')
...         else:
...             return super().__getattribute__(attrname)
>>>
>>>
>>> mark = User()
>>>
>>> mark.name = 'Mark Watney'
>>> print(mark.name)
Mark Watney
>>>
>>> print(mark._salary)
Traceback (most recent call last):
PermissionError: Field is protected


Use Case - 0x06
---------------
>>> class User:
...     def __init__(self, name):
...         self.name = name
>>>
>>>
>>> mark = User('Mark Watney')
>>>
>>> hasattr(mark, 'name')
True
>>>
>>> hasattr(mark, 'mission')
False
>>>
>>> mark.mission = 'Ares3'
>>> hasattr(mark, 'mission')
True


Use Case - 0x07
---------------
>>> class User:
...     def __init__(self):
...         self.name = None
...
...     def __getattr__(self, attrname):
...         return 'Sorry, field does not exist'
>>>
>>>
>>> mark = User()
>>> mark.name = 'Mark Watney'
>>>
>>> print(mark.name)
Mark Watney
>>>
>>> print(mark._salary)
Sorry, field does not exist

>>> class User:
...     def __init__(self):
...         self.name = None
...
...     def __getattribute__(self, attrname):
...         print('Getattribute called... ')
...         result = super().__getattribute__(attrname)
...         print(f'Result was: "{result}"')
...         return result
...
...     def __getattr__(self, attrname):
...         print('Not found. Getattr called...')
...         print(f'Creating attribute {attrname} with `None` value')
...         super().__setattr__(attrname, None)
>>>
>>>
>>>
>>> mark = User()
>>> mark.name = 'Mark Watney'
>>>
>>> mark.name  # doctest: +NORMALIZE_WHITESPACE
Getattribute called...
Result was: "Mark Watney"
'Mark Watney'
>>>
>>> mark._salary  # doctest: +NORMALIZE_WHITESPACE
Getattribute called...
Not found. Getattr called...
Creating attribute _salary with `None` value
>>>
>>> mark._salary  # doctest: +NORMALIZE_WHITESPACE
Getattribute called...
Result was: "None"


Use Case - 0x08
---------------
>>> class User:
...     def __getattribute__(self, attrname):
...         if attrname.startswith('_'):
...             raise PermissionError('Field is protected')
...         else:
...             return super().__getattribute__(attrname)
...
...     def __setattr__(self, attrname, value):
...         if attrname.startswith('_'):
...             raise PermissionError('Field is protected')
...         else:
...             return super().__setattr__(attrname, value)
>>>
>>>
>>> mark = User()
>>>
>>> mark.name = 'Mark Watney'
>>> print(mark.name)
Mark Watney
>>>
>>> mark._salary = 1000
Traceback (most recent call last):
PermissionError: Field is protected
>>>
>>> print(mark._salary)
Traceback (most recent call last):
PermissionError: Field is protected


Use Case - 0x09
---------------
>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> mark = User('Mark', 'Watney')
>>>
>>> if mark._salary is None:
...     mark._salary = 1000
Traceback (most recent call last):
AttributeError: 'User' object has no attribute '_salary'
>>>
>>>
>>> if not hasattr(mark, '_salary'):
...     mark._salary = 1000
>>>
>>> print(mark._salary)
1000

>>> def input(prompt):
...     return '_salary'
>>>
>>>
>>> attrname = input('Type attribute name: ')   # _salary
>>> value = getattr(mark, attrname, 'no such attribute')
>>> print(value)  # doctest: +SKIP
1000

>>> def input(prompt):
...     return 'notexisting'
>>>
>>>
>>> attrname = input('Type attribute name: ')  # notexisting
>>> value = getattr(mark, attrname, 'no such attribute')
>>> print(value)
no such attribute


Use Case - 0x0A
---------------
>>> class User:
...     def __init__(self, firstname, lastname, username, password):
...         self.firstname = firstname
...         self.lastname = lastname
...         self._username = username
...         self._password = password
...
...     def __getattribute__(self, attrname):
...         if attrname in ('_username', '_password'):
...             raise PermissionError('Access to this field is forbidden')
...         return super().__getattribute__(attrname)

>>> mark = User('Mark', 'Watney', username='mwatney', password='Ares3')

>>> mark.firstname
'Mark'
>>> mark.lastname
'Watney'

>>> mark._username
Traceback (most recent call last):
PermissionError: Access to this field is forbidden
>>>
>>> mark._password
Traceback (most recent call last):
PermissionError: Access to this field is forbidden

>>> vars(mark)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 '_username': 'mwatney',
 '_password': 'Ares3'}


Use Case - 0x0B
---------------
>>> class User:
...     def __init__(self, firstname, lastname, username, password):
...         self.firstname = firstname
...         self.lastname = lastname
...         self._username = username
...         self._password = password
...
...     def __getattribute__(self, attrname):
...         return super().__getattribute__(attrname)
...
...     def __setattr__(self, attrname, value):
...         if not hasattr(self, attrname) and attrname in ('_username', '_password'):
...             return super().__setattr__(attrname, value)
...         if attrname.startswith('_'):
...             raise PermissionError('Access to this field is forbidden')
...         return super().__setattr__(attrname, value)

>>> mark = User('Mark', 'Watney', username='mwatney', password='Ares3')

>>> mark._salary = 1000
Traceback (most recent call last):
PermissionError: Access to this field is forbidden

>>> vars(mark)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 '_username': 'mwatney',
 '_password': 'Ares3'}

>>> mark._username = 'mlewis'
Traceback (most recent call last):
PermissionError: Access to this field is forbidden


Use Case - 0x0C
---------------
>>> class User:
...     def __init__(self, firstname, lastname, username, password):
...         self.firstname = firstname
...         self.lastname = lastname
...         self._username = username
...         self._password = password
...
...     def __delattr__(self, attrname):
...         self.__setattr__(attrname, None)

>>> mark = User('Mark', 'Watney', username='mwatney', password='Ares3')

>>> vars(mark)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 '_username': 'mwatney',
 '_password': 'Ares3'}

>>> del mark._username
>>> del mark._password

>>> vars(mark)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 '_username': None,
 '_password': None}


Use Case - 0x0D
---------------
>>> class User:
...     def __init__(self, firstname, lastname, username, password):
...         self.firstname = firstname
...         self.lastname = lastname
...         self._username = username
...         self._password = password
...
...     def __getattribute__(self, attrname):
...         if attrname.startswith('_'):
...             raise PermissionError('Access to this field is forbidden')
...         return super().__getattribute__(attrname)

>>> mark = User('Mark', 'Watney', username='mwatney', password='Ares3')

>>> vars(mark)
Traceback (most recent call last):
PermissionError: Access to this field is forbidden
>>>
>>> mark.__dict__
Traceback (most recent call last):
PermissionError: Access to this field is forbidden

>>> dir(mark)
Traceback (most recent call last):
PermissionError: Access to this field is forbidden
>>>
>>> mark.__dir__()
Traceback (most recent call last):
PermissionError: Access to this field is forbidden

>>> help(mark)
Traceback (most recent call last):
PermissionError: Access to this field is forbidden
>>>
>>> mark.__doc__
Traceback (most recent call last):
PermissionError: Access to this field is forbidden

>>> type(mark)
<class '__main__.User'>
>>>
>>> mark.__class__
Traceback (most recent call last):
PermissionError: Access to this field is forbidden


Use Case - 0x0E
---------------
>>> class User:
...     def __init__(self, firstname, lastname, username, password):
...         self.firstname = firstname
...         self.lastname = lastname
...         self._username = username
...         self._password = password
...
...     def __getattribute__(self, attrname):
...         if attrname.startswith('_') and not attrname.startswith('__'):
...             raise PermissionError('Access to this field is forbidden')
...         return super().__getattribute__(attrname)

>>> mark = User('Mark', 'Watney', username='mwatney', password='Ares3')

>>> vars(mark)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 '_username': 'mwatney',
 '_password': 'Ares3'}

>>> mark._username
Traceback (most recent call last):
PermissionError: Access to this field is forbidden

>>> mark._password
Traceback (most recent call last):
PermissionError: Access to this field is forbidden


Use Case - 0x0F
---------------
>>> class User:
...     def __init__(self, firstname, lastname, phone, email, username, password):
...         self.firstname = firstname
...         self.lastname = lastname
...         self._phone = phone
...         self._email = email
...         self.__username = username
...         self.__password = password
...
...     def __getattribute__(self, attrname):
...         if attrname.startswith('_') and not attrname.startswith('__'):
...             raise PermissionError('Access to this field is forbidden')
...         return super().__getattribute__(attrname)

>>> mark = User(
...     firstname='Mark',
...     lastname='Watney',
...     phone='+1 (234) 555 1337',
...     email='mwatney@nasa.gov',
...     username='mwatney',
...     password='Ares3',
... )

>>> vars(mark)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 '_phone': '+1 (234) 555 1337',
 '_email': 'mwatney@nasa.gov',
 '_User__username': 'mwatney',
 '_User__password': 'Ares3'}

>>> mark._email
Traceback (most recent call last):
PermissionError: Access to this field is forbidden

>>> mark._phone
Traceback (most recent call last):
PermissionError: Access to this field is forbidden

>>> mark._User__username
Traceback (most recent call last):
PermissionError: Access to this field is forbidden

>>> mark._User__password
Traceback (most recent call last):
PermissionError: Access to this field is forbidden


Use Case - 0x10
---------------
>>> class Immutable:
...     def __setattr__(self, attrname, value):
...         raise PermissionError('Immutable')

>>> class Protected:
...     def __setattr__(self, attrname, value):
...         if attrname.startswith('_'):
...             raise PermissionError('Field is protected')
...         else:
...             return super().__setattr__(attrname, value)


Use Case - 0x11
---------------
>>> class Temperature:
...     kelvin: float
...
...     def __init__(self, kelvin):
...         self.kelvin = kelvin
...
...     def __setattr__(self, attrname, value):
...         if attrname == 'kelvin' and value < 0.0:
...             raise ValueError('Kelvin temperature cannot be negative')
...         else:
...             return super().__setattr__(attrname, value)
>>>
>>>
>>> t = Temperature(100)
>>>
>>> t.kelvin = 20
>>> print(t.kelvin)
20
>>>
>>> t.kelvin = -10
Traceback (most recent call last):
ValueError: Kelvin temperature cannot be negative


Use Case - 0x12
---------------
>>> class Temperature:
...     kelvin: float
...     celsius: float
...     fahrenheit: float
...
...     def __getattr__(self, attrname):
...         if attrname == 'kelvin':
...             return super().__getattribute__('kelvin')
...         if attrname == 'celsius':
...             return self.kelvin - 273.15
...         if attrname == 'fahrenheit':
...             return (self.kelvin-273.15) * 1.8 + 32
>>>
>>>
>>> t = Temperature()
>>> t.kelvin = 373.15
>>>
>>> print(t.kelvin)
373.15
>>> print(t.celsius)
100.0
>>> print(t.fahrenheit)
212.0


Use Case - 0x13
---------------
>>> class Container:
...     def __init__(self, **kwargs: dict) -> None:
...         for key, value in kwargs.items():
...             setattr(self, key, value)
>>>
>>>
>>> a = Container(firstname='Pan', lastname='Twardowski')
>>> vars(a)
{'firstname': 'Pan', 'lastname': 'Twardowski'}
>>>
>>> b = Container(color='red')
>>> vars(b)
{'color': 'red'}
>>>
>>> c = Container(min=1, max=10)
>>> vars(c)
{'min': 1, 'max': 10}


Assignments
-----------
.. literalinclude:: assignments/operator_reflection_a.py
    :caption: :download:`Solution <assignments/operator_reflection_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/operator_reflection_b.py
    :caption: :download:`Solution <assignments/operator_reflection_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/operator_reflection_c.py
    :caption: :download:`Solution <assignments/operator_reflection_c.py>`
    :end-before: # Solution
