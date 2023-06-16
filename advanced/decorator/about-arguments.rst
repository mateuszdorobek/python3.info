Decorator About Arguments
=========================
* Without Arguments
* With Positional Arguments
* With Mixed Arguments
* With Keyword Arguments

In Python, decorators can also take arguments. This allows you to customize
the behavior of the decorator for different use cases.

To create a decorator with arguments, you need to define a function that
takes the arguments you want to use, and then returns a decorator function
that takes the original function as its argument. The decorator function can
then use the arguments passed to the outer function to modify the behavior
of the original function.

Here is an example of a decorator with arguments:

>>> def repeat(num_repeats):
...     def decorator(func):
...         def wrapper(*args, **kwargs):
...             for i in range(num_repeats):
...                 func(*args, **kwargs)
...         return wrapper
...     return decorator
>>>
>>> @repeat(num_repeats=3)
... def say_hello(name):
...     print(f'Hello {name}')
>>>
>>> say_hello('Mark')
Hello Mark
Hello Mark
Hello Mark

In this example, the ``repeat`` function takes an argument ``num_repeats``
and returns a decorator function. The decorator function takes the original
function ``func`` as its argument and returns a new function ``wrapper``
that calls the original function multiple times based on the value of
``num_repeats``.

The ``@repeat(num_repeats=3)`` syntax is used to apply the decorator to the
``say_hello`` function with the argument ``num_repeats`` set to 3. When
``say_hello`` is called with the argument "Mark", it will print "Hello Mark"
three times.


Without Arguments
-----------------
>>> @mydecorator  # doctest: +SKIP
... def myfunction(*args, **kwargs):
...     ...


With Positional Arguments
-------------------------
>>> @mydecorator('Mark', 'Watney')  # doctest: +SKIP
... def myfunction(*args, **kwargs):
...     ...


With Mixed Arguments
--------------------
>>> @mydecorator('Mark', lastname='Watney')  # doctest: +SKIP
... def myfunction(*args, **kwargs):
...     ...


With Keyword Arguments
----------------------
>>> @mydecorator(firstname='Mark', lastname='Watney')  # doctest: +SKIP
... def myfunction(*args, **kwargs):
...     ...
