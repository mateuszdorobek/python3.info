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

In Python, a coroutine is a special type of function that allows for
asynchronous programming. Coroutines are defined using the ``async def``
syntax and can be paused and resumed at specific points using the ``await``
keyword.

When a coroutine is called, it returns a coroutine object, which is a type
of generator object. The coroutine object can be used to control the
execution of the coroutine, allowing it to be paused and resumed at specific
points.

Here is an example of a simple coroutine in Python:

>>> async def my_coroutine():
...     print("Coroutine started.")
...     await asyncio.sleep(0.5)
...     print("Coroutine resumed.")
...     await asyncio.sleep(1.0)
...     print("Coroutine complete.")

In this example, the ``my_coroutine`` function is defined using the
``async def`` syntax. It prints a message, sleeps for 0.5 second using
the ``await`` keyword and the ``asyncio.sleep()`` function, prints another
message, sleeps for an additional 1.0 seconds using the ``await`` keyword
and the ``asyncio.sleep()`` function, and then prints a final message.

To call the coroutine, you can use the ``await`` keyword:

>>> await my_coroutine()  # doctest: +SKIP

When the coroutine is called using ``await``, it will execute until it reaches
the first ``await`` statement, which will pause the coroutine and return
control to the event loop. The event loop will then continue to run other
coroutines until the first ``await`` statement has completed its task. The
coroutine will then resume from where it left off until it reaches the
second ``await`` statement, and so on.

Coroutines are a powerful tool for writing asynchronous code in Python,
allowing for efficient and scalable programs that can handle multiple tasks
simultaneously.


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
