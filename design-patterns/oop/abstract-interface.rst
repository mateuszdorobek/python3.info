OOP Abstract Interface
======================
* Python don't have interfaces, although you can achieve similar effect
* Since Python 3.8 there are Protocols, which effectively are interfaces
* Interfaces cannot be instantiated
* Interfaces can be implemented
* Implemented class must define all interface methods (implement interface)
* Only public method declaration

.. glossary::

    interface
        Software entity with public methods and attribute declaration

    implement
        Class implements interface if has all public fields and methods
        from interface

How do you specify and enforce an interface spec in Python?

An interface specification for a module as provided by languages such
as C++ and Java describes the prototypes for the methods and functions
of the module. Many feel that compile-time enforcement of interface
specifications helps in the construction of large programs.

Python 3.0 adds an abc module that lets you define Abstract Base Classes
(ABCs). You can then use ``isinstance()`` and ``issubclass()`` to check
whether an instance or a class implements a particular ``ABC``. The
``collections.abc`` module defines a set of useful abstract base classes
such as ``Iterable``, ``Container``, and ``MutableMapping``.

For Python, many of the advantages of interface specifications can be
obtained by an appropriate test discipline for components.

A good test suite for a module can both provide a regression test and serve
as a module interface specification and a set of examples. Many Python
modules can be run as a script to provide a simple "self test". Even
modules which use complex external interfaces can often be tested in
isolation using trivial "stub" emulations of the external interface.
The ``doctest`` and ``unittest`` modules or third-party test frameworks
can be used to construct exhaustive test suites that exercise every line
of code in a module.

An appropriate testing discipline can help build large complex applications
in Python as well as having interface specifications would. In fact, it can
be better because an interface specification cannot test certain properties
of a program. For example, the ``append()`` method is expected to add new
elements to the end of some internal ``list``; an interface specification
cannot test that your ``append()`` implementation will actually do this
correctly, but it's trivial to check this property in a test suite.

Writing test suites is very helpful, and you might want to design your code
to make it easily tested. One increasingly popular technique, test-driven
development, calls for writing parts of the test suite first, before you
write any of the actual code. Of course Python allows you to be sloppy
and not write test cases at all.

.. note:: Source [#PyDocIFace]_


Problem
-------
>>> class DatabaseCache:
...     def insert(self, key, value): ...
...     def select(self, key): ...
...     def delete(self): ...
>>>
>>>
>>> class MemoryCache:
...     def store(self, value, key): ...
...     def retrieve(self, key): ...
...     def purge(self): ...
>>>
>>>
>>> class FilesystemCache:
...     def write(self, key, value): ...
...     def read(self, key): ...
...     def remove(self): ...

Each of those classes has different names for methods which eventually
does the same job. This is lack of consistency and common interface:

>>> cache = DatabaseCache()
>>> cache.insert('firstname', 'Mark')
>>> cache.insert('lastname', 'Watney')
>>> cache.select('firstname')
>>> cache.select('lastname')
>>> cache.delete()

>>> cache = MemoryCache()
>>> cache.store('firstname', 'Mark')
>>> cache.store('lastname', 'Watney')
>>> cache.retrieve('firstname')
>>> cache.retrieve('lastname')
>>> cache.purge()

>>> cache = FilesystemCache()
>>> cache.write('firstname', 'Mark')
>>> cache.write('lastname', 'Watney')
>>> cache.read('firstname')
>>> cache.read('lastname')
>>> cache.remove()


Solution
--------
* S.O.L.I.D.
* DIP - Dependency Inversion Principle
* Always depend on an abstraction not con

.. epigraph::

    The principle states: High-level modules should not import anything from
    low-level modules. Both should depend on abstractions (e.g., interfaces).
    Abstractions should not depend on details. Details (concrete
    implementations) should depend on abstractions.

    -- SOLID, Dependency Inversion Principle, Robert C. Martin

>>> class ICache:
...     def set(self, key: str, value: str) -> None: raise NotImplementedError
...     def get(self, key: str) -> str: raise NotImplementedError
...     def clear(self) -> None: raise NotImplementedError
>>>
>>>
>>> class DatabaseCache(ICache):
...     def set(self, key: str, value: str) -> None: ...
...     def get(self, key: str) -> str: ...
...     def clear(self) -> None: ...
>>>
>>>
>>> class FilesystemCache(ICache):
...     def set(self, key: str, value: str) -> None: ...
...     def get(self, key: str) -> str: ...
...     def clear(self) -> None: ...
>>>
>>>
>>> class MemoryCache(ICache):
...     def set(self, key: str, value: str) -> None: ...
...     def get(self, key: str) -> str: ...
...     def clear(self) -> None: ...

>>> cache: ICache = DatabaseCache()
>>> cache.set('firstname', 'Mark')
>>> cache.set('lastname', 'Watney')
>>> cache.get('firstname')
>>> cache.get('lastname')
>>> cache.clear()

>>> cache: ICache = FilesystemCache()
>>> cache.set('firstname', 'Mark')
>>> cache.set('lastname', 'Watney')
>>> cache.get('firstname')
>>> cache.get('lastname')
>>> cache.clear()

>>> cache: ICache = MemoryCache()
>>> cache.set('firstname', 'Mark')
>>> cache.set('lastname', 'Watney')
>>> cache.get('firstname')
>>> cache.get('lastname')
>>> cache.clear()


Interface Names
---------------
* ``Cache``
* ``CacheInterface``
* ``CacheIface``
* ``ICache``

>>> class Cache:
...     ...

>>> class CacheInterface:
...     ...

>>> class CacheIface:
...     ...

>>> class ICache:
...     ...


Alternative Notation
--------------------
>>> class ICache:
...     def set(self, key: str, value: str) -> None:
...         raise NotImplementedError
...
...     def get(self, key: str) -> str:
...         raise NotImplementedError
...
...     def clear(self) -> None:
...         raise NotImplementedError

Interfaces do not have any implementation, so you can write them as
one-liners. It is a bit more easier to read. You will also focus more
on method names and attribute types.

>>> class ICache:
...     def set(self, key: str, value: str) -> None: raise NotImplementedError
...     def get(self, key: str) -> str: raise NotImplementedError
...     def clear(self) -> None: raise NotImplementedError

Sometimes you may get a shorter code, but it will not raise an error
in case of implementing class do not cover the name.

>>> class ICache:
...     def set(self, key: str, value: str) -> None: pass
...     def get(self, key: str) -> str: pass
...     def clear(self) -> None: pass

As of three dots (``...``) is a valid Python object (Ellipsis) you can write
that:

>>> class ICache:
...     def set(self, key: str, value: str) -> None: ...
...     def get(self, key: str) -> str: ...
...     def clear(self) -> None: ...


Not Existing Notation
---------------------
* This currently does not exists in Python
* In fact it is not even a valid Python syntax
* But it could greatly improve readability

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


Use Case - 0x01
---------------
>>> class Account:
...     def login(self, username: str, password: str) -> None: ...
...     def logout(self) -> None: ...
>>>
>>>
>>> class Guest(Account):
...      ...
>>>
>>> class User(Account):
...      ...
>>>
>>> class Admin(Account):
...      ...


Use Case - 0x02
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
...     def clear(self) -> None:
...         raise NotImplementedError

File ``cache_impl.py``:

>>> class DatabaseCache(ICache):
...     def get(self, key: str) -> str:
...         ...
...
...     def set(self, key: str, value: str) -> None:
...         ...
...
...     def clear(self) -> None:
...         ...
>>>
>>>
>>> class InMemoryCache(ICache):
...     def get(self, key: str) -> str:
...         ...
...
...     def set(self, key: str, value: str) -> None:
...         ...
...
...     def clear(self) -> None:
...         ...
>>>
>>>
>>> class FilesystemCache(ICache):
...     def get(self, key: str) -> str:
...         ...
...
...     def set(self, key: str, value: str) -> None:
...         ...
...
...     def clear(self) -> None:
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
>>> cache.set('firstname', 'Mark')
>>> cache.set('lastname', 'Watney')
>>> cache.get('firstname')
>>> cache.get('lastname')
>>> cache.clear()

Note, that myapp doesn't know which cache is being used. It only depends
on configuration in settings file.


Use Case - 0x03
---------------
.. figure:: img/oop-interface-gimp.jpg

    GIMP (GNU Image Manipulation Project) window with tools and canvas [#GIMP]_

Interface definition with all event handler specification:

>>> class ITool:
...     def on_mouse_over(self): raise NotImplementedError
...     def on_mouse_out(self): raise NotImplementedError
...     def on_mouse_leftbutton(self): raise NotImplementedError
...     def on_mouse_rightbutton(self): raise NotImplementedError
...     def on_key_press(self): raise NotImplementedError
...     def on_key_unpress(self): raise NotImplementedError

Implementation:

>>> class Pencil(ITool):
...     def on_mouse_over(self): ...
...     def on_mouse_out(self): ...
...     def on_mouse_leftbutton(self): ...
...     def on_mouse_rightbutton(self): ...
...     def on_key_press(self): ...
...     def on_key_unpress(self): ...
>>>
>>>
>>> class Pen(ITool):
...     def on_mouse_over(self): ...
...     def on_mouse_out(self): ...
...     def on_mouse_leftbutton(self): ...
...     def on_mouse_rightbutton(self): ...
...     def on_key_press(self): ...
...     def on_key_unpress(self): ...
>>>
>>>
>>> class Brush(ITool):
...     def on_mouse_over(self): ...
...     def on_mouse_out(self): ...
...     def on_mouse_leftbutton(self): ...
...     def on_mouse_rightbutton(self): ...
...     def on_key_press(self): ...
...     def on_key_unpress(self): ...
>>>
>>>
>>> class Eraser(ITool):
...     def on_mouse_over(self): ...
...     def on_mouse_out(self): ...
...     def on_mouse_leftbutton(self): ...
...     def on_mouse_rightbutton(self): ...
...     def on_key_press(self): ...
...     def on_key_unpress(self): ...


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
