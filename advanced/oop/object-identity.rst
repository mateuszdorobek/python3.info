OOP Object Identity
===================
* ``=`` assignment
* ``==`` checks for object equality
* ``is`` checks for object identity

>>> valid = True
>>>
>>> valid == True
True
>>> valid is True
True


Identity
--------
* ``id(obj) -> int``
* ``id()`` will change every time you execute script
* ``id()`` returns an integer which is guaranteed to be unique and constant for object during its lifetime
* Two objects with non-overlapping lifetimes may have the same ``id()`` value
* In CPython it's also the memory address of the corresponding C object

>>> id('Watney')  # doctest: +SKIP
4499664048
>>>
>>> hex(id('Watney'))  # doctest: +SKIP
'0x10c336cb0'

Identity Check
--------------
* ``is`` checks for object identity
* ``is`` compares ``id()`` output for both objects
* CPython: compares the memory address a object resides in
* Testing strings with ``is`` only works when the strings are interned
* Since Python 3.8 - Compiler produces a ``SyntaxWarning`` when identity checks (``is`` and ``is not``) are used with certain types of literals (e.g. ``str``, ``int``). These can often work by accident in *CPython*, but are not guaranteed by the language spec. The warning advises users to use equality tests (``==`` and ``!=``) instead.

>>> name = None
>>>
>>> name is None
True
>>> name is not None
False


Caching
-------
>>> a = 256
>>>
>>> a == 256
True
>>>
>>> a is 256  # doctest: +SKIP
SyntaxWarning: "is" with a literal. Did you mean "=="?
True

>>> b = 257
>>>
>>> b == 257
True
>>>
>>> b is 257  # doctest: +SKIP
SyntaxWarning: "is" with a literal. Did you mean "=="?
False


Integer Caching
---------------
* Values between -5 and 256 are cached from start
* After using any integer two times it is being cached
* Python caches also the next integer
* Cached numbers are invalidated after a while

>>> id(256)  # doctest: +SKIP
4514832592
>>>
>>> id(256)  # doctest: +SKIP
4514832592
>>>
>>> id(256)  # doctest: +SKIP
4514832592
>>>
>>> id(256)  # doctest: +SKIP
4514832592
>>>
>>>
>>> id(257)  # doctest: +SKIP
4561903248
>>>
>>> id(257)  # doctest: +SKIP
4561904272
>>>
>>> id(257)  # doctest: +SKIP
4561903344
>>>
>>> id(257)  # doctest: +SKIP
4561903344

>>> id(-5)  # doctest: +SKIP
4423729200
>>>
>>> id(-5)  # doctest: +SKIP
4423729200
>>>
>>>
>>> id(-6)  # doctest: +SKIP
4463320144
>>>
>>> id(-6)  # doctest: +SKIP
4463321840


Float Caching
-------------
* It takes a bit more hits for float to start being cached
* Cached numbers are invalidated after a while

>>> id(1.0)  # doctest: +SKIP
4491972048
>>>
>>> id(1.0)  # doctest: +SKIP
4492804656
>>>
>>> id(1.0)  # doctest: +SKIP
4491972048
>>>
>>> id(1.0)  # doctest: +SKIP
4492804656
>>>
>>> id(1.0)  # doctest: +SKIP
4492811728
>>>
>>> id(1.0)  # doctest: +SKIP
4492817392
>>>
>>> id(1.0)  # doctest: +SKIP
4492811792
>>>
>>> id(1.0)  # doctest: +SKIP
4492817392
>>>
>>> id(1.0)  # doctest: +SKIP
4492817616


Bool Type Identity
------------------
* Bool object is a singleton
* It always has the same identity (during one run)

>>> id(True)  # doctest: +SKIP
4469679168
>>>
>>> id(True)  # doctest: +SKIP
4469679168

>>> id(False)  # doctest: +SKIP
4469679896
>>>
>>> id(False)  # doctest: +SKIP
4469679896


None Type Identity
------------------
* NoneType object is a singleton
* It always has the same identity (during one run)

>>> id(None)  # doctest: +SKIP
4469761584
>>>
>>> id(None)  # doctest: +SKIP
4469761584


String Type Identity
--------------------
>>> a = 'Mark Watney'
>>> b = 'Mark Watney'
>>>
>>> a == b
True
>>> a is b
False

>>> 'Mark Watney' is 'Mark Watney'  # doctest: +SKIP
<...>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
True


String Interning
----------------
* Caching mechanism
* String intern pool
* String is immutable

Each time an instance of a string is created Python will create a new object
with completely new identity:

>>> id('Watney')  # doctest: +SKIP
4354445296
>>>
>>> id('Watney')  # doctest: +SKIP
4354447728

However if we create an identifier, then each time a string is created it
will result with the same interned string. Value of an identifier will add
to the string interning pool, from which Python returns a new objects:

>>> name = 'Watney'
>>>
>>> id('Watney')  # doctest: +SKIP
4354447984
>>>
>>> id('Watney')  # doctest: +SKIP
4354447984

However if we delete entry from string interning pool, Python will now
create a new instance of a string each time:

>>> del name
>>>
>>> id('Watney')  # doctest: +SKIP
4354449136
>>>
>>> id('Watney')  # doctest: +SKIP
4354449328


Type Identity
-------------
>>> name = ...
>>>
>>> type(name) is int
False
>>> type(name) is float
False
>>> type(name) is complex
False
>>> type(name) is bool
False
>>> type(name) is None
False
>>> type(name) is str
False
>>> type(name) is bytes
False
>>> type(name) is list
False
>>> type(name) is tuple
False
>>> type(name) is set
False
>>> type(name) is frozenset
False
>>> type(name) is dict
False


Object Identity
---------------
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> astro1 = Astronaut('Mark', 'Watney')
>>> astro2 = Astronaut('Mark', 'Watney')
>>>
>>> astro1 is astro2
False
>>>
>>> id(astro1)  # doctest: +SKIP
4421890496
>>> id(astro2)  # doctest: +SKIP
4421893328
>>>
>>> hex(id(astro1))  # doctest: +SKIP
'0x10790b1c0'
>>> hex(id(astro2))  # doctest: +SKIP
'0x10790bcd0'
>>>
>>> print(astro1)  # doctest: +SKIP
<Astronaut object at 0x107905820>
>>> print(astro2)  # doctest: +SKIP
<Astronaut object at 0x10790bcd0>


>>> class Astronaut:
...     pass
>>>
>>> class Cosmonaut:
...     pass
>>>
>>>
>>> Astronaut is Astronaut
True
>>>
>>> Cosmonaut is Cosmonaut
True
>>>
>>> Astronaut is Cosmonaut
False
>>>
>>> id(Astronaut)  # doctest: +SKIP
140570740200304
>>>
>>> id(Cosmonaut)  # doctest: +SKIP
140570185653984


Object Equality
---------------
>>> class Astronaut:
...     pass
>>>
>>> class Cosmonaut:
...     pass
>>>
>>> a = Astronaut()
>>> a.firstname = 'Mark'
>>> a.lastname = 'Watney'
>>>
>>> c = Cosmonaut()
>>> c.firstname = 'Mark'
>>> c.lastname = 'Watney'
>>>
>>> a is c
False
>>>
>>> a == c
False
>>>
>>>
>>> id(a)  # doctest: +SKIP
4503461584
>>>
>>> id(c)  # doctest: +SKIP
4503287120
>>>
>>> id(a.firstname)  # doctest: +SKIP
4488983024
>>>
>>> id(c.firstname)  # doctest: +SKIP
4488983024
>>>
>>> id(a.lastname)  # doctest: +SKIP
4503976496
>>>
>>> id(c.lastname)  # doctest: +SKIP
4503976496
>>>
>>> id(a.__dict__)  # doctest: +SKIP
4503717056
>>>
>>> id(c.__dict__)  # doctest: +SKIP
4503973504
>>>
>>> a.__dict__ is c.__dict__
False
>>>
>>> a.__dict__ == c.__dict__
True


Value Comparison
----------------
* ``==`` checks for object equality

>>> 'Mark Watney' == 'Mark Watney'
True

>>> a = 'Mark Watney'
>>> b = 'Mark Watney'
>>>
>>> a == b
True

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> astro1 = Astronaut('Mark', 'Watney')
>>> astro2 = Astronaut('Mark', 'Watney')
>>>
>>> astro1 == astro2
False


Compare Value vs. Identity
--------------------------
>>> name = 'Mark Watney'
>>> expected = 'Mark Watney'
>>>
>>> name == expected
True
>>> name is expected
False

>>> name = 'Mark Watney'
>>>
>>> name == 'Mark Watney'
True
>>>
>>> name is 'Mark Watney'  # doctest: +SKIP
<...>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
False


String Value vs Identity Problem
--------------------------------
* CPython optimization
* Can be misleading

>>> a = 'Mark Watney'
>>> b = 'Mark Watney'
>>>
>>> a == b
True
>>> a is b
False
>>> a is 'Mark Watney'  # doctest: +SKIP
<...>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
False

>>> a = 'Mark'
>>> b = 'Mark'
>>>
>>> a == b
True
>>> a is b
True
>>> a is 'Mark'  # doctest: +SKIP
<...>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
True


Use Case - 0x01
---------------
* Make Equal

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __eq__(self, other):
...         return self.firstname == other.firstname \
...            and self.lastname == other.lastname
>>>
>>>
>>> a1 = Astronaut('Mark', 'Watney')
>>> a2 = Astronaut('Mark', 'Watney')
>>>
>>> a1 == a2
True
>>> a1 is a2
False


Use Case - 0x02
---------------
* Equal Problem

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __eq__(self, other):
...         return self.firstname == other.firstname \
...            and self.lastname == other.lastname
>>>
>>>
>>> class Cosmonaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> a = Astronaut('Mark', 'Watney')
>>> c = Cosmonaut('Mark', 'Watney')
>>>
>>> a == c
True
>>> a is c
False


Use Case - 0x03
---------------
* Make Unequal

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __eq__(self, other):
...         return self.__class__ is other.__class__ \
...            and self.firstname == other.firstname \
...            and self.lastname == other.lastname
>>>
>>>
>>> class Cosmonaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> a = Astronaut('Mark', 'Watney')
>>> c = Cosmonaut('Mark', 'Watney')
>>>
>>> a == c
False
>>> a is c
False


Use Case - 0x04
---------------
* Overload
* Could be implemented through ``from functools import singledispatchmethod``
* More information: https://python.astrotech.io/advanced/funcprog/functools.html#singledispatchmethod

>>> # doctest: +SKIP
... from functools import singledispatchmethod
...
...
... class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     @singledispatchmethod
...     def __eq__(self, other):
...         return False
...
...     @__eq__.register
...     def _(self, other: 'Astronaut'):
...         return self.firstname == other.firstname \
...            and self.lastname == other.lastname
...
...     @__eq__.register
...     def _(self, other: 'Cosmonaut'):
...         return False
...
...
... class Cosmonaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...
... a = Astronaut('Mark', 'Watney')
... c = Cosmonaut('Mark', 'Watney')
...
... a == c
False
>>> a is c  # doctest: +SKIP
False


.. todo:: Assignments
