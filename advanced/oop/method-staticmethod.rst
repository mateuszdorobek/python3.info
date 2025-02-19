OOP Method Staticmethod
=======================
* Should **not** be in a class: method which don't use ``self`` in its body
* Should be in class: if method takes ``self`` and use it (it requires instances to work)
* If a method don't use ``self`` but uses class as a namespace use ``@staticmethod`` decorator
* Using class as namespace
* No need to create a class instance
* Will not pass instance (``self``) as a first method argument

>>> class User:
...     def say_hello():
...         pass

>>> class User:
...     @staticmethod
...     def say_hello():
...         pass


Problem
-------
Assume we received ``DATA`` from the REST API endpoint:

>>> DATA = '{"firstname": "Mark", "lastname": "Watney"}'

Let's define a ``User`` class:

>>> class User:
...    def __init__(self, firstname, lastname):
...        self.firstname = firstname
...        self.lastname = lastname
...
...    def __repr__(self):
...         firstname = self.firstname
...         lastname = self.lastname
...         return f'User({firstname=}, {lastname=})'
...
...    def from_json(self, data):
...        import json
...        data = json.loads(data)
...        return User(**data)

Let's use ``.from_json()`` to create an instance:

>>> User.from_json(DATA)
Traceback (most recent call last):
TypeError: User.from_json() missing 1 required positional argument: 'data'

The data is unfilled. This is due to the fact, that we are running a method
on a class, not on an instance. Typically while running on an instance,
Python will pass it as ``self`` argument and we will fill the other one.
Running this on a class, turns off this behavior, and therefore this is why
the second parameter is unfilled.

We can create an instance and then run ``.from_json()`` method.

>>> User().from_json(DATA)
Traceback (most recent call last):
TypeError: User.__init__() missing 2 required positional arguments: 'firstname' and 'lastname'

Nope, we cannot. In order to create an instance we need to pass firstname
and lastname. We can pass ``None`` objects instead. We can also make a class
to always assume a default value for firstname and lastname as ``None``, but
this will remove those arguments from required list and allow to create a
User object without passing those values. In both cases this will work,
but it is not good:

>>> User(None, None).from_json(DATA)
User(firstname='Mark', lastname='Watney')


Solution
--------
With the same ``DATA`` as before:

>>> DATA = '{"firstname": "Mark", "lastname": "Watney"}'

We can define a static method ``.from_json()`` which will not require
creating instance in order to use it:

>>> class User:
...    def __init__(self, firstname, lastname):
...        self.firstname = firstname
...        self.lastname = lastname
...
...    def __repr__(self):
...         firstname = self.firstname
...         lastname = self.lastname
...         return f'User({firstname=}, {lastname=})'
...
...    @staticmethod
...    def from_json(data):
...        import json
...        data = json.loads(data)
...        return User(**data)

Now, we can use this without creating an instance first:

>>> user = User.from_json(DATA)
>>> vars(user)
{'firstname': 'Mark', 'lastname': 'Watney'}


Dataclass
---------
The same implementation as before, but this time using ``dataclasses``
in order to get some more readability:

>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...
...     @staticmethod
...     def from_json(data):
...         data = json.loads(data)
...         return User(**data)
>>>
>>>
>>> DATA = '{"firstname": "Mark", "lastname": "Watney"}'
>>>
>>> User.from_json(DATA)
User(firstname='Mark', lastname='Watney')


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
>>> sub(2, 1)
1

When ``add`` and ``sub`` are in ``Calculator`` class (namespace) they get
instance (``self``) as a first argument. Instantiating Calculator is not
needed, as of functions do not read or write to instance variables:

>>> class Calculator:
...     def add(self, a, b):
...         return a + b
...
...     def sub(self, a, b):
...         return a - b
>>>
>>>
>>> Calculator.add(1, 2)
Traceback (most recent call last):
TypeError: Calculator.add() missing 1 required positional argument: 'b'
>>>
>>> Calculator.sub(2, 1)
Traceback (most recent call last):
TypeError: Calculator.sub() missing 1 required positional argument: 'b'
>>>
>>> calc = Calculator()
>>> calc.add(1, 2)
3
>>> calc.sub(2, 1)
1

Class ``Calculator`` is a namespace for functions. ``@staticmethod`` remove
instance (``self``) argument to method:

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
>>> Calculator.sub(2, 1)
1


To @staticmethod or Not
-----------------------
SetUp:

>>> from random import randint, seed
>>> seed(0)

Instance Method:

>>> class Hero:
...     def make_damage(self):
...         return randint(5,20)
>>>
>>>
>>> hero = Hero()
>>> hero.make_damage()  # Will work (as expected)
17
>>>
>>> Hero.make_damage()  # Will fail (as expected)
Traceback (most recent call last):
TypeError: Hero.make_damage() missing 1 required positional argument: 'self'

Function:

>>> def make_damage():
...     return randint(5,20)
>>>
>>> class Hero:
...     pass
>>>
>>>
>>> mark = Hero()
>>> mark.make_damage()  # AttributeError (unexpected)
Traceback (most recent call last):
AttributeError: 'Hero' object has no attribute 'make_damage'
>>>
>>> Hero.make_damage()  # AttributeError (unexpected)
Traceback (most recent call last):
AttributeError: type object 'Hero' has no attribute 'make_damage'

Staticmethod:

>>> class Hero:
...     @staticmethod
...     def make_damage():
...         return randint(5,20)
>>>
>>>
>>> hero = Hero()
>>> hero.make_damage()  # Will work (as expected)
18
>>>
>>> Hero.make_damage()  # Will work (unexpected)
6

No Warning:

>>> class Hero:
...     def make_damage(self):
...         str(self)  # We use self, doesn't matter what we do with it
...         return randint(5,20)
>>>
>>>
>>> hero = Hero()
>>> hero.make_damage()  # Will work (as expected)
13
>>>
>>> Hero.make_damage()  # Will fail (as expected)
Traceback (most recent call last):
TypeError: Hero.make_damage() missing 1 required positional argument: 'self'


Use Case - 0x01
---------------
* Singleton

>>> class MyClass:
...     _instance = None
...
...     @staticmethod
...     def get_instance():
...         if not MyClass._instance:
...             MyClass._instance = object.__new__(MyClass)
...         return MyClass._instance
>>>
>>>
>>> my1 = MyClass.get_instance()
>>> my2 = MyClass.get_instance()
>>>
>>> my1  # doctest: +ELLIPSIS
<__main__.MyClass object at 0x...>
>>>
>>> my2  # doctest: +ELLIPSIS
<__main__.MyClass object at 0x...>


Use Case - 0x02
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
>>> http.get('https://python3.info')
>>> http.post('https://python3.info', data={'username': 'mwatney'})


Use Case - 0x03
---------------
>>> def user_create():
...     print('Create User')
>>>
>>>
>>> class User:
...     pass

>>> class User:
...     @staticmethod
...     def create(self):
...         print('Logged-in')


Use Case - 0x04
---------------
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


Use Case - 0x05
---------------
Helper `habitatOS <https://astronaut.center/habitatOS>`_ Z-Wave sensor model:

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


Assignments
-----------
.. todo:: Assignments
