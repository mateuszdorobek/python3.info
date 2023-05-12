Protocol Reflection
===================
* When accessing an attribute
* ``setattr(obj, 'attrname', 'new_value') -> None``
* ``delattr(obj, 'attrname') -> None``
* ``getattr(obj, 'attrname', 'default_value') -> Any``
* ``hasattr(obj, 'attrname') -> bool``



>>> class Point:
...     def __init__(self, x, y, z):
...         self.x = x
...         self.y = y
...         self.z = z
...
...     def __setattr__(self, attrname, attrvalue):
...         if attrname not in {'x', 'y', 'z'}:
...             raise NameError('You can set only x, y, z attributes')
...         if type(attrvalue) not in (int,float):
...             raise TypeError('Attribute value must be int or float')
...         if attrvalue < 0:
...             raise ValueError('Attribute cannot be less than 0')
...         return super().__setattr__(attrname, attrvalue)

>>> pt = Point(1,2,3)
>>>
>>> pt.x = 1
>>>
>>> pt.x = -1
Traceback (most recent call last):
ValueError: Attribute cannot be less than 0
>>>
>>> pt.x = 'one'
Traceback (most recent call last):
TypeError: Attribute value must be int or float
>>>
>>> pt.notexisting = 1
Traceback (most recent call last):
NameError: You can set only x, y, z attributes


>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
>>>
>>>
>>> mark = Astronaut('Mark Watney')
>>>
>>> if mark._salary is None:
...     mark._salary = 100
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute '_salary'
>>>
>>>
>>> if not hasattr(mark, '_salary'):
...     mark._salary = 100
>>>
>>> print(mark._salary)
100

>>> def input(prompt):
...     return '_salary'
>>>
>>>
>>> attrname = input('Type attribute name: ')   # _salary
>>> value = getattr(mark, attrname, 'no such attribute')
>>> print(value)  # doctest: +SKIP
100

>>> def input(prompt):
...     return 'notexisting'
>>>
>>>
>>> attrname = input('Type attribute name: ')  # notexisting
>>> value = getattr(mark, attrname, 'no such attribute')
>>> print(value)
no such attribute


Protocol
--------
* ``__setattr__(self, attrname, value) -> None``
* ``__delattr__(self, attrname) -> None``
* ``__getattribute__(self, attrname, default) -> Any``
* ``__getattr__(self, attrname, default) -> Any``

>>> class Reflection:
...
...     def __setattr__(self, attrname, value):
...         ...
...
...     def __delattr__(self, attrname):
...         ...
...
...     def __getattribute__(self, attrname, default):
...         ...
...
...     def __getattr__(self, attrname, default):
...         ...


Example
-------
>>> class Immutable:
...     def __setattr__(self, attrname, value):
...         raise PermissionError('Immutable')

>>> class Protected:
...     def __setattr__(self, attrname, value):
...         if attrname.startswith('_'):
...             raise PermissionError('Field is protected')
...         else:
...             return super().__setattr__(attrname, value)


Set Attribute
-------------
* Called when trying to set attribute to a value
* Call Stack:

    * ``mark.name = 'Mark Watney'``
    * => ``setattr(mark, 'name', 'Mark Watney')``
    * => ``mark.__setattr__('name', 'Mark Watney')``

>>> class Astronaut:
...     def __setattr__(self, attrname, value):
...         if attrname.startswith('_'):
...             raise PermissionError('Field is protected')
...         else:
...             return super().__setattr__(attrname, value)
>>>
>>>
>>> mark = Astronaut()
>>>
>>> mark.name = 'Mark Watney'
>>> print(mark.name)
Mark Watney
>>>
>>> mark._salary = 100
Traceback (most recent call last):
PermissionError: Field is protected


Delete Attribute
----------------
* Called when trying to delete attribute
* Call stack:

    * ``del mark.name``
    * => ``delattr(mark, 'name')``
    * => ``mark.__delattr__(name)``

>>> class Astronaut:
...     def __delattr__(self, attrname):
...         if attrname.startswith('_'):
...             raise PermissionError('Field is protected')
...         else:
...             return super().__delattr__(attrname)
>>>
>>>
>>> mark = Astronaut()
>>>
>>> mark.name = 'Mark Watney'
>>> mark._salary = 100
>>>
>>> del mark.name
>>> del mark._salary
Traceback (most recent call last):
PermissionError: Field is protected


Get Attribute
-------------
* Called for every time, when you want to access any attribute
* Before even checking if this attribute exists
* If attribute is not found, then raises ``AttributeError`` and calls ``__getattr__()``
* Call stack:

    * ``mark.name``
    * => ``getattr(mark, 'name')``
    * => ``mark.__getattribute__('name')``
    * if ``mark.__getattribute__('name')`` raises ``AttributeError``
    * => ``mark.__getattr__('name')``

>>> class Astronaut:
...     def __getattribute__(self, attrname):
...         if attrname.startswith('_'):
...             raise PermissionError('Field is protected')
...         else:
...             return super().__getattribute__(attrname)
>>>
>>>
>>> mark = Astronaut()
>>>
>>> mark.name = 'Mark Watney'
>>> print(mark.name)
Mark Watney
>>>
>>> print(mark._salary)
Traceback (most recent call last):
PermissionError: Field is protected


Get Attribute if Missing
------------------------
* Called whenever you request an attribute that hasn't already been defined
* It will not execute, when attribute already exist
* Implementing a fallback for missing attributes

Example ``__getattr__()``:

>>> class Astronaut:
...     def __init__(self):
...         self.name = None
...
...     def __getattr__(self, attrname):
...         return 'Sorry, field does not exist'
>>>
>>>
>>> mark = Astronaut()
>>> mark.name = 'Mark Watney'
>>>
>>> print(mark.name)
Mark Watney
>>>
>>> print(mark._salary)
Sorry, field does not exist

>>> class Astronaut:
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
>>> mark = Astronaut()
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


Has Attribute
-------------
* Check if object has attribute
* There is no ``__hasattr__()`` method
* Calls ``__getattribute__()`` and checks if raises ``AttributeError``

>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
>>>
>>>
>>> mark = Astronaut('Mark Watney')
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


Use Case - 0x01
---------------
>>> class Astronaut:
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
>>> mark = Astronaut()
>>>
>>> mark.name = 'Mark Watney'
>>> print(mark.name)
Mark Watney
>>>
>>> mark._salary = 100
Traceback (most recent call last):
PermissionError: Field is protected
>>>
>>> print(mark._salary)
Traceback (most recent call last):
PermissionError: Field is protected


Use Case - 0x02
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


Use Case - 0x03
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


Use Case - 0x04
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
.. literalinclude:: assignments/protocol_reflection_a.py
    :caption: :download:`Solution <assignments/protocol_reflection_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/protocol_reflection_b.py
    :caption: :download:`Solution <assignments/protocol_reflection_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/protocol_reflection_c.py
    :caption: :download:`Solution <assignments/protocol_reflection_c.py>`
    :end-before: # Solution
