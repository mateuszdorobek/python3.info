Pickle Load
===========
* ``pickle.load()`` -> load from file
* ``pickle.loads()`` -> load from string (bytes)
* What if name was ``pickle.from_file()``?
* What if name was ``pickle.from_text()``?


SetUp
-----
>>> import pickle


Deserialize Str
---------------
>>> pickle.loads(b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00\x8c\x0bMark Watney\x94.')
'Mark Watney'


Deserialize Int
---------------
>>> pickle.loads(b'\x80\x03K\x01.')
1

>>> pickle.loads(b'\x80\x04K\x00.')
0

>>> pickle.loads(b'\x80\x04\x95\x06\x00\x00\x00\x00\x00\x00\x00J\xff\xff\xff\xff.')
-1


Deserialize Float
-----------------
>>> pickle.loads(b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xb9\x99\x99\x99\x99\x99\x9a.')
0.1

>>> pickle.loads(b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xc9\x99\x99\x99\x99\x99\x9a.')
0.2

>>> pickle.loads(b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xd3333333.')
0.3


Deserialize Sequence
--------------------
>>> pickle.loads(b'\x80\x03]q\x00(K\x01K\x02K\x03e.')
[1, 2, 3]

>>> pickle.loads(b'\x80\x03K\x01K\x02K\x03\x87q\x00.')
(1, 2, 3)

>>> pickle.loads(b'\x80\x03cbuiltins\nset\nq\x00]q\x01(K\x01K\x02K\x03e\x85q\x02Rq\x03.')
{1, 2, 3}


Deserialize Mapping
-------------------
>>> pickle.loads(b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01K\x01X\x01\x00\x00\x00bq\x02K\x02X\x01\x00\x00\x00cq\x03K\x03u.')
{'a': 1, 'b': 2, 'c': 3}


Use Case - 0x01
---------------
* Astronaut

>>> from dataclasses import dataclass, field, asdict
>>> from datetime import date, time, datetime, timezone, timedelta
>>> from pprint import pprint
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

>>> DATA = b'\x80\x04\x95\xc1\x01\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x04User\x94\x93\x94)\x81\x94}\x94(\x8c\tfirstname\x94\x8c\x04Mark\x94\x8c\x08lastname\x94\x8c\x06Watney\x94\x8c\x05email\x94\x8c\x10mwatney@nasa.gov\x94\x8c\x04born\x94\x8c\x08datetime\x94\x8c\x04date\x94\x93\x94C\x04\x07\xb1\x04\x0c\x94\x85\x94R\x94\x8c\x06height\x94G@f@\x00\x00\x00\x00\x00\x8c\x06weight\x94G@R\xe0\x00\x00\x00\x00\x00\x8c\x06groups\x94]\x94(h\x00\x8c\x05Group\x94\x93\x94)\x81\x94}\x94(\x8c\x03gid\x94K\x01\x8c\x04name\x94\x8c\x05users\x94ubh\x17)\x81\x94}\x94(h\x1aK\x02h\x1b\x8c\x05staff\x94ube\x8c\x0caccount_type\x94\x8c\x04user\x94\x8c\x0faccount_created\x94h\x0c\x8c\x08datetime\x94\x93\x94C\n\x07\xb1\x07\x15\x028\x0f\x00\x00\x00\x94h\x0c\x8c\x08timezone\x94\x93\x94h\x0c\x8c\ttimedelta\x94\x93\x94K\x00K\x00K\x00\x87\x94R\x94\x85\x94R\x94\x86\x94R\x94\x8c\x10account_modified\x94h$C\n\x07\xb1\x07\x15\x028\x0f\x00\x00\x00\x94h-\x86\x94R\x94\x8c\x11account_lastlogin\x94N\x8c\x12account_expiration\x94Nub.'
>>> mark = pickle.loads(DATA)  # doctest: +SKIP
>>>
>>> pprint(mark)  # doctest: +SKIP
User(firstname='Mark',
     lastname='Watney',
     email='mwatney@nasa.gov',
     born=datetime.date(1969, 4, 12),
     height=178.0,
     weight=75.5,
     groups=[Group(gid=1, name='users'), Group(gid=2, name='staff')],
     account_type='user',
     account_created=datetime.datetime(1969, 7, 21, 2, 56, 15, tzinfo=datetime.timezone.utc),
     account_modified=datetime.datetime(1969, 7, 21, 2, 56, 15, tzinfo=datetime.timezone.utc),
     account_lastlogin=None,
     account_expiration=None)
