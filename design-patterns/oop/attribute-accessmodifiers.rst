OOP Attribute Access Modifiers
==============================
* Attributes and methods are always public
* No protected and private keywords
* Private and protected is only by convention [#pydocprivatevar]_
* ``name`` - public attribute
* ``_name`` - protected attribute (non-public by convention)
* ``__name`` - private attribute (name mangling)
* ``__name__`` - system attribute (dunder)
* ``name_`` - avoid name collision with built-ins

>>> class Astronaut:
...     firstname: str          # public
...     lastname: str           # public
...     _height: int            # public, but... protected by convention
...     _weight: int            # public, but... protected by convention
...     __salary: str           # public, but... private by convention (name mangling)
...     __address: str          # public, but... private by convention (name mangling)
...     id_: int                # public, but... public, avoid name collision
...     type_: str              # public, but... public, avoid name collision
...     __doc__: str            # public, but... special meaning built-in (dunder)
...     __module__: str         # public, but... special meaning built-in (dunder)
...     __version__: str        # public, but... special meaning custom made (dunder)
...     __author__: str         # public, but... special meaning custom made (dunder)


SetUp
-----
>>> from dataclasses import dataclass


Example
-------
>>> class Astronaut:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
...         self._salary = 10_000
...         self._address = '2101 E NASA Pkwy, Houston 77058, Texas, USA'
...         self.__username = 'mwatney'
...         self.__password = 'ares3'
...         self.id_ = 1337
...         self.type_ = 'astronaut'
...         self.__doc__ = 'Class representing an Astronaut'
...         self.__module__ = '__main__'
...         self.__version__ = '1.0.0'
...         self.__author__ = 'Mark Watney <mwatney@nasa.gov>'


Public Attribute
----------------
* ``name`` - public attribute

>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')

To print attributes directly:

>>> print(mark.firstname)
Mark
>>>
>>> print(mark.lastname)
Watney

To list all the attributes once again we can use `vars()`:

>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}


Protected Attribute
-------------------
* ``_name`` - protected attribute (non-public by convention)

>>> @dataclass
... class Astronaut:
...     _firstname: str
...     _lastname: str
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')

Python will allow the following statement, however your IDE should
warn you "Access to a protected member _firstname of a class":

>>> print(mark._firstname)
Mark
>>>
>>> print(mark._lastname)
Watney

To list all the attributes once again we can use `vars()`:

>>> vars(mark)
{'_firstname': 'Mark', '_lastname': 'Watney'}


Private Attribute
-----------------
* ``__name`` - private attribute (name mangling)

>>> @dataclass
... class Astronaut:
...     __firstname: str
...     __lastname: str
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')

There are no attributes with names ``__firstname`` and ``__lastname``:

>>> print(mark.__firstname)
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute '__firstname'
>>>
>>> print(mark.__lastname)
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute '__lastname'

To print attributes directly:

>>> print(mark._Astronaut__firstname)
Mark
>>>
>>> print(mark._Astronaut__lastname)
Watney

To list all the attributes once again we can use `vars()`:

>>> vars(mark)  # doctest: +NORMALIZE_WHITESPACE
{'_Astronaut__firstname': 'Mark',
 '_Astronaut__lastname': 'Watney'}


Name Mangling
-------------
Name mangling is a mechanism which adds the class name to the field name.
It is particularly useful when we have an inheritance and the child class
is overwriting parent field, which we eventually want to get:

>>> class FormalEnglish:
...     __greeting: str = 'Good Morning'
...     __farewell: str = 'Goodbye'
...     greeting = __greeting
...     farewell = __farewell
>>>
>>>
>>> class SlangEnglish(FormalEnglish):
...     __greeting: str = 'Wassup'
...     __farewell: str = 'Cya'
...     greeting = __greeting
...     farewell = __farewell
>>>
>>>
>>> lang = SlangEnglish()

As expected, when accessing field we will get the latest value.
The previous value was overwritten by inheritance.

>>> lang.greeting
'Wassup'
>>>
>>> lang.farewell
'Cya'

However thanks to the name mangling we have an additional access to both
``FormalEnglish`` and ``SlangEnglish`` fields:

>>> lang._FormalEnglish__greeting
'Good Morning'
>>>
>>> lang._FormalEnglish__farewell
'Goodbye'
>>>
>>> lang._SlangEnglish__greeting
'Wassup'
>>>
>>> lang._SlangEnglish__farewell
'Cya'

Name mangling works for both class variables and instance variables.


Name Collision
--------------
* Example colliding names: ``type_``, ``id_``, ``hash_``

>>> type_ = type('myobject')
>>> id_ = id('myobject')
>>> hash_ = hash('myobject')

Example:

>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.type_ = type(self)
...         self.id_ = id(self)
...         self.hash_ = hash(self)


System Attributes
-----------------
* ``__name__`` - Current module
* ``obj.__class__`` - Class from which object was instantiated
* ``obj.__dict__`` - Stores instance variables
* ``obj.__doc__`` - Object docstring
* ``obj.__annotations__`` - Object attributes type annotations
* ``obj.__module__`` - Name of a module in which object was defined

>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')

>>> mark.__class__
<class '__main__.Astronaut'>
>>>
>>> mark.__dict__
{'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> mark.__doc__
'Astronaut(firstname: str, lastname: str)'
>>>
>>> mark.__annotations__
{'firstname': <class 'str'>, 'lastname': <class 'str'>}
>>>
>>> mark.__module__
'__main__'


Show Attributes
---------------
* ``vars()`` display ``obj.__dict__``

>>> class Astronaut:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
...         self._salary = 10_000
...         self._address = '2101 E NASA Pkwy, Houston 77058, Texas, USA'
...         self.__username = 'mwatney'
...         self.__password = 'ares3'
...         self.id_ = 1337
...         self.type_ = 'astronaut'
...         self.__doc__ = 'Class representing an Astronaut'
...         self.__module__ = '__main__'
...         self.__version__ = '1.0.0'
...         self.__author__ = 'Mark Watney <mwatney@nasa.gov>'
>>>
>>>
>>> mark = Astronaut()

All attributes:

>>> vars(mark)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 '_salary': 10000,
 '_address': '2101 E NASA Pkwy, Houston 77058, Texas, USA',
 '_Astronaut__username': 'mwatney',
 '_Astronaut__password': 'ares3',
 'id_': 1337,
 'type_': 'astronaut',
 '__doc__': 'Class representing an Astronaut',
 '__module__': '__main__',
 '__version__': '1.0.0',
 '__author__': 'Mark Watney <mwatney@nasa.gov>'}

Public attributes:

>>> def get_public_attributes(obj):
...     return {attrname: attrvalue
...             for attrname in dir(obj)
...             if (attrvalue := getattr(mark, attrname))
...             and not callable(attrvalue)
...             and not attrname.startswith('_')}
>>>
>>>
>>> get_public_attributes(mark)
{'firstname': 'Mark', 'id_': 1337, 'lastname': 'Watney', 'type_': 'astronaut'}

Protected attributes:

>>> def get_protected_attributes(obj):
...     return {attrname: attrvalue
...             for attrname in dir(obj)
...             if (attrvalue := getattr(obj, attrname))
...             and not callable(attrvalue)
...             and attrname.startswith('_')
...             and not attrname.startswith(f'_{obj.__class__.__name__}_')
...             and not attrname.endswith('_')}
>>>
>>>
>>> get_protected_attributes(mark)
{'_address': '2101 E NASA Pkwy, Houston 77058, Texas, USA', '_salary': 10000}

Private attributes:

>>> def get_private_attributes(obj):
...     return {attrname: attrvalue
...             for attrname in dir(obj)
...             if (attrvalue := getattr(obj, attrname))
...             and not callable(attrvalue)
...             and attrname.startswith(f'_{obj.__class__.__name__}_')}
>>>
>>>
>>> get_private_attributes(mark)
{'_Astronaut__password': 'ares3', '_Astronaut__username': 'mwatney'}

System attributes:

>>> def get_system_attributes(obj):
...     return {attrname: attrvalue
...             for attrname in dir(obj)
...             if (attrvalue := getattr(obj, attrname))
...             and not callable(attrvalue)
...             and attrname.startswith('__')
...             and attrname.endswith('__')}
>>>
>>>
>>> get_system_attributes(mark)  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
{'__author__': 'Mark Watney <mwatney@nasa.gov>',
 '__dict__': {...},
 '__doc__': 'Class representing an Astronaut',
 '__module__': '__main__',
 '__version__': '1.0.0'}


References
----------
.. [#pydocprivatevar] https://docs.python.org/3/tutorial/classes.html#private-variables


Assignments
-----------
.. literalinclude:: assignments/oop_attribute_accessmodifiers_a.py
    :caption: :download:`Solution <assignments/oop_attribute_accessmodifiers_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_attribute_accessmodifiers_b.py
    :caption: :download:`Solution <assignments/oop_attribute_accessmodifiers_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_attribute_accessmodifiers_c.py
    :caption: :download:`Solution <assignments/oop_attribute_accessmodifiers_c.py>`
    :end-before: # Solution
