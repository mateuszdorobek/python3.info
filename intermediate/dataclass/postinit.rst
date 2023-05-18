Dataclass Postinit
==================
* Dataclasses generate ``__init__()``
* Overloading ``__init__()`` manually will destroy it
* For init time validation there is ``__post_init__()``
* It is run after all parameters are set in the class
* Hence you have to take care about negative cases (errors)


SetUp
-----
>>> from dataclasses import dataclass
>>> from typing import ClassVar
>>> from datetime import date, datetime


Initial Validation in Classes
-----------------------------
* Init serves not only for fields initialization
* It could be also used for value validation

>>> class User:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: ClassVar[int] = 30
...     AGE_MAX: ClassVar[int] = 50
...
...     def __init__(self, firstname, lastname, age):
...         self.firstname = firstname
...         self.lastname = lastname
...         if not self.AGE_MIN <= age < self.AGE_MAX:
...             raise ValueError('Age is out of range')
...         else:
...             self.age = age
>>>
>>>
>>> mark = User('Mark', 'Watney', age=42)
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney', 'age': 42}
>>>
>>> User('Mark', 'Watney', age=60)
Traceback (most recent call last):
ValueError: Age is out of range


Initial Validation in Dataclasses
---------------------------------
* Creating own ``__init__()`` will overload init from dataclasses
* Therefore in dataclasses there is ``__post_init__()`` method
* It is run after init (as the name suggest)
* It works on fields, which already saved (it was done in ``__init__``)
* No need to assign it once again
* You can focus only on bailing-out (checking only negative path - errors)

>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: ClassVar[int] = 30
...     AGE_MAX: ClassVar[int] = 50
...
...     def __post_init__(self):
...         if not self.AGE_MIN <= self.age < self.AGE_MAX:
...             raise ValueError('Age is out of range')
>>>
>>>
>>> User('Mark', 'Watney', age=42)
User(firstname='Mark', lastname='Watney', age=42)
>>>
>>> User('Mark', 'Watney', age=60)
Traceback (most recent call last):
ValueError: Age is out of range


Date and Time Conversion
------------------------
* ``__post_init__()`` can also be used to convert data
* Example str ``1969-07-21`` to date object ``date(1969, 7, 21)``

>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     birthday: date
...
...     def __post_init__(self):
...         self.birthday = date.fromisoformat(self.birthday)
>>>
>>>
>>> User('Mark', 'Watney', '1961-04-12')  # doctest: +NORMALIZE_WHITESPACE
User(firstname='Mark', lastname='Watney',
     birthday=datetime.date(1961, 4, 12))

>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     launch: datetime | None = None
...
...     def __post_init__(self):
...         if self.launch is not None:
...             self.launch = datetime.fromisoformat(self.launch)
>>>
>>>
>>> User('Mark', 'Watney')
User(firstname='Mark', lastname='Watney', launch=None)
>>>
>>> User('Mark', 'Watney', '1969-07-21T02:56:15+00:00')  # doctest: +NORMALIZE_WHITESPACE
User(firstname='Mark', lastname='Watney',
     launch=datetime.datetime(1969, 7, 21, 2, 56, 15, tzinfo=datetime.timezone.utc))


InitVar
-------
* Init-only fields
* Added as parameters to the generated ``__init__``
* Passed to the optional ``__post_init__`` method
* They are not otherwise used by Data Classes

Import:

>>> from dataclasses import dataclass, field, InitVar
>>> from datetime import date

Definition:

>>> @dataclass
... class Date:
...     year: InitVar[int]
...     month: InitVar[int]
...     day: InitVar[int]
...     current: date = field(default=None, init=False)
...
...     def __post_init__(self, year: int, month: int, day: int):
...         self.current = date(year, month, day)

Usage:

>>> result = Date(1969, 7, 21)
>>> vars(result)
{'current': datetime.date(1969, 7, 21)}


Use Case - 0x01
---------------
>>> from dataclasses import dataclass, KW_ONLY
>>> from typing import ClassVar
>>>
>>>
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     _: KW_ONLY
...     age: int
...     AGE_MIN: ClassVar[int] = 30
...     AGE_MAX: ClassVar[int] = 50
...
...     def __post_init__(self):
...         if self.age not in range(self.AGE_MIN, self.AGE_MAX):
...             raise ValueError
>>>
>>>
>>> mark = User('Mark', 'Watney', age=42)


Use Case - 0x02
---------------
>>> from dataclasses import dataclass, InitVar
>>> from datetime import date, time, datetime, timezone
>>> from zoneinfo import ZoneInfo
>>>
>>>
>>> @dataclass
... class CurrentTime:
...     tzname: InitVar[str]
...     d: date | None = None
...     t: time | None = None
...     tz: ZoneInfo | None = None
...
...     def __post_init__(self, tzname):
...         current = datetime.now(ZoneInfo('UTC'))
...         localized = current.astimezone(ZoneInfo(tzname))
...         self.d = localized.date()
...         self.t = localized.time()
...         self.tz = localized.tzname()

Usage:

>>> now = CurrentTime('Europe/Warsaw')
>>> now  # doctest: +SKIP
CurrentTime(d=datetime.date(1969, 7, 21),
            t=datetime.time(2, 56, 15),
            tz='CEST')


Use Case - 0x03
---------------
>>> from dataclasses import dataclass, InitVar
>>> import datetime
>>>
>>>
>>> @dataclass
... class DateTime:
...     string: InitVar[str]
...     date: datetime.date | None = None
...     time: datetime.time | None = None
...
...     def __post_init__(self, string: str):
...         dt = datetime.datetime.fromisoformat(string)
...         self.date = dt.date()
...         self.time = dt.time()

Usage:

>>> apollo11 = DateTime('1969-07-21 02:56:15')
>>>
>>> apollo11
DateTime(date=datetime.date(1969, 7, 21), time=datetime.time(2, 56, 15))
>>>
>>> apollo11.date
datetime.date(1969, 7, 21)
>>>
>>> apollo11.time
datetime.time(2, 56, 15)


Use Case - 0x04
---------------
>>> from dataclasses import dataclass, InitVar
>>>
>>>
>>> @dataclass
... class User:
...     fullname: InitVar[str] = None
...     firstname: str | None = None
...     lastname: str | None = None
...
...     def __post_init__(self, fullname):
...         if fullname:
...             self.firstname, self.lastname = fullname.split()

Usage:

>>> User('Mark Watney')
User(firstname='Mark', lastname='Watney')

>>> User(firstname='Mark', lastname='Watney')
User(firstname='Mark', lastname='Watney')


Use Case - 0x05
---------------
>>> from dataclasses import dataclass, InitVar
>>>
>>>
>>> @dataclass
... class Email:
...     address: InitVar[str]
...     username: str | None = None
...     domain: str | None = None
...
...     def __post_init__(self, address):
...         self.username, self.domain = address.split('@')
...
...     def get_address(self):
...         return f'{self.username}@{self.domain}'

Usage:

>>> email = Email('mwatney@nasa.gov')
>>>
>>> print(email)
Email(username='mwatney', domain='nasa.gov')
>>>
>>> print(email.username)
mwatney
>>>
>>> print(email.domain)
nasa.gov
>>>
>>> print(email.get_address())
mwatney@nasa.gov
>>>
>>> print(email.address)
Traceback (most recent call last):
AttributeError: 'Email' object has no attribute 'address'


Use Case - 0x06
---------------
>>> from dataclasses import dataclass
>>> from typing import ClassVar
>>>
>>>
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: ClassVar[int] = 30
...     AGE_MAX: ClassVar[int] = 50
...
...     def __post_init__(self):
...         min = self.AGE_MIN
...         max = self.AGE_MAX
...         if self.age not in range(min, max):
...             raise ValueError(f'Age {self.age} not in range {min} to {max}')

Usage:

>>> User('Mark', 'Watney', 60)
Traceback (most recent call last):
ValueError: Age 60 not in range 30 to 50

>>> User('Mark', 'Watney', 60, AGE_MAX=70)
Traceback (most recent call last):
TypeError: User.__init__() got an unexpected keyword argument 'AGE_MAX'


Use Case - 0x07
---------------
* Boundary check

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Point:
...     x: int = 0
...     y: int = 0
...
...     def __post_init__(self):
...         if self.x < 0 or self.y < 0:
...             raise ValueError('Coordinate cannot be negative')


Use Case - 0x08
---------------
* Var Range

>>> from dataclasses import dataclass, field
>>> from typing import Final
>>>
>>>
>>> @dataclass
... class Point:
...     x: int = 0
...     y: int = 0
...     X_MIN: Final[int] = 0
...     X_MAX: Final[int] = 1024
...     Y_MIN: Final[int] = 0
...     Y_MAX: Final[int] = 768
...
...     def __post_init__(self):
...         if not self.X_MIN <= self.x < self.X_MAX:
...             raise ValueError(f'x value ({self.x}) is not between {self.X_MIN} and {self.X_MAX}')
...         if not self.Y_MIN <= self.y < self.Y_MAX:
...             raise ValueError(f'y value ({self.y}) is not between {self.Y_MIN} and {self.Y_MAX}')

Usage:

>>> Point(0, 0)
Point(x=0, y=0, X_MIN=0, X_MAX=1024, Y_MIN=0, Y_MAX=768)

>>> Point(-1, 0)
Traceback (most recent call last):
ValueError: x value (-1) is not between 0 and 1024

>>> Point(0, 2000)
Traceback (most recent call last):
ValueError: y value (2000) is not between 0 and 768

>>> Point(0, 0, X_MIN=10, X_MAX=100)
Traceback (most recent call last):
ValueError: x value (0) is not between 10 and 100


Use Case - 0x09
---------------
* Const Range

>>> from dataclasses import dataclass, field
>>> from typing import Final
>>>
>>>
>>> @dataclass
... class Point:
...     x: int = 0
...     y: int = 0
...     X_MIN: Final[int] = field(init=False, default=0)
...     X_MAX: Final[int] = field(init=False, default=1024)
...     Y_MIN: Final[int] = field(init=False, default=0)
...     Y_MAX: Final[int] = field(init=False, default=768)
...
...     def __post_init__(self):
...         if not self.X_MIN <= self.x < self.X_MAX:
...             raise ValueError(f'x value ({self.x}) is not between {self.X_MIN} and {self.X_MAX}')
...         if not self.Y_MIN <= self.y < self.Y_MAX:
...             raise ValueError(f'y value ({self.y}) is not between {self.Y_MIN} and {self.Y_MAX}')

Usage:

>>> Point(0, 0)
Point(x=0, y=0, X_MIN=0, X_MAX=1024, Y_MIN=0, Y_MAX=768)

>>> Point(0, 0, X_MIN=10, X_MAX=100)
Traceback (most recent call last):
TypeError: Point.__init__() got an unexpected keyword argument 'X_MIN'


Use Case - 0x0A
---------------
* Init, Repr

>>> from dataclasses import dataclass, field
>>> from typing import Final
>>>
>>>
>>> @dataclass
... class Point:
...     x: int = 0
...     y: int = 0
...     X_MIN: Final[int] = field(init=False, repr=False, default=0)
...     X_MAX: Final[int] = field(init=False, repr=False, default=1024)
...     Y_MIN: Final[int] = field(init=False, repr=False, default=0)
...     Y_MAX: Final[int] = field(init=False, repr=False, default=768)
...
...     def __post_init__(self):
...         if not self.X_MIN <= self.x < self.X_MAX:
...             raise ValueError(f'x value ({self.x}) is not between {self.X_MIN} and {self.X_MAX}')
...         if not self.Y_MIN <= self.y < self.Y_MAX:
...             raise ValueError(f'y value ({self.y}) is not between {self.Y_MIN} and {self.Y_MAX}')

Usage:

>>> Point(0, 0)
Point(x=0, y=0)

>>> Point(-1, 0)
Traceback (most recent call last):
ValueError: x value (-1) is not between 0 and 1024

>>> Point(0, -1)
Traceback (most recent call last):
ValueError: y value (-1) is not between 0 and 768


Use Case - 0x0B
---------------
>>> from dataclasses import dataclass, InitVar
>>>
>>> @dataclass
... class Phone:
...     full_number: InitVar[str]
...
...     country_code: int = None
...     number: int = None
...
...     def __post_init__(self, full_number: str):
...         self.country_code, self.number = full_number.split(' ', maxsplit=1)

Usage:

>>> phone = Phone('+48 123 456 789')
>>> phone
Phone(country_code='+48', number='123 456 789')


Use Case - 0x0C
---------------
* https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/pl/pesel.py

>>> from dataclasses import dataclass, InitVar
>>> from datetime import datetime
>>>
>>>
>>> @dataclass
... class Pesel:
...     number: InitVar[str]
...
...     pesel: str = None
...     birthday: str = None
...     gender: str = None
...     valid: bool = None
...
...     def calc_check_digit(self):
...         weights = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
...         check = sum(w * int(n) for w, n in zip(weights, self.pesel))
...         return str((10 - check) % 10)
...
...     def __post_init__(self, number: str):
...         self.pesel = number
...         self.birthday = datetime.strptime(number[:6], '%y%m%d').date()
...         self.gender =  'male' if int(number[-2]) % 2 else 'female'
...         self.valid = number[-1] == self.calc_check_digit()

Usage:

>>> pesel = Pesel('69072101234')
>>> pesel  # doctest: +NORMALIZE_WHITESPACE
Pesel(pesel='69072101234',
      birthday=datetime.date(1969, 7, 21),
      gender='male',
      valid=False)


Assignments
-----------
.. literalinclude:: assignments/dataclass_postinit_a.py
    :caption: :download:`Solution <assignments/dataclass_postinit_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/dataclass_postinit_b.py
    :caption: :download:`Solution <assignments/dataclass_postinit_b.py>`
    :end-before: # Solution
