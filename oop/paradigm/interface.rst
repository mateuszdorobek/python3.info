Interface
=========
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


Example
-------
Interfaces:

.. code-block:: python

    from datetime import timedelta


    class CacheInterface:
        timeout: timedelta

        def get(self, key: str) -> str:
            raise NotImplementedError

        def set(self, key: str, value: str) -> None:
            raise NotImplementedError

        def is_valid(self, key: str) -> bool:
            raise NotImplementedError


Use Case - 0x01
---------------
Interfaces:

.. code-block:: python

    from datetime import timedelta


    class Cache:
        timeout: timedelta

        def get(self, key: str) -> str:
            raise NotImplementedError

        def set(self, key: str, value: str) -> None:
            raise NotImplementedError

        def is_valid(self, key: str) -> bool:
            raise NotImplementedError


    class CacheDatabase(Cache):
        timeout: timedelta

        def is_valid(self, key: str) -> bool:
            ...

        def get(self, key: str) -> str:
            ...

        def set(self, key: str, value: str) -> None:
            ...


    class CacheRAM(Cache):
        timeout: timedelta

        def is_valid(self, key: str) -> bool:
            ...

        def get(self, key: str) -> str:
            ...

        def set(self, key: str, value: str) -> None:
            ...


    class CacheFilesystem(Cache):
        timeout: timedelta

        def is_valid(self, key: str) -> bool:
            ...

        def get(self, key: str) -> str:
            ...

        def set(self, key: str, value: str) -> None:
            ...


    fs: Cache = CacheFilesystem()
    fs.set('name', 'Mark Watney')
    fs.is_valid('name')
    fs.get('name')

    ram: Cache = CacheRAM()
    ram.set('name', 'Mark Watney')
    ram.is_valid('name')
    ram.get('name')

    db: Cache = CacheDatabase()
    db.set('name', 'Mark Watney')
    db.is_valid('name')
    db.get('name')


Assignments
-----------
.. literalinclude:: assignments/oop_interface_define.py
    :caption: :download:`Solution <assignments/oop_interface_define.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_interface_implement.py
    :caption: :download:`Solution <assignments/oop_interface_implement.py>`
    :end-before: # Solution
