Enum Use Cases
==============


SetUp
-----
>>> from enum import Enum, IntEnum, StrEnum, auto


Use Case - 0x03
---------------
* Issue Status

>>> class IssueStatus(Enum):
...     TODO = 'todo'
...     IN_PROGRESS = 'in-progress'
...     IN_REVIEW = 'in-review'
...     IN_TEST = 'in-test'
...     DONE = 'done'
...     REJECTED = 'rejected'


Use Case - 0x05
---------------
>>> Point = tuple[int,int]
>>>
>>> class Color(Enum):
...     RED = '#FF0000'
...     GREEN = '#00FF00'
...     BLUE = '#0000FF'

>>> def draw_line(A: Point, B: Point, color: Color):
...     if type(color) is not Color:
...         possible = [str(c) for c in Color]
...         raise TypeError(f'Invalid color, possible choices: {possible}')
...     print(f'Drawing line from {A} to {B} with color {color.value}')

>>> draw_line(A=(0,0), B=(3,5), color=Color.RED)
Drawing line from (0, 0) to (3, 5) with color #FF0000

>>> draw_line(A=(0,0), B=(3,5), color='red')
Traceback (most recent call last):
TypeError: Invalid color, possible choices: ['Color.RED', 'Color.GREEN', 'Color.BLUE']


Use Case - 0x08
---------------
>>> from dataclasses import dataclass
>>>
>>>
>>> class Agency(Enum):
...     NASA = auto()
...     ESA = auto()
...     JAXA = auto()
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     agency: Agency
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney', agency='not-existing')
>>> mark = Astronaut('Mark', 'Watney', agency=Agency.NASA)


Use Case - 0x06
---------------
* ``r`` - read
* ``w`` - write
* ``x`` - execute
* ``rwx`` - read, write, execute; 0b111 == 0o7
* ``rw-`` - read, write; 0b110 == 0o6
* ``r-x`` - read, execute; 0b101 == 0o5
* ``r--`` - read only; 0b100 == 0o4
* ``rwxr-xr--`` - user=(read,write,execute); group=(read,execute); others=(read)

* https://docs.python.org/3/library/os.html#os.stat

>>> from enum import Enum
>>> from pathlib import Path
>>>
>>>
>>> class Permission(Enum):
...     READ_WRITE_EXECUTE = 0b111
...     READ_WRITE = 0b110
...     READ_EXECUTE = 0b101
...     READ = 0b100
...     WRITE_EXECUTE = 0b011
...     WRITE = 0b010
...     EXECUTE = 0b001
...     NONE = 0b000
>>>
>>>
>>> file = Path('/tmp/myfile.txt')
>>> file.touch()
>>> file.stat()  # doctest: +SKIP
os.stat_result(st_mode=33188, st_ino=98480473, st_dev=16777220,
               st_nlink=1, st_uid=501, st_gid=20, st_size=0,
               st_atime=1624458230, st_mtime=1624458230,
               st_ctime=1624458230)
>>>
>>> permissions = file.stat().st_mode
>>> decimal = int(permissions)
>>> octal = oct(permissions)
>>> binary = bin(permissions)
>>> print(f'{decimal=}, {octal=}, {binary}')
decimal=33188, octal='0o100644', 0b1000000110100100
>>>
>>> *_, user, group, others = oct(permissions)
>>> print(f'{user=} {group=} {others=}')
user='6' group='4' others='4'
>>>
>>> Permission(int(user))
<Permission.READ_WRITE: 6>
>>>
>>> Permission(int(group))
<Permission.READ: 4>
>>>
>>> Permission(int(others))
<Permission.READ: 4>
>>>
>>> file.unlink()


Use Case - 0x09
---------------
>>> # doctest: +SKIP
... from django.db import models
...
... class HttpMethod(models.TextChoices):
...     GET = 'GET', _('GET')
...     POST = 'POST', _('POST')
...     PATCH = 'PATCH', _('PATCH')
...     PUT = 'PUT', _('PUT')
...     HEAD = 'HEAD', _('HEAD')
...     DELETE = 'DELETE', _('DELETE')
...     OPTIONS = 'OPTIONS', _('OPTIONS')
...     TRACE = 'TRACE', _('TRACE')
...     CONNECT = 'CONNECT', _('CONNECT')
...
...
... class Stage(models.TextChoices):
...     PRODUCTION = 'production', _('Production')
...     TEST = 'test', _('Test')


Pattern Matching
----------------
* Since Python 3.10: :pep:`636` -- Structural Pattern Matching: Tutorial

.. figure:: img/enum-usecase-keycodes.png

Note, keycodes can vary depending on operating system and programming
language used [mskeycodes]_, [jskeycodes]_.

>>> int('0x1B', base=16)
27
>>>
>>> hex(27)
'0x1b'

>>> class Key(Enum):
...     ESC = 27            # 0x1B
...     ARROW_LEFT = 37     # 0x25
...     ARROW_UP = 38       # 0x26
...     ARROW_RIGHT = 39    # 0x27
...     ARROW_DOWN = 40     # 0x28
>>>
>>>
>>> # doctest: +SKIP
... match keyboard.on_key_press():
...     case Key.ESC:          game.quit()
...     case Key.ARROW_LEFT:   game.move_left()
...     case Key.ARROW_UP:     game.move_up()
...     case Key.ARROW_RIGHT:  game.move_right()
...     case Key.ARROW_DOWN:   game.move_down()
...     case _: raise ValueError(f'Unrecognized key')


Use Case - 0x01
---------------
>>> class Planet(Enum):
...     MERCURY = (3.303e+23, 2.4397e6)
...     VENUS   = (4.869e+24, 6.0518e6)
...     EARTH   = (5.976e+24, 6.37814e6)
...     MARS    = (6.421e+23, 3.3972e6)
...     JUPITER = (1.9e+27,   7.1492e7)
...     SATURN  = (5.688e+26, 6.0268e7)
...     URANUS  = (8.686e+25, 2.5559e7)
...     NEPTUNE = (1.024e+26, 2.4746e7)
...
...     def __init__(self, mass, radius):
...         self.mass = mass       # in kilograms
...         self.radius = radius   # in meters
...
...     @property
...     def surface_gravity(self):
...         # universal gravitational constant  (m3 kg-1 s-2)
...         G = 6.67300E-11
...         return G * self.mass / (self.radius * self.radius)

>>> Planet.EARTH.value
(5.976e+24, 6378140.0)
>>>
>>> Planet.EARTH.surface_gravity
9.802652743337129


Use Case - 0x05
---------------
>>> Point = tuple[int,int]
>>>
>>> class Color(Enum):
...     RED = '#FF0000'
...     GREEN = '#00FF00'
...     BLUE = '#0000FF'

>>> def draw_line(A: Point, B: Point, color: Color):
...     if type(color) is not Color:
...         possible = [str(c) for c in Color]
...         raise TypeError(f'Invalid color, possible choices: {possible}')
...     print(f'Drawing line from {A} to {B} with color {color.value}')

>>> draw_line(A=(0,0), B=(3,5), color=Color.RED)
Drawing line from (0, 0) to (3, 5) with color #FF0000

>>> draw_line(A=(0,0), B=(3,5), color='red')
Traceback (most recent call last):
TypeError: Invalid color, possible choices: ['Color.RED', 'Color.GREEN', 'Color.BLUE']


Use Case - 0x06
---------------
* ``r`` - read
* ``w`` - write
* ``x`` - execute
* ``rwx`` - read, write, execute; 0b111 == 0o7
* ``rw-`` - read, write; 0b110 == 0o6
* ``r-x`` - read, execute; 0b101 == 0o5
* ``r--`` - read only; 0b100 == 0o4
* ``rwxr-xr--`` - user=(read,write,execute); group=(read,execute); others=(read)

* https://docs.python.org/3/library/os.html#os.stat

>>> from enum import Enum
>>> from pathlib import Path
>>>
>>>
>>> class Permission(Enum):
...     READ_WRITE_EXECUTE = 0b111
...     READ_WRITE = 0b110
...     READ_EXECUTE = 0b101
...     READ = 0b100
...     WRITE_EXECUTE = 0b011
...     WRITE = 0b010
...     EXECUTE = 0b001
...     NONE = 0b000
>>>
>>>
>>> file = Path('/tmp/myfile.txt')
>>> file.touch()
>>> file.stat()  # doctest: +SKIP
os.stat_result(st_mode=33188, st_ino=98480473, st_dev=16777220,
               st_nlink=1, st_uid=501, st_gid=20, st_size=0,
               st_atime=1624458230, st_mtime=1624458230,
               st_ctime=1624458230)
>>>
>>> permissions = file.stat().st_mode
>>> decimal = int(permissions)
>>> octal = oct(permissions)
>>> binary = bin(permissions)
>>> print(f'{decimal=}, {octal=}, {binary}')
decimal=33188, octal='0o100644', 0b1000000110100100
>>>
>>> *_, user, group, others = oct(permissions)
>>> print(f'{user=} {group=} {others=}')
user='6' group='4' others='4'
>>>
>>> Permission(int(user))
<Permission.READ_WRITE: 6>
>>>
>>> Permission(int(group))
<Permission.READ: 4>
>>>
>>> Permission(int(others))
<Permission.READ: 4>
>>>
>>> file.unlink()


Use Case - 0x07
------------------
>>> class IndexDrives(IntEnum):
...     ControlWord = 0x6040
...     StatusWord = 0x6041
...     OperationMode = 0x6060


Use Case - 0x08
---------------
>>> from dataclasses import dataclass
>>>
>>>
>>> class Agency(Enum):
...     NASA = auto()
...     ESA = auto()
...     JAXA = auto()
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     agency: Agency
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney', agency='not-existing')
>>> mark = Astronaut('Mark', 'Watney', agency=Agency.NASA)


Use Case - 0x09
---------------
>>> # doctest: +SKIP
... from django.db import models
...
... class HttpMethod(models.TextChoices):
...     GET = 'GET', _('GET')
...     POST = 'POST', _('POST')
...     PATCH = 'PATCH', _('PATCH')
...     PUT = 'PUT', _('PUT')
...     HEAD = 'HEAD', _('HEAD')
...     DELETE = 'DELETE', _('DELETE')
...     OPTIONS = 'OPTIONS', _('OPTIONS')
...     TRACE = 'TRACE', _('TRACE')
...     CONNECT = 'CONNECT', _('CONNECT')
...
...
... class Stage(models.TextChoices):
...     PRODUCTION = 'production', _('Production')
...     TEST = 'test', _('Test')


Use Case - 0x0A
---------------
* https://www.euvat.org/vat-returns-poland/
* https://www.infor.pl/akt-prawny/DZU.2019.084.0000816,rozporzadzenie-ministra-finansow-w-sprawie-kas-rejestrujacych.html
* §6 pkt. 5 - Rozporządzenie Ministra Finansów z dnia 29 kwietnia 2019 r. w sprawie kas rejestrujących. Dziennik Ustaw - rok 2019 poz. 816
* PTU - Podatek od Towarów i Usług (Services and Goods Tax)

.. figure:: img/enum-usecase-biedronka.png

>>> class PTU(Enum):
...     A = 1.23   # VAT 23%
...     B = 1.08   # VAT 8%
...     C = 1.05   # VAT 5%
...     D = 1.00   # VAT 0%
...     E = None   # VAT Exempt
>>>
>>> PLN = 1

>>> shopping_cart = [
...     {'name': 'Bread',   'price': 3.99*PLN, 'ptu': PTU.C},
...     {'name': 'Butter',  'price': 2.69*PLN, 'ptu': PTU.B},
...     {'name': 'Ham',     'price': 5.99*PLN, 'ptu': PTU.A},
...     {'name': 'Cheese',  'price': 4.19*PLN, 'ptu': PTU.B},
... ]

>>> total = sum(product['price'] * product['ptu'].value
...             for product in shopping_cart)

>>> print(f'Total is: {total:.2f} PLN')
Total is: 18.99 PLN

.. todo:: Assignments


References
----------
.. [mskeycodes] https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN
.. [jskeycodes] https://www.cambiaresearch.com/articles/15/javascript-char-codes-key-codes


.. todo:: Assignments
