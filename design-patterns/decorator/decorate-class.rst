Decorate Class
==============
* ``mydecorator`` is a decorator name
* ``MyClass`` is a class name

Syntax:

>>> @mydecorator  # doctest: +SKIP
... class MyClass:
...     ...

Is equivalent to:

>>> MyClass = mydecorator(MyClass)  # doctest: +SKIP


Syntax
------
* ``mydecorator`` is a decorator name
* ``MyClass`` is a class name

>>> def decorator(cls):
...     class Wrapper(cls):
...         def __new__(cls, *args, **kwargs):
...             ...
...     return Wrapper
>>>
>>>
>>> def decorator(cls):
...     def wrapper(*args, **kwargs):
...         instance = cls.__new__(cls, *args, **kwargs)
...         return instance
...     return wrapper
>>>
>>>
>>> @decorator
... class MyClass:
...     ...
>>>
>>>
>>> my = MyClass()


Example
-------
>>> def run(cls):
...     def wrapper(*args, **kwargs):
...         instance = cls.__new__(cls, *args, **kwargs)
...         return instance
...     return wrapper
>>>
>>>
>>> @run
... class Astronaut:
...     def hello(self, name):
...         return f'My name... {name}'
>>>
>>>
>>> mark = Astronaut()
>>> mark.hello('José Jiménez')
'My name... José Jiménez'


Use Case - 0x01
---------------
* Logger

>>> import logging
>>>
>>>
>>> def logger(cls):
...     class Wrapper(cls):
...         logger = logging.getLogger(cls.__name__)
...     return Wrapper
>>>
>>>
>>> @logger
... class Astronaut:
...     pass
>>>
>>>
>>> print(Astronaut.logger)
<Logger Astronaut (WARNING)>


Use Case - 0x02
---------------
* Since

>>> from datetime import datetime, timezone
>>>
>>>
>>> def since(cls):
...     class Wrapper(cls):
...         _since = datetime.now(timezone.utc)
...     return Wrapper
>>>
>>>
>>> @since
... class Astronaut:
...     pass
>>>
>>>
>>> print(Astronaut._since)  # doctest: +SKIP
datetime.datetime(1969, 7, 21, 2, 56, 15, tzinfo=datetime.timezone.utc)


Use Case - 0x03
---------------
* Singleton Func

>>> def singleton(cls):
...     def wrapper(*args, **kwargs):
...         if not hasattr(cls, '_instance'):
...             instance = object.__new__(cls, *args, **kwargs)
...             setattr(cls, '_instance', instance)
...         return getattr(cls, '_instance')
...     return wrapper
>>>
>>>
>>> @singleton
... class DatabaseConnection:
...     def connect(self):
...         print(f'Connecting...')
>>>
>>>
>>> a = DatabaseConnection()  # Will create instance
>>> a.connect()  # doctest: +ELLIPSIS
Connecting...
>>>
>>> b = DatabaseConnection()  # Will reuse instance
>>> b.connect()  # doctest: +ELLIPSIS
Connecting...


Use Case - 0x04
---------------
* Singleton Cls

>>> def singleton(cls):
...     class Wrapper(cls):
...         def __new__(cls, *args, **kwargs):
...             if not hasattr(cls, '_instance'):
...                 instance = object.__new__(cls, *args, **kwargs)
...                 setattr(cls, '_instance', instance)
...             return getattr(cls, '_instance')
...     return Wrapper
>>>
>>>
>>> @singleton
... class DatabaseConnection:
...     def connect(self):
...         print(f'Connecting...')
>>>
>>>
>>> a = DatabaseConnection()  # Will create instance
>>> a.connect()  # doctest: +ELLIPSIS
Connecting...
>>>
>>> b = DatabaseConnection()  # Will reuse instance
>>> b.connect()  # doctest: +ELLIPSIS
Connecting...


Use Case - 0x05
---------------
>>> from datetime import datetime, timezone
>>> from uuid import uuid4
>>>
>>>
>>> def trace(cls):
...     class Wrapper(cls):
...         __name__ = cls.__name__
...         __doc__ = cls.__doc__
...         __qualname__ = cls.__qualname__
...
...         def __init__(self, *args, **kwargs):
...             self._uuid = str(uuid4())
...             self._log = logging.getLogger(cls.__name__)
...             self._since = datetime.now(timezone.utc)
...             super().__init__(*args, **kwargs)
...
...         def _life_duration(self):
...             now = datetime.now(timezone.utc)
...             duration = now - self._since
...             return duration.total_seconds()
...
...     return Wrapper

>>> @trace
... class Astronaut:
...     pass
>>>
>>>
>>> mark = Astronaut()
>>> melissa = Astronaut()

>>> mark._uuid  # doctest: +SKIP
'8b383148-1dd8-4eca-aaa2-6e1deba7ff46'
>>>
>>> melissa._uuid  # doctest: +SKIP
'0a598bb9-cecc-4d3f-82e1-33207ada09ab'

>>> mark._since  # doctest: +SKIP
datetime.datetime(1961, 4, 12, 6, 7, 00, tzinfo=datetime.timezone.utc)
>>>
>>> melissa._since  # doctest: +SKIP
datetime.datetime(1969, 7, 21, 2, 56, 15, tzinfo=datetime.timezone.utc)
>>>
>>>
>>> mark._life_duration()  # doctest: +SKIP
85.035824
>>>
>>> melissa._life_duration()  # doctest: +SKIP
76.601305

>>> mark._log
<Logger Astronaut (WARNING)>
>>> melissa._log
<Logger Astronaut (WARNING)>
>>>
>>>
>>> mark._log.warning('Some warning...')  # doctest: +SKIP
Some warning...
>>>
>>> melissa._log.warning('Some warning...')  # doctest: +SKIP
Some warning...

.. todo:: Assignments
