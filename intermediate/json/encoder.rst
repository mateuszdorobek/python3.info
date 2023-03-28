JSON Encoder
============
* Problem with ``date``, ``datetime``, ``time``, ``timedelta``
* Exception during encoding datetime
* Encoder will be used, when standard procedure fails


SetUp
-----
>>> from datetime import datetime, date, time, timedelta
>>> import json


Problem
-------
>>> DATA = {
...     'firstname': 'Mark',
...     'lastname': 'Watney',
...     'birthday': date(1994, 10, 12)
... }
>>>
>>> result = json.dumps(DATA)
Traceback (most recent call last):
TypeError: Object of type date is not JSON serializable


Default Function with Lambda
----------------------------
>>> DATA = {
...     'firstname': 'Mark',
...     'lastname': 'Watney',
...     'birthday': date(1994, 10, 12)
... }
>>>
>>> result = json.dumps(DATA, default=lambda x: x.isoformat(), indent=2)
>>> print(result)
{
  "firstname": "Mark",
  "lastname": "Watney",
  "birthday": "1994-10-12"
}


Default Function with If
------------------------
>>> DATA = {
...     'firstname': 'Mark',
...     'lastname': 'Watney',
...     'birthday': date(1994, 10, 12)
... }
>>>
>>>
>>> def encoder(x):
...     if type(x) is date:
...         return x.isoformat()
>>>
>>>
>>> result = json.dumps(DATA, default=encoder, indent=2)
>>> print(result)
{
  "firstname": "Mark",
  "lastname": "Watney",
  "birthday": "1994-10-12"
}


Default Function with Match
---------------------------
>>> DATA = {
...     'firstname': 'Mark',
...     'lastname': 'Watney',
...     'birthday': date(1994, 10, 12)
... }
>>>
>>>
>>> def encoder(x):
...     match x:
...         case datetime() | date() | time():
...             return x.isoformat()
...         case timedelta():
...             return x.total_seconds()
>>>
>>>
>>> result = json.dumps(DATA, default=encoder, indent=2)
>>> print(result)
{
  "firstname": "Mark",
  "lastname": "Watney",
  "birthday": "1994-10-12"
}


Monkey Patching with Lambda Expression
--------------------------------------
>>> DATA = {
...     'firstname': 'Mark',
...     'lastname': 'Watney',
...     'birthday': date(1994, 10, 12)
... }
>>>
>>> json.JSONEncoder.default = lambda self,x: x.isoformat()
>>>
>>> result = json.dumps(DATA, indent=2)
>>> print(result)
{
  "firstname": "Mark",
  "lastname": "Watney",
  "birthday": "1994-10-12"
}


Dependency Injection
--------------------
>>> DATA = {
...     'firstname': 'Mark',
...     'lastname': 'Watney',
...     'birthday': date(1994, 10, 12)
... }
>>>
>>>
>>> class Encoder(json.JSONEncoder):
...     def default(self, x):
...         if type(x) is date:
...             return x.isoformat()
>>>
>>>
>>> result = json.dumps(DATA, cls=Encoder, indent=2)
>>> print(result)
{
  "firstname": "Mark",
  "lastname": "Watney",
  "birthday": "1994-10-12"
}


Use Case - 0x01
---------------
>>> from datetime import datetime, date, time, timedelta
>>> import json
>>>
>>>
>>> DATA = {
...     'name': 'Mark Watney',
...     'birthday': date(1994, 10, 12),
...     'launch': datetime(1969, 7, 21, 2, 56, 15),
...     'landing': time(12, 30),
...     'duration': timedelta(days=13),
... }
>>>
>>>
>>> class Encoder(json.JSONEncoder):
...     def default(self, value):
...         if type(value) in (datetime, date, time):
...             return value.isoformat()
...         if type(value) is timedelta:
...             return value.total_seconds()
>>>
>>>
>>> result = json.dumps(DATA, cls=Encoder, indent=2)
>>> print(result)
{
  "name": "Mark Watney",
  "birthday": "1994-10-12",
  "launch": "1969-07-21T02:56:15",
  "landing": "12:30:00",
  "duration": 1123200.0
}


Use Case - 0x02
---------------
>>> from datetime import datetime, date, time, timedelta
>>> import json
>>>
>>>
>>> DATA = {
...     'name': 'Mark Watney',
...     'birthday': date(1994, 10, 12),
...     'launch': datetime(1969, 7, 21, 2, 56, 15),
...     'landing': time(12, 30),
...     'duration': timedelta(days=13),
... }
>>>
>>>
>>> def encoder(x):
...     match x:
...         case datetime() | date() | time():
...             return x.isoformat()
...         case timedelta():
...             return x.total_seconds()
>>>
>>>
>>> result = json.dumps(DATA, default=encoder, indent=2)
>>> print(result)
{
  "name": "Mark Watney",
  "birthday": "1994-10-12",
  "launch": "1969-07-21T02:56:15",
  "landing": "12:30:00",
  "duration": 1123200.0
}


Assignments
-----------
.. literalinclude:: assignments/json_encoder_a.py
    :caption: :download:`Solution <assignments/json_encoder_a.py>`
    :end-before: # Solution
