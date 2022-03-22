Dataclass Helpers
=================
* ``fields()`` - Returns a tuple of Field objects
* ``asdict()`` - converts the dataclass to a dict
* ``astuple()`` - converts the dataclass to a tuple
* ``make_dataclass()`` - creates a new dataclass
* ``replace()`` - replaces field of a dataclass
* ``is_dataclass()`` - checks if argument is a dataclass


Fields
------
* ``fields(class_or_instance)``

Returns a tuple of Field objects that define the fields for this Data
Class. Accepts either a Data Class, or an instance of a Data Class. Raises
ValueError if not passed a Data Class or instance of one. Does not return
pseudo-fields which are ClassVar or InitVar.

>>> from dataclasses import dataclass, fields
>>>
>>>
>>> @dataclass
... class Mission:
...     year: int
...     name: str
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[Mission]
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney', missions=[Mission(2035, 'Ares3')])
>>> fields(Astronaut)  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
(Field(name='firstname',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object at 0x...>,default_factory=<dataclasses._MISSING_TYPE object at 0x...>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD),
 Field(name='lastname',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object at 0x...>,default_factory=<dataclasses._MISSING_TYPE object at 0x...>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD),
 Field(name='missions',type=list[Mission],default=<dataclasses._MISSING_TYPE object at 0x...>,default_factory=<dataclasses._MISSING_TYPE object at 0x...>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD))


As Dict
-------
* ``asdict(instance, *, dict_factory=dict)``

Converts the Data Class instance to a dict (by using the factory function
dict_factory). As dict does the conversion recursively.

>>> from dataclasses import dataclass, asdict
>>>
>>>
>>> @dataclass
... class Mission:
...     year: int
...     name: str
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[Mission]
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney', missions=[Mission(2035, 'Ares3')])
>>>
>>> asdict(astro)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'missions': [{'year': 2035, 'name': 'Ares3'}]}
>>>
>>> vars(astro)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'missions': [Mission(year=2035, name='Ares3')]}
>>>
>>> dict(astro)
Traceback (most recent call last):
TypeError: 'Astronaut' object is not iterable


As Tuple
--------
* ``astuple(*, tuple_factory=tuple)``

Converts the Data Class instance to a tuple (by using the factory function
tuple_factory). Each Data Class is converted to a tuple of its field
values. Data Classes, dicts, lists, and tuples are recursed into.

>>> from dataclasses import dataclass, astuple
>>>
>>>
>>> @dataclass
... class Mission:
...     year: int
...     name: str
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[Mission]
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney', missions=[Mission(2035, 'Ares3')])
>>>
>>> astuple(astro)
('Mark', 'Watney', [(2035, 'Ares3')])


Make Dataclass
--------------
* ``make_dataclass(cls_name, fields, *, bases=(), namespace=None)``

Creates a new Data Class with name cls_name, fields as defined in fields,
base classes as given in bases, and initialized with a namespace as given
in namespace.


Replace
-------
* ``replace(instance, **changes)``

Creates a new object of the same type of instance, replacing fields with
values from changes. If instance is not a Data Class, raises TypeError.
If values in changes do not specify fields, raises TypeError.


Is Dataclass
------------
* ``is_dataclass(class_or_instance)``

Returns True if its parameter is a dataclass or an instance of one,
otherwise returns False.

>>> from dataclasses import dataclass, is_dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> is_dataclass(Astronaut)
True
>>>
>>> is_dataclass(astro)
True

>>> from dataclasses import is_dataclass
>>>
>>>
>>> class Astronaut:
...     firstname: str
...     lastname: str
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> is_dataclass(Astronaut)
False
>>>
>>> is_dataclass(astro)
False
