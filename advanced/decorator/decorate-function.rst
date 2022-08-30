Decorate Function
=================
* Decorator must return reference to ``wrapper``
* ``wrapper`` is a closure function
* ``wrapper`` name is a convention, but you can name it anyhow
* ``wrapper`` gets arguments passed to ``function``

Definition:

>>> def mydecorator(func):
...     def wrapper(*args, **kwargs):
...         return func(*args, **kwargs)
...     return wrapper

Decoration:

>>> @mydecorator
... def myfunction():
...     ...

Usage:

>>> myfunction()


Example
-------
>>> def run(func):
...     def wrapper(*args, **kwargs):
...         return func(*args, **kwargs)
...     return wrapper
>>>
>>>
>>> @run
... def hello(name):
...     return f'My name... {name}'
>>>
>>>
>>> hello('José Jiménez')
'My name... José Jiménez'


Use Case - 0x01
---------------
* Check if file exists, before executing function:

>>> import os
>>>
>>>
>>> def ifexists(func):
...     def wrapper(file):
...         if os.path.exists(file):
...             return func(file)
...         else:
...             print(f'File {file} does not exist')
...     return wrapper
>>>
>>>
>>> @ifexists
... def display(file):
...     print(f'Printing file {file}')
>>>
>>>
>>> display('/etc/passwd')
Printing file /etc/passwd
>>>
>>> display('/tmp/passwd')
File /tmp/passwd does not exist


Use Case - 0x02
---------------
* Timeit

>>> from time import time
>>>
>>>
>>> def timeit(func):
...     def wrapper(*args, **kwargs):
...         start = time()
...         result = func(*args, **kwargs)
...         end = time()
...         duration = end - start
...         print(f'Duration: {duration}')
...         return result
...     return wrapper
>>>
>>>
>>> @timeit
... def add(a, b):
...     return a + b
>>>
>>>
>>> add(1, 2)  # doctest: +SKIP
Duration: 0:00:00.000006
3
>>>
>>> add(1, b=2)  # doctest: +SKIP
Duration: 0:00:00.000007
3
>>>
>>> add(a=1, b=2)  # doctest: +SKIP
Duration: 0:00:00.000008
3


Use Case - 0x03
---------------
* Debug

>>> def debug(func):
...     def wrapper(*args, **kwargs):
...         function = func.__name__
...         print(f'Calling: {function=}, {args=}, {kwargs=}')
...         result = func(*args, **kwargs)
...         print(f'Result: {result}')
...         return result
...     return wrapper
>>>
>>>
>>> @debug
... def add(a, b):
...     return a + b
>>>
>>>
>>> add(1, 2)  # doctest: +SKIP
Calling: function='add', args=(1, 2), kwargs={}
Result: 3
3
>>>
>>> add(1, b=2)  # doctest: +SKIP
Calling: function='add', args=(1,), kwargs={'b': 2}
Result: 3
3
>>>
>>> add(a=1, b=2)  # doctest: +SKIP
Calling: function='add', args=(), kwargs={'a': 1, 'b': 2}
Result: 3
3


Use Case - 0x04
---------------
* Deprecated

>>> import warnings
>>>
>>>
>>> def deprecated(func):
...     def wrapper(*args, **kwargs):
...         name = func.__name__
...         file = func.__code__.co_filename
...         line = func.__code__.co_firstlineno + 1
...         message = f'Call to deprecated function `{name}` in {file} at line {line}'
...         warnings.warn(message, DeprecationWarning)
...         return func(*args, **kwargs)
...     return wrapper
>>>
>>>
>>> @deprecated
... def add(a, b):
...     return a + b
>>>
>>>
>>> add(1, 2)  # doctest: +SKIP
/home/python/myscript.py:11: DeprecationWarning: Call to deprecated function `add` in /home/python/myscript.py at line 19


Use Case - 0x05
---------------
* Stacked Decorators

>>> from datetime import datetime
>>> import logging
>>>
>>> logging.basicConfig(
...     level='DEBUG',
...     format='{asctime}, "{levelname}", "{message}"',
...     datefmt='"%Y-%m-%d", "%H:%M:%S"',
...     style='{')
>>>
>>> log = logging.getLogger(__name__)
>>>
>>>
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


Use Case - 0x06
---------------
* Global Scope Cache

Recap information about factorial (``n!``):

.. code-block:: text

    5! = 5 * 4!
    4! = 4 * 3!
    3! = 3 * 2!
    2! = 2 * 1!
    1! = 1 * 0!
    0! = 1

.. code-block:: text

    n! = n * (n-1)!  # 1 for n=0

>>> def factorial(n):
...     if n == 0:
...         return 1
...     else:
...         return n * factorial(n-1)


Use Case - 0x07
---------------
Cache with global scope:

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
>>> factorial(5)
120
>>>
>>> print(_cache)
{0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120}


Use Case - 0x08
---------------
* Local Scope Cache

Cache with local scope:

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
>>> factorial(5)
120


Use Case - 0x09
---------------
Cache with embedded scope:

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
>>> print(factorial(4))
24
>>>
>>> print(factorial._cache)
{0: 1, 1: 1, 2: 2, 3: 6, 4: 24}
>>>
>>> print(factorial(6))
720
>>>
>>> print(factorial._cache)
{0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720}
>>>
>>> print(factorial(6))
720
>>>
>>> print(factorial(3))
6
>>>
>>> print(factorial._cache)
{0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720}


Use Case - 0x0A
---------------
* Database Cache

>>> DATABASE = {
...     'mlewis':       {'name': 'Melissa Lewis',   'email': 'melissa.lewis@nasa.gov'},
...     'mwatney':      {'name': 'Mark Watney',     'email': 'mark.watney@nasa.gov'},
...     'avogel':       {'name': 'Alex Vogel',      'email': 'alex.vogel@nasa.gov'},
...     'rmartinez':    {'name': 'Rick Martinez',   'email': 'rick.martinez@nasa.gov'},
...     'bjohanssen':   {'name': 'Beth Johanssen',  'email': 'beth.johanssen@nasa.gov'},
...     'cbeck':        {'name': 'Chris Beck',      'email': 'chris.beck@nasa.gov'},
... }
>>>
>>> _cache = {}
>>>
>>> def cache(func):
...     def wrapper(username):
...         if username not in _cache:
...             _cache[username] = func(username)
...         return _cache[username]
...     return wrapper
>>>
>>>
>>> @cache
... def db_search(username):
...     return DATABASE[username]['name']
>>>
>>>
>>>
>>> db_search('mwatney')  # not in cache, searches database and updates cache with result
'Mark Watney'
>>>
>>> db_search('mwatney')  # found in cache and returns from it, no database search
'Mark Watney'
>>>
>>> print(_cache)
{'mwatney': 'Mark Watney'}


Use Case - 0x0B
---------------
* FastAPI URL Routing

>>> # doctest: +SKIP
... from fastapi import FastAPI
...
... app = FastAPI()
...
...
... @app.get('/')
... async def index():
...     return {'message': 'Hello World'}
...
...
... @app.get('/user/{pk}')
... async def user(pk: int):
...     return {'pk': pk}
...
...
... @app.get('/search')
... async def items(q: str | None = None):
...     return {'q': q}


Use Case - 0x0C
---------------
* Django Login Required

Decorator checks whether user is_authenticated.
If not, user will be redirected to login page:

>>> # doctest: +SKIP
... from django.shortcuts import render
...
...
... def edit_profile(request):
...     if not request.user.is_authenticated:
...         return render(request, 'templates/login_error.html')
...     else:
...         return render(request, 'templates/edit-profile.html')
...
...
... def delete_profile(request):
...     if not request.user.is_authenticated:
...         return render(request, 'templates/login_error.html')
...     else:
...         return render(request, 'templates/delete-profile.html')

>>> # doctest: +SKIP
... from django.shortcuts import render
... from django.contrib.auth.decorators import login_required
...
...
... @login_required
... def edit_profile(request):
...     return render(request, 'templates/edit-profile.html')
...
...
... @login_required
... def delete_profile(request):
...     return render(request, 'templates/delete-profile.html')


Assignments
-----------
.. literalinclude:: assignments/decorator_func_a.py
    :caption: :download:`Solution <assignments/decorator_func_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/decorator_func_b.py
    :caption: :download:`Solution <assignments/decorator_func_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/decorator_func_c.py
    :caption: :download:`Solution <assignments/decorator_func_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/decorator_func_d.py
    :caption: :download:`Solution <assignments/decorator_func_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/decorator_func_e.py
    :caption: :download:`Solution <assignments/decorator_func_e.py>`
    :end-before: # Solution

.. literalinclude:: assignments/decorator_func_f.py
    :caption: :download:`Solution <assignments/decorator_func_f.py>`
    :end-before: # Solution
