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
... class User:
...     firstname: str
...     lastname: str
...     role: str = field(default='user')

>>> User('Mark', 'Watney')
User(firstname='Mark', lastname='Watney', role='user')

>>> User('Mark', 'Watney', role='admin')
User(firstname='Mark', lastname='Watney', role='admin')

Note, that this is equal to:

>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     role: str = 'user'


Default Factory
---------------
* ``default_factory`` - Field factory

The following code will not work:

>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     groups: list[str] = ['users', 'staff', 'admins']
Traceback (most recent call last):
ValueError: mutable default <class 'list'> for field groups is not allowed: use default_factory

If you want to create a list with default values, you have to create a field
with ``default_factory=lambda: ['users', 'staff', 'admins']``. Lambda
expression will be evaluated on field initialization.

>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     groups: list[str] = field(default_factory=lambda: ['users', 'staff', 'admins'])

>>> User('Mark', 'Watney')
User(firstname='Mark', lastname='Watney', groups=['users', 'staff', 'admins'])


Init
----
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     role: str = field(default='user', init=False)

>>> User('Mark', 'Watney')
User(firstname='Mark', lastname='Watney', role='user')

>>> User('Mark', 'Watney', role='admin')
Traceback (most recent call last):
TypeError: User.__init__() got an unexpected keyword argument 'role'


Repr
----
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     role: str = field(repr=False)

>>> User('Mark', 'Watney', role='admin')
User(firstname='Mark', lastname='Watney')


kw_only
-------
* Since Python 3.10
* keyword-only

If true, this field will be marked as keyword-only. This is used when the
generated __init__() method's parameters are computed.

>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     role: str = field(kw_only=True)

>>> User('Mark', 'Watney', role='admin')
User(firstname='Mark', lastname='Watney', role='admin')

>>> User('Mark', 'Watney', 'admin')
Traceback (most recent call last):
TypeError: User.__init__() takes 3 positional arguments but 4 were given


Use Case - 0x01
---------------
* Validation

>>> from typing import ClassVar, Self
>>> from dataclasses import dataclass, field
>>> from datetime import time, datetime, timezone
>>>
>>>
>>> @dataclass
... class Group:
...     gid: int
...     name: str
>>>
>>> @dataclass(frozen=True)
... class User:
...     firstname: str
...     lastname: str
...     roles: list[str] = field(default_factory=lambda: ['users', 'staff', 'admins'])
...     friends: list[Self] = field(default_factory=list, kw_only=True)
...     groups: list[Group] = field(default_factory=list, kw_only=True)
...     account_created: datetime = field(default_factory=lambda: datetime.now(tz=timezone.utc), kw_only=True)
...     permissions: list[dict] = field(default_factory=dict, kw_only=True)
