Decorator Stdlib Functools
==========================


Wraps
-----
* ``from functools import wraps``
* ``@wraps(func)``

Without Wraps:

>>> def mydecorator(func):
...     def wrapper(*args, **kwargs):
...         """wrapper docstring"""
...         return func(*args, **kwargs)
...     return wrapper
>>>
>>>
>>> @mydecorator
... def myfunction(x):
...     """myfunction docstring"""
...     print(x)
>>>
>>>
>>> print(myfunction.__name__)
wrapper
>>>
>>> print(myfunction.__doc__)
wrapper docstring

With Wraps:

>>> from functools import wraps
>>>
>>>
>>> def mydecorator(func):
...     @wraps(func)
...     def wrapper(*args, **kwargs):
...         """wrapper docstring"""
...         return func(*args, **kwargs)
...     return wrapper
>>>
>>>
>>> @mydecorator
... def myfunction(x):
...     """myfunction docstring"""
...     print(x)
>>>
>>>
>>> print(myfunction.__name__)
myfunction
>>>
>>> print(myfunction.__doc__)
myfunction docstring


Cached Property
---------------
* ``from functools import cached_property``
* ``@cached_property(method)``

>>> import statistics
>>> from functools import cached_property
>>>
>>>
>>> class Iris:
...     def __init__(self, *args):
...         self._measurements = args
...
...     @cached_property
...     def mean(self):
...         return statistics.mean(self._measurements)
...
...     @cached_property
...     def stdev(self):
...         return statistics.stdev(self._measurements)
>>>
>>>
>>> flower = Iris(5.1, 3.5, 1.4, 0.2)
>>>
>>> flower.stdev
2.1794494717703365
>>>
>>> flower.mean
2.55


LRU (least recently used) cache
-------------------------------
* ``from functools import lru_cache``
* ``@lru_cache(maxsize=None)``

>>> from functools import lru_cache
>>>
>>>
>>> @lru_cache(maxsize=None)
... def fib(n):
...     if n < 2:
...         return n
...     return fib(n-1) + fib(n-2)
>>>
>>>
>>> [fib(n) for n in range(16)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
>>>
>>> fib.cache_info()
CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)


Assignments
-----------
.. literalinclude:: assignments/decorator_functools_a.py
    :caption: :download:`Solution <assignments/decorator_functools_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/decorator_functools_b.py
    :caption: :download:`Solution <assignments/decorator_functools_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/decorator_functools_c.py
    :caption: :download:`Solution <assignments/decorator_functools_c.py>`
    :end-before: # Solution
