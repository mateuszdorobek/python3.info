Decorator Arguments
===================


Important
---------
* Used for passing extra configuration to decorators
* Use more one level of nesting


Syntax
------
>>> def mydecorator(a=1, b=2):
...     def decorator(func):
...         def wrapper(*args, **kwargs):
...             return func(*args, **kwargs)
...         return wrapper
...     return decorator
>>>
>>>
>>> @mydecorator(a=0)
... def myfunction():
...     ...
>>>
>>>
>>> myfunction()


Example
-------
>>> def translate(lang='en'):
...     TRANSLATION = {
...         'Hello': {'en': 'Hello', 'pl': 'Cześć', 'ru': 'Привет'},
...         'Goodbye': {'en': 'Goodbye', 'pl': 'Pa', 'ru': 'Пока'},
...     }
...     def decorator(func):
...         def wrapper(*args, **kwargs):
...             result = func(*args, **kwargs)
...             i18n = TRANSLATION.get(result, result)
...             return i18n.get(lang, result) if type(i18n) else i18n
...         return wrapper
...     return decorator
>>>
>>>
>>> @translate(lang='en')
... def say_hello():
...     return 'Hello'
>>>
>>> say_hello()
'Hello'
>>>
>>>
>>> @translate(lang='pl')
... def say_hello():
...     return 'Hello'
>>>
>>> say_hello()
'Cześć'


Use Case - 0x01
---------------
* Deprecated

>>> import warnings
>>>
>>>
>>> def deprecated(removed_in_version=None):
...     def decorator(func):
...         def wrapper(*args, **kwargs):
...             name = func.__name__
...             file = func.__code__.co_filename
...             line = func.__code__.co_firstlineno + 1
...             message = f'Call to deprecated function {name} in {file} at line {line}'
...             message += f'\nIt will be removed in {removed_in_version}'
...             warnings.warn(message, DeprecationWarning)
...             return func(*args, **kwargs)
...         return wrapper
...     return decorator
>>>
>>>
>>> @deprecated(removed_in_version=2.0)
... def myfunction():
...     pass
>>>
>>>
>>> myfunction()  # doctest: +SKIP
/home/python/myscript.py:11: DeprecationWarning: Call to deprecated function myfunction in /home/python/myscript.py at line 19
It will be removed in 2.0


Use Case - 0x02
---------------
* Timeout (SIGALRM)

>>> from signal import signal, alarm, SIGALRM
>>> from time import sleep
>>>
>>>
>>> def timeout(seconds=2.0, error_message='Timeout'):
...     def on_timeout(signum, frame):
...         raise TimeoutError
...
...     def decorator(func):
...         def wrapper(*args, **kwargs):
...             signal(SIGALRM, on_timeout)
...             alarm(int(seconds))
...             try:
...                 return func(*args, **kwargs)
...             except TimeoutError:
...                 print(error_message)
...             finally:
...                 alarm(0)
...         return wrapper
...     return decorator
>>>
>>>
>>> @timeout(seconds=3.0)
... def countdown(n):
...     for i in reversed(range(n)):
...         print(i)
...         sleep(1)
...     print('countdown finished')
>>>
>>>
>>> countdown(5)
4
3
2
Timeout


Use Case - 0x03
---------------
* Timeout (Timer)

>>> from _thread import interrupt_main
>>> from threading import Timer
>>> from time import sleep
>>>
>>>
>>> def timeout(seconds=2.0, error_message='Timeout'):
...     def decorator(func):
...         def wrapper(*args, **kwargs):
...             timer = Timer(seconds, interrupt_main)
...             timer.start()
...             try:
...                 result = func(*args, **kwargs)
...             except KeyboardInterrupt:
...                 raise TimeoutError(error_message)
...             finally:
...                 timer.cancel()
...             return result
...         return wrapper
...     return decorator
>>>
>>>
>>> @timeout(seconds=3.0)
... def countdown(n):
...     for i in reversed(range(n)):
...         print(i)
...         sleep(1)
...     print('countdown finished')
>>>
>>> countdown(5)  # doctest: +SKIP
4
3
2
Traceback (most recent call last):
TimeoutError: Timeout


Assignments
-----------
.. literalinclude:: assignments/decorator_arguments_a.py
    :caption: :download:`Solution <assignments/decorator_arguments_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/decorator_arguments_b.py
    :caption: :download:`Solution <assignments/decorator_arguments_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/decorator_arguments_c.py
    :caption: :download:`Solution <assignments/decorator_arguments_c.py>`
    :end-before: # Solution
