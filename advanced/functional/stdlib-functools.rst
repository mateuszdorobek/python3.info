Functional Stdlib Functools
===========================
* ``import functools``
* ``functools.partial()``
* ``functools.partialmethod()``
* ``functools.reduce()``
* ``functools.singledispatch()``
* ``functools.singledispatchmethod()``

The functools module in Python provides a set of higher-order functions that
can be used to manipulate functions and other callable objects. These
functions can be used to modify the behavior of functions, create new
functions from existing ones, and perform other operations on functions.

One of the most commonly used functions in the functools module is
``partial()``, which allows you to create a new function with some of the
arguments of an existing function already set. This can be useful in
situations where you need to repeatedly call a function with the same
arguments, but don't want to keep typing them out.

Another useful function in the functools module is ``reduce()``, which applies
a function to a sequence of values and returns a single value. This can be
used to perform operations such as calculating the sum of a list of numbers
or finding the maximum value in a list.

The functools module also includes functions for caching function results
(``lru_cache()``), creating decorators (``wraps()``), and performing other
operations on functions and callable objects.

Overall, the functools module provides a powerful set of tools for working
with functions in Python and can be particularly useful in functional
programming.

>>> import functools
>>>
>>> [method for method in dir(functools)
...         if not method.startswith('_')
...         and callable(getattr(functools, method))]   # doctest: +NORMALIZE_WHITESPACE
['GenericAlias', 'RLock', 'cache', 'cached_property', 'cmp_to_key',
 'get_cache_token', 'lru_cache', 'namedtuple', 'partial', 'partialmethod',
 'recursive_repr', 'reduce', 'singledispatch', 'singledispatchmethod',
 'total_ordering', 'update_wrapper', 'wraps']


Partial
-------
* Create alias function and its arguments
* Useful when you need to pass function with arguments to for example ``map`` or ``filter``

>>> from functools import partial
>>>
>>>
>>> basetwo = partial(int, base=2)
>>> basetwo.__doc__ = 'Convert base 2 string to an int.'
>>> basetwo('10010')
18


Partialmethod
-------------
>>> from functools import partialmethod
>>>
>>>
>>> class Cell(object):
...     def __init__(self):
...         self._alive = False
...
...     @property
...     def alive(self):
...         return self._alive
...
...     def set_state(self, state):
...         self._alive = bool(state)
...
...     set_alive = partialmethod(set_state, True)
...     set_dead = partialmethod(set_state, False)
>>>
>>>
>>> c = Cell()
>>>
>>> c.alive
False
>>>
>>> c.set_alive()
>>> c.alive
True


Reduce
------
* split-apply-combine strategy

Apply function of two arguments cumulatively to the items of iterable, from
left to right, so as to reduce the iterable to a single value. For example,
``reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])`` calculates
``((((1+2)+3)+4)+5)``. The left argument, x, is the accumulated value and
the right argument, y, is the update value from the iterable. If the
optional initializer is present, it is placed before the items of the
iterable in the calculation, and serves as a default when the iterable is
empty. If initializer is not given and iterable contains only one item, the
first item is returned.

Roughly equivalent to:

>>> def reduce(function, iterable, initializer=None):
...     it = iter(iterable)
...     if initializer is None:
...         value = next(it)
...     else:
...         value = initializer
...     for element in it:
...         value = function(value, element)
...     return value

SetUp:

>>> from functools import reduce
>>>
>>> DATA = [1, 2, 3, 4, 5]

Usage:

>>> def add(x, y):
...     return (x + y)
>>>
>>> reduce(add, DATA)
15

>>> reduce(lambda x, y: x + y, DATA)
15


Singledispatch
--------------
* Since Python 3.4
* Overload a method
* Python will choose function to run based on argument type

>>> from functools import singledispatch
>>>
>>>
>>> @singledispatch
... def celsius_to_kelvin(arg):
...     raise NotImplementedError('Argument must be int or list')
>>>
>>> @celsius_to_kelvin.register
... def _(degree: int):
...     return degree + 273.15
>>>
>>> @celsius_to_kelvin.register
... def _(degrees: list):
...     return [d+273.15 for d in degrees]
>>>
>>>
>>> celsius_to_kelvin(1)
274.15
>>>
>>> celsius_to_kelvin([1,2])
[274.15, 275.15]
>>>
>>> celsius_to_kelvin((1,2))
Traceback (most recent call last):
NotImplementedError: Argument must be int or list

>>> from functools import singledispatch
>>>
>>>
>>> @singledispatch
... def km_to_m(km):
...     raise NotImplementedError('...')
>>>
>>>
>>> @km_to_m.register
... def _(km: int):
...     return km * 1000
>>>
>>>
>>> @km_to_m.register
... def _(km: float):
...     return km * 1000.0
>>>
>>>
>>> @km_to_m.register
... def _(km: list):
...     return [x*1000 for x in km]


Singledispatchmethod
--------------------
* Since Python 3.8
* Overload a method
* Python will choose method to run based on argument type

>>> from functools import singledispatchmethod
>>>
>>>
>>> class Converter:
...
...     @singledispatchmethod
...     def celsius_to_kelvin(*args):
...         raise NotImplementedError('Argument must be int or list')
...
...     @celsius_to_kelvin.register
...     def _(self, degree: int):
...         return degree + 273.15
...
...     @celsius_to_kelvin.register
...     def _(self, degrees: list):
...         return [d+273.15 for d in degrees]
>>>
>>>
>>> conv = Converter()
>>>
>>> conv.celsius_to_kelvin(1)
274.15
>>>
>>> conv.celsius_to_kelvin([1,2])
[274.15, 275.15]
>>>
>>> conv.celsius_to_kelvin((1,2))
Traceback (most recent call last):
NotImplementedError: Argument must be int or list


Use Case - 0x01
---------------
>>> def square(x):
...     return x ** 2
>>>
>>> def cube(x):
...     return x ** 3
>>>
>>> def apply(data, fn):
...     return map(fn, data)
>>>
>>> def add(x, y):
...     return x + y

>>> data = [1,2,3,4]
>>> transformations = [square, cube]

>>> result = reduce(apply, transformations, data)
>>> list(result)
[1, 64, 729, 4096]

>>> result = reduce(apply, transformations, data)
>>> reduce(add, result)
4890


References
----------
.. [#dask] Dask core developers. Dask. Year: 2019. Retrieved: 2022-03-15. URL: https://raw.githubusercontent.com/dask/dask-org/main/images/grid_search_schedule.gif

.. todo:: Assignments
