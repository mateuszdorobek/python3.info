Dataclass Field
===============
* ``default`` - Default value for the field
* ``default_factory`` - Field factory
* ``init`` - Use this field in ``__init__()``
* ``repr`` - Use this field in ``__repr__()``
* ``hash`` - Use this field in ``__hash__()``
* ``compare`` - Use this field in comparison functions (le, lt, gt, ge, eq, ne)
* ``metadata`` - For storing extra information about field
* ``kw_only`` - field will become a keyword-only parameter to ``__init__()``

.. code-block:: text

    def field(*,
              default: Any,
              default_factory: Any,
              init: bool = True,
              repr: bool = True,
              hash: bool = None,
              compare: bool = True,
              metadata: dict[str,Any] = None,
              kw_only: bool) -> None

SetUp
-----
>>> from dataclasses import dataclass, field
>>> from typing import ClassVar


Default
-------
* ``default`` - Default value for the field

>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     mission: str = 'Ares3'

>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     mission: str = field(default='Ares3')


Default Factory
---------------
* ``default_factory`` - Field factory

The following code will not work:

>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[str] = ['Ares3', 'Apollo18']
Traceback (most recent call last):
ValueError: mutable default <class 'list'> for field missions is not allowed: use default_factory

If you want to create a list with default values, you have to create a field
with ``default_factory=lambda: ['Ares3', 'Apollo18']``. Lambda expression
will be evaluated on field initialization.

>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[str] = field(default_factory=lambda: ['Ares3', 'Apollo18'])
>>>
>>>
>>> Astronaut('Mark', 'Watney')
Astronaut(firstname='Mark', lastname='Watney', missions=['Ares3', 'Apollo18'])


Init
----
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: ClassVar[int] = field(default=27, init=False)
...     AGE_MAX: ClassVar[int] = field(default=50, init=False)
>>>
>>>
>>> Astronaut('Mark', 'Watney', age=44)
Astronaut(firstname='Mark', lastname='Watney', age=44)


Repr
----
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: ClassVar[int] = field(default=27, init=False, repr=False)
...     AGE_MAX: ClassVar[int] = field(default=50, init=False, repr=False)
>>>
>>>
>>> Astronaut('Mark', 'Watney', age=44)
Astronaut(firstname='Mark', lastname='Watney', age=44)


kw_only
-------
* Since Python 3.10

If true, this field will be marked as keyword-only. This is used when the
generated __init__() method's parameters are computed.

>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: int = field(kw_only=True)


Use Case - 0x01
---------------
* Validation

>>> from typing import ClassVar
>>> from dataclasses import dataclass, field
>>> from datetime import time, datetime, timezone
>>>
>>>
>>> @dataclass
... class Mission:
...     year: int
...     name: str
>>>
>>>
>>> @dataclass(frozen=True)
... class Astronaut:
...     firstname: str
...     lastname: str
...     groups: list[str] = field(default_factory=lambda: ['astronauts', 'managers'])
...     friends: dict[str,str] = field(default_factory=dict, kw_only=True)
...     assignments: list[str] = field(default_factory=list, kw_only=True)
...     missions: list[Mission] = field(default_factory=list, kw_only=True)
...     account_created: datetime = field(default_factory=lambda: datetime.now(tz=timezone.utc), kw_only=True)
...     AGE_MIN: ClassVar[int] = field(default=30, init=False, repr=False)
...     AGE_MAX: ClassVar[int] = field(default=50, init=False, repr=False)
