Enum IntEnum
============
* List of finite choices
* Enumerations
* ``IntEnum``
* ``Flag``
* ``IntFlag``


SetUp
-----
>>> from enum import Enum, IntEnum


Example
-------
>>> class Select(Enum):
...     OPTION1 = 1
...     OPTION2 = 2


Use Case - 0x01
---------------
>>> class HTTPStatus(Enum):
...     OK = 200
...     CREATED = 201
...     BAD_REQUEST = 400
...     NOT_FOUND = 404
...     INTERNAL_ERROR = 500


Use Case - 0x02
---------------
>>> class Status(IntEnum):
...     FULL_HEALTH = 100
...     DEAD = 0

>>> hit_points = 100
>>> Status(hit_points)
<Status.FULL_HEALTH: 100>

>>> hit_points = 0
>>> Status(hit_points)
<Status.DEAD: 0>


Use Case - 0x03
---------------
>>> class IndexDrives(IntEnum):
...     ControlWord = 0x6040
...     StatusWord = 0x6041
...     OperationMode = 0x6060


Use Case - 0x04
---------------
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


Use Case - 0x05
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


References
----------
.. [mskeycodes] https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN
.. [jskeycodes] https://www.cambiaresearch.com/articles/15/javascript-char-codes-key-codes


.. todo:: Assignments
