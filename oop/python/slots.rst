Slots
=====
* Faster attribute access
* Space savings in memory (overhead of dict for every object)
* Prevents from adding new attributes
* The space savings is from:
* Store value references in slots instead of ``__dict__``
* Denying ``__dict__`` and ``__weakref__`` creation if parent classes deny them and you declare ``__slots__``

.. code-block:: python

    class Astronaut:
        __slots__ = ('firstname', 'lastname')


    mark = Astronaut()

    mark.firstname = 'Mark'
    mark.lastname = 'Watney'

    mark.mission = 'Ares 3'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'mission'


Example
-------
.. code-block:: python

    class Astronaut:
        __slots__ = ()


    mark = Astronaut()

    mark.name = 'Mark Watney'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'name'

.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)


    mark = Astronaut()

    mark.name = 'Mark Watney'
    mark.mission = 'Ares 3'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'mission'


``__slots__`` and ``__dict__``
------------------------------
* Using ``__slots__`` will prevent from creating ``__dict__``

.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)


    mark = Astronaut()
    mark.name = 'Mark Watney'

    print(mark.__slots__)
    # ('name',)

    print(mark.__dict__)
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute '__dict__'

.. code-block:: python

    class Astronaut:
        __slots__ = ('__dict__', 'name')


    mark = Astronaut()
    mark.name = 'Mark Watney'   # will use __slots__
    mark.mission = 'Ares 3'     # will use __dict__

    print(mark.__slots__)
    # ('__dict__', 'name')

    print(mark.__dict__)
    # {'mission': 'Ares 3'}


Slots and Methods
-----------------
.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)

        def say_hello(self):
            print(f'My name... {self.name}')


    mark = Astronaut()
    mark.name = 'Mark Watney'
    mark.say_hello()


Slots and Init
--------------
.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)

        def __init__(self, name)
            self.name = name


    mark = Astronaut('Mark Watney')
    print(mark.name)
    # Mark Watney

.. codemark-block:: python

    class Astronaut:
        __slots__ = ('name',)

        def __init__(self, name, mission):
            self.name = name
            self.mission = mission


    mark = Astronaut('Mark Watney', 'Ares 3')
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'mission'


Inheritance
-----------
* Slots do not inherit, unless they are specified in subclass
* Slots are added on inheritance

.. code-block:: python

    class Pilot:
        __slots__ = ('name',)

    class Astronaut(Pilot):
        pass


    mark = Astronaut()
    mark.name = 'Mark Watney'
    mark.mission = 'Ares 3'

    print(mark.mission)
    # Ares 3

.. code-block:: python

    class Pilot:
        __slots__ = ('name',)

    class Astronaut(Pilot):
        __slots__ = ('name', 'mission')


    mark = Astronaut()
    mark.firstname = 'Mark Watney'
    mark.mission = 'Ares 3'
    mark.rank = 'Senior'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'rank'

.. code-block:: python

    class Pilot:
        __slots__ = ('name',)


    class Astronaut(Pilot):
        __slots__ = ('mission',)


    mark = Astronaut()
    mark.name = 'Mark Watney'
    mark.mission = 'Ares 3'
    mark.rank = 'Senior'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'rank'


Use Case - 0x01
---------------
.. code-block:: python

    class Astronaut:
        __slots__ = ('firstname', 'lastname')


    mark = Astronaut()
    mark.firstname = 'Mark'
    mark.lastname = 'Watney'

    print(mark.firstname)
    # Mark

    print(mark.lastname)
    # Watney

    print(mark.__slots__)
    # ('firstname', 'lastname')

    print(mark.__dict__)
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute '__dict__'

    result = {attr: getattr(mark, attr)
              for attr in mark.__slots__}

    print(result)
    # {'firstname': 'Mark', 'lastname': 'Watney'}


Assignments
-----------
.. literalinclude:: assignments/oop_slots_define.py
    :caption: :download:`Solution <assignments/oop_slots_define.py>`
    :end-before: # Solution
