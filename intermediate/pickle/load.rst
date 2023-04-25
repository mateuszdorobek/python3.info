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

>>> import pickle
>>> from dataclasses import dataclass, field
>>> from datetime import date, time, datetime, timezone, timedelta
>>>
>>>
>>> @dataclass
... class Mission:
...     year: int
...     name: str
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     born: date
...     job: str = 'astronaut'
...     agency: str = field(default='NASA', metadata={'choices': ['NASA', 'ESA']})
...     age: int | None = None
...     height: int | float | None = field(default=None, metadata={'unit': 'cm', 'min': 156, 'max': 210})
...     weight: int | float | None = field(default=None, metadata={'unit': 'kg', 'min': 50, 'max': 90})
...     groups: list[str] = field(default_factory=lambda: ['astronauts', 'managers'])
...     friends: dict[str,str] = field(default_factory=dict)
...     assignments: list[str] | None = field(default=None, metadata={'choices': ['Apollo18', 'Ares3', 'STS-136']})
...     missions: list[Mission] = field(default_factory=list)
...     experience: timedelta = timedelta(hours=0)
...     account_last_login: datetime | None = None
...     account_created: datetime = datetime.now(tz=timezone.utc)
...     AGE_MIN: int = field(default=30, repr=False)
...     AGE_MAX: int = field(default=50, repr=False)
...
...     def __post_init__(self):
...         HEIGHT_MIN = self.__dataclass_fields__['height'].metadata['min']
...         HEIGHT_MAX = self.__dataclass_fields__['height'].metadata['max']
...         WEIGHT_MIN = self.__dataclass_fields__['weight'].metadata['min']
...         WEIGHT_MAX = self.__dataclass_fields__['weight'].metadata['max']
...         if not HEIGHT_MIN <= self.height < HEIGHT_MAX:
...             raise ValueError(f'Height {self.height} is not in between {HEIGHT_MIN} and {HEIGHT_MAX}')
...         if not WEIGHT_MIN <= self.weight < WEIGHT_MAX:
...             raise ValueError(f'Height {self.weight} is not in between {WEIGHT_MIN} and {WEIGHT_MAX}')
...         if self.age not in range(self.AGE_MIN, self.AGE_MAX):
...             raise ValueError('Age is not valid for an astronaut')
>>>
>>>
>>> astro = Astronaut(firstname='Mark',
...                   lastname='Watney',
...                   born=date(1961, 4, 12),
...                   age=44,
...                   height=175.5,
...                   weight=75.5,
...                   assignments=['STS-136'],
...                   missions=[Mission(2035, 'Ares 3'), Mission(1973, 'Apollo 18')])
>>>
>>>
>>> data = pickle.loads(b'\x80\x04\x95\xd6\x01\x00\x00\x00\x00\x00\x00}\x94(\x8c\tfirstname\x94\x8c\x04Mark\x94\x8c\x08lastname\x94\x8c\x06Watney\x94\x8c\x04born\x94\x8c\x08datetime\x94\x8c\x04date\x94\x93\x94C\x04\x07\xa9\x04\x0c\x94\x85\x94R\x94\x8c\x03job\x94\x8c\tastronaut\x94\x8c\x06agency\x94\x8c\x04NASA\x94\x8c\x03age\x94K,\x8c\x06height\x94G@e\xf0\x00\x00\x00\x00\x00\x8c\x06weight\x94G@R\xe0\x00\x00\x00\x00\x00\x8c\x06groups\x94]\x94(\x8c\nastronauts\x94\x8c\x08managers\x94e\x8c\x07friends\x94}\x94\x8c\x0bassignments\x94]\x94\x8c\x07STS-136\x94a\x8c\x08missions\x94]\x94(}\x94(\x8c\x04year\x94M\xf3\x07\x8c\x04name\x94\x8c\x06Ares 3\x94u}\x94(h\x1fM\xb5\x07h \x8c\tApollo 18\x94ue\x8c\nexperience\x94h\x06\x8c\ttimedelta\x94\x93\x94K\x00K\x00K\x00\x87\x94R\x94\x8c\x12account_last_login\x94N\x8c\x0faccount_created\x94h\x06\x8c\x08datetime\x94\x93\x94C\n\x07\xe5\x08\x15\x11\x07\x1c\n\xc1\x94\x94h\x06\x8c\x08timezone\x94\x93\x94h&K\x00K\x00K\x00\x87\x94R\x94\x85\x94R\x94\x86\x94R\x94\x8c\x07AGE_MIN\x94K\x1e\x8c\x07AGE_MAX\x94K2u.')
>>>
>>> astro = Astronaut(**data)
>>>
>>> astro.missions
[{'year': 2035, 'name': 'Ares 3'}, {'year': 1973, 'name': 'Apollo 18'}]
>>>
>>> astro.missions = [Mission(**data) for data in astro.missions]
>>> astro.missions
[Mission(year=2035, name='Ares 3'), Mission(year=1973, name='Apollo 18')]
>>>
>>> astro
Astronaut(firstname='Mark', lastname='Watney', born=datetime.date(1961, 4, 12), job='astronaut', agency='NASA', age=44, height=175.5, weight=75.5, groups=['astronauts', 'managers'], friends={}, assignments=['STS-136'], missions=[Mission(year=2035, name='Ares 3'), Mission(year=1973, name='Apollo 18')], experience=datetime.timedelta(0), account_last_login=None, account_created=datetime.datetime(2021, 8, 21, 17, 7, 28, 704916, tzinfo=datetime.timezone.utc))
