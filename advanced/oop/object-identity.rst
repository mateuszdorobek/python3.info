OOP Object Identity
===================
* ``=`` assignment
* ``==`` checks for object equality
* ``is`` checks for object identity

In Python, identity and value comparison are two different ways of comparing
objects. Identity comparison (``is`` operator) checks whether two objects are
the same object in memory, i.e. whether they have the same memory address.
Value comparison (``==`` operator) checks whether two objects have the same
value, i.e. whether they are equal according to their values.

Here's an example to illustrate the difference between identity and value
comparison:

>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>>
>>> # Identity comparison
>>> print(a is b)
False
>>>
>>> # Value comparison
>>> print(a == b)
True

In this example, ``a`` and ``b`` are two different objects in memory, even
though they have the same value. The identity comparison using the ``is``
operator returns ``False``, because ``a`` and ``b`` are not the same object
in memory. The value comparison using the ``==`` operator returns ``True``,
because ``a`` and ``b`` have the same value.

It's important to note that identity comparison (``is`` operator) is more
strict than value comparison (``==`` operator). If two objects are identical,
they are also equal in value. However, two objects that are equal in value
are not necessarily identical. In general, it's more common to use value
comparison (``==`` operator) when comparing objects in Python, unless you
specifically need to check whether two objects are the same object in memory.

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


Increment Add
-------------
>>> x = 1
>>> id(x)  # doctest: +SKIP
4535726776
>>>
>>> x += 1
>>> id(x)  # doctest: +SKIP
4535726808

>>> x = [1]
>>> id(x)  # doctest: +SKIP
4570905344
>>>
>>> x[0] += 1
>>> id(x)  # doctest: +SKIP
4570905344


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

>>> x = 256
>>> id(x)  # doctest: +SKIP
4474506792
>>>
>>> del x
>>>
>>> x = 256
>>> id(x)  # doctest: +SKIP
4474506792

>>> x = 257
>>> id(x)  # doctest: +SKIP
4509456400
>>>
>>> del x
>>>
>>> x = 257
>>> id(x)  # doctest: +SKIP
4509455696

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

>>> id(-6)  # doctest: +SKIP
4463320144
>>>
>>> id(-6)  # doctest: +SKIP
4463321840

Mind, that address for objects less or equal to 256 is the same, but
above 256 object address is different:

>>> a = 256
>>> b = 257
>>>
>>> id(a)  # doctest: +SKIP
4565299048
>>> id(b)  # doctest: +SKIP
4602009488
>>>
>>> del a
>>> del b
>>>
>>> a = 256
>>> b = 257
>>>
>>> id(a)  # doctest: +SKIP
4565299048
>>> id(b)  # doctest: +SKIP
4602005616

Mind, that address for objects less or equal to 256 is the same, but
above 256 object address is different:

>>> a = 256
>>> b = 256
>>> x = 257
>>> y = 257
>>>
>>> id(a)  # doctest: +SKIP
4565299048
>>>
>>> id(b)  # doctest: +SKIP
4565299048
>>>
>>> id(x)  # doctest: +SKIP
4602004784
>>>
>>> id(y)  # doctest: +SKIP
4602012112


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

Example:

>>> a = 'Mark'
>>> b = 'Mark'
>>> c = format('Mark')
>>> d = str('Mark')
>>> e = str('Mark'+'')
>>> f = str.__new__(str, 'Mark')
>>> g = a + ''
>>>
>>> id(a)  # doctest: +SKIP
4498017136
>>> id(b)  # doctest: +SKIP
4498017136
>>> id(c)  # doctest: +SKIP
4498017136
>>> id(d)  # doctest: +SKIP
4498017136
>>> id(e)  # doctest: +SKIP
4498017136
>>> id(f)  # doctest: +SKIP
4498017136
>>> id(g)  # doctest: +SKIP
4498017136


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
>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> a = User('Mark', 'Watney')
>>> b = User('Mark', 'Watney')
>>>
>>> a is b
False
>>>
>>> id(a)  # doctest: +SKIP
4421890496
>>> id(b)  # doctest: +SKIP
4421893328
>>>
>>> hex(id(a))  # doctest: +SKIP
'0x10790b1c0'
>>> hex(id(b))  # doctest: +SKIP
'0x10790bcd0'
>>>
>>> print(a)  # doctest: +SKIP
<User object at 0x107905820>
>>> print(b)  # doctest: +SKIP
<User object at 0x10790bcd0>


>>> class User:
...     pass
>>>
>>> class Admin:
...     pass
>>>
>>>
>>> User is User
True
>>>
>>> Admin is Admin
True
>>>
>>> User is Admin
False
>>>
>>> id(User)  # doctest: +SKIP
140570740200304
>>>
>>> id(Admin)  # doctest: +SKIP
140570185653984


Object Equality
---------------
>>> class Vehicle:
...     def __init__(self, name):
...         self.name = name
...
...     def __eq__(self, other):
...         return isinstance(self, other.__class__) \
...            and self.name == other.name
...
...
>>> class Car(Vehicle):
...     pass
...
>>> class Truck(Vehicle):
...     pass
...
...
...
>>> a = Car('Mercedes')
>>> b = Car('Mercedes')
>>> c = Truck('Mercedes')
>>> d = Vehicle('Mercedes')

>>> a == a
True
>>> a == b
True
>>> a == c
False
>>> a == d
True

>>> d == a
True
>>> d == b
True
>>> d == c
True
>>> d == d
True

>>> c == a
False
>>> c == b
False
>>> c == c
True
>>> c == d
True


Dataclasses Equality
--------------------
* By default ``eq=True`` (if not specified)

>>> from dataclasses import dataclass

>>> @dataclass(eq=False)
... class Fruit:
...     name: str
>>>
>>> a = Fruit('Apple')
>>> b = Fruit('Apple')
>>>
>>> a is b
False
>>>
>>> a == b
False

>>> @dataclass(eq=True)
... class Fruit:
...     name: str
>>>
>>> a = Fruit('Apple')
>>> b = Fruit('Apple')
>>>
>>> a is b
False
>>>
>>> a == b
True

>>> @dataclass
... class Fruit:
...     name: str
>>>
>>> @dataclass
... class Company:
...     name: str
>>>
>>> a = Fruit('Apple')
>>> b = Fruit('Apple')
>>> c = Company('Apple')
>>>
>>> a is b
False
>>>
>>> a is c
False
>>>
>>> a == b
True
>>>
>>> a == c
False


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

>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> a = User('Mark', 'Watney')
>>> b = User('Mark', 'Watney')
>>>
>>> a == b
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


Performance
-----------
Cached int:

>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... x = 1
15.5 ns ± 5.22 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
>>>
>>>
>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... x = int(1)
69.4 ns ± 22.2 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

Uncached int:

>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... x = 257
16 ns ± 8.24 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
>>>
>>>
>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... x = int(257)
64.7 ns ± 19.6 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

str:

>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... x = 'Mark'
17.8 ns ± 6.41 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
>>>
>>>
>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... x = str('Mark')
33.3 ns ± 6.99 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

bool:

>>> x = True
>>>
>>>
>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... x == True
29.2 ns ± 8.83 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
>>>
>>>
... %%timeit -r 1000 -n 1000  # doctest: +SKIP
... x is True
22.9 ns ± 7.37 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> x = True
>>>
>>>
>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... x == 1
31.7 ns ± 9.2 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
>>>
>>>
>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... x is 1
<magic-timeit-stmt>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
<magic-timeit>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
22.4 ns ± 7.01 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

None:

>>> x = None
>>>
>>>
>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... x is None
22.2 ns ± 6.89 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
>>>
>>>
>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... x == None
27.9 ns ± 7.41 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

Builtin type:

>>> x = 1
>>>
>>>
>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... type(x) == int
38.9 ns ± 9.52 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
>>>
>>>
>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... type(x) is int
34.2 ns ± 7.59 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

Custom type:

>>> class User:
...     pass
>>>
>>> x = User()
>>>
>>>
>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... type(x) is User
33.9 ns ± 11.2 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
>>>
>>>
>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... type(x) == User
40.3 ns ± 10.3 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)


Use Case - 0x01
---------------
>>> class User:
...     pass
>>>
>>> class Admin:
...     pass
>>>
>>> a = User()
>>> a.firstname = 'Mark'
>>> a.lastname = 'Watney'
>>>
>>> c = Admin()
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


Use Case - 0x02
---------------
* Make Equal

>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __eq__(self, other):
...         return self.firstname == other.firstname \
...            and self.lastname == other.lastname
>>>
>>>
>>> a = User('Mark', 'Watney')
>>> b = User('Mark', 'Watney')
>>>
>>> a == b
True
>>> a is b
False


Use Case - 0x03
---------------
* Equal Problem

>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __eq__(self, other):
...         return self.firstname == other.firstname \
...            and self.lastname == other.lastname
>>>
>>>
>>> class Admin:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> a = User('Mark', 'Watney')
>>> b = Admin('Mark', 'Watney')
>>>
>>> a == b
True
>>> a is b
False


Use Case - 0x04
---------------
* Make Unequal

>>> class User:
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
>>> class Admin:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> a = User('Mark', 'Watney')
>>> b = Admin('Mark', 'Watney')
>>>
>>> a == b
False
>>> a is b
False


.. todo:: Assignments
