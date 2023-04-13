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


    astro = Astronaut()

    astro.firstname = 'Mark'
    astro.lastname = 'Watney'

    astro.mission = 'Ares 3'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'mission'


Example
-------
.. code-block:: python

    class Astronaut:
        __slots__ = ()


    astro = Astronaut()

    astro.name = 'Mark Watney'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'name'

.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)


    astro = Astronaut()

    astro.name = 'Mark Watney'
    astro.mission = 'Ares 3'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'mission'


``__slots__`` and ``__dict__``
------------------------------
* Using ``__slots__`` will prevent from creating ``__dict__``

.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)


    astro = Astronaut()
    astro.name = 'Mark Watney'

    print(astro.__slots__)
    # ('name',)

    print(astro.__dict__)
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute '__dict__'

.. code-block:: python

    class Astronaut:
        __slots__ = ('__dict__', 'name')


    astro = Astronaut()
    astro.name = 'Mark Watney'   # will use __slots__
    astro.mission = 'Ares 3'     # will use __dict__

    print(astro.__slots__)
    # ('__dict__', 'name')

    print(astro.__dict__)
    # {'mission': 'Ares 3'}


Slots and Methods
-----------------
.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)

        def say_hello(self):
            print(f'My name... {self.name}')


    astro = Astronaut()
    astro.name = 'Mark Watney'
    astro.say_hello()


Slots and Init
--------------
.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)

        def __init__(self, name)
            self.name = name


    astro = Astronaut('Mark Watney')
    print(astro.name)
    # Mark Watney

.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)

        def __init__(self, name, mission):
            self.name = name
            self.mission = mission


    astro = Astronaut('Mark Watney', 'Ares 3')
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


    astro = Astronaut()
    astro.name = 'Mark Watney'
    astro.mission = 'Ares 3'

    print(astro.mission)
    # Ares 3

.. code-block:: python

    class Pilot:
        __slots__ = ('name',)

    class Astronaut(Pilot):
        __slots__ = ('name', 'mission')


    astro = Astronaut()
    astro.firstname = 'Mark Watney'
    astro.mission = 'Ares 3'
    astro.rank = 'Senior'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'rank'

.. code-block:: python

    class Pilot:
        __slots__ = ('name',)


    class Astronaut(Pilot):
        __slots__ = ('mission',)


    astro = Astronaut()
    astro.name = 'Mark Watney'
    astro.mission = 'Ares 3'
    astro.rank = 'Senior'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'rank'


Use Case - 0x01
---------------
.. code-block:: python

    class Astronaut:
        __slots__ = ('firstname', 'lastname')


    astro = Astronaut()
    astro.firstname = 'Mark'
    astro.lastname = 'Watney'

    print(astro.firstname)
    # Mark

    print(astro.lastname)
    # Watney

    print(astro.__slots__)
    # ('firstname', 'lastname')

    print(astro.__dict__)
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute '__dict__'

    result = {attr: getattr(astro, attr)
              for attr in astro.__slots__}

    print(result)
    # {'firstname': 'Mark', 'lastname': 'Watney'}


Assignments
-----------
.. literalinclude:: assignments/oop_slots_define.py
    :caption: :download:`Solution <assignments/oop_slots_define.py>`
    :end-before: # Solution
