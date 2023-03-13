OOP Attribute Slots
===================
* Faster attribute access
* Space savings in memory (overhead of dict for every object)
* Prevents from adding new attributes
* The space savings is from:
* Store value references in slots instead of ``__dict__``
* Denying ``__dict__`` and ``__weakref__`` creation

>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'

When inheriting from a class without ``__slots__``, the ``__dict__``
and ``__weakref__`` attribute of the instances will always be accessible.

Without a ``__dict__`` variable, instances cannot be assigned new variables
not listed in the ``__slots__`` definition. Attempts to assign to an
unlisted variable name raises AttributeError. If dynamic assignment of new
variables is desired, then add ``'__dict__'`` to the sequence of strings
in the ``__slots__`` declaration.

Without a ``__weakref__`` variable for each instance, classes defining
``__slots__`` do not support weak references to its instances. If weak
reference support is needed, then add ``'__weakref__'`` to the sequence
of strings in the ``__slots__`` declaration.

``__slots__`` are implemented at the class level by creating descriptors
for each variable name. As a result, class attributes cannot be used to set
default values for instance variables defined by ``__slots__``; otherwise,
the class attribute would overwrite the descriptor assignment.

The action of a ``__slots__`` declaration is not limited to the class
where it is defined. ``__slots__`` declared in parents are available in
child classes. However, child subclasses will get a ``__dict__`` and
``__weakref__`` unless they also define ``__slots__`` (which should only
contain names of any additional slots).

If a class defines a slot also defined in a base class, the instance
variable defined by the base class slot is inaccessible (except by
retrieving its descriptor directly from the base class). This renders
the meaning of the program undefined. In the future, a check may be added
to prevent this.

Nonempty ``__slots__`` does not work for classes derived from
``'variable-length'`` built-in types such as ``int``, ``bytes`` and
``tuple``.

Any non-string iterable may be assigned to ``__slots__``.

If a dictionary is used to assign ``__slots__``, the dictionary keys will
be used as the slot names. The values of the dictionary can be used to
provide per-attribute docstrings that will be recognised by
``inspect.getdoc()`` and displayed in the output of ``help()``.

``__class__`` assignment works only if both classes have the same
``__slots__``.

Multiple inheritance with multiple slotted parent classes can be used, but
only one parent is allowed to have attributes created by slots (the other
bases must have empty slot layouts) - violations raise ``TypeError``.

If an iterator is used for ``__slots__`` then a descriptor is created for
each of the iterator's values. However, the ``__slots__`` attribute will
be an empty iterator.

Source: [#pydocDataModelSlots]_


Weakref
-------
A weak reference to an object is not enough to keep the object alive: when
the only remaining references to a referent are weak references, garbage
collection is free to destroy the referent and reuse its memory for
something else. However, until the object is actually destroyed the weak
reference may return the object even if there are no strong references to it.
A primary use for weak references is to implement caches or mappings holding
large objects, where it's desired that a large object not be kept alive
solely because it appears in a cache or mapping [#pydocWeakref]_.

``__weakref__`` is just an opaque object that references all the weak
references to the current object. It's just an implementation detail that
allows the garbage collector to inform weak references that its referent
has been collected, and to not allow access to its underlying pointer
anymore. The weak reference can't rely on checking the reference count of
the object it refers to. This is because that memory may have been reclaimed
and is now being used by another object. Best case scenario the VM will
crash, worst case the weak reference will allow access to an object it
wasn't originally referring to. This is why the garbage collector must
inform the weak reference its referent is no longer valid. Weak references
form a stack. The top of that stack (the most recent weak reference to an
object) is available via ``__weakref__``. Weakrefs are re-used whenever
possible, so the stack is typically either empty or contains a single
element. [#Dunes2016]_

Garbage collection is simply the process of freeing memory when it is not
used/reached by any reference/pointer anymore. Python performs garbage
collection via a technique called reference counting (and a cyclic garbage
collector that is used to detect and break reference cycles). Using
reference counting, GC collects the objects as soon as they become
unreachable which happens when the number of references to the object is 0.
[#pydocDataModelObjectValues]_

The way with which weak references perform the task of NOT protecting the
object from being collected by GC, or better to say the way with which they
cause an object to be collected by GC is that (in case of a GC that uses
reference counting rather than tracing technique) they just don't get to be
counted as a reference. Otherwise, if counted, they will be called strong
references [#Mazdak2016]_.


Empty Slots
-----------
>>> class Astronaut:
...     __slots__ = ()
>>>
>>>
>>> astro = Astronaut()
>>>
>>> astro.fullname = 'Mark Watney'
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'fullname'


One Slot
--------
>>> class Astronaut:
...     __slots__ = ('fullname',)
>>>
>>>
>>> astro = Astronaut()
>>>
>>> astro.fullname = 'Mark Watney'
>>> astro.role = 'Botanist'
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'role'


Many Slots
----------
>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>>
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>> astro.role = 'Botanist'
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'role'


Get Value
---------
>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>>
>>> print(astro.firstname)
Mark
>>> print(astro.lastname)
Watney


Slots and Methods
-----------------
>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
...
...     def say_hello(self):
...         print(f'My name... {self.firstname} {self.lastname}')
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>>
>>> astro.say_hello()
My name... Mark Watney


Slots and Init
--------------
>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> print(astro.firstname)
Mark
>>> print(astro.lastname)
Watney

>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
...
...     def __init__(self, firstname, lastname, role):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.role = role
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney', 'Botanist')
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'role'


Vars
----
* Using ``__slots__`` will prevent from creating ``__dict__``

>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>>
>>> vars(astro)
Traceback (most recent call last):
TypeError: vars() argument must have __dict__ attribute
>>>
>>> print(astro.__dict__)
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute '__dict__'


Slots Internals
---------------
* Slots are descriptors

>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> vars(Astronaut)  # doctest: +NORMALIZE_WHITESPACE
mappingproxy({'__module__': '__main__',
              '__slots__': ('firstname', 'lastname'),
              'firstname': <member 'firstname' of 'Astronaut' objects>,
              'lastname': <member 'lastname' of 'Astronaut' objects>,
              '__doc__': None})
>>>
>>> Astronaut.firstname
<member 'firstname' of 'Astronaut' objects>
>>>
>>> type(Astronaut.firstname)
<class 'member_descriptor'>


Slots Dict
----------
* Docstring for slotted names
* Used for documentation

If a dictionary is used to assign ``__slots__``, the dictionary keys will
be used as the slot names. The values of the dictionary can be used to
provide per-attribute docstrings that will be recognised by
``inspect.getdoc()`` and displayed in the output of ``help()``.

>>> class Astronaut:
...     __slots__ = {
...         'firstname': 'Docstring for firstname attribute',
...         'lastname': 'Docstring for lastname attribute',
...     }
>>>
>>>
>>> vars(Astronaut)  # doctest: +NORMALIZE_WHITESPACE
mappingproxy({'__module__': '__main__',
              '__slots__': {'firstname': 'Docstring for firstname attribute',
                            'lastname': 'Docstring for lastname attribute'},
              'firstname': <member 'firstname' of 'Astronaut' objects>,
              'lastname': <member 'lastname' of 'Astronaut' objects>,
              '__doc__': None})


Get Attributes and Values
-------------------------
* To get values iterate over ``self.__slots__`` and use ``getattr(self, x)``

>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>>
>>> print(astro.__slots__)
('firstname', 'lastname')
>>>
>>> {x: getattr(astro, x) for x in astro.__slots__}
{'firstname': 'Mark', 'lastname': 'Watney'}


Slots and Dunder Dict
---------------------
* Using ``__slots__`` will prevent from creating ``__dict__``
* Adding ``__dict__`` to ``__slots__`` will combine both worlds

>>> class Astronaut:
...     __slots__ = ('__dict__', 'firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'   # will use __slots__
>>> astro.lastname = 'Watney'  # will use __slots__
>>> astro.role = 'Botanist'    # will use __dict__
>>> astro.mission = 'Ares3'    # will use __dict__
>>>
>>> print(astro.__slots__)
('__dict__', 'firstname', 'lastname')
>>>
>>> vars(astro)
{'role': 'Botanist', 'mission': 'Ares3'}
>>>
>>> {x:getattr(astro, x) for x in astro.__slots__ if x != '__dict__'} | vars(astro)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'role': 'Botanist',
 'mission': 'Ares3'}


Inheritance
-----------
* Slots do not inherit, unless they are specified in subclass
* Slots are added on inheritance
* If class does not specify slots, the ``__dict__`` will be added

>>> class Person:
...     __slots__ = ('firstname', 'lastname')
>>>
>>> class Astronaut(Person):
...     pass
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>> astro.role = 'Botanist'
>>>
>>> print(astro.firstname)
Mark
>>> print(astro.lastname)
Watney
>>> print(astro.role)
Botanist
>>>
>>>
>>> vars(astro)
{'role': 'Botanist'}
>>>
>>> vars(Astronaut)  # doctest: +NORMALIZE_WHITESPACE
mappingproxy({'__module__': '__main__',
              '__dict__': <attribute '__dict__' of 'Astronaut' objects>,
              '__weakref__': <attribute '__weakref__' of 'Astronaut' objects>,
              '__doc__': None})

>>> class Person:
...     __slots__ = ('firstname', 'lastname')
>>>
>>> class Astronaut(Person):
...     __slots__ = ()
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>> astro.role = 'Botanist'
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'role'
>>>
>>>
>>> vars(astro)
Traceback (most recent call last):
TypeError: vars() argument must have __dict__ attribute
>>>
>>> vars(Astronaut)
mappingproxy({'__module__': '__main__', '__slots__': (), '__doc__': None})


>>> class Person:
...     __slots__ = ('firstname', 'lastname')
>>>
>>> class Astronaut(Person):
...     __slots__ = ('role',)
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>> astro.role = 'Botanist'
>>> astro.agency = 'NASA'
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'agency'
>>>
>>>
>>> vars(astro)
Traceback (most recent call last):
TypeError: vars() argument must have __dict__ attribute
>>>
>>> vars(Person)  # doctest: +NORMALIZE_WHITESPACE
mappingproxy({'__module__': '__main__',
              '__slots__': ('firstname', 'lastname'),
              'firstname': <member 'firstname' of 'Person' objects>,
              'lastname': <member 'lastname' of 'Person' objects>,
              '__doc__': None})
>>>
>>> vars(Astronaut)  # doctest: +NORMALIZE_WHITESPACE
mappingproxy({'__module__': '__main__',
              '__slots__': ('role',),
              'role': <member 'role' of 'Astronaut' objects>,
              '__doc__': None})


Change Slots
------------
>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>>
>>> astro.__slots__
('firstname', 'lastname')
>>>
>>> astro.__slots__ = ('myslot1', 'myslot2')
Traceback (most recent call last):
AttributeError: 'Astronaut' object attribute '__slots__' is read-only

>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>>
>>> Astronaut.__slots__ = ('myslot1', 'myslot2')
>>> Astronaut.__slots__
('myslot1', 'myslot2')
>>>
>>> vars(Astronaut)  # doctest: +NORMALIZE_WHITESPACE
mappingproxy({'__module__': '__main__',
              '__slots__': ('myslot1', 'myslot2'),
              'firstname': <member 'firstname' of 'Astronaut' objects>,
              'lastname': <member 'lastname' of 'Astronaut' objects>,
              '__doc__': None})

>>> class Astronaut:
...     __slots__ = ('firstname', 'lastname')
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>>
>>> Astronaut.__slots__ = ('myslot1', 'myslot2')
>>> Astronaut.__slots__
('myslot1', 'myslot2')
>>>
>>>
>>> Astronaut.firstname
<member 'firstname' of 'Astronaut' objects>
>>>
>>> Astronaut.lastname
<member 'lastname' of 'Astronaut' objects>
>>>
>>> Astronaut.myslot1
Traceback (most recent call last):
AttributeError: type object 'Astronaut' has no attribute 'myslot1'
>>>
>>> Astronaut.myslot2
Traceback (most recent call last):
AttributeError: type object 'Astronaut' has no attribute 'myslot2'
>>>
>>> astro.firstname
'Mark'
>>>
>>> astro.lastname
'Watney'
>>>
>>> astro.myslot1
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'myslot1'
>>>
>>> astro.myslot2
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'myslot2'


Slots in Dataclasses
--------------------
* Since Python 3.10

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(slots=True)
... class Iris:
...     sl: float
...     sw: float
...     pl: float
...     pw: float
...     species: str


Use Case - 0x01
---------------
>>> from dataclasses import dataclass
>>> from itertools import starmap
>>>
>>>
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica'),
...     (4.9, 3.0, 1.4, 0.2, 'setosa'),
...     (4.9, 2.5, 4.5, 1.7, 'virginica'),
...     (7.1, 3.0, 5.9, 2.1, 'virginica'),
...     (4.6, 3.4, 1.4, 0.3, 'setosa'),
...     (5.4, 3.9, 1.7, 0.4, 'setosa'),
...     (5.7, 2.8, 4.5, 1.3, 'versicolor'),
...     (5.0, 3.6, 1.4, 0.3, 'setosa'),
...     (5.5, 2.3, 4.0, 1.3, 'versicolor'),
...     (6.5, 3.0, 5.8, 2.2, 'virginica'),
...     (6.5, 2.8, 4.6, 1.5, 'versicolor'),
...     (6.3, 3.3, 6.0, 2.5, 'virginica'),
...     (6.9, 3.1, 4.9, 1.5, 'versicolor'),
...     (4.6, 3.1, 1.5, 0.2, 'setosa'),
... ]
>>>
>>> @dataclass(slots=True)
... class Iris:
...     sl: float
...     sw: float
...     pl: float
...     pw: float
...     species: str
>>>
>>>
>>> result = starmap(Iris, DATA[1:])
>>>
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[Iris(sl=5.8, sw=2.7, pl=5.1, pw=1.9, species='virginica'),
 Iris(sl=5.1, sw=3.5, pl=1.4, pw=0.2, species='setosa'),
 Iris(sl=5.7, sw=2.8, pl=4.1, pw=1.3, species='versicolor'),
 Iris(sl=6.3, sw=2.9, pl=5.6, pw=1.8, species='virginica'),
 Iris(sl=6.4, sw=3.2, pl=4.5, pw=1.5, species='versicolor'),
 Iris(sl=4.7, sw=3.2, pl=1.3, pw=0.2, species='setosa'),
 Iris(sl=7.0, sw=3.2, pl=4.7, pw=1.4, species='versicolor'),
 Iris(sl=7.6, sw=3.0, pl=6.6, pw=2.1, species='virginica'),
 Iris(sl=4.9, sw=3.0, pl=1.4, pw=0.2, species='setosa'),
 Iris(sl=4.9, sw=2.5, pl=4.5, pw=1.7, species='virginica'),
 Iris(sl=7.1, sw=3.0, pl=5.9, pw=2.1, species='virginica'),
 Iris(sl=4.6, sw=3.4, pl=1.4, pw=0.3, species='setosa'),
 Iris(sl=5.4, sw=3.9, pl=1.7, pw=0.4, species='setosa'),
 Iris(sl=5.7, sw=2.8, pl=4.5, pw=1.3, species='versicolor'),
 Iris(sl=5.0, sw=3.6, pl=1.4, pw=0.3, species='setosa'),
 Iris(sl=5.5, sw=2.3, pl=4.0, pw=1.3, species='versicolor'),
 Iris(sl=6.5, sw=3.0, pl=5.8, pw=2.2, species='virginica'),
 Iris(sl=6.5, sw=2.8, pl=4.6, pw=1.5, species='versicolor'),
 Iris(sl=6.3, sw=3.3, pl=6.0, pw=2.5, species='virginica'),
 Iris(sl=6.9, sw=3.1, pl=4.9, pw=1.5, species='versicolor'),
 Iris(sl=4.6, sw=3.1, pl=1.5, pw=0.2, species='setosa')]


Use Case - 0x02
---------------
* Deep Size
* Source: https://code.activestate.com/recipes/577504/

>>> from sys import getsizeof
>>> from itertools import chain
>>> from collections import deque
>>> import logging
>>>
>>>
>>> logging.basicConfig(level='DEBUG')
>>> log = logging.getLogger('deepsizeof')
>>>
>>>
>>> def deepsizeof(o, handlers={}):
...     """
...     Returns the approximate memory footprint an object and all of its contents.
...
...     Automatically finds the contents of the following builtin containers and
...     their subclasses: tuple, list, deque, dict, set and frozenset
...     """
...     dict_handler = lambda d: chain.from_iterable(d.items())
...     all_handlers = {tuple: iter,
...                     list: iter,
...                     deque: iter,
...                     dict: dict_handler,
...                     set: iter,
...                     frozenset: iter}
...     all_handlers.update(handlers)     # user handlers take precedence
...     seen = set()                      # track which object id's have already been seen
...     default_size = getsizeof(0)       # estimate sizeof object without __sizeof__
...
...     def sizeof(o):
...         if id(o) in seen:       # do not double count the same object
...             return 0
...         seen.add(id(o))
...         s = getsizeof(o, default_size)
...
...         log.debug('Size: %s, Type: %s, Repr: %s', s, type(o), repr(o))
...
...         for typ, handler in all_handlers.items():
...             if isinstance(o, typ):
...                 s += sum(map(sizeof, handler(o)))
...                 break
...         else:
...             if not hasattr(o.__class__, '__slots__'):
...                 if hasattr(o, '__dict__'):
...                     # no __slots__ *usually* means a
...                     # __dict__, but some special builtin classes (such
...                     # as `type(None)`) have neither
...                     # else, `o` has no attributes at all, so sys.getsizeof()
...                     # actually returned the correct value
...                     s += sizeof(o.__dict__)
...             else:
...                 s += sum(
...                     sizeof(getattr(o, x))
...                            for x in o.__class__.__slots__
...                            if hasattr(o, x))
...         return s
...     return sizeof(o)
>>>
>>>
>>> # doctest: +SKIP
... if __name__ == '__main__':
...     class Astronaut:
...        __slots__ = ('firstname', 'lastname')
...
...     class Cosmonaut:
...         pass
...
...     a = Astronaut()
...     a.firstname = 'Mark'
...     a.lastname = 'Watney'
...
...     c = Cosmonaut()
...     c.firstname = 'Mark'
...     c.lastname = 'Watney'
...
...     print('Astronaut', deepsizeof(a))
...     print('Cosmonaut', deepsizeof(c))
DEBUG:deepsizeof:Size: 48, Type: <class 'Astronaut'>, Repr: <Astronaut object at 0x10790b940>
DEBUG:deepsizeof:Size: 53, Type: <class 'str'>, Repr: 'Mark'
DEBUG:deepsizeof:Size: 55, Type: <class 'str'>, Repr: 'Watney'
DEBUG:deepsizeof:Size: 48, Type: <class 'Cosmonaut'>, Repr: <Cosmonaut object at 0x10790b9d0>
DEBUG:deepsizeof:Size: 104, Type: <class 'dict'>, Repr: {'firstname': 'Mark', 'lastname': 'Watney'}
DEBUG:deepsizeof:Size: 58, Type: <class 'str'>, Repr: 'firstname'
DEBUG:deepsizeof:Size: 53, Type: <class 'str'>, Repr: 'Mark'
DEBUG:deepsizeof:Size: 57, Type: <class 'str'>, Repr: 'lastname'
DEBUG:deepsizeof:Size: 55, Type: <class 'str'>, Repr: 'Watney'
Astronaut 156
Cosmonaut 375


Further Reading
---------------
* https://docs.python.org/3/reference/datamodel.html#slots
* https://stackoverflow.com/questions/472000/usage-of-slots


References
----------
.. [#pydocDataModelSlots] van Rossum, G. et al. Data model. Customizing attribute access. Notes on using __slots__. Python documentation. Year: 2022. Retrieved: 2022-03-16. URL: https://docs.python.org/3/reference/datamodel.html#slots

.. [#pydocDataModelObjectValues] van Rossum, G. et al. Data model. Objects, values and types. Python documentation. Year: 2022. Retrieved: 2022-04-01. URL: https://docs.python.org/3/reference/datamodel.html#objects-values-and-types

.. [#pydocWeakref] van Rossum, G. et al. Weak references. Python documentation. Year: 2022. Retrieved: 2022-03-16. URL: https://docs.python.org/3/library/weakref.html

.. [#Dunes2016] Dunes. What exactly is __weakref__ in Python? Year: 2016. Retrieved: 2022-03-16. URL https://stackoverflow.com/a/36789779

.. [#Mazdak2016] Mazdak. What exactly is __weakref__ in Python? Year: 2016. Retrieved: 2022-03-16. URL  https://stackoverflow.com/a/36788031


Assignments
-----------
.. literalinclude:: assignments/oop_attribute_slots_a.py
    :caption: :download:`Solution <assignments/oop_attribute_slots_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_attribute_slots_b.py
    :caption: :download:`Solution <assignments/oop_attribute_slots_b.py>`
    :end-before: # Solution
