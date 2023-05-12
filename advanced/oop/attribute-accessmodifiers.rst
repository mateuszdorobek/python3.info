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

>>> class User:
...     firstname = 'Mark'            # public
...     lastname = 'Watney'           # public
...     _phone = '+1 (234) 567-8910'  # public, but... protected by convention
...     _email = 'mwatney@nasa.gov'   # public, but... protected by convention
...     __username = 'mwatney'        # public, but... private by convention (name mangling)
...     __password = 'Ares3'          # public, but... private by convention (name mangling)
...     type_ = 'admin'               # public, but... public, avoid name collision
...     id_ = 1                       # public, but... public, avoid name collision
...     __doc__ = 'whatever'          # public, but... special meaning built-in (dunder)
...     __module__ = '__main__'       # public, but... special meaning built-in (dunder)
...     __author__ = 'Mark Watney'    # public, but... special meaning custom made (dunder)
...     __version__ = '1.0.0'         # public, but... special meaning custom made (dunder)


SetUp
-----
>>> from dataclasses import dataclass


Example
-------
>>> class User:
...     def __init__(self):
...         self.firstname = 'Mark'             # public
...         self.lastname = 'Watney'            # public
...         self._phone = '+1 (234) 567-8910'   # convention: protected
...         self._email = 'mwatney@nasa.gov'    # convention: protected
...         self.__username = 'mwatney'         # convention: private (name mangling)
...         self.__password = 'Ares3'           # convention: private (name mangling)
...         self.type_ = 'admin'                # convention: name collision avoidance (input, type, id, vars, print, sum, max, min)
...         self.id_ = 1                        # convention: name collision avoidance
...         self.__doc__ = 'whatever'           # internals: system field
...         self.__module__ = '__main__'        # internals: system field
...         self.__author__ = 'Mark Watney'     # convention: special fields
...         self.__version__ = '1.0.0'          # convention: special fields

>>> mark = User()
>>>
>>> vars(mark)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 '_phone': '+1 (234) 567-8910',
 '_email': 'mwatney@nasa.gov',
 '_User__username': 'mwatney',
 '_User__password': 'Ares3',
 'type_': 'admin',
 'id_': 1,
 '__doc__': 'whatever',
 '__module__': '__main__',
 '__author__': 'Mark Watney',
 '__version__': '1.0.0'}


Public Attribute
----------------
* ``name`` - public attribute

>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
>>>
>>>
>>> mark = User('Mark', 'Watney')

To print attributes directly:

>>> print(mark.firstname)
Mark
>>>
>>> print(mark.lastname)
Watney

To list all the attributes once again we can use ``vars()``:

>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}


Protected Attribute
-------------------
* ``_name`` - protected attribute (non-public by convention)

>>> @dataclass
... class User:
...     _firstname: str
...     _lastname: str
>>>
>>>
>>> mark = User('Mark', 'Watney')

Python will allow the following statement, however your IDE should
warn you "Access to a protected member _firstname of a class":

>>> print(mark._firstname)
Mark
>>>
>>> print(mark._lastname)
Watney

To list all the attributes once again we can use ``vars()``:

>>> vars(mark)
{'_firstname': 'Mark', '_lastname': 'Watney'}


Private Attribute
-----------------
* ``__name`` - private attribute (name mangling)

>>> @dataclass
... class User:
...     __firstname: str
...     __lastname: str
>>>
>>>
>>> mark = User('Mark', 'Watney')

There are no attributes with names ``__firstname`` and ``__lastname``:

>>> print(mark.__firstname)
Traceback (most recent call last):
AttributeError: 'User' object has no attribute '__firstname'
>>>
>>> print(mark.__lastname)
Traceback (most recent call last):
AttributeError: 'User' object has no attribute '__lastname'

To print attributes directly:

>>> print(mark._User__firstname)
Mark
>>>
>>> print(mark._User__lastname)
Watney

To list all the attributes once again we can use `vars()`:

>>> vars(mark)  # doctest: +NORMALIZE_WHITESPACE
{'_User__firstname': 'Mark',
 '_User__lastname': 'Watney'}


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
... class User:
...     firstname: str
...     lastname: str
>>>
>>>
>>> mark = User('Mark', 'Watney')

>>> mark.__class__
<class '__main__.User'>
>>>
>>> mark.__dict__
{'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> mark.__doc__
'User(firstname: str, lastname: str)'
>>>
>>> mark.__annotations__
{'firstname': <class 'str'>, 'lastname': <class 'str'>}
>>>
>>> mark.__module__
'__main__'


Show Attributes
---------------
* ``vars()`` display ``obj.__dict__``

>>> class User:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
...         self._salary = 10_000
...         self._address = '2101 E NASA Pkwy, Houston 77058, Texas, USA'
...         self.__username = 'mwatney'
...         self.__password = 'ares3'
...         self.id_ = 1337
...         self.type_ = 'User'
...         self.__doc__ = 'Class representing an User'
...         self.__module__ = '__main__'
...         self.__version__ = '1.0.0'
...         self.__author__ = 'Mark Watney <mwatney@nasa.gov>'
>>>
>>>
>>> mark = User()

All attributes:

>>> vars(mark)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 '_salary': 10000,
 '_address': '2101 E NASA Pkwy, Houston 77058, Texas, USA',
 '_User__username': 'mwatney',
 '_User__password': 'ares3',
 'id_': 1337,
 'type_': 'User',
 '__doc__': 'Class representing an User',
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
{'firstname': 'Mark', 'id_': 1337, 'lastname': 'Watney', 'type_': 'User'}

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
{'_User__password': 'ares3', '_User__username': 'mwatney'}

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
 '__doc__': 'Class representing an User',
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
