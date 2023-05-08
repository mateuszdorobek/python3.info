FuncProg Higher-Order
=====================
* Function can take other function as arguments
* Function can return function

Functions in the functional programming style are treated as variables. This makes them first-class functions. These can be passed to other functions as parameters or returned from functions or stored in data structures. [#Inouye2022]_

A higher-order function is a function that takes other functions as arguments and/or returns functions. First-class functions can be higher-order functions in functional programming languages. [#Inouye2022]_

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


Use Case - 0x02
---------------
>>> def http_request(url, on_success, on_error):
...     try:
...         result = ...
...     except Exception as error:
...         return on_error(error)
...     else:
...         return on_success(result)
>>>
>>>
>>> http_request(
...     url = 'https://python3.info',
...     on_success = lambda result: print(result),
...     on_error = lambda error: print(error))
Ellipsis


Use Case - 0x03
---------------
>>> from functools import reduce

>>> class MapReduce:
...     def __init__(self, values):
...         self.values = values
...
...     def filter(self, fn):
...          self.values = filter(fn, self.values)
...          return self
...
...     def map(self, fn):
...         self.values = map(fn, self.values)
...         return self
...
...     def reduce(self, fn):
...         return reduce(fn, self.values)

>>> DATA = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> result = (
...     MapReduce(DATA)
...     .map(lambda x: x ** 2)
...     .map(lambda x: x / 2)
...     .map(lambda x: x + 2)
...     .map(lambda x: round(x, 2))
...     .map(lambda x: int(x))
...     .filter(lambda x: x > 10)
...     .reduce(lambda x,y: x + y)
... )

>>> result
136


Use Case - 0x04
---------------
* Maybe monad
* Continues execution, even, if there is an error
* Final state will be none
* But no intermediate error handling is needed

>>> class Maybe:
...     def __init__(self, value):
...         self.value = value
...
...     def __repr__(self):
...         return f"Maybe({self.value})"
...
...     def unwrap(self):
...         return self.value
...
...     def bind(self, func):
...         if self.value is None:
...             return Maybe(None)
...         return Maybe(func(self.value))

>>> DATA = 4
>>>
>>> result = (
...     Maybe(DATA)
...     .bind(lambda x: 2*x)
...     .bind(lambda y: y+1)
... )
>>>
>>> print(result)
Maybe(9)
>>>
>>> print(result.unwrap())
9

>>> DATA = 4
>>>
>>> result = (
...     Maybe(DATA)
...     .bind(lambda x: None if x < 10 else x)  # this could fail
...     .bind(lambda x: 2*x)
...     .bind(lambda y: y+1)
... )
>>>
>>> result
Maybe(None)
>>>
>>> result.unwrap()



References
----------
.. [#Inouye2022] Inouye, Jenna. "Functional Programming Languages: Concepts & Advantages". Year: 2022. Retrieved: 2022-07-28, URL: https://hackr.io/blog/functional-programming
