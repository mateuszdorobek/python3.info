OOP Method Classmethod
======================
* Using class as namespace
* Will pass class as a first argument
* ``self`` is not required

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
* Interplanetary time

>>> # myapp/time.py
>>> class AbstractTime:
...     tzname: str
...     tzcode: str
...
...     def __init__(self, date, time):
...         ...
...
...     @classmethod
...     def from_utc(cls, utc):
...         values = {'date': ..., 'time': ...}
...         return cls(**values)
>>>
>>>
>>> class MartianTime(AbstractTime):
...     tzname = 'Coordinated Mars Time'
...     tzcode = 'MTC'
>>>
>>> class LunarTime(AbstractTime):
...     tzname = 'Lunar Standard Time'
...     tzcode = 'LST'
>>>
>>> class EarthTime(AbstractTime):
...     tzname = 'Universal Time Coordinated'
...     tzcode = 'UTC'

>>> # myapp/settings.py
>>> # doctest: +SKIP
... import myapp.time
... from myapp.time import *
... from os import getenv
...
... time = getattr(myapp.time, getenv('MISSION_TIME'))  # doctest: +SKIP

>>> # myapp/usage.py
>>> # doctest: +SKIP
... from myapp.settings import time
...
... dt = time.from_utc('1969-07-21T02:53:07Z')
... print(dt.tzname)
Coordinated Mars Time


Assignments
-----------
.. literalinclude:: assignments/oop_method_classmethod_a.py
    :caption: :download:`Solution <assignments/oop_method_classmethod_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_method_classmethod_b.py
    :caption: :download:`Solution <assignments/oop_method_classmethod_b.py>`
    :end-before: # Solution
