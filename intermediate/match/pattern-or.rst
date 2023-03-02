Match Pattern OR
================

An `OR pattern` looks like ``[*x] | {"elems": [*x]}``. It matches if
any of its sub-patterns match. It uses the binding for the leftmost
pattern that matched.

>>> from http import HTTPStatus
>>> import requests
>>>
>>>
>>> resp = requests.get('https://python.astrotech.io')
>>>
>>> match resp.status_code:
...     case 200 | 201: print('No error')
...     case 300 | 301: print('Redirect')
...     case 400|401|402: print('Client Error')
...     case 500|501|502: print('Server Error')
...
No error


Use Case - 0x01
---------------
* ``ares3_landing = datetime(2035, 11, 7)``
* ``ares3_start = datetime(2035, 6, 29)``
* ``ares3_duration = timedelta(days=557, seconds=80025)``

>>> from dataclasses import dataclass
>>>
>>>
>>> SECOND = 1
>>> MINUTE = 60 * SECOND
>>> HOUR = 60 * MINUTE
>>> DAY = 24 * HOUR
>>> WEEK = 7 * DAY
>>> MONTH = 30.4375 * DAY
>>> YEAR = 365.25 * DAY
>>>
>>> SOL = 24*HOUR + 39*MINUTE + 35*SECOND
>>>
>>>
>>> @dataclass
... class Duration:
...     seconds: int
...
...     def __format__(self, unit):
...         duration = self.seconds
...         match unit:
...             case 's' | 'seconds': duration /= SECOND
...             case 'm' | 'minutes': duration /= MINUTE
...             case 'h' | 'hours':   duration /= HOUR
...             case 'd' | 'days':    duration /= DAY
...             case 'w' | 'weeks':   duration /= WEEK
...             case 'M' | 'months':  duration /= MONTH
...             case 'y' | 'years':   duration /= YEAR
...             case _: raise TypeError('Invalid unit')
...         return f'{duration:.1f} {unit}'
>>>
>>>
>>> ares3 = Duration(543*SOL)
>>>
>>> print(f'Ares3 mission to Mars took {ares3:seconds}')
Ares3 mission to Mars took 48204825.0 seconds
>>>
>>> print(f'Ares3 mission to Mars took {ares3:minutes}')
Ares3 mission to Mars took 803413.8 minutes
>>>
>>> print(f'Ares3 mission to Mars took {ares3:hours}')
Ares3 mission to Mars took 13390.2 hours
>>>
>>> print(f'Ares3 mission to Mars took {ares3:days}')
Ares3 mission to Mars took 557.9 days
>>>
>>> print(f'Ares3 mission to Mars took {ares3:weeks}')
Ares3 mission to Mars took 79.7 weeks
>>>
>>> print(f'Ares3 mission to Mars took {ares3:months}')
Ares3 mission to Mars took 18.3 months
>>>
>>> print(f'Ares3 mission to Mars took {ares3:years}')
Ares3 mission to Mars took 1.5 years
