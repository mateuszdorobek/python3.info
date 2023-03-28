JSON Decoder
============


Problem
-------
* Problem with ``date``, ``datetime``, ``time``, ``timedelta``
* Python does not decode values automatically


SetUp
-----
>>> from pprint import pprint
>>> from datetime import date
>>> import json


Problem
-------
SetUp:

>>> DATA = """{
...     "firstname": "Mark",
...     "lastname": "Watney",
...     "birthday": "1994-10-12"
... }"""

Usage:

>>> result = json.loads(DATA)

Result:

>>> result  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'birthday': '1994-10-12'}


Function Decoder
----------------
* This works for simple (flat) data
* This works for nested data structures

SetUp:

>>> DATA = """{
...     "firstname": "Mark",
...     "lastname": "Watney",
...     "birthday": "1994-10-12"
... }"""

Usage:

>>> def decoder(data: dict) -> dict:
...     for field, value in data.items():
...         if field == 'birthday':
...             data[field] = date.fromisoformat(value)
...     return data
>>>
>>> result = json.loads(DATA, object_hook=decoder)

Result:

>>> result  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'birthday': datetime.date(1994, 10, 12)}


Context Dependency Injection
----------------------------
SetUp:

>>> DATA = """{
...     "firstname": "Mark",
...     "lastname": "Watney",
...     "birthday": "1994-10-12"
... }"""

Usage:

>>> class Decoder(json.JSONDecoder):
...     def __init__(self):
...         super().__init__(object_hook=self.default)
...
...     def default(self, data: dict) -> dict:
...         for field, value in data.items():
...             if field == 'birthday':
...                 data[field] = date.fromisoformat(value)
...         return data
>>>
>>> result = json.loads(DATA, cls=Decoder)

Result:

>>> result  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'birthday': datetime.date(1994, 10, 12)}


Use Case - 0x01
---------------
* This works for simple (flat) data
* This won't work for nested data structures

>>> import json
>>> from datetime import date
>>>
>>>
>>> DATA = """{
...     "firstname": "Mark",
...     "lastname": "Watney",
...     "birthday": "1994-10-12"
... }"""
>>>
>>> def decoder(obj: dict) -> dict:
...     obj['birthday'] = date.fromisoformat(obj['birthday'])
...     return obj
...
>>>
>>> result = json.loads(DATA, object_hook=decoder)
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'birthday': datetime.date(1994, 10, 12)}


Use Case - 0x02
---------------
* This works for simple (flat) data
* This won't work for nested data structures

>>> import json
>>> from datetime import date
>>>
>>>
>>> DATA = """{
...     "firstname": "Mark",
...     "lastname": "Watney",
...     "birthday": "1994-10-12"
... }"""
>>>
>>> def decoder(obj: dict) -> dict:
...     return obj | {
...         'birthday': date.fromisoformat(obj['birthday'])
...     }
...
>>> result = json.loads(DATA, object_hook=decoder)
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'birthday': datetime.date(1994, 10, 12)}


Use Case - 0x03
---------------
>>> from datetime import date, timedelta
>>> import json
>>>
>>>
>>> DATA = """{
...     "firstname": "Mark",
...     "lastname": "Watney",
...     "birthday": "1994-10-12",
...     "flight_time": 15552000
... }"""
>>>
>>>
>>> def decoder(x):
...     for key, value in x.items():
...         match key:
...             case 'birthday' | 'birthday':
...                 x[key] = date.fromisoformat(value)
...             case 'flight_time' | 'mission_time':
...                 x[key] = timedelta(seconds=float(value))
...     return x
>>>
>>>
>>> result = json.loads(DATA, object_hook=decoder)
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'birthday': datetime.date(1994, 10, 12),
 'flight_time': datetime.timedelta(days=180)}


Use Case - 0x04
---------------
>>> from datetime import date, time, datetime, timedelta
>>> import json
>>>
>>>
>>> DATA = """{
...     "firstname": "Mark",
...     "lastname": "Watney",
...     "birthday": "1994-10-12",
...     "launch": "1969-07-21T02:56:15",
...     "landing": "12:30:00",
...     "duration": 13
... }"""
>>>
>>> class Decoder(json.JSONDecoder):
...      name: str
...      birthday: date
...      launch: datetime
...      landing: time
...      duration: timedelta
...      flight_time: timedelta
...
...      def __init__(self) -> None:
...          super().__init__(object_hook=lambda data: {
...                  field: getattr(self, method)(value)
...                  for field, value in data.items()
...                  if (method := self.__annotations__.get(field, str).__name__)})
...
...      def datetime(self, value: str) -> date:
...          return datetime.fromisoformat(value)
...
...      def date(self, value: str) -> date:
...          return date.fromisoformat(value)
...
...      def time(self, value: str) -> date:
...          return time.fromisoformat(value)
...
...      def timedelta(self, value: str) -> date:
...          return timedelta(days=value)
...
...      def str(self, value: str) -> str:
...          return str(value)
>>>
>>>
>>> result = json.loads(DATA, cls=Decoder)
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'birthday': datetime.date(1994, 10, 12),
 'launch': datetime.datetime(1969, 7, 21, 2, 56, 15),
 'landing': datetime.time(12, 30),
 'duration': datetime.timedelta(days=13)}


Use Case - 0x05
---------------
>>> from datetime import datetime, date, time, timedelta
>>> import json
>>>
>>>
>>> DATA = """{
...     "firstname": "Mark",
...     "lastname": "Watney",
...     "birthday": "1994-10-12",
...     "launch": "1969-07-21T02:56:15",
...     "landing": "12:30:00",
...     "flight_time": 15552000,
...     "duration": 13
... }"""
>>>
>>>
>>> class Decoder(json.JSONDecoder):
...     def __init__(self):
...         super().__init__(object_hook=lambda data: {
...                 field: self.default(field, value)
...                 for field, value in data.items()})
...
...     def default(self, field, value):
...         result = {
...             'birthday': lambda x: date.fromisoformat(x),
...             'launch': lambda x: datetime.fromisoformat(x),
...             'landing': lambda x: time.fromisoformat(x),
...             'duration': lambda x: timedelta(days=x),
...             'flight_time': lambda x: timedelta(seconds=x),
...         }.get(field, value)
...         return result(value) if callable(result) else result
>>>
>>>
>>> result = json.loads(DATA, cls=Decoder)
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'birthday': datetime.date(1994, 10, 12),
 'launch': datetime.datetime(1969, 7, 21, 2, 56, 15),
 'landing': datetime.time(12, 30),
 'flight_time': datetime.timedelta(days=180),
 'duration': datetime.timedelta(days=13)}


Assignments
-----------
.. literalinclude:: assignments/json_decoder_a.py
    :caption: :download:`Solution <assignments/json_decoder_a.py>`
    :end-before: # Solution
