Operator String Format
======================
* Calling function ``format(obj, fmt)`` calls ``obj.__format__(fmt)``
* Method ``obj.__format__()`` must return ``str``
* Used for advanced formatting in f-strings (``f'...'``)


Example
-------
>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
...
...     def __format__(self, mood):
...         if mood == 'happy':
...             return f"Yuppi, we're going to space!"
...         elif mood == 'scared':
...             return f"I hope we don't crash"
>>>
>>>
>>> jose = Astronaut('José Jiménez')
>>>
>>> print(f'{jose:happy}')
Yuppi, we're going to space!
>>>
>>> print(f'{jose:scared}')
I hope we don't crash


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


Use Case - 0x02
---------------
* Temperature conversion

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Temperature:
...     kelvin: float
...
...     def to_fahrenheit(self):
...         return (self.kelvin-273.15) * 1.8 + 32
...
...     def to_celsius(self):
...         return self.kelvin - 273.15
...
...     def __format__(self, unit):
...         match unit:
...             case 'K' | 'kelvin':     value = self.kelvin
...             case 'C' | 'celsius':    value = self.to_celsius()
...             case 'F' | 'fahrenheit': value = self.to_fahrenheit()
...         unit = unit[0].upper()
...         return f'{value:.2f} {unit}'
>>>
>>>
>>> temp = Temperature(kelvin=309.75)
>>>
>>>
>>> print(f'Temperature is {temp:kelvin}')
Temperature is 309.75 K
>>>
>>> print(f'Temperature is {temp:celsius}')
Temperature is 36.60 C
>>>
>>> print(f'Temperature is {temp:fahrenheit}')
Temperature is 97.88 F


Use Case - 0x03
---------------
* Format output

>>> from dataclasses import dataclass
>>> import json
>>>
>>>
>>> @dataclass
... class Point:
...     x: int
...     y: int
...     z: int = 0
...
...     def __format__(self, format):
...         match format:
...             case 'repr':  result = f"Point(x={self.x}, y={self.y}, z={self.z})"
...             case 'dict':  result = vars(self)
...             case 'tuple': result = tuple(vars(self).values())
...             case 'json':  result = json.dumps(vars(self))
...         return str(result)
>>>
>>>
>>> point = Point(x=1, y=2)
>>>
>>>
>>> print(f'{point:repr}')
Point(x=1, y=2, z=0)
>>>
>>> print(f'{point:tuple}')
(1, 2, 0)
>>>
>>> print(f'{point:dict}')
{'x': 1, 'y': 2, 'z': 0}
>>>
>>> print(f'{point:json}')
{"x": 1, "y": 2, "z": 0}


Assignments
-----------
.. literalinclude:: assignments/operator_string_format_a.py
    :caption: :download:`Solution <assignments/operator_string_format_a.py>`
    :end-before: # Solution
