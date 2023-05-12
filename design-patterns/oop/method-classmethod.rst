OOP Method Classmethod
======================
* Using class as namespace
* Will pass class as a first argument
* ``self`` is not required

Dynamic methods:

>>> class MyClass:
...     def mymethod(self):
...         pass

Static methods:

>>> class MyClass:
...     @staticmethod
...     def mymethod():
...         pass

Class methods:

>>> class MyClass:
...     @classmethod
...     def mymethod(cls):
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
>>> class Astronaut(Singleton):
...     pass
>>>
>>> class Cosmonaut(Singleton):
...     pass
>>>
>>>
>>> a = Astronaut.get_instance()
>>> b = Cosmonaut.get_instance()
>>>
>>>
>>> print(a)  # doctest: +SKIP
<__main__.Astronaut object at 0x102453ee0>
>>>
>>> print(b)  # doctest: +SKIP
<__main__.Cosmonaut object at 0x102453ee0>


Use Case - 0x02
---------------
* JSONMixin

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
... class Guest(JSONMixin):
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
>>> Guest.from_json(data)
Guest(firstname='Mark', lastname='Watney')
>>>
>>> Admin.from_json(data)
Admin(firstname='Mark', lastname='Watney')


Use Case - 0x03
---------------
File ``myapp/database.py``:

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Database:
...     dbtype: str | None = None
...     dbname: str | None = None
...     host: str | None = None
...     port: str | None = None
...     username: str | None = None
...     password: str | None = None
...
...     @classmethod
...     def connect(cls, host, port, dbname, username, password):
...         driver = cls.driver
...         return driver.connect(host, port, dbname, username, password)
...
...     def execute(self, sql: str):
...         return ...
>>>
>>> @dataclass
... class PostgreSQL(Database):
...     driver: str = 'psycopg3'
...     port: int = 5432
>>>
>>> @dataclass
... class MySQL(Database):
...     driver: str = 'pymysql'
...     port: int = 3306
>>>
>>> @dataclass
... class Oracle(Database):
...     driver: str = 'oracledb'
...     port: int = 1521

File ``myapp/settings.py``:

>>> # doctest: +SKIP
... from myapp.database import *
...
... database = PostgreSQL

File ``myapp/main.py``:

>>> # doctest: +SKIP
... from myapp.settings import db
...
... connection = database.connect(
...     host='localhost',
...     port=5432,
...     dbname='nasa',
...     username='mwatney',
...     password='Ares3',
... )
...
... connection.execute('SELECT * FROM astronauts')


Use Case - 0x04
---------------
* STAGE: prod / test


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
...     def parse(cls, text):
...         result = {'date': ..., 'time': ...}
...         return cls(**result)
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
>>> from myapp.time import *  # doctest: +SKIP
>>>
>>> time = MartianTime

>>> # myapp/usage.py
>>> from myapp.settings import time  # doctest: +SKIP
>>>
>>> UTC = '1969-07-21T02:53:07Z'
>>>
>>> dt = time.parse(UTC)
>>> print(dt.tzname)
Coordinated Mars Time


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
...     def parse(cls, text):
...         result = {'date': ..., 'time': ...}
...         return cls(**result)
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
... UTC = '1969-07-21T02:53:07Z'
...
... dt = time.parse(UTC)
... print(dt.tzname)
Coordinated Mars Time


Use Case - 0x05
---------------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class User:
...     firstname: str = None
...     lastname: str = None
...
...     @classmethod
...     def from_json(cls, data):
...         import json
...         data = json.loads(data)
...         return cls(**data)
>>>
>>> class Admin(User):
...     pass
>>>
>>> class Guest(User):
...     pass
>>>
>>>
>>> data = '{"firstname": "Mark", "lastname": "Watney"}'
>>>
>>> Admin.from_json(data)
Admin(firstname='Mark', lastname='Watney')
>>>
>>> Guest.from_json(data)
Guest(firstname='Mark', lastname='Watney')
>>>
>>> User.from_json(data)
User(firstname='Mark', lastname='Watney')


Assignments
-----------
.. literalinclude:: assignments/oop_method_classmethod_a.py
    :caption: :download:`Solution <assignments/oop_method_classmethod_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_method_classmethod_b.py
    :caption: :download:`Solution <assignments/oop_method_classmethod_b.py>`
    :end-before: # Solution
