Decorate Stacked
================


SetUp
-----
>>> from datetime import datetime
>>> import logging

>>> logging.basicConfig(
...     level='DEBUG',
...     format='{asctime}, "{levelname}", "{message}"',
...     datefmt='"%Y-%m-%d", "%H:%M:%S"',
...     style='{')
>>>
>>> log = logging.getLogger(__name__)


Example
-------
>>> def timeit(func):
...     def wrapper(*args, **kwargs):
...         start = datetime.now()
...         result = func(*args, **kwargs)
...         end = datetime.now()
...         log.info(f'Duration: {end - start}')
...         return result
...     return wrapper
>>>
>>>
>>> def debug(func):
...     def wrapper(*args, **kwargs):
...         function = func.__name__
...         log.debug(f'Calling: {function=}, {args=}, {kwargs=}')
...         result = func(*args, **kwargs)
...         log.debug(f'Result: {result}')
...         return result
...     return wrapper
>>>
>>>
>>> @timeit
... @debug
... def add(a, b):
...     return a + b
>>>
>>>
>>> add(1, 2)  # doctest: +SKIP
"1969-07-21", "02:56:15", "DEBUG", "Calling: function='add', args=(1, 2), kwargs={}"
"1969-07-21", "02:56:15", "DEBUG", "Result: 3"
"1969-07-21", "02:56:15", "INFO", "Duration: 0:00:00.000209"
>>>
>>> add(1, b=2)  # doctest: +SKIP
"1969-07-21", "02:56:15", "DEBUG", "Calling: function='add', args=(1,), kwargs={'b': 2}"
"1969-07-21", "02:56:15", "DEBUG", "Result: 3"
"1969-07-21", "02:56:15", "INFO", "Duration: 0:00:00.000154"
>>>
>>> add(a=1, b=2)  # doctest: +SKIP
"1969-07-21", "02:56:15", "DEBUG", "Calling: function='add', args=(), kwargs={'a': 1, 'b': 2}"
"1969-07-21", "02:56:15", "DEBUG", "Result: 3"
"1969-07-21", "02:56:15", "INFO", "Duration: 0:00:00.000083"


Assignments
-----------
.. todo:: Assignments
