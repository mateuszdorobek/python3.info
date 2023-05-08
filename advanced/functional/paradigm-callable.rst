Functional Callable
===================

>>> def hello():
...     return 'Hello World'
>>>
>>>
>>> callable(hello)
True
>>>
>>> type(hello)
<class 'function'>
>>>
>>> hello  # doctest: +ELLIPSIS
<function hello at 0x...>
>>>
>>> hello()
'Hello World'


Calling Call Method
-------------------
* ``__call__()`` method makes object callable

>>> def hello():
...     return 'Hello World'
>>>
>>>
>>> hello()
'Hello World'
>>>
>>> hello.__call__()
'Hello World'


Overloading Call Method
-----------------------
>>> data = str('Mark Watney')
>>>
>>> data()
Traceback (most recent call last):
TypeError: 'str' object is not callable
>>>
>>> callable(data)
False

>>> class str(str):
...     def __call__(self):
...         print('Calling str')
>>>
>>>
>>> data = str('Mark Watney')
>>>
>>> data()
Calling str
>>>
>>> callable(data)
True


Typing
------
>>> from typing import Callable
>>>
>>>
>>> def add(a: int, b: int) -> int:
...     return a + b
>>>
>>>
>>> total: Callable = add
>>> total: Callable[[int, int], int] = add

>>> from typing import Callable
>>>
>>>
>>> def lower() -> str:
...     return 'hello'
>>>
>>>
>>> def higher() -> Callable:
...     return lower

>>> from typing import Callable
>>>
>>>
>>> def http_request(url: str,
...                  on_success: Callable = lambda: ...,
...                  on_error: Callable = lambda: ...) -> None:
...     ...

>>> from typing import Callable
>>>
>>>
>>> def request(url: str,
...             on_success: Callable[[int,int], int],
...             on_error: Callable) -> callable:
...     ...
>>>
>>> def handle_success(x: int, y: int) -> int:
...     ...
>>>
>>> request('https://...',
...         on_success=handle_success,
...         on_error=lambda: ...)

>>> from typing import Callable, Iterator, Iterable
>>>
>>>
>>> def map(func: Callable, data: Iterable) -> Iterator:
...     ...
>>>
>>> def filter(func: Callable, data: Iterable) -> Iterator:
...     ...


Assignments
-----------
.. literalinclude:: assignments/functional_callable_a.py
    :caption: :download:`Solution <assignments/functional_callable_a.py>`
    :end-before: # Solution
