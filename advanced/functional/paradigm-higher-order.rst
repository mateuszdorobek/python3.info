Functional Higher-Order
=======================
* Function can take other function as arguments
* Function can return function

Functions in the functional programming style are treated as variables.
This makes them first-class functions. These can be passed to other
functions as parameters or returned from functions or stored in data
structures. [#Inouye2022]_

A higher-order function is a function that takes other functions as
arguments and/or returns functions. First-class functions can be
higher-order functions in functional programming languages. [#Inouye2022]_

>>> def lower():
...     ...
>>>
>>>
>>> def higher():
...     return lower


Calling
-------
>>> def lower():
...     return 'My name... José Jiménez'
>>>
>>> def higher():
...     return lower
>>>
>>>
>>> a = higher
>>> b = higher()
>>>
>>> a  # doctest: +ELLIPSIS
<function higher at 0x...>
>>>
>>> a()  # doctest: +ELLIPSIS
<function lower at 0x...>
>>>
>>> a()()
'My name... José Jiménez'
>>>
>>> b  # doctest: +ELLIPSIS
<function lower at 0x...>
>>>
>>> b()
'My name... José Jiménez'


Use Case - 0x01
---------------
>>> def apply(fn, data):
...     return fn(data)
>>>
>>> def square(x):
...     return x ** 2
>>>
>>>
>>> apply(square, 2)
4


References
----------
.. [#Inouye2022] Inouye, Jenna. "Functional Programming Languages: Concepts & Advantages". Year: 2022. Retrieved: 2022-07-28, URL: https://hackr.io/blog/functional-programming
