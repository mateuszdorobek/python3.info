Match Pattern Class
===================
A `class pattern` is similar to the above but matches attributes
instead of keys. It looks like ``datetime.date(year=y, day=d)``. It
matches instances of the given type, having at least the specified
attributes, as long as the attributes match with the corresponding
sub-patterns. It binds whatever the sub-patterns bind when matching
with the values of the given attributes. An optional protocol also
allows matching positional arguments.



Use Case - 0x01
---------------
>>> import json
>>> from datetime import date, time, datetime, timezone
>>>
>>>
>>> DATA = {'firstname': 'Mark',
...         'lastname': 'Watney',
...         'born': date(1994, 10, 12)}
>>>
>>>
>>> def encoder(value):
...     match value:
...         case date() | time() | datetime():
...             return value.isoformat()
...         case timedelta():
...             return value.total_seconds()
>>>
>>>
>>> json.dumps(DATA, default=encoder)
'{"firstname": "Mark", "lastname": "Watney", "born": "1994-10-12"}'


Use Case - 0x02
---------------
>>> import json
>>> from datetime import date, time, datetime, timezone
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

>>> json.dumps(DATA)
Traceback (most recent call last):
TypeError: Object of type datetime is not JSON serializable

>>> def encoder(obj):
...     if type(obj) is datetime or type(obj) is date:
...         return obj.isoformat()
...     elif type(obj) is timedelta:
...         return obj.total_seconds()
>>>
>>>
>>> json.dumps(DATA, default=encoder)
'{"mission": "Ares 3", "launch_date": "2035-06-29T00:00:00", "destination": "Mars", "destination_landing": "2035-11-07T00:00:00", "destination_location": "Acidalia Planitia", "crew": [{"name": "Melissa Lewis", "born": "1995-07-15"}, {"name": "Rick Martinez", "born": "1996-01-21"}, {"name": "Alex Vogel", "born": "1994-11-15"}, {"name": "Chris Beck", "born": "1999-08-02"}, {"name": "Beth Johanssen", "born": "2006-05-09"}, {"name": "Mark Watney", "born": "1994-10-12"}]}'

>>> def encoder(obj):
...     if isinstance(obj, date|datetime):
...         return obj.isoformat()
...     elif isinstance(obj, timedelta):
...         return obj.total_seconds()
>>>
>>>
>>> json.dumps(DATA, default=encoder)
'{"mission": "Ares 3", "launch_date": "2035-06-29T00:00:00", "destination": "Mars", "destination_landing": "2035-11-07T00:00:00", "destination_location": "Acidalia Planitia", "crew": [{"name": "Melissa Lewis", "born": "1995-07-15"}, {"name": "Rick Martinez", "born": "1996-01-21"}, {"name": "Alex Vogel", "born": "1994-11-15"}, {"name": "Chris Beck", "born": "1999-08-02"}, {"name": "Beth Johanssen", "born": "2006-05-09"}, {"name": "Mark Watney", "born": "1994-10-12"}]}'

>>> def encoder(obj):
...     match obj:
...         case date() | datetime():
...             return obj.isoformat()
...         case timedelta():
...             return obj.total_seconds()
>>>
>>> json.dumps(DATA, default=encoder)
'{"mission": "Ares 3", "launch_date": "2035-06-29T00:00:00", "destination": "Mars", "destination_landing": "2035-11-07T00:00:00", "destination_location": "Acidalia Planitia", "crew": [{"name": "Melissa Lewis", "born": "1995-07-15"}, {"name": "Rick Martinez", "born": "1996-01-21"}, {"name": "Alex Vogel", "born": "1994-11-15"}, {"name": "Chris Beck", "born": "1999-08-02"}, {"name": "Beth Johanssen", "born": "2006-05-09"}, {"name": "Mark Watney", "born": "1994-10-12"}]}'
