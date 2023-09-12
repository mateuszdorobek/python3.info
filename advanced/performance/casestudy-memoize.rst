Case Study: Memoize
===================


Recap
-----
Recap information about factorial (``n!``):

.. code-block:: text

    5! = 5 * 4!
    4! = 4 * 3!
    3! = 3 * 2!
    2! = 2 * 1!
    1! = 1 * 0!
    0! = 1

.. code-block:: python

    factorial(5)                                    # = 120
        return 5 * factorial(4)                     # 5 * 24 = 120
            return 4 * factorial(3)                 # 4 * 6 = 24
                return 3 * factorial(2)             # 3 * 2 = 6
                    return 2 * factorial(1)         # 2 * 1 = 2
                        return 1 * factorial(0)     # 1 * 1 = 1
                            return 1                # 1


No Cache
--------
>>> #%%timeit -r 1000 -n 10_000
>>> def factorial(n: int) -> int:
...     if n == 0:
...         return 1
...     else:
...         return n * factorial(n-1)
>>>
>>>
>>> factorial(50)  # doctest: +SKIP
>>> factorial(40)  # doctest: +SKIP
>>> factorial(45)  # doctest: +SKIP
283 µs ± 6.63 µs per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


Global Scope
------------
>>> _cache = {}
>>>
>>> def cache(func):
...     def wrapper(n):
...         if n not in _cache:
...             _cache[n] = func(n)
...         return _cache[n]
...     return wrapper
>>>
>>>
>>> @cache
... def factorial(n):
...     if n == 0:
...         return 1
...     else:
...         return n * factorial(n-1)
>>>
>>>
>>> factorial(50)  # doctest: +SKIP
>>> factorial(40)  # doctest: +SKIP
>>> factorial(45)  # doctest: +SKIP


Local Scope
-----------
>>> def cache(func):
...     _cache = {}
...     def wrapper(n):
...         if n not in _cache:
...             _cache[n] = func(n)
...         return _cache[n]
...     return wrapper
>>>
>>>
>>> @cache
... def factorial(n):
...     if n == 0:
...         return 1
...     else:
...         return n * factorial(n-1)
>>>
>>>
>>> factorial(50)  # doctest: +SKIP
>>> factorial(40)  # doctest: +SKIP
>>> factorial(45)  # doctest: +SKIP


Embedded Scope
--------------
>>> def cache(func):
...     def wrapper(n):
...         if n not in wrapper._cache:
...             wrapper._cache[n] = func(n)
...         return wrapper._cache[n]
...     if not hasattr(wrapper, '_cache'):
...         setattr(wrapper, '_cache', {})
...     return wrapper
>>>
>>>
>>> @cache
... def factorial(n: int) -> int:
...     if n == 0:
...         return 1
...     else:
...         return n * factorial(n-1)
>>>
>>>
>>> factorial(50)  # doctest: +SKIP
>>> factorial(40)  # doctest: +SKIP
>>> factorial(45)  # doctest: +SKIP


Contains
--------
>>> #%%timeit -r 1000 -n 10_000
>>> _cache = {}
>>>
>>> def factorial(n: int) -> int:
...     if n in _cache:
...         return _cache[n]
...     if n == 0:
...         return 1
...     else:
...         result = _cache[n] = n * factorial(n-1)
...         return result
>>>
>>>
>>> factorial(50)  # doctest: +SKIP
>>> factorial(40)  # doctest: +SKIP
>>> factorial(45)  # doctest: +SKIP
153 µs ± 2.49 µs per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


Get
---
>>> #%%timeit -r 1000 -n 10_000
>>> _cache = {}
>>>
>>> def factorial(n: int) -> int:
...     result = _cache.get(n)
...     if result:
...         return result
...     if n == 0:
...         return 1
...     else:
...         result = _cache[n] = n * factorial(n-1)
...         return result
>>>
>>>
>>> factorial(50)  # doctest: +SKIP
>>> factorial(40)  # doctest: +SKIP
>>> factorial(45)  # doctest: +SKIP
181 µs ± 10.3 µs per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


Exceptions
----------
>>> #%%timeit -r 1000 -n 10_000
>>> _cache = {}
>>>
>>> def factorial(n: int) -> int:
...     if n == 0:
...         return 1
...     try:
...         return _cache[n]
...     except KeyError:
...         _cache[n] = result = n * factorial(n-1)
...         return result
>>>
>>>
>>> factorial(50)  # doctest: +SKIP
>>> factorial(40)  # doctest: +SKIP
>>> factorial(45)  # doctest: +SKIP
618 µs ± 6.6 µs per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


Layer
-----
>>> #%%timeit -r 1000 -n 10_000
>>> _cache = {}
>>>
>>> def fac(n: int) -> int:
...     def factorial(n: int) -> int:
...         if n == 0:
...             return 1
...         return n * factorial(n-1)
...     if not n in _cache:
...         _cache[n] = factorial(n)
...     return _cache[n]
>>>
>>>
>>> fac(50)  # doctest: +SKIP
>>> fac(40)  # doctest: +SKIP
>>> fac(45)  # doctest: +SKIP
283 µs ± 6.44 µs per loop (mean ± std. dev. of 1000 runs, 10000 loops each)

Get from cache

>>> #%%timeit -r 1000 -n 10_000
>>> _cache = {}
>>>
>>> def factorial(n: int) -> int:
...     if n == 0:
...         return 1
...     if n in _cache:
...         return _cache[n]
...     result = _cache[n] = n * factorial(n-1)
...     return result
>>>
>>>
>>> factorial(50)  # doctest: +SKIP
>>> factorial(40)  # doctest: +SKIP
>>> factorial(45)  # doctest: +SKIP
153 µs ± 9.64 µs per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


Assignment Expression
---------------------
>>> #%%timeit -r 1000 -n 10_000
>>> _cache = {}
>>>
>>> def factorial(n):
...     if n == 0:
...         return 1
...     if (result := _cache.get(n)):
...         return result
...     result = n * factorial(n-1)
...     _cache[n] = result
...     return result
>>>
>>>
>>> factorial(50)  # doctest: +SKIP
>>> factorial(40)  # doctest: +SKIP
>>> factorial(45)  # doctest: +SKIP
153 µs ± 9.64 µs per loop (mean ± std. dev. of 1000 runs, 10000 loops each)
