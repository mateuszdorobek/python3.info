Dataclass Field
===============


Important
---------
.. code-block:: text

    def field(*,
              default: Any,
              default_factory: Any,
              init: Any = True,
              repr: Any = True,
              hash: Any = None,
              compare: Any = True,
              metadata: Any = None) -> None

* ``default`` - Default value for the field
* ``default_factory`` - Field factory
* ``init`` - Use this field in ``__init__()``
* ``repr`` - Use this field in ``__repr__()``
* ``hash`` - Use this field in ``__hash__()``
* ``compare`` - Use this field in comparison functions
  (le, lt, gt, ge, eq, ne)
* ``metadata`` - For storing extra information about field


Default
-------
>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     mission: str = 'Ares3'

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     mission: str = field(default='Ares3')


Default Factory
---------------
The following code will not work:

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[str] = ['Ares3', 'Apollo18']
Traceback (most recent call last):
ValueError: mutable default <class 'list'> for field missions is not allowed: use default_factory

If you want to create a list with default values, you have to create a field
with ``default_factory=lambda: ['Ares3', 'Apollo18']``. Lambda expression
will be evaluated on field initialization.

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[str] = field(default_factory=lambda: ['Ares3', 'Apollo18'])
>>>
>>>
>>> Astronaut('Mark', 'Watney')
Astronaut(firstname='Mark', lastname='Watney', missions=['Ares3', 'Apollo18'])


Init
----
>>> from dataclasses import dataclass, field
>>> from typing import Final
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: Final[int] = field(default=27, init=False)
...     AGE_MAX: Final[int] = field(default=50, init=False)
>>>
>>>
>>> Astronaut('Mark', 'Watney', age=44)
Astronaut(firstname='Mark', lastname='Watney', age=44, AGE_MIN=27, AGE_MAX=50)


Repr
----
>>> from dataclasses import dataclass, field
>>> from typing import Final
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: Final[int] = field(default=27, init=False, repr=False)
...     AGE_MAX: Final[int] = field(default=50, init=False, repr=False)
>>>
>>>
>>> Astronaut('Mark', 'Watney', age=44)
Astronaut(firstname='Mark', lastname='Watney', age=44)

kw_only
-------
* Since Python 3.10

If true, this field will be marked as keyword-only. This is used when the
generated __init__() method's parameters are computed. Default: dataclasses.MISSING


Use Case - 0x01
---------------
* Validation

>>> from dataclasses import dataclass, field, KW_ONLY
>>> from datetime import date, time, datetime, timezone, timedelta
>>>
>>>
>>> @dataclass
... class Mission:
...     year: int
...     name: str
>>>
>>>
>>> @dataclass(frozen=True)
... class Astronaut:
...     firstname: str
...     lastname: str
...     _: KW_ONLY
...     born: date
...     job: str = 'astronaut'
...     agency: str = field(default='NASA', metadata={'choices': ['NASA', 'ESA']})
...     age: int | None = None
...     height: float | int | None = field(default=None, metadata={'unit': 'cm', 'min': 156, 'max': 210})
...     weight: float | int | None = field(default=None, metadata={'unit': 'kg', 'min': 50, 'max': 90})
...     groups: list[str] = field(default_factory=lambda: ['astronauts', 'managers'])
...     friends: dict[str,str] = field(default_factory=dict)
...     assignments: list[str] | None = field(default=None, metadata={'choices': ['Apollo18', 'Ares3', 'STS-136']})
...     missions: list[Mission] = field(default_factory=list)
...     experience: timedelta = timedelta(hours=0)
...     account_last_login: datetime | None = None
...     account_created: datetime = datetime.now(tz=timezone.utc)
...     AGE_MIN: int = field(default=30, init=False, repr=False)
...     AGE_MAX: int = field(default=50, init=False, repr=False)
...
...     def __post_init__(self):
...         HEIGHT_MIN = self.__dataclass_fields__['height'].metadata['min']
...         HEIGHT_MAX = self.__dataclass_fields__['height'].metadata['max']
...         WEIGHT_MIN = self.__dataclass_fields__['weight'].metadata['min']
...         WEIGHT_MAX = self.__dataclass_fields__['weight'].metadata['max']
...         if not HEIGHT_MIN <= self.height < HEIGHT_MAX:
...             raise ValueError(f'Height {self.height} is not in between {HEIGHT_MIN} and {HEIGHT_MAX}')
...         if not WEIGHT_MIN <= self.weight < WEIGHT_MAX:
...             raise ValueError(f'Height {self.weight} is not in between {WEIGHT_MIN} and {WEIGHT_MAX}')
...         if self.age not in range(self.AGE_MIN, self.AGE_MAX):
...             raise ValueError('Age is not valid for an astronaut')
>>>
>>>
>>> astro = Astronaut(firstname='Mark',
...                   lastname='Watney',
...                   born=date(1961, 4, 12),
...                   age=44,
...                   height=175.5,
...                   weight=75.5,
...                   assignments=['STS-136'],
...                   missions=[Mission(2035, 'Ares 3'), Mission(1973, 'Apollo 18')])
>>>
>>> print(astro)  # doctest: +NORMALIZE_WHITESPACE +SKIP
Astronaut(firstname='Mark', lastname='Watney', born=datetime.date(1961, 4, 12),
          job='astronaut', agency='NASA', age=44, height=175.5, weight=75.5,
          groups=['astronauts', 'managers'], friends={}, assignments=['STS-136'],
          missions=[Mission(year=2035, name='Ares 3'), Mission(year=1973, name='Apollo 18')],
          experience=datetime.timedelta(0), account_last_login=None,
          account_created=datetime.datetime(1969, 7, 21, 2, 56, 15, 123456, tzinfo=datetime.timezone.utc))


Use Case - 0x02
---------------
* Setattr

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: float = field(default=None, metadata={'unit': 'cm', 'min': 30, 'max': 50})
...     height: float = field(default=None, metadata={'unit': 'cm', 'min': 156, 'max': 210})
...     weight: float = field(default=None, metadata={'unit': 'kg', 'min': 50, 'max': 90})
...
...     def __setattr__(self, attrname, attrvalue):
...         if attrvalue is None:
...             return super().__setattr__(attrname, attrvalue)
...         try:
...             min = Astronaut.__dataclass_fields__[attrname].metadata['min']
...             max = Astronaut.__dataclass_fields__[attrname].metadata['max']
...         except KeyError:
...             # field does not have min and max metadata
...             pass
...         else:
...             assert min <= attrvalue < max, f'{attrname} value {attrvalue} is not between {min} and {max}'
...         finally:
...             super().__setattr__(attrname, attrvalue)
>>>
>>>
>>>
>>> Astronaut('Mark', 'Watney')
Astronaut(firstname='Mark', lastname='Watney', age=None, height=None, weight=None)
>>>
>>> Astronaut('Mark', 'Watney', age=44)
Astronaut(firstname='Mark', lastname='Watney', age=44, height=None, weight=None)
>>>
>>> Astronaut('Mark', 'Watney', age=44, height=175, weight=75)
Astronaut(firstname='Mark', lastname='Watney', age=44, height=175, weight=75)
>>>
>>> Astronaut('Mark', 'Watney', age=99)
Traceback (most recent call last):
AssertionError: age value 99 is not between 30 and 50
>>>
>>> Astronaut('Mark', 'Watney', age=44, weight=200)
Traceback (most recent call last):
AssertionError: weight value 200 is not between 50 and 90
>>>
>>> Astronaut('Mark', 'Watney', age=44, height=120)
Traceback (most recent call last):
AssertionError: height value 120 is not between 156 and 210


Assignments
-----------
.. literalinclude:: assignments/dataclass_field_a.py
    :caption: :download:`Solution <assignments/dataclass_field_a.py>`
    :end-before: # Solution
