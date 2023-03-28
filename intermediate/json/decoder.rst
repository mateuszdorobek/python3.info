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
>>> DATA = """{
...     "firstname": "Mark",
...     "lastname": "Watney",
...     "birthday": "1994-10-12"
... }"""
>>>
>>> result = json.loads(DATA)
>>> print(result)   # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'birthday': '1994-10-12'}


Function Decoder
----------------
* This works for simple (flat) data
* This works for nested data structures

>>> DATA = """{
...     "firstname": "Mark",
...     "lastname": "Watney",
...     "birthday": "1994-10-12"
... }"""
>>>
>>>
>>> def decoder(data: dict) -> dict:
...     for field, value in data.items():
...         if field == 'birthday':
...             data[field] = date.fromisoformat(value)
...     return data
>>>
>>>
>>> result = json.loads(DATA, object_hook=decoder)
>>> print(result)   # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'birthday': datetime.date(1994, 10, 12)}


Context Dependency Injection
----------------------------
>>> DATA = """{
...     "firstname": "Mark",
...     "lastname": "Watney",
...     "birthday": "1994-10-12"
... }"""
>>>
>>>
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
>>>
>>> result = json.loads(DATA, cls=Decoder)
>>> print(result)   # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'birthday': datetime.date(1994, 10, 12)}


Use Case - 0x01
---------------
* This works for simple (flat) data
* This won't work for nested data structures

>>> import json
>>> from datetime import datetime, date, time, timedelta
>>> from pprint import pprint
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
>>> def decoder(obj: dict) -> dict:
...     obj['birthday'] = date.fromisoformat(obj['birthday'])
...     obj['launch'] = datetime.fromisoformat(obj['launch'])
...     obj['landing'] = time.fromisoformat(obj['landing'])
...     obj['flight_time'] = timedelta(seconds=obj['flight_time'])
...     obj['duration'] = timedelta(days=obj['duration'])
...     return obj
>>>
>>>
>>> result = json.loads(DATA, object_hook=decoder)
>>> pprint(result, sort_dicts=False)
{'firstname': 'Mark',
 'lastname': 'Watney',
 'birthday': datetime.date(1994, 10, 12),
 'launch': datetime.datetime(1969, 7, 21, 2, 56, 15),
 'landing': datetime.time(12, 30),
 'flight_time': datetime.timedelta(days=180),
 'duration': datetime.timedelta(days=13)}


Use Case - 0x02
---------------
* This works for simple (flat) data
* This won't work for nested data structures

>>> import json
>>> from datetime import datetime, date, time, timedelta
>>> from pprint import pprint
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
>>> def decoder(obj: dict) -> dict:
...     return obj | {
...         'birthday': date.fromisoformat(obj['birthday']),
...         'launch': datetime.fromisoformat(obj['launch']),
...         'landing': time.fromisoformat(obj['landing']),
...         'flight_time': timedelta(seconds=obj['flight_time']),
...         'duration': timedelta(days=obj['duration']),
...     }
>>>
>>>
>>> result = json.loads(DATA, object_hook=decoder)
>>> pprint(result, sort_dicts=False)
{'firstname': 'Mark',
 'lastname': 'Watney',
 'birthday': datetime.date(1994, 10, 12),
 'launch': datetime.datetime(1969, 7, 21, 2, 56, 15),
 'landing': datetime.time(12, 30),
 'flight_time': datetime.timedelta(days=180),
 'duration': datetime.timedelta(days=13)}


Use Case - 0x03
---------------
>>> from datetime import datetime, date, time, timedelta
>>> import json
>>> from pprint import pprint
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
>>> def decoder(x):
...     for key, value in x.items():
...         match key:
...             case 'birthday':
...                 x[key] = date.fromisoformat(value)
...             case 'launch':
...                 x[key] = datetime.fromisoformat(value)
...             case 'landing':
...                 x[key] = time.fromisoformat(value)
...             case 'flight_time' | 'mission_time':
...                 x[key] = timedelta(seconds=float(value))
...             case 'duration':
...                 x[key] = timedelta(days=int(value))
...     return x
>>>
>>>
>>> result = json.loads(DATA, object_hook=decoder)
>>> pprint(result, sort_dicts=False)
{'firstname': 'Mark',
 'lastname': 'Watney',
 'birthday': datetime.date(1994, 10, 12),
 'launch': datetime.datetime(1969, 7, 21, 2, 56, 15),
 'landing': datetime.time(12, 30),
 'flight_time': datetime.timedelta(days=180),
 'duration': datetime.timedelta(days=13)}


Use Case - 0x04
---------------
>>> from datetime import datetime, date, time, timedelta
>>> import json
>>> from pprint import pprint
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
...     def __init__(self) -> None:
...         super().__init__(object_hook=lambda data: {
...             field: getattr(self, field)(value)
...             for field, value in data.items()})
...
...     def firstname(self, value: str) -> str:
...         return value
...
...     def lastname(self, value: str) -> str:
...         return value
...
...     def birthday(self, value: str) -> date:
...         return date.fromisoformat(value)
...
...     def launch(self, value: str) -> datetime:
...         return datetime.fromisoformat(value)
...
...     def landing(self, value: str) -> time:
...         return time.fromisoformat(value)
...
...     def flight_time(self, value: str) -> timedelta:
...         return timedelta(seconds=float(value))
...
...     def duration(self, value: str) -> timedelta:
...         return timedelta(days=int(value))
>>>
>>>
>>> result = json.loads(DATA, cls=Decoder)
>>> pprint(result, sort_dicts=False)
{'firstname': 'Mark',
 'lastname': 'Watney',
 'birthday': datetime.date(1994, 10, 12),
 'launch': datetime.datetime(1969, 7, 21, 2, 56, 15),
 'landing': datetime.time(12, 30),
 'flight_time': datetime.timedelta(days=180),
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
>>> print(result)   # doctest: +NORMALIZE_WHITESPACE
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
