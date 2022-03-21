OOP Staticmethod
================


Important
---------
* Should **not** be in a class: method which don't use ``self`` in its body
* Should be in class: if method takes ``self`` and use it (it requires instances to work)
* If a method don't use ``self`` but uses class as a namespace use ``@staticmethod`` decorator
* Using class as namespace
* No need to create a class instance
* Will not pass instance (``self``) as a first method argument

>>> class MyClass:
...
...     @staticmethod
...     def mymethod():
...         pass
>>>
>>>
>>> MyClass.mymethod()


Example
-------
>>> class Astronaut:
...     def __init__(self):
...         self.name = 'José Jiménez'
...
...     def say_hello(self):
...         print(f'My name... {self.name}')
...
...     @staticmethod
...     def say_goodbye():
...         print('Goodbye')


Instances
---------
>>> class MyClass:
...     def say_hello(self):
...         print('Hello')
>>>
>>>
>>> my = MyClass()
>>> my.say_hello()
Hello

>>> class MyClass:
...     @staticmethod
...     def say_hello():
...         print('Hello')
>>>
>>> MyClass.say_hello()
Hello


Namespace
---------
Functions on a high level of a module lack namespace:

>>> def add(a, b):
...     return a + b
>>>
>>> def sub(a, b):
...     return a - b
>>>
>>>
>>> add(1, 2)
3
>>> sub(8, 4)
4

When ``add`` and ``sub`` are in ``Calculator`` class (namespace) they get instance (``self``) as a first argument. Instantiating Calculator is not needed, as of functions do not read or write to instance variables:

>>> class Calculator:
...     def add(self, a, b):
...         return a + b
...
...     def sub(self, a, b):
...         return a - b
>>>
>>>
>>> Calculator.add(10, 20)
Traceback (most recent call last):
TypeError: add() missing 1 required positional argument: 'b'
>>>
>>> Calculator.sub(8, 4)
Traceback (most recent call last):
TypeError: add() missing 1 required positional argument: 'b'
>>>
>>> calc = Calculator()
>>> calc.add(1, 2)
3
>>> calc.sub(8, 4)
4

Class ``Calculator`` is a namespace for functions. ``@staticmethod`` remove instance (``self``) argument to method:

>>> class Calculator:
...     @staticmethod
...     def add(a, b):
...         return a + b
...
...     @staticmethod
...     def sub(a, b):
...         return a - b
>>>
>>>
>>> Calculator.add(1, 2)
3
>>> Calculator.sub(8, 4)
4


Use Case - 0x01
---------------
* Http Client

>>> class http:
...     @staticmethod
...     def get(url):
...         ...
...
...     @staticmethod
...     def post(url, data):
...         ...
>>>
>>> http.get('https://python.astrotech.io')
>>> http.post('https://python.astrotech.io', data={'astronaut': 'Mark Watney'})


Use Case - 0x02
---------------
* Hello

>>> def astronaut_say_hello():
...     print('hello')
>>>
>>> def astronaut_say_goodbye():
...     print('goodbye')
>>>
>>>
>>> class Astronaut:
...     pass
>>>
>>>
>>> a = Astronaut()
>>> astronaut_say_hello()
hello
>>> astronaut_say_goodbye()
goodbye

>>> class Astronaut:
...     def say_hello(self):
...         print('hello')
...
...     def say_goodbye(self):
...         print('goodbye')
>>>
>>>
>>> a = Astronaut()
>>> a.say_hello()
hello
>>> a.say_goodbye()
goodbye
>>>
>>> Astronaut.say_hello()
Traceback (most recent call last):
TypeError: say_hello() missing 1 required positional argument: 'self'
>>>
>>> Astronaut.say_goodbye()
Traceback (most recent call last):
TypeError: say_goodbye() missing 1 required positional argument: 'self'

>>> class Astronaut:
...     @staticmethod
...     def say_hello():
...         print('hello')
...
...     @staticmethod
...     def say_goodbye():
...         print('goodbye')
>>>
>>>
>>> Astronaut.say_hello()
hello
>>>
>>> Astronaut.say_goodbye()
goodbye
>>>
>>> astro = Astronaut()
>>> astro.say_hello()
hello
>>> astro.say_goodbye()
goodbye


Use Case - 0x03
---------------
* Measurement

>>> from dataclasses import dataclass
>>> from datetime import datetime, timezone
>>> from typing import Literal
>>>
>>>
>>> @dataclass
... class Measurement:
...     device_id: str
...     parameter: Literal['temperature', 'humidity']
...     value: float
...     unit: Literal['Celsius', 'Kelvin', 'Fahrenheit', '%']
...     when: datetime = datetime.now(timezone.utc)
...
...     def __post_init__(self):
...         if self.unit == 'Kelvin' and self.value < 0:
...             raise ValueError('Negative Kelvin')
>>>
>>>
>>> m = Measurement(
...         device_id='1a2b7c8d38',
...         parameter='temperature',
...         value=21.3,
...         unit='Celsius')


Use Case - 0x04
---------------
* ZWave Sensor

Helper `HabitatOS <https://www.habitatos.space>`_ Z-Wave sensor model:

>>> from datetime import datetime, timezone
>>> from decimal import Decimal, InvalidOperation
>>> import logging
>>> from django.db import models  # doctest: +SKIP
>>> from django.utils.translation import ugettext_lazy as _  # doctest: +SKIP
>>> from habitat._common.models import HabitatModel  # doctest: +SKIP
>>> from habitat._common.models import MissionDateTime  # doctest: +SKIP
>>> from habitat.time import MissionTime  # doctest: +SKIP
>>>
>>> log = logging.getLogger('habitat.sensor')
>>>
>>>
>>> def clean_unit(unit: str) -> str:
...     try:
...         return {
...             'C': 'celsius',
...             'F': 'fahrenheit',
...             'dB': 'decibel',
...             'lux': 'lux',
...             '%': 'percent',
...         }[unit]
...     except KeyError:
...         return None
>>>
>>>
>>> def clean_type(type: str) -> str:
...     return type.lower().replace(' ', '-')
>>>
>>>
>>> def clean_value(value: str) -> Decimal:
...     try:
...         return Decimal(value)
...     except InvalidOperation:
...         return Decimal(0)
>>>
>>>
>>> def clean_device(device: str) -> str:
...     return device
>>>
>>>
>>> def clean_datetime(dt: str) -> datetime:
...     try:
...         return datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f+00:00').replace(tzinfo=timezone.utc)
...     except ValueError:
...         return datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f')
>>>
>>>
>>> class ZWaveSensor(HabitatModel, MissionDateTime):  # doctest: +SKIP
...     TYPE_BATTERY_LEVEL = 'battery-level'
...     TYPE_POWER_LEVEL = 'powerlevel'
...     TYPE_TEMPERATURE = 'temperature'
...     TYPE_LUMINANCE = 'luminance'
...     TYPE_RELATIVE_HUMIDITY = 'relative-humidity'
...     TYPE_ULTRAVIOLET = 'ultraviolet'
...     TYPE_BURGLAR = 'burglar'
...     TYPE_CHOICES = [
...         (TYPE_BATTERY_LEVEL, _('Battery Level')),
...         (TYPE_POWER_LEVEL, _('Power Level')),
...         (TYPE_TEMPERATURE, _('Temperature')),
...         (TYPE_LUMINANCE, _('Luminance')),
...         (TYPE_RELATIVE_HUMIDITY, _('Relative Humidity')),
...         (TYPE_ULTRAVIOLET, _('Ultraviolet')),
...         (TYPE_BURGLAR, _('Burglar'))]
...
...     UNIT_CELSIUS = 'celsius'
...     UNIT_KELVIN = 'kelvin'
...     UNIT_FAHRENHEIT = 'fahrenheit'
...     UNIT_DECIBEL = 'decibel'
...     UNIT_LUMINANCE = 'lux'
...     UNIT_PERCENT = 'percent'
...     UNIT_DIMENSIONLESS = None
...     UNIT_CHOICES = [
...         (UNIT_DIMENSIONLESS, _('n/a')),
...         (UNIT_PERCENT, _('%')),
...         (UNIT_LUMINANCE, _('Lux')),
...         (UNIT_DECIBEL, _('dB')),
...         (UNIT_CELSIUS, _('°C')),
...         (UNIT_KELVIN, _('K')),
...         (UNIT_FAHRENHEIT, _('°F'))]
...
...     DEVICE_ATRIUM = 'c1344062-2'
...     DEVICE_ANALYTIC_LAB = 'c1344062-3'
...     DEVICE_OPERATIONS = 'c1344062-4'
...     DEVICE_TOILET = 'c1344062-5'
...     DEVICE_DORMITORY = 'c1344062-6'
...     DEVICE_STORAGE = 'c1344062-7'
...     DEVICE_KITCHEN = 'c1344062-8'
...     DEVICE_BIOLAB = 'c1344062-9'
...     DEVICE_AIRLOCK = None
...     DEVICE_CHOICES = [
...         (DEVICE_ATRIUM, _('Atrium')),
...         (DEVICE_ANALYTIC_LAB, _('Analytic Lab')),
...         (DEVICE_OPERATIONS, _('Operations')),
...         (DEVICE_TOILET, _('Toilet')),
...         (DEVICE_DORMITORY, _('Dormitory')),
...         (DEVICE_STORAGE, _('Storage')),
...         (DEVICE_KITCHEN, _('Kitchen')),
...         (DEVICE_BIOLAB, _('Biolab'))]
...
...     datetime = models.DateTimeField(verbose_name=_('Datetime [UTC]'), db_index=True)
...     device = models.CharField(verbose_name=_('Sensor Location'), max_length=30, choices=DEVICE_CHOICES, db_index=True)
...     type = models.CharField(verbose_name=_('Type'), max_length=30, choices=TYPE_CHOICES)
...     value = models.DecimalField(verbose_name=_('Value'), max_digits=7, decimal_places=2, default=None)
...     unit = models.CharField(verbose_name=_('Unit'), max_length=15, choices=UNIT_CHOICES, null=True, blank=True, default=None)
...
...     def __str__(self) -> str:
...         return f'[{self.date} {self.time}] (device: {self.device}) {self.type}: {self.value} {self.unit}'
...
...     class Meta:
...         verbose_name = _('Data')
...         verbose_name_plural = _('Zwave Sensors')
...
...     @staticmethod
...     def add(datetime: str, device: str, type: str, value: str, unit: str):
...         dt = clean_datetime(datetime)
...         time = MissionTime().get_time_dict(from_datetime=dt)
...         data = {'date': time['date'],
...                 'time': time['time'],
...                 'device': clean_device(device),
...                 'type': clean_type(type),
...                 'value': clean_value(value),
...                 'unit': clean_unit(unit)}
...         return ZWaveSensor.objects.update_or_create(datetime=dt, defaults=data)

In order to create an object in database, I have to do the following code
every time, when new data arrives. It is very easy to forget something and
cumbersome to import all that validators and cleaning methods at all times.

>>> # doctest: +SKIP
... from habitat.time import MissionTime
... from habitat.sensors.models import ZWaveSensor
... from habitat.sensors.models import clean_datetime
... from habitat.sensors.models import clean_device
... from habitat.sensors.models import clean_type
... from habitat.sensors.models import clean_value
... from habitat.sensors.models import clean_unit
...
...
... dt = clean_datetime(datetime)
... time = MissionTime().get_time_dict(from_datetime=dt)
... data = {'date': time['date'],
...         'time': time['time'],
...         'device': clean_device(device),
...         'type': clean_type(type),
...         'value': clean_value(value),
...         'unit': clean_unit(unit)}
...
... obj = ZWaveSensor.objects.update_or_create(datetime=dt, defaults=data)

Instead I can use:

>>> obj = ZWaveSensor.add(datetime, device, type, value, unit)  # doctest: +SKIP


.. todo:: Assignments
