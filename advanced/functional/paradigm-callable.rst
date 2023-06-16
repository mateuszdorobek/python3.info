Functional Callable
===================
In Python, a callable is an object that can be called like a function. It
can be any of the following:

1. Functions: Defined using the `def` keyword or `lambda` keyword.

2. Methods: Functions that are defined inside a class.

3. Classes: A class can be called to create an instance of that class.

4. Objects: If an object has a `__call__()` method, it can be called like a
function.

5. Built-in functions: Functions that are built into the Python language,
such as `print()` and `len()`.

6. Built-in methods: Methods that are built into objects, such as `append()`
for lists.

To check if an object is callable, you can use the `callable()` function. It
returns `True` if the object is callable, and `False` otherwise.

Here's an example of using the `callable()` function:

```
>>> def my_function():
...     print('Hello, world!')
>>>
>>> class MyClass:
...     def __call__(self):
...         print('Hello from MyClass!')
>>>
>>> obj = MyClass()
>>>
>>> callable(my_function)
True
>>> callable(obj)
True
>>> callable('Hello')
False

In this example, `my_function` and `obj` are callable objects, while the
string "Hello" is not callable. The `__call__()` method in the `MyClass`
class allows instances of the class to be called like functions.

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
>>> def fetch(url: str,
...           on_success: Callable = lambda: ...,
...           on_error: Callable = lambda: ...) -> None:
...     ...

>>> from typing import Callable
>>>
>>>
>>> def fetch(url: str,
...           on_success: Callable[[int,int], int],
...           on_error: Callable) -> callable:
...     ...
>>>
>>> def ok(x: int, y: int) -> int:
...     ...
>>>
>>> fetch('https://...',
...         on_success=ok,
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
