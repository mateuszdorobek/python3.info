Type Annotation TypedDict
=========================
* Since Python 3.8
* :pep:`589` -- TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys
* :pep:`655` –- Marking individual TypedDict items as required or potentially-missing

SetUp
-----
>>> from typing import TypedDict


Dict
----
>>> pt: dict = {'x':1 , 'y':2}
>>> pt: dict = {'a':1 , 'b':2}


Dict[...]
---------
>>> pt: dict[str, int] = {'x':1 , 'y':2}
>>> pt: dict[str, int] = {'a':1 , 'b':2}


TypedDict
---------
* Since Python 3.8
* :pep:`589` -- TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys

>>> class Point(TypedDict):
...     x: int
...     y: int
>>>
>>> pt = Point(x=1, y=2)  # ok
>>> pt = Point(x=1, y=2, z=3)  # error, Extra key 'z' for TypedDict 'Point'
>>> pt = Point(x=1, y=2)  # error, TypedDict 'Point' has missing keys: 'x', 'y'


Optional Values
---------------
>>> class Point(TypedDict):
...     x: int
...     y: int
...     z: int | None

>>> Point(x=1, y=2, z=3)  # ok
{'x': 1, 'y': 2, 'z': 3}

>>> Point(x=1, y=2, z=None)  # ok
{'x': 1, 'y': 2, 'z': None}

>>> Point(x=1, y=2)  # error, TypedDict 'Point' has missing key: 'z'
{'x': 1, 'y': 2}


Default Values
--------------
* Does not support default values

>>> class Point(TypedDict):
...     x: int
...     y: int
...     z: int = 0

>>> Point(x=1, y=2, z=3)  # ok
{'x': 1, 'y': 2, 'z': 3}

>>> Point(x=1, y=2)  # error, TypedDict 'Point' has missing key: 'z'
{'x': 1, 'y': 2}


NotRequired
-----------
* Since Python 3.11
* :pep:`655` –- Marking individual TypedDict items as required or potentially-missing

>>> from typing import NotRequired

>>> class Point(TypedDict):
...     x: int
...     y: int
...     z: NotRequired[int]

>>> Point(x=1, y=2)  # ok
{'x': 1, 'y': 2}

>>> Point(x=1, y=2, z=3)  # ok
{'x': 1, 'y': 2, 'z': 3}


Required
--------
* Since Python 3.11
* :pep:`655` –- Marking individual TypedDict items as required or potentially-missing

>>> from typing import Required, NotRequired

>>> class Point(TypedDict):
...     x: Required[int]
...     y: Required[int]
...     z: NotRequired[int]

>>> Point(x=1, y=2)  # ok
{'x': 1, 'y': 2}

>>> Point(x=1, y=2, z=3)  # ok
{'x': 1, 'y': 2, 'z': 3}


Total
-----
* Since Python 3.11
* :pep:`655` –- Marking individual TypedDict items as required or potentially-missing

>>> class Point(TypedDict, total=True):
...     x: int
...     y: int
...     z: int

>>> Point(x=1, y=2)  # error, TypedDict 'Point' has missing key: 'z'
{'x': 1, 'y': 2}

>>> Point(x=1, y=2, z=3)  # ok
{'x': 1, 'y': 2, 'z': 3}


Use Case - 0x01
---------------
>>> class User(TypedDict):
...     firstname: str
...     lastname: str

>>> def hello(user: User):
...     result = f'Hello {user["firstname"]} {user["lastname"]}'

>>> mark: User = {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}
>>> hello(mark)  # ok

>>> mark: User = {'firstname': 'Mark', 'lastname': 'Watney'}
>>> hello(mark)  # error: missing `age`  # doctest: +SKIP

>>> mark: User = {'firstname': 'Mark'}
>>> hello(mark)  # error: missing `lastname` and `age`  # doctest: +SKIP

>>> mark = User(firstname='Mark', lastname='Watney', age=40)
>>> hello(mark)  # ok

>>> mark = User(firstname='Mark', lastname='Watney')
>>> hello(mark)  # error: missing `age`  # doctest: +SKIP

>>> mark = User(firstname='Mark')
>>> hello(mark)  # error: missing `lastname`  # doctest: +SKIP

>>> iris = {'genus': 'Iris', 'species': 'Setosa'}
>>> hello(iris)  # error: not an user  # doctest: +SKIP


Use Case - 0x02
---------------
>>> from datetime import datetime, date, time
>>> from typing import Literal, TypedDict
>>>
>>> class Log(TypedDict):
...     when: datetime
...     level: Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
...     message: str
>>>
>>>
>>> def parse(line: str) -> Log:
...     d, t, lvl, msg = line.strip().split(', ', maxsplit=3)
...     d = date.fromisoformat(d)
...     t = time.fromisoformat(t)
...     dt = datetime.combine(d,t)
...     return Log(when=dt, level=lvl, message=msg)

>>> line = '1969-07-21, 02:56:15, WARNING, Neil Armstrong first words on the Moon'
>>>
>>> parse(line)  # doctest: +NORMALIZE_WHITESPACE
{'when': datetime.datetime(1969, 7, 21, 2, 56, 15),
 'level': 'WARNING',
 'message': 'Neil Armstrong first words on the Moon'}


Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`


References
----------
.. [#pyDocTyping] https://docs.python.org/3/library/typing.html#module-contents
