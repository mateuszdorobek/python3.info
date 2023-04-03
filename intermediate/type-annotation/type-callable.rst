Type Annotation Callable
========================
* Before Python 3.9 you need ``from typing import List, Set, Tuple, Dict``
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections


Return
------
>>> def say_hello() -> str:
...     return 'My name... José Jiménez'


Parameters
----------
Required:

>>> def add(a: int, b: int):
...     return a + b

Optional:

>>> def add(a: int = 1, b: int = 1):
...     return a + b


Union
-----
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y

>>> def add(a: int | float, b: int | float) -> int | float:
...     return a + b


Optional
--------
>>> def find(character, text) -> int | None:
...     position = text.find(character)
...     if position == -1:
...         return None
...     return position


Alias
-----
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y

>>> number = int | float
>>>
>>> def add(a: number, b: number) -> number:
...     return a + b


Exception
---------
>>> def div(a: float, b: float) -> float:
...     if b == 0:
...         raise ZeroDivisionError
...     return a / b

>>> def div(a: float, b: float) -> float | Exception:
...     if b == 0:
...         raise ZeroDivisionError
...     return a / b

>>> def div(a: float, b: float) -> float | ZeroDivisionError:
...     if b == 0:
...         raise ZeroDivisionError
...     return a / b


Literal
-------
* Since Python 3.8: :pep:`586` -- Literal Types
* Literal de-duplicates parameters
* Equality comparisons of Literal objects are not order dependent
* https://docs.python.org/3/library/typing.html#typing.Literal

SetUp:

>>> from typing import Literal

Definition:

>>> def open(filename: str, mode: Literal['r','w','a']) -> None:
...     pass

Usage:

>>> open('data.csv', mode='w')  # mypy: OK
>>> open('data.csv', mode='r')  # mypy: OK
>>> open('data.csv', mode='a')  # mypy: OK
>>> open('data.csv', mode='x')  # mypy: ERROR


Callable
--------
* Function is Callable
* ``Callable``
* ``Callable[[int, int], float]`` is a function of ``(int, int) -> float``
* There is no syntax to indicate optional or keyword arguments
* https://docs.python.org/3/library/typing.html#typing.Callable

SetUp:

>>> from typing import Callable

Define:

>>> def add(a: int, b: int) -> int:
...     return a + b
>>>
>>> x: Callable = add
>>> x: Callable[..., int] = add
>>> x: Callable[[int,int], int] = add

Parameter:

>>> def run(func: Callable[[int, int], float]):
...     ...


Iterator
--------
* All Generators are Iterators
* ``Generator[yield_type, send_type, return_type]``
* ``Iterator[yield_type]``

SetUp:

>>> from typing import Iterator, Generator

Generator type annotations:

>>> def fib(n: int) -> Generator[int, None, None]:
...     a, b = 0, 1
...     while a < n:
...         yield a
...         a, b = b, a + b

All Generators are Iterators so you can write:

>>> def fib(n: int) -> Iterator[int]:
...     a, b = 0, 1
...     while a < n:
...         yield a
...         a, b = b, a + b


Annotations
-----------
>>> def add(a: int, b: int) -> int:
...     return a + b
>>>
>>>
>>> add.__annotations__
{'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}


Errors
------
* Python will execute without even warning
* Your IDE and ``mypy`` et. al. will yield errors

>>> def add(a: int, b: int) -> int:
...     return a + b
>>>
>>>
>>> add('Mark', 'Watney')
'MarkWatney'


Good Engineering Practices
--------------------------
>>> def add(a: int | float,
...         b: int | float,
...         ) -> int | float:
...     return a + b


Literal String
--------------
* Since Python 3.11: :pep:`675` -- Arbitrary Literal String Type

SetUp:

>>> from typing import LiteralSting  # doctest: +SKIP

Example:

>>> # doctest: +SKIP
... def execute(sql: LiteralString) -> ...
...     ...
...
...
... execute('SELECT * FROM users WHERE login="mwatney"')                  # ok
... execute('SELECT * FROM users WHERE login=' + username)                # ok
... execute(f'SELECT * FROM users WHERE login=%s' % username)             # error
... execute(f'SELECT * FROM users WHERE login=%(login)s' % {'login': username}) # error
... execute(f'SELECT * FROM users WHERE login={}'.format(username))       # error
... execute(f'SELECT * FROM users WHERE login={0}'.format(username))      # error
... execute(f'SELECT * FROM users WHERE login={login}'.format(username))  # error
... execute(f'SELECT * FROM users WHERE login={username}')                # error


Use Case - 0x01
---------------
>>> def valid_email(email: str) -> str | Exception:
...     if '@' in email:
...         return email
...     else:
...         raise ValueError('Invalid Email')
>>>
>>>
>>> valid_email('mwatney@nasa.gov')
'mwatney@nasa.gov'
>>>
>>> valid_email('mwatney_at_nasa.gov')
Traceback (most recent call last):
ValueError: Invalid Email


Use Case - 0x02
---------------
>>> def find(text: str, what: str) -> int | None:
...     position = text.find(what)
...     if position == -1:
...         return None
...     else:
...         return position
>>>
>>>
>>> find('Python', 'x')
>>> find('Python', 'o')
4


Use Case - 0x03
---------------
>>> from urllib.request import urlopen
>>> from typing import Any
>>>
>>>
>>> def fetch(url: str,
...           on_success: Callable[[str], Any] = lambda result: ...,
...           on_error: Callable[[Exception], Any] = lambda error: ...,
...           ) -> None:
...     try:
...         result: str = urlopen(url).read().decode('utf-8')
...     except Exception as err:
...         on_error(err)
...     else:
...         on_success(result)

>>> def handle_result(result: str) -> None:
...     print('Success', result)
>>>
>>> def handle_error(error: Exception) -> None:
...     print('Error', error)
>>>
>>>
>>> fetch(
...     url='https://python3.info',
...     on_success=handle_result,
...     on_error=handle_error,
... )  # doctest: +SKIP

>>> fetch(
...     url='https://python3.info',
...     on_success=lambda result: print(result),
...     on_error=lambda error: print(error),
... )  # doctest: +SKIP


Use Case - 0x04
---------------
>>> import json
>>> from datetime import date
>>> from typing import Any

>>> data = {'firstname': 'Mark', 'lastname': 'Watney'}
>>> json.dumps(data)
'{"firstname": "Mark", "lastname": "Watney"}'

>>> data = {'firstname': 'Mark', 'lastname': 'Watney', 'birthday': date(1969, 7, 21)}
>>> json.dumps(data)
Traceback (most recent call last):
TypeError: Object of type date is not JSON serializable

>>> def encoder(obj: Any) -> str:
...     if isinstance(obj, date):
...         return obj.isoformat()
...
>>>
>>> json.dumps(data, default=encoder)
'{"firstname": "Mark", "lastname": "Watney", "birthday": "1969-07-21"}'


Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`
