Pickle Dump
===========
* ``pickle.dump()`` -> dump to file
* ``pickle.dumps()`` -> dump to string (bytes)
* What if name was ``pickle.to_file()``?
* What if name was ``pickle.to_text()``?

SetUp
-----
>>> import pickle


Serialize Str
-------------
>>> pickle.dumps('Mark Watney')
b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00\x8c\x0bMark Watney\x94.'


Serialize Int
-------------
>>> pickle.dumps(1)
b'\x80\x04K\x01.'

>>> pickle.dumps(0)
b'\x80\x04K\x00.'

>>> pickle.dumps(-1)
b'\x80\x04\x95\x06\x00\x00\x00\x00\x00\x00\x00J\xff\xff\xff\xff.'


Serialize Float
---------------
Note the difference in length between int and float:

>>> pickle.dumps(1)
b'\x80\x04K\x01.'
>>>
>>> pickle.dumps(1.0)
b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xf0\x00\x00\x00\x00\x00\x00.'


>>> pickle.dumps(0.1)
b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xb9\x99\x99\x99\x99\x99\x9a.'

>>> pickle.dumps(0.2)
b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xc9\x99\x99\x99\x99\x99\x9a.'

>>> pickle.dumps(0.3)
b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xd3333333.'


Serialize Sequence
------------------
>>> pickle.dumps([1, 2, 3])
b'\x80\x04\x95\x0b\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03e.'

>>> pickle.dumps((1, 2, 3))
b'\x80\x04\x95\t\x00\x00\x00\x00\x00\x00\x00K\x01K\x02K\x03\x87\x94.'

>>> pickle.dumps({1, 2, 3})
b'\x80\x04\x95\x0b\x00\x00\x00\x00\x00\x00\x00\x8f\x94(K\x01K\x02K\x03\x90.'


Serialize Mapping
-----------------
>>> pickle.dumps({'a': 1, 'b': 2, 'c': 3})
b'\x80\x04\x95\x17\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x01a\x94K\x01\x8c\x01b\x94K\x02\x8c\x01c\x94K\x03u.'


Use Case - 0x01
---------------
* Astronaut

>>> from dataclasses import dataclass, field, asdict
>>> from datetime import date, time, datetime, timezone, timedelta
>>> from typing import ClassVar
>>> import pickle
>>>
>>>
>>> @dataclass
... class Group:
...     gid: int
...     name: str
>>>
>>>
>>> @dataclass(frozen=True)
... class User:
...     firstname: str
...     lastname: str
...     email: str | None = None
...     born: date | None = None
...     height: int | float | None = field(default=None, metadata={'unit': 'cm', 'min': 156, 'max': 210})
...     weight: int | float | None = field(default=None, metadata={'unit': 'kg', 'min': 50, 'max': 90})
...     groups: list[Group] = field(default_factory=list)
...     account_type: str = field(default='user', metadata={'choices': ['guest', 'user', 'admin']})
...     account_created: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
...     account_modified: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
...     account_lastlogin: datetime | None = None
...     account_expiration: timedelta | None = None
...     AGE_MIN: ClassVar[int] = 30
...     AGE_MAX: ClassVar[int] = 50

>>> mark = User(
...     firstname='Mark',
...     lastname='Watney',
...     email='mwatney@nasa.gov',
...     born=date(1969, 4, 12),
...     height=178.0,
...     weight=75.5,
...     groups=[Group(gid=1, name='users'), Group(gid=2, name='staff')],
...     account_type='user',
...     account_created=datetime(1969, 7, 21, 2, 56, 15, 0, tzinfo=timezone.utc),
...     account_modified=datetime(1969, 7, 21, 2, 56, 15, 0, tzinfo=timezone.utc),
...     account_lastlogin=None,
...     account_expiration=None,
... )
>>>
>>> pickle.dumps(mark)  # doctest: +SKIP
b'\x80\x04\x95\xc1\x01\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x04User\x94\x93\x94)\x81\x94}\x94(\x8c\tfirstname\x94\x8c\x04Mark\x94\x8c\x08lastname\x94\x8c\x06Watney\x94\x8c\x05email\x94\x8c\x10mwatney@nasa.gov\x94\x8c\x04born\x94\x8c\x08datetime\x94\x8c\x04date\x94\x93\x94C\x04\x07\xb1\x04\x0c\x94\x85\x94R\x94\x8c\x06height\x94G@f@\x00\x00\x00\x00\x00\x8c\x06weight\x94G@R\xe0\x00\x00\x00\x00\x00\x8c\x06groups\x94]\x94(h\x00\x8c\x05Group\x94\x93\x94)\x81\x94}\x94(\x8c\x03gid\x94K\x01\x8c\x04name\x94\x8c\x05users\x94ubh\x17)\x81\x94}\x94(h\x1aK\x02h\x1b\x8c\x05staff\x94ube\x8c\x0caccount_type\x94\x8c\x04user\x94\x8c\x0faccount_created\x94h\x0c\x8c\x08datetime\x94\x93\x94C\n\x07\xb1\x07\x15\x028\x0f\x00\x00\x00\x94h\x0c\x8c\x08timezone\x94\x93\x94h\x0c\x8c\ttimedelta\x94\x93\x94K\x00K\x00K\x00\x87\x94R\x94\x85\x94R\x94\x86\x94R\x94\x8c\x10account_modified\x94h$C\n\x07\xb1\x07\x15\x028\x0f\x00\x00\x00\x94h-\x86\x94R\x94\x8c\x11account_lastlogin\x94N\x8c\x12account_expiration\x94Nub.'
