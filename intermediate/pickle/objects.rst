Pickle Objects
==============


Serialize and Deserialize Datetimes
-----------------------------------
>>> from datetime import datetime
>>> import pickle
>>>
>>>
>>> dt = datetime(1969, 7, 21, 2, 56, 15)
>>> pickle.dumps(dt)
b'\x80\x04\x95*\x00\x00\x00\x00\x00\x00\x00\x8c\x08datetime\x94\x8c\x08datetime\x94\x93\x94C\n\x07\xb1\x07\x15\x028\x0f\x00\x00\x00\x94\x85\x94R\x94.'

>>> import pickle
>>>
>>>
>>> pickle.loads(b'\x80\x04\x95*\x00\x00\x00\x00\x00\x00\x00\x8c\x08datetime\x94\x8c\x08datetime\x94\x93\x94C\n\x07\xb1\x07\x15\x028\x0f\x00\x00\x00\x94\x85\x94R\x94.')
datetime.datetime(1969, 7, 21, 2, 56, 15)


Serialize and Deserialize Objects
---------------------------------
>>> import pickle
>>>
>>>
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>> result = pickle.dumps(vars(mark))
>>>
>>> result
b'\x80\x04\x95,\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\tfirstname\x94\x8c\x04Mark\x94\x8c\x08lastname\x94\x8c\x06Watney\x94u.'
>>>
>>> data = pickle.loads(result)
>>> Astronaut(**data)  # doctest: +ELLIPSIS
<__main__.Astronaut object at 0x...>


Examples
--------
Advanced Example:

>>> from datetime import date, datetime
>>> import pickle
>>>
>>>
>>> DATA = {'mission': 'Ares 3',
...         'launch_date': datetime(2035, 6, 29),
...         'destination': 'Mars',
...         'destination_landing': datetime(2035, 11, 7),
...         'destination_location': 'Acidalia Planitia',
...         'crew': [{'name': 'Melissa Lewis', 'born': date(1995, 7, 15)},
...                  {'name': 'Rick Martinez', 'born': date(1996, 1, 21)},
...                  {'name': 'Alex Vogel', 'born': date(1994, 11, 15)},
...                  {'name': 'Chris Beck', 'born': date(1999, 8, 2)},
...                  {'name': 'Beth Johanssen', 'born': date(2006, 5, 9)},
...                  {'name': 'Mark Watney', 'born': date(1994, 10, 12)}]}
>>>
>>>
>>> result = pickle.dumps(DATA)
>>> print(result)
b'\x80\x04\x95\xad\x01\x00\x00\x00\x00\x00\x00}\x94(\x8c\x07mission\x94\x8c\x06Ares 3\x94\x8c\x0blaunch_date\x94\x8c\x08datetime\x94\x8c\x08datetime\x94\x93\x94C\n\x07\xf3\x06\x1d\x00\x00\x00\x00\x00\x00\x94\x85\x94R\x94\x8c\x0bdestination\x94\x8c\x04Mars\x94\x8c\x13destination_landing\x94h\x06C\n\x07\xf3\x0b\x07\x00\x00\x00\x00\x00\x00\x94\x85\x94R\x94\x8c\x14destination_location\x94\x8c\x11Acidalia Planitia\x94\x8c\x04crew\x94]\x94(}\x94(\x8c\x04name\x94\x8c\rMelissa Lewis\x94\x8c\x04born\x94h\x04\x8c\x04date\x94\x93\x94C\x04\x07\xcb\x07\x0f\x94\x85\x94R\x94u}\x94(h\x15\x8c\rRick Martinez\x94h\x17h\x19C\x04\x07\xcc\x01\x15\x94\x85\x94R\x94u}\x94(h\x15\x8c\nAlex Vogel\x94h\x17h\x19C\x04\x07\xca\x0b\x0f\x94\x85\x94R\x94u}\x94(h\x15\x8c\nChris Beck\x94h\x17h\x19C\x04\x07\xcf\x08\x02\x94\x85\x94R\x94u}\x94(h\x15\x8c\x0eBeth Johanssen\x94h\x17h\x19C\x04\x07\xd6\x05\t\x94\x85\x94R\x94u}\x94(h\x15\x8c\x0bMark Watney\x94h\x17h\x19C\x04\x07\xca\n\x0c\x94\x85\x94R\x94ueu.'
>>>
>>> result = pickle.loads(result)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'mission': 'Ares 3',
 'launch_date': datetime.datetime(2035, 6, 29, 0, 0),
 'destination': 'Mars',
 'destination_landing': datetime.datetime(2035, 11, 7, 0, 0),
 'destination_location': 'Acidalia Planitia',
 'crew': [{'name': 'Melissa Lewis', 'born': datetime.date(1995, 7, 15)},
          {'name': 'Rick Martinez', 'born': datetime.date(1996, 1, 21)},
          {'name': 'Alex Vogel', 'born': datetime.date(1994, 11, 15)},
          {'name': 'Chris Beck', 'born': datetime.date(1999, 8, 2)},
          {'name': 'Beth Johanssen', 'born': datetime.date(2006, 5, 9)},
          {'name': 'Mark Watney', 'born': datetime.date(1994, 10, 12)}]}
