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

>>> import pickle
>>> from dataclasses import dataclass, field, asdict
>>> from datetime import date, time, datetime, timezone, timedelta
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
...     account_created: datetime = datetime(1961, 4, 12, 6, 7, tzinfo=timezone.utc)  # datetime.now(tz=timezone.utc)
...     AGE_MIN: int = field(default=30, init=False, repr=False)
...     AGE_MAX: int = field(default=50, init=False, repr=False)
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
>>> mark = Astronaut(firstname='Mark',
...                   lastname='Watney',
...                   born=date(1961, 4, 12),
...                   age=44,
...                   height=175.5,
...                   weight=75.5,
...                   assignments=['STS-136'],
...                   missions=[Mission(2035, 'Ares 3'), Mission(1973, 'Apollo 18')])
>>>
>>> asdict(mark)
{'firstname': 'Mark', 'lastname': 'Watney', 'born': datetime.date(1961, 4, 12), 'job': 'astronaut', 'agency': 'NASA', 'age': 44, 'height': 175.5, 'weight': 75.5, 'groups': ['astronauts', 'managers'], 'friends': {}, 'assignments': ['STS-136'], 'missions': [{'year': 2035, 'name': 'Ares 3'}, {'year': 1973, 'name': 'Apollo 18'}], 'experience': datetime.timedelta(0), 'account_last_login': None, 'account_created': datetime.datetime(1961, 4, 12, 6, 7, tzinfo=datetime.timezone.utc), 'AGE_MIN': 30, 'AGE_MAX': 50}
>>>
>>> pickle.dumps(asdict(mark))
b'\x80\x04\x95\xd6\x01\x00\x00\x00\x00\x00\x00}\x94(\x8c\tfirstname\x94\x8c\x04Mark\x94\x8c\x08lastname\x94\x8c\x06Watney\x94\x8c\x04born\x94\x8c\x08datetime\x94\x8c\x04date\x94\x93\x94C\x04\x07\xa9\x04\x0c\x94\x85\x94R\x94\x8c\x03job\x94\x8c\tastronaut\x94\x8c\x06agency\x94\x8c\x04NASA\x94\x8c\x03age\x94K,\x8c\x06height\x94G@e\xf0\x00\x00\x00\x00\x00\x8c\x06weight\x94G@R\xe0\x00\x00\x00\x00\x00\x8c\x06groups\x94]\x94(\x8c\nastronauts\x94\x8c\x08managers\x94e\x8c\x07friends\x94}\x94\x8c\x0bassignments\x94]\x94\x8c\x07STS-136\x94a\x8c\x08missions\x94]\x94(}\x94(\x8c\x04year\x94M\xf3\x07\x8c\x04name\x94\x8c\x06Ares 3\x94u}\x94(h\x1fM\xb5\x07h \x8c\tApollo 18\x94ue\x8c\nexperience\x94h\x06\x8c\ttimedelta\x94\x93\x94K\x00K\x00K\x00\x87\x94R\x94\x8c\x12account_last_login\x94N\x8c\x0faccount_created\x94h\x06\x8c\x08datetime\x94\x93\x94C\n\x07\xa9\x04\x0c\x06\x07\x00\x00\x00\x00\x94h\x06\x8c\x08timezone\x94\x93\x94h&K\x00K\x00K\x00\x87\x94R\x94\x85\x94R\x94\x86\x94R\x94\x8c\x07AGE_MIN\x94K\x1e\x8c\x07AGE_MAX\x94K2u.'
