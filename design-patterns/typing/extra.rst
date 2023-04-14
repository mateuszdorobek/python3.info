Typing Extra
============


TypeGuard
---------
https://docs.python.org/3/library/typing.html#typing.TypeGuard


TypeAlias
---------
* Since Python 3.10 :pep:`613` -- TypeAlias Annotation

Type annotations can be written in both ``str`` and identifier form.
Both are equivalent.

>>> age: int
>>> age: 'int'

Now consider creating variable with common value such as word 'Any'. Is this
just a variable with some more or less random text, or a type alias to
``typing.Any``? This is very problematic for a type checker.

>>> from typing import Any
>>>
>>>
>>> x = Any
>>> x = 'Any'

In order to avoid such ambiguity we can use ``TypeAlias`` annotation and
therefore explicitly declare a type alias.

>>> from typing import Any, TypeAlias
>>>
>>>
>>> x: TypeAlias = Any
>>> x: TypeAlias = 'Any'


TypeVar
-------
SetUp:

>>> from typing import TypeVar

Definition:

>>> T = TypeVar('T', int, float)
>>>
>>> def add(a: T, b: T) -> T:
...     return a + b

Usage:

>>> add(1, 2)
3

>>> add(1.0, 2.0)
3.0


NewType
-------
You can create new types which are identical to some other type, and those
new values made with the new type will have access to all the methods and
properties as the original type.

>>> from typing import NewType
>>>
>>>
>>> class Person:
... 	...
>>>
>>> Astronaut = NewType('Astronaut', Person)
>>> Cosmonaut = NewType('Cosmonaut', Person)
>>>
>>> def fly_to_space(who: Astronaut):
... 	...


Use Case - 0x01
---------------
* Annotated
* Source: https://stackoverflow.com/a/68489244

>>> from functools import wraps
>>> from typing import get_type_hints, get_origin, get_args, Annotated
>>>
>>>
>>> class MaxLen:
...     def __init__(self, value):
...         self.value = value
>>>
>>>
>>> def check_annotations(func):
...     @wraps(func)
...     def wrapped(**kwargs):
...         type_hints = get_type_hints(func, include_extras=True)
...         for param, hint in type_hints.items():
...             if get_origin(hint) is not Annotated:
...                 continue
...             hint_type, *hint_args = get_args(hint)
...             if hint_type is str or get_origin(hint_type) is str:
...                 for arg in hint_args:
...                     if isinstance(arg, MaxLen):
...                         max_len = arg.value
...                         actual_len = len(kwargs[param])
...                         if actual_len > max_len:
...                             raise ValueError(f"Parameter '{param}' cannot have a length "
...                                              f"larger than {max_len} (got length {actual_len}).")
...         return func(**kwargs)
...     return wrapped
>>>
>>>
>>> word = Annotated[str, MaxLen(10)]
>>>
>>> @check_annotations
... def echo(text: word):
...     return text
>>>
>>>
>>> echo(text='abcdefghij')
'abcdefghij'
>>>
>>> echo(text='abcdefghijk')
Traceback (most recent call last):
ValueError: Parameter 'text' cannot have a length larger than 10 (got length 11).


Use Case - 0x02
---------------
>>> from typing import TypeVar
>>>
>>>
>>> T = TypeVar('T', int, float)
>>> Vector = tuple[T, T]
>>>
>>>
>>> def product(data: Vector[T]) -> T:
...     return sum(x*y for x,y in data)
