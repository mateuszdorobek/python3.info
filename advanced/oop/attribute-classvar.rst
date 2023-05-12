OOP Attribute ClassVar
======================
* Class Variables
* Instance Variables
* Type Annotations


Class Variables
---------------
* Fields defined on a class
* Must have default values
* Share state
* Also known as 'static attributes'

Class variables are defined on a class:

>>> class User:
...     pass
>>>
>>>
>>> User.firstname = 'Mark'
>>> User.lastname = 'Watney'

Class variables are defined in a class:

>>> class User:
...     firstname = 'Mark'
...     lastname = 'Watney'

In order to show all the variables use ``vars()`` on the class:

>>> vars(User)  # doctest: +NORMALIZE_WHITESPACE
mappingproxy({'__module__': '__main__',
              'firstname': 'Mark',
              'lastname': 'Watney',
              '__dict__': <attribute '__dict__' of 'User' objects>,
              '__weakref__': <attribute '__weakref__' of 'User' objects>,
              '__doc__': None})


Instance Variables
------------------
* Fields defined on an instance
* Do not share state (unless mutable argument in method signature)
* By convention initialized in ``__init__()``
* Also known as 'dynamic attributes'

Instance variables are defined on an instance:

>>> class User:
...     pass
>>>
>>>
>>> mark = User()
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'

Instance variables are defined in init:

>>> class User:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'

Instance variables with variable values:

>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname

In order to show all the variables use ``vars()`` on an instance:

>>> mark = User('Mark', 'Watney')
>>>
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}


Class and Instance Variables
----------------------------
Class and instance variables defined in code:

>>> class User:
...     pass
>>>
>>>
>>> User.firstname = 'Mark'
>>> User.lastname = 'Watney'
>>>
>>> mark = User()
>>> mark.firstname = 'Melissa'
>>> mark.lastname = 'Lewis'

Class and instance variables defined in class:

>>> class User:
...     firstname = 'Mark'
...     lastname = 'Watney'
...
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'

Note, the last example makes not meaningful sense. Instance variables
will shadow class variables.

>>> vars(User)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
mappingproxy({'__module__': '__main__',
              'firstname': 'Mark',
              'lastname': 'Watney',
              '__init__': <function User.__init__ at 0x...>,
              '__dict__': <attribute '__dict__' of 'User' objects>,
              '__weakref__': <attribute '__weakref__' of 'User' objects>,
              '__doc__': None})

>>> mark = User()
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}


Annotations
-----------
Type annotations are not variable definition:

>>> x: int
>>>
>>> print(x)
Traceback (most recent call last):
NameError: name 'x' is not defined

Type annotations will only tell, that if there will be an identifier
with name ``x`` then it should be an ``int``:

>>> x: int
>>> x = 1
>>>
>>> print(x)
1

Typically it is written in shorter form:

>>> x: int = 1
>>>
>>> print(x)
1

These are not attributes at all (sic!). These are type annotations only,
and they do not exist before initialization in a code:

>>> class User:
...     firstname: str
...     lastname: str

>>> vars(User)  # doctest: +NORMALIZE_WHITESPACE
mappingproxy({'__module__': '__main__',
              '__annotations__': {'firstname': <class 'str'>, 'lastname': <class 'str'>},
              '__dict__': <attribute '__dict__' of 'User' objects>,
              '__weakref__': <attribute '__weakref__' of 'User' objects>,
              '__doc__': None})

Class variables with type annotations:

>>> class User:
...     firstname: str = 'Mark'
...     lastname: str = 'Watney'

>>> vars(User)  # doctest: +NORMALIZE_WHITESPACE
mappingproxy({'__module__': '__main__',
              '__annotations__': {'firstname': <class 'str'>, 'lastname': <class 'str'>},
              'firstname': 'Mark',
              'lastname': 'Watney',
              '__dict__': <attribute '__dict__' of 'User' objects>,
              '__weakref__': <attribute '__weakref__' of 'User' objects>,
              '__doc__': None})

Class variables with proper type annotations:

>>> from typing import ClassVar
>>>
>>>
>>> class User:
...     firstname: ClassVar[str] = 'Mark'
...     lastname: ClassVar[str] = 'Watney'

Instance variables with type annotations:

>>> class User:
...     firstname: str
...     lastname: str
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname


Dataclass Fields
----------------
* Dataclass uses class variables notation to create instance fields
* Dataclass do not validate type annotations, unless ``ClassVar``

>>> from dataclasses import dataclass
>>> from typing import ClassVar

Instance variables:

>>> @dataclass
... class User:
...     firstname: str
...     lastname: str

>>> vars(User)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
mappingproxy({'__module__': '__main__',
              '__annotations__': {'firstname': <class 'str'>, 'lastname': <class 'str'>},
              '__dict__': <attribute '__dict__' of 'User' objects>,
              '__weakref__': <attribute '__weakref__' of 'User' objects>,
              '__doc__': 'User(firstname: str, lastname: str)',
              '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False),
              '__dataclass_fields__': {'firstname': Field(name='firstname',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object at 0x...>,default_factory=<dataclasses._MISSING_TYPE object at 0x...>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD),
               'lastname': Field(name='lastname',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object at 0x...>,default_factory=<dataclasses._MISSING_TYPE object at 0x...>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)},
              '__init__': <function User.__init__ at 0x...>,
              '__repr__': <function User.__repr__ at 0x...>,
              '__eq__': <function User.__eq__ at 0x...>,
              '__hash__': None,
              '__match_args__': ('firstname', 'lastname')})

Instance variables with default values:

>>> @dataclass
... class User:
...     firstname: str = 'Mark'
...     lastname: str = 'Watney'

>>> vars(User)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
mappingproxy({'__module__': '__main__',
              '__annotations__': {'firstname': <class 'str'>, 'lastname': <class 'str'>},
              'firstname': 'Mark',
              'lastname': 'Watney',
              '__dict__': <attribute '__dict__' of 'User' objects>,
              '__weakref__': <attribute '__weakref__' of 'User' objects>,
              '__doc__': "User(firstname: str = 'Mark', lastname: str = 'Watney')",
              '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False),
              '__dataclass_fields__': {'firstname': Field(name='firstname',type=<class 'str'>,default='Mark',default_factory=<dataclasses._MISSING_TYPE object at 0x...>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD),
               'lastname': Field(name='lastname',type=<class 'str'>,default='Watney',default_factory=<dataclasses._MISSING_TYPE object at 0x...>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)},
              '__init__': <function User.__init__ at 0x...>,
              '__repr__': <function User.__repr__ at 0x...>,
              '__eq__': <function User.__eq__ at 0x...>,
              '__hash__': None,
              '__match_args__': ('firstname', 'lastname')})

>>> mark = User()
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}


Class variables must have default values:

>>> @dataclass
... class User:
...     firstname: ClassVar[str] = 'Mark'
...     lastname: ClassVar[str] = 'Watney'


Init Variables
--------------
>>> from dataclasses import InitVar

>>> @dataclass
... class User:
...     firstname: InitVar[str] = 'Mark'
...     lastname: InitVar[str] = 'Watney'


Class vs. Instance Variables
----------------------------
Lets define a class with class variable:

>>> class User:
...     agency = 'NASA'

Lets create three instances of ``User`` class:

>>> mark = User()
>>> melissa = User()
>>> rick = User()

We will print ``agency`` field:

>>> print(mark.agency)
NASA
>>>
>>> print(melissa.agency)
NASA
>>>
>>> print(rick.agency)
NASA
>>>
>>> print(User.agency)
NASA

Lets change field on a class and print ``agency`` field:

>>> User.agency = 'ESA'
>>>
>>>
>>> print(mark.agency)
ESA
>>>
>>> print(melissa.agency)
ESA
>>>
>>> print(rick.agency)
ESA
>>>
>>> print(User.agency)
ESA

Lets change field on an instance and print ``agency`` field:

>>> mark.agency = 'POLSA'
>>>
>>>
>>> print(mark.agency)
POLSA
>>>
>>> print(melissa.agency)
ESA
>>>
>>> print(rick.agency)
ESA
>>>
>>> print(User.agency)
ESA

Note, that the class which defined instance variable shadowed
the class variable.

Lets change field on a class and print ``agency`` field:

>>> User.agency = 'NASA'
>>>
>>>
>>> print(mark.agency)
POLSA
>>>
>>> print(melissa.agency)
NASA
>>>
>>> print(rick.agency)
NASA
>>>
>>> print(User.agency)
NASA

Lets delete field from an instance and print ``agency`` field:

>>> del mark.agency
>>>
>>>
>>> print(mark.agency)
NASA
>>>
>>> print(melissa.agency)
NASA
>>>
>>> print(rick.agency)
NASA
>>>
>>> print(User.agency)
NASA


Mechanism
---------
* ``vars(obj)`` is will return ``obj.__dict__``

>>> class User:
...     firstname = 'Mark'
...     lastname = 'Watney'
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> melissa = User('Melissa', 'Lewis')
>>>
>>> vars(melissa)
{'firstname': 'Melissa', 'lastname': 'Lewis'}
>>>
>>> vars(User)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
mappingproxy({'__module__': '__main__',
              'firstname': 'Mark',
              'lastname': 'Watney',
              '__init__': <function User.__init__ at 0x...>,
              '__dict__': <attribute '__dict__' of 'User' objects>,
              '__weakref__': <attribute '__weakref__' of 'User' objects>,
              '__doc__': None})


Use Case - 0x01
---------------
>>> from typing import ClassVar
>>>
>>>
>>> class User:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: ClassVar[int] = 30
...     AGE_MAX: ClassVar[int] = 50


Use Case - 0x02
---------------
>>> from typing import ClassVar
>>>
>>>
>>> class User:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: ClassVar[int] = 30
...     AGE_MAX: ClassVar[int] = 50
...
...     def __init__(self, firstname, lastname, age):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.age = age
...
...         if not self.AGE_MIN <= self.age < self.AGE_MAX:
...             raise ValueError('age is invalid')


Use Case - 0x03
---------------
>>> from dataclasses import dataclass
>>> from typing import ClassVar
>>>
>>>
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: ClassVar[int] = 30
...     AGE_MAX: ClassVar[int] = 50
...
...     def __post_init__(self):
...         if not self.AGE_MIN <= self.age < self.AGE_MAX:
...             raise ValueError('age is invalid')


Assignments
-----------
.. todo:: Assignments
