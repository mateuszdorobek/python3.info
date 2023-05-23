Dataclass Parameters
====================
* ``init`` - Generate ``__init__()`` method
* ``repr`` - Generate ``__repr__()`` method
* ``eq`` - Generate ``__eq__()`` and ``__ne__()`` methods
* ``order`` - Generate ``__lt__()``, ``__le__()``, ``__gt__()``, and ``__ge__()`` methods
* ``unsafe_hash`` - If False: the ``__hash__()`` method is generated according to how eq and frozen are set
* ``frozen`` - If ``True``: assigning to fields will generate an exception
* ``match_args`` - Generate ``__match_args__()`` method
* ``kw_only`` - Mark all fields as keyword-only
* ``slots`` - Create class with ``__slots__``

.. csv-table:: Dataclass options
    :header: "Option", "Default", "Description (if True)"
    :widths: 10, 10, 80

    ``init``,         ``True``,   "Generate ``__init__()`` method"
    ``repr``,         ``True``,   "Generate ``__repr__()`` method"
    ``eq``,           ``True``,   "Generate ``__eq__()`` and ``__ne__()`` methods"
    ``order``,        ``False``,  "Generate ``__lt__()``, ``__le__()``, ``__gt__()``, and ``__ge__()`` methods"
    ``unsafe_hash``,  ``False``,  "If False: the ``__hash__()`` method is generated according to how eq and frozen are set"
    ``frozen``,       ``False``,  "If ``True``: assigning to fields will generate an exception"
    ``match_args``,   ``True``,   "Generate ``__match_args__()`` method"
    ``kw_only``,      ``False``,  "Mark all fields as keyword-only"
    ``slots``,        ``False``,  "Create class with ``__slots__``"


SetUp
-----
>>> from dataclasses import dataclass


Example
-------
>>> @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False,
...            frozen=False, match_args=True, kw_only=False, slots=False)
... class User:
...     firstname: str
...     lastname: str
>>>
>>> a = User('Mark', 'Watney')
>>> b = User('Mark', 'Watney')
>>> c = User('Melissa', 'Lewis')


Init
----
* ``init=True`` by default
* Generate ``__init__()`` method

>>> @dataclass(init=True)
... class Point:
...     x: int
...     y: int
>>>
>>>
>>> p = Point(10, 20)
>>>
>>> print(p)
Point(x=10, y=20)

>>> @dataclass(init=False)
... class Point:
...     x: int
...     y: int
>>>
>>>
>>> p = Point(10, 20)
Traceback (most recent call last):
TypeError: Point() takes no arguments


Repr
----
* ``repr=True`` by default
* Generate ``__repr__()`` for pretty printing

>>> @dataclass(repr=True)
... class Point:
...     x: int
...     y: int
>>>
>>>
>>> p = Point(10, 20)
>>>
>>> print(p)
Point(x=10, y=20)

>>> @dataclass(repr=False)
... class Point:
...     x: int
...     y: int
>>>
>>>
>>> p = Point(10, 20)
>>>
>>> print(p)  # doctest: +ELLIPSIS
<__main__.Point object at 0x...>


Frozen
------
* ``frozen=False`` by default
* Prevents object from modifications
* Assigning to fields will generate an exception

>>> @dataclass(frozen=False)
... class Point:
...     x: int
...     y: int
>>>
>>>
>>> p = Point(10, 20)
>>> p.x = 30
>>>
>>> print(p)
Point(x=30, y=20)

>>> @dataclass(frozen=True)
... class Point:
...     x: int
...     y: int
>>>
>>>
>>> p = Point(10, 20)
>>> p.x = 30
Traceback (most recent call last):
dataclasses.FrozenInstanceError: cannot assign to field 'x'


Eq
--
* ``eq=True`` by default
* when ``eq=False`` compare objects by ``id()`` not values
* when ``eq=True`` compare objects by value not ``id()``

>>> @dataclass(eq=True)
... class User:
...     firstname: str
...     lastname: str
>>>
>>>
>>> a = User('Mark', 'Watney')
>>> b = User('Mark', 'Watney')
>>> c = User('Melissa', 'Lewis')
>>>
>>> a == a
True
>>> a == b
True
>>> a == c
False

>>> @dataclass(eq=False)
... class User:
...     firstname: str
...     lastname: str
>>>
>>>
>>> a = User('Mark', 'Watney')
>>> b = User('Mark', 'Watney')
>>> c = User('Melissa', 'Lewis')
>>>
>>> a == a
True
>>> a == b
False
>>> a == c
False


Hash
----
* ``hash=False`` by default
* the ``__hash__()`` method is generated according to how eq and frozen are set


Order
-----
* ``order=False`` by default
* Generate ``__lt__()``, ``__le__()``, ``__gt__()``, and ``__ge__()`` methods


Match_args
----------
* ``match_args=True`` by default
* Since Python 3.10

If true, the __match_args__ tuple will be created from the list of parameters
to the generated __init__() method (even if __init__() is not generated, see
above). If false, or if __match_args__ is already defined in the class, then
__match_args__ will not be generated.
New in version 3.10.


Kw_only
----------
* ``kw_only=False`` by default
* Mark all fields as keyword-only
* Since Python 3.10

If true, then all fields will be marked as keyword-only. If a field is marked
as keyword-only, then the only affect is that the __init__() parameter
generated from a keyword-only field must be specified with a keyword when
__init__() is called. There is no effect on any other aspect of dataclasses.


Slots
-----
* ``slots=False`` by default
* Create class with ``__slots__``
* Since Python 3.10

If true, __slots__ attribute will be generated and new class will be returned
instead of the original one. If __slots__ is already defined in the class,
then TypeError is raised.

>>> @dataclass(slots=True)
... class User:
...     firstname: str
...     lastname: str
...     __slots__ = ('firstname', 'lastname')
...
...     def say_hello(self):
...         return f'Hello {self.firstname} {self.lastname}'
...
Traceback (most recent call last):
TypeError: User already specifies __slots__

>>> @dataclass(slots=True)
... class User:
...     firstname: str
...     lastname: str
...
...     def say_hello(self):
...         return f'Hello {self.firstname} {self.lastname}'
>>>
>>> vars(User)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
mappingproxy({'__module__': '__main__',
              '__annotations__': {'firstname': <class 'str'>, 'lastname': <class 'str'>},
              'say_hello': <function User.say_hello at 0x...>,
              '__doc__': 'User(firstname: str, lastname: str)',
              '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False),
              '__dataclass_fields__': {'firstname': Field(name='firstname',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object at 0x...>,default_factory=<dataclasses._MISSING_TYPE object at 0x...>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD),
               'lastname': Field(name='lastname',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object at 0x...>,default_factory=<dataclasses._MISSING_TYPE object at 0x...>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)},
              '__init__': <function User.__init__ at 0x...>,
              '__repr__': <function User.__repr__ at 0x...>,
              '__eq__': <function User.__eq__ at 0x...>,
              '__hash__': None,
              '__match_args__': ('firstname', 'lastname'),
              '__slots__': ('firstname', 'lastname'),
              'firstname': <member 'firstname' of 'User' objects>,
              'lastname': <member 'lastname' of 'User' objects>})
>>>
>>> a = User('Mark', 'Watney')
>>>
>>> a
User(firstname='Mark', lastname='Watney')
>>>
>>> vars(a)
Traceback (most recent call last):
TypeError: vars() argument must have __dict__ attribute
>>>
>>> a.__slots__
('firstname', 'lastname')
>>>
>>> {attrname: getattr(a, attrname) for attrname in a.__slots__}
{'firstname': 'Mark', 'lastname': 'Watney'}
