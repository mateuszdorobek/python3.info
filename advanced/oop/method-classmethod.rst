OOP Method Classmethod
======================
* Using class as namespace
* Will pass class as a first argument
* ``self`` is not required

In Python, ``classmethod`` is a built-in decorator that defines a method
that belongs to the class rather than to an instance of the class.
This means that the method can be called on the class itself, rather
than on an instance of the class.

A ``classmethod`` takes a ``cls`` parameter as its first argument,
which refers to the class itself, rather than to an instance of the class.
This allows the method to access and modify class-level attributes and methods.

Here's an example of using the ``classmethod`` decorator to define a method
that returns the number of instances of a class:

>>> class MyClass:
...     count = 0
...
...     def __init__(self):
...         MyClass.count += 1
...
...     @classmethod
...     def get_count(cls):
...         return cls.count
>>>
>>> # Create some instances of MyClass
>>> obj1 = MyClass()
>>> obj2 = MyClass()
>>> obj3 = MyClass()
>>>
>>> # Call the classmethod on the class itself
>>> print(MyClass.get_count())
3

In this example, the ``MyClass`` class defines a class-level attribute
``count`` and a ``classmethod`` called ``get_count()``. The ``__init__()``
method of the class increments the ``count`` attribute each time a new
instance of the class is created.

The ``get_count()`` method is decorated with the ``classmethod`` decorator,
which means that it can be called on the class itself, rather than on an
instance of the class. The method returns the value of the ``count``
attribute, which represents the number of instances of the class that have
been created.

The ``get_count()`` method takes a ``cls`` parameter as its first argument,
which refers to the class itself. This allows the method to access the
``count`` attribute of the class and return its value.

Dynamic methods:

>>> class User:
...     def say_hello(self):
...         pass

Static methods:

>>> class User:
...     def say_hello():
...         pass

Static and dynamic method:

>>> class User:
...     @staticmethod
...     def say_hello():
...         pass

Class methods:

>>> class User:
...     @classmethod
...     def say_hello(cls):
...         pass


Manifestation
-------------
>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...
...     @staticmethod
...     def from_json(data):
...         data = json.loads(data)
...         return User(**data)
>>>
>>> data = '{"firstname": "Mark", "lastname": "Watney"}'
>>> result = User.from_json(data)
>>>
>>> print(result)
User(firstname='Mark', lastname='Watney')

>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> class JSONMixin:
...     @staticmethod
...     def from_json(data):
...         data = json.loads(data)
...         return User(**data)
>>>
>>>
>>> @dataclass
... class User(JSONMixin):
...     firstname: str
...     lastname: str
>>>
>>>
>>> data = '{"firstname": "Mark", "lastname": "Watney"}'
>>> result = User.from_json(data)
>>>
>>> print(result)
User(firstname='Mark', lastname='Watney')

>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> class JSONMixin:
...     @classmethod
...     def from_json(cls, data):
...         data = json.loads(data)
...         return cls(**data)
>>>
>>> @dataclass
... class User(JSONMixin):
...     firstname: str
...     lastname: str
>>>
>>>
>>> data = '{"firstname": "Mark", "lastname": "Watney"}'
>>> result = User.from_json(data)
>>>
>>> print(result)
User(firstname='Mark', lastname='Watney')


Use Case - 0x01
---------------
>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> class JSONMixin:
...     @classmethod
...     def from_json(cls, data):
...         data = json.loads(data)
...         return cls(**data)
>>>
>>> @dataclass
... class User(JSONMixin):
...     firstname: str
...     lastname: str
>>>
>>> @dataclass
... class Admin(JSONMixin):
...     firstname: str
...     lastname: str
>>>
>>>
>>> data = '{"firstname": "Mark", "lastname": "Watney"}'
>>>
>>> User.from_json(data)
User(firstname='Mark', lastname='Watney')
>>>
>>> Admin.from_json(data)
Admin(firstname='Mark', lastname='Watney')


Use Case - 0x02
---------------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Account:
...     firstname: str = None
...     lastname: str = None
...
...     @classmethod
...     def from_json(cls, data):
...         import json
...         data = json.loads(data)
...         return cls(**data)
>>>
>>> class User(Account):
...     pass
>>>
>>> class Admin(Account):
...     pass
>>>
>>>
>>> data = '{"firstname": "Mark", "lastname": "Watney"}'
>>>
>>> User.from_json(data)
User(firstname='Mark', lastname='Watney')
>>>
>>> Admin.from_json(data)
Admin(firstname='Mark', lastname='Watney')


Use Case - 0x03
---------------
* Singleton

>>> class Singleton:
...     _instance: object
...
...     @classmethod
...     def get_instance(cls):
...         if not hasattr(cls, '_instance'):
...             cls._instance = object.__new__(cls)
...         return cls._instance
>>>
>>>
>>> class DatabaseConnection(Singleton):
...     pass
>>>
>>>
>>> db1 = DatabaseConnection.get_instance()
>>> db2 = DatabaseConnection.get_instance()
>>>
>>>
>>> print(db1)  # doctest: +SKIP
<__main__.DatabaseConnection object at 0x102453ee0>
>>>
>>> print(db2)  # doctest: +SKIP
<__main__.DatabaseConnection object at 0x102453ee0>


Use Case - 0x04
---------------

File ``myapp/timezone.py``:

>>> class AbstractTimezone:
...     tzname: str
...     tzcode: str
...
...     def __init__(self, date, time):
...         ...
...
...     @classmethod
...     def from_utc(cls, string):
...         values = datetime.fromisoformat(string)
...         return cls(**values)
>>>
>>>
>>> class CentralEuropeanTime(AbstractTimezone):
...     tzname = 'Central European Time'
...     tzcode = 'CET'
>>>
>>> class CentralEuropeanSummerTime(AbstractTimezone):
...     tzname = 'Central European Summer Time'
...     tzcode = 'CEST'

Operating system:

.. code-block:: console

    export TIMEZONE=CET

File: ``myapp/settings.py``:

>>> # doctest: +SKIP
... import myapp.timezone
... from os import getenv
...
... time = getattr(myapp.timezone, getenv('TIMEZONE'))

File `myapp/usage.py`:

>>> # doctest: +SKIP
... from myapp.settings import time
...
... dt = time.from_utc('1969-07-21T02:53:07Z')
... print(dt.tzname)
Central European Time


Assignments
-----------
.. literalinclude:: assignments/oop_method_classmethod_a.py
    :caption: :download:`Solution <assignments/oop_method_classmethod_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_method_classmethod_b.py
    :caption: :download:`Solution <assignments/oop_method_classmethod_b.py>`
    :end-before: # Solution
