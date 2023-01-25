OOP Abstract Interface
======================
* Python don't have interfaces
* Cannot instantiate
* Inheriting class must implement all methods
* Only method declaration
* Since Python 3.8: :pep:`544` -- Protocols: Structural subtyping (static duck typing)

.. glossary::

    interface
        Software entity with public methods and attribute declaration

    implement
        Class implements interface if has all public fields and methods from interface

How do you specify and enforce an interface spec in Python? [#PyDocIFace]_

An interface specification for a module as provided by languages such
as C++ and Java describes the prototypes for the methods and functions
of the module. Many feel that compile-time enforcement of interface
specifications helps in the construction of large programs.

Python 2.6 adds an abc module that lets you define Abstract Base Classes
(ABCs). You can then use isinstance() and issubclass() to check whether
an instance or a class implements a particular ABC. The collections.abc
module defines a set of useful ABCs such as Iterable, Container, and
MutableMapping.

For Python, many of the advantages of interface specifications can be
obtained by an appropriate test discipline for components.

A good test suite for a module can both provide a regression test and serve
as a module interface specification and a set of examples. Many Python
modules can be run as a script to provide a simple “self test.” Even
modules which use complex external interfaces can often be tested in
isolation using trivial “stub” emulations of the external interface.
The doctest and unittest modules or third-party test frameworks can be
used to construct exhaustive test suites that exercise every line of code
in a module.

An appropriate testing discipline can help build large complex applications
in Python as well as having interface specifications would. In fact, it can
be better because an interface specification cannot test certain properties
of a program. For example, the append() method is expected to add new
elements to the end of some internal list; an interface specification
cannot test that your append() implementation will actually do this
correctly, but it's trivial to check this property in a test suite.

Writing test suites is very helpful, and you might want to design your code
to make it easily tested. One increasingly popular technique, test-driven
development, calls for writing parts of the test suite first, before you
write any of the actual code. Of course Python allows you to be sloppy
and not write test cases at all.


Problem
-------
>>> class DatabaseCache:
...     def insert(self, key, value): ...
...     def select(self, key): ...
...     def ok(self, key): ...
>>>
>>>
>>> class MemoryCache:
...     def store(self, value, key): ...
...     def retrieve(self, key): ...
...     def valid(self, key): ...
>>>
>>>
>>> class FilesystemCache:
...     def write(self, key, value): ...
...     def read(self, key): ...
...     def exists(self, key): ...

Each of those classes has different names for methods which eventually
does the same job. This is lack of consistency and common interface:

>>> mycache = DatabaseCache()
>>> mycache.insert('firstname', 'Mark')
>>> mycache.insert('lastname', 'Watney')
>>>
>>> if mycache.ok('firstname'):
...     fname = mycache.select('firstname')
>>>
>>> if mycache.ok('lastname'):
...     lname = mycache.select('lastname')

>>> mycache = MemoryCache()
>>> mycache.store('firstname', 'Mark')
>>> mycache.store('lastname', 'Watney')
>>>
>>> if mycache.valid('firstname'):
...     fname = mycache.retrieve('firstname')
>>>
>>> if mycache.valid('lastname'):
...     lname = mycache.retrieve('lastname')

>>> mycache = FilesystemCache()
>>> mycache.write('firstname', 'Mark')
>>> mycache.write('lastname', 'Watney')
>>>
>>> if mycache.exists('firstname'):
...     fname = mycache.read('firstname')
>>>
>>> if mycache.exists('lastname'):
...     lname = mycache.read('lastname')


Solution
--------
class CacheInterface:
    ...


class CacheIface:
    ...


class ICache:
    ...


# specyfikują publiczne elementy klasy
# w Javie, C#, C++, ...
# atrybuty (pola klasy) są zawsze protected lub private
# dlatego nie ma ich w interfejsie
# ...
# w Python atrybuty są publiczne więc... powinny być w interfejsie
# ponieważ można nimi publicznie manipulować

class ICache:
    def set_duration(self, days): raise NotImplementedError
    def set(self, key: str, value: str) -> None: raise NotImplementedError
    def get(self, key: str) -> str: raise NotImplementedError
    def valid(self, key: str) -> bool: raise NotImplementedError
    def clear(self) -> None: raise NotImplementedError


class DatabaseCache(ICache):
    duration = timedelta(days=30)

    def set(self, key: str, value: str) -> None:
        pass

    def get(self, key: str) -> str:
        pass

    def valid(self, key: str) -> bool:
        pass


class FilesystemCache(ICache):
    def set(self, key: str, value: str) -> None:
        pass

    def get(self, key: str) -> str:
        pass

    def valid(self, key: str) -> bool:
        pass


class MemoryCache(ICache):
    def set(self, key: str, value: str) -> None:
        pass

    def get(self, key: str) -> str:
        pass

    def valid(self, key: str) -> bool:
        pass


# S.O.L.I.D.
# DIP - Dependency Inversion Principle

mycache: ICache = MemoryCache()
mycache.set_duration(days=30)

mycache.set('firstname', 'Mark')
mycache.set('lastname', 'Watney')

if mycache.valid('firstname'):
    fname = mycache.get('firstname')

if mycache.valid('lastname'):
    lname = mycache.get('lastname')



Syntax
------
* Names: ``Cache``, ``CacheInterface``, ``ICache``, ``CacheIface``

>>> class CacheInterface:
...     def set(self, key: str, value: str) -> None:
...         raise NotImplementedError
...
...     def get(self, key: str) -> str:
...         raise NotImplementedError
...
...     def is_valid(self, key: str) -> bool:
...         raise NotImplementedError


Alternative Notation
--------------------
>>> class CacheInterface:
...     def set(self, key: str, value: str) -> None: raise NotImplementedError
...     def get(self, key: str) -> str: raise NotImplementedError
...     def is_valid(self, key: str) -> bool: raise NotImplementedError

Sometimes you may get a shorter code, but it will not raise an error.

>>> class CacheInterface:
...     def set(self, key: str, value: str) -> None: pass
...     def get(self, key: str) -> str: pass
...     def is_valid(self, key: str) -> bool: pass

As of three dots (``...``) is a valid Python object (Ellipsis) you can write that:

>>> class CacheInterface:
...     def set(self, key: str, value: str) -> None: ...
...     def get(self, key: str) -> str: ...
...     def is_valid(self, key: str) -> bool: ...

The following code is not a valid Python syntax...
How nice it would be to write:

>>> @interface # doctest: +SKIP
... class Cache:
...     def set(self, key: str, value: str) -> None: ...
...     def get(self, key: str) -> str: ...
...     def is_valid(self, key: str) -> bool: ...

>>> class Cache(interface=True): # doctest: +SKIP
...     def set(self, key: str, value: str) -> None: ...
...     def get(self, key: str) -> str: ...
...     def is_valid(self, key: str) -> bool: ...

>>> interface Cache: # doctest: +SKIP
...     def set(self, key: str, value: str) -> None
...     def get(self, key: str) -> str
...     def is_valid(self, key: str) -> bool


Example
-------
>>> class ICache:
...     def set(self, key: str, value: str) -> None: ...
...     def get(self, key: str) -> str: ...
...     def is_valid(self, key: str) -> bool: ...
>>>
>>>
>>> class DatabaseCache(ICache):
...      ...
>>>
>>> class InMemoryCache(ICache):
...      ...
>>>
>>> class FilesystemCache(ICache):
...      ...

>>> mycache: ICache = DatabaseCache()
>>> mycache.set('firstname', 'Mark')
>>> mycache.is_valid('firstname')
>>> mycache.is_valid('lastname')
>>> mycache.get('firstname')

>>> mycache: ICache = InMemoryCache()
>>> mycache.set('firstname', 'Mark')
>>> mycache.is_valid('firstname')
>>> mycache.is_valid('lastname')
>>> mycache.get('firstname')

>>> mycache: ICache = FilesystemCache()
>>> mycache.set('firstname', 'Mark')
>>> mycache.is_valid('firstname')
>>> mycache.is_valid('lastname')
>>> mycache.get('firstname')


Use Case - 0x01
---------------
* Cache

File ``cache_iface.py``:

>>> class ICache:
...     def get(self, key: str) -> str:
...         raise NotImplementedError
...
...     def set(self, key: str, value: str) -> None:
...         raise NotImplementedError
...
...     def is_valid(self, key: str) -> bool:
...         raise NotImplementedError

File ``cache_impl.py``:

>>> class DatabaseCache(ICache):
...     def is_valid(self, key: str) -> bool:
...         ...
...
...     def get(self, key: str) -> str:
...         ...
...
...     def set(self, key: str, value: str) -> None:
...         ...
>>>
>>>
>>> class InMemoryCache(ICache):
...     def is_valid(self, key: str) -> bool:
...         ...
...
...     def get(self, key: str) -> str:
...         ...
...
...     def set(self, key: str, value: str) -> None:
...         ...
>>>
>>>
>>> class FilesystemCache(ICache):
...     def is_valid(self, key: str) -> bool:
...         ...
...
...     def get(self, key: str) -> str:
...         ...
...
...     def set(self, key: str, value: str) -> None:
...         ...

File ``settings.py``

>>> from myapp.cache_iface import ICache  # doctest: +SKIP
>>> from myapp.cache_impl import DatabaseCache  # doctest: +SKIP
>>> from myapp.cache_impl import InMemoryCache  # doctest: +SKIP
>>> from myapp.cache_impl import FilesystemCache  # doctest: +SKIP
>>>
>>>
>>> DefaultCache = InMemoryCache

File ``myapp.py``:

>>> from myapp.settings import DefaultCache, ICache  # doctest: +SKIP
>>>
>>>
>>> cache: ICache = DefaultCache()
>>> cache.set('name', 'Mark Watney')
>>> cache.is_valid('name')
>>> cache.get('name')

Note, that myapp doesn't know which cache is being used. It only depends
on configuration in settings file.


Use Case - 0x02
---------------
.. figure:: img/oop-interface-gimp.jpg

    GIMP (GNU Image Manipulation Project) window with tools and canvas [#GIMP]_

>>> class Tool:
...     def on_mouse_over(self): raise NotImplementedError
...     def on_mouse_out(self): raise NotImplementedError
...     def on_mouse_click_leftbutton(self): raise NotImplementedError
...     def on_mouse_unclick_leftbutton(self): raise NotImplementedError
...     def on_mouse_click_rightbutton(self): raise NotImplementedError
...     def on_mouse_unclick_rightbutton(self): raise NotImplementedError
...     def on_key_press(self): raise NotImplementedError
...     def on_key_unpress(self): raise NotImplementedError
>>>
>>>
>>> class Pencil(Tool):
...     def on_mouse_over(self):
...         ...
...
...     def on_mouse_out(self):
...         ...
...
...     def on_mouse_click_leftbutton(self):
...         ...
...
...     def on_mouse_unclick_leftbutton(self):
...         ...
...
...     def on_mouse_click_rightbutton(self):
...         ...
...
...     def on_mouse_unclick_rightbutton(self):
...         ...
...
...     def on_key_press(self):
...         ...
...
...     def on_key_unpress(self):
...         ...
>>>
>>>
>>> class Pen(Tool):
...     def on_mouse_over(self):
...         ...
...
...     def on_mouse_out(self):
...         ...
...
...     def on_mouse_click_leftbutton(self):
...         ...
...
...     def on_mouse_unclick_leftbutton(self):
...         ...
...
...     def on_mouse_click_rightbutton(self):
...         ...
...
...     def on_mouse_unclick_rightbutton(self):
...         ...
...
...     def on_key_press(self):
...         ...
...
...     def on_key_unpress(self):
...         ...


References
----------
.. [#GIMP] Download GIMP. Year: 2022. Retrieved: 2022-08-11. URL: https://anderbot.com/wp-content/uploads/2020/10/GIMP5.jpg

.. [#PyDocIFace] van Rossum, G. et al. How do you specify and enforce an interface spec in Python? Year: 2022. Retrieved: 2022-09-25. URL: https://docs.python.org/3/faq/design.html#how-do-you-specify-and-enforce-an-interface-spec-in-python


Assignments
-----------
.. literalinclude:: assignments/oop_abstract_interface_a.py
    :caption: :download:`Solution <assignments/oop_abstract_interface_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_abstract_interface_b.py
    :caption: :download:`Solution <assignments/oop_abstract_interface_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_abstract_interface_c.py
    :caption: :download:`Solution <assignments/oop_abstract_interface_c.py>`
    :end-before: # Solution
