AsyncIO Coroutine
=================
* Coroutine function and coroutine object are two different things
* Coroutine function is the definition (``async def``)
* Coroutine function will create coroutine when called
* This is similar to generator object and generator function
* Coroutine functions are not awaitables
* Coroutine objects are awaitables
* Coroutines declared with the ``async``/``await`` syntax is the preferred way of writing asyncio applications. [#pydocAsyncioTask]_
* https://peps.python.org/pep-0492/

Syntax
------
>>> async def hello():
...     return 'hello'
>>>
>>>
>>> type(hello)
<class 'function'>
>>>
>>> type(hello())
<class 'coroutine'>


SetUp
-----
>>> import asyncio


Coroutine Function
------------------
* Coroutine function is the definition (``async def``)
* Also known as async functions
* Defined by putting ``async`` in front of the ``def``
* Only a coroutine function (``async def``) can use ``await``
* Non-coroutine functions (``def``) cannot use ``await``
* Coroutine functions are not awaitables

Calling a coroutine function does not execute it, but rather returns a
coroutine object. This is analogous to generator functions - calling them
doesn't execute the function, it returns a generator object, which we then
use later.

>>> async def hello():
...     return 'hello'


Coroutine Object
----------------
* Coroutine function will create coroutine when called
* Coroutine objects are awaitables
* To execute coroutine object you can ``await`` it
* To execute coroutine object you can ``asyncio.run()``
* To schedule coroutine object: ``ensure_future()`` or ``create_task()``

To execute a coroutine object, either:

* use it in an expression with ``await`` in front of it, or
* use ``asyncio.run()``, or
* schedule it with ``ensure_future()`` or ``create_task()``.

>>> async def hello():
...     return 'hello'
>>>
>>>
>>> asyncio.run(hello())
'hello'


Run Sequentially
----------------
* All lines inside of coroutine function will be executed sequentially

>>> async def hello():
...     await asyncio.sleep(0.1)
...     return 'hello'
>>>
>>>
>>> asyncio.run(hello())
'hello'

All lines inside of coroutine function will be executed sequentially. When
``await`` happen, other coroutine will start running. When other coroutine
finishes, it returns to our function. Then next line is executed (which
could also be an ``await`` statement:

>>> async def hello():
...     await asyncio.sleep(0.1)
...     await asyncio.sleep(0.1)
...     await asyncio.sleep(0.1)
...     return 'hello'
>>>
>>>
>>> asyncio.run(hello())
'hello'


Run Concurrently
----------------
* To run coroutine objects use ``asyncio.gather()``
* This won't execute in parallel (won't use multiple threads)
* It will run concurrently (in a single thread)

>>> async def hello():
...     await asyncio.sleep(0.1)
>>>
>>> async def main():
...     await asyncio.gather(
...         hello(),
...         hello(),
...         hello(),
...     )
>>>
>>> asyncio.run(main())

.. figure:: img/asyncio-coroutine-concurrency.gif

    Only one hammer is hitting the pole in the same time,
    however the work continues to be done concurrently.
    This is faster than one worker with one hammer.
    Source [#imgHammertime]_


Error: Created but not awaited
------------------------------
* Created but not awaited objects will raise an exception
* This prevents from creating coroutines and forgetting to "await" on it


Error: Running Coroutine Functions
----------------------------------
* Only coroutine objects can be run
* It is not possible to run coroutine function

>>> def hello():
...     return 'hello'
>>>
>>>
>>> asyncio.run(hello)  # doctest: +ELLIPSIS
Traceback (most recent call last):
ValueError: a coroutine was expected, got <function hello at 0x...>


Error: Multiple Awaiting
------------------------
* Coroutine object can only be awaited once

>>> async def hello():
...     return 'hello'
>>>
>>>
>>> coro = hello()
>>>
>>> asyncio.run(coro)
'hello'
>>>
>>> asyncio.run(coro)
Traceback (most recent call last):
RuntimeError: cannot reuse already awaited coroutine


Error: Await Outside Coroutine Function
---------------------------------------
* Only a coroutine function (``async def``) can use ``await``
* Non-coroutine functions (``def``) cannot use ``await``

>>> def hello():
...     await asyncio.sleep(0.1)
...     return 'hello'
...
Traceback (most recent call last):
SyntaxError: 'await' outside async function


Getting Results
---------------
>>> async def hello():
...     await asyncio.sleep(0.1)
...     return 'hello'
>>>
>>>
>>> async def main():
...     return await hello()
>>>
>>>
>>> asyncio.run(main())
'hello'

>>> async def hello():
...     await asyncio.sleep(0.1)
...     return 'hello'
>>>
>>> async def main():
...     return await asyncio.gather(
...         hello(),
...         hello(),
...         hello(),
...     )
>>>
>>> asyncio.run(main())
['hello', 'hello', 'hello']

Inspect
-------
>>> from inspect import isawaitable
>>>
>>>
>>> async def hello():
...     return 'hello'
>>>
>>>
>>> isawaitable(hello)
False
>>>
>>> isawaitable(hello())
True
>>>
>>>
>>> type(hello)
<class 'function'>
>>>
>>> type(hello())
<class 'coroutine'>


References
----------
.. [#imgHammertime] Orboloops3. Forever Hammer Time. Year: 2014. Retrieved: 2022-03-17. URL: https://imgur.com/gallery/pIDs2ff

.. [#pydocAsyncioTask] Python3 Documentation. Coroutines and Tasks. Year: 2022. Retrieved: 2022-03-17. URL: https://docs.python.org/3/library/asyncio-task.html
