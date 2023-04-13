AsyncIO Run
===========
* ``asyncio.run()`` is a main entrypoint
* ``asyncio.gather()`` can run concurrently and gather result (in order of its arguments)


SetUp
-----
>>> import asyncio
>>>
>>>


Run Coroutine
-------------
* ``asyncio.run(coro, *, debug=False)``
* Execute the coroutine ``coro`` and return the result
* Takes care of managing the asyncio event loop, finalizing asynchronous generators, and closing the threadpool
* Cannot be called when another asyncio event loop is running in the same thread
* Always creates a new event loop and closes it at the end
* It should be used as a main entry point for asyncio programs, and should ideally only be called once

>>> async def hello():
...     print('hello')
>>>
>>>
>>> asyncio.run(hello())
hello


Run Sequentially
----------------
>>> async def hello():
...     print('hello')
>>>
>>>
>>> async def main():
...     await hello()
...     await hello()
...     await hello()
>>>
>>>
>>> asyncio.run(main())
hello
hello
hello


Run Concurrently
----------------
* awaitable ``asyncio.gather(*aws, return_exceptions=False)``
* Run awaitable objects in the ``aws`` sequence concurrently
* If any awaitable in ``aws`` is a coroutine, it is automatically scheduled as a ``Task``
* If all awaitables are completed successfully, the result is an aggregate list of returned values
* The order of result values corresponds to the order of awaitables in ``aws``
* ``return_exceptions=False`` (default): the first raised exception is immediately propagated to the task that awaits on ``gather()``; other awaitables in the ``aws`` sequence won't be cancelled and will continue to run
* ``return_exceptions=True``: exceptions are treated the same as successful results, and aggregated in the result list
* If ``gather()`` is cancelled (ie. on timeout), all submitted awaitables (that have not completed yet) are also cancelled
* If any ``Task`` or ``Future`` from the ``aws`` sequence is cancelled, it is treated as if it raised ``CancelledError`` – the ``gather()`` call is not cancelled in this case
* This is to prevent the cancellation of one submitted Task/Future to cause other Tasks/Futures to be cancelled

>>> async def a():
...     print('a: started')
...     await asyncio.sleep(0.2)
...     print('a: finished')
...     return 'a'
>>>
>>> async def b():
...     print('b: started')
...     await asyncio.sleep(0.1)
...     print('b: finished')
...     return 'b'
>>>
>>> async def c():
...     print('c: started')
...     await asyncio.sleep(0.3)
...     print('c: finished')
...     return 'c'
>>>
>>>
>>> async def main():
...     result = await asyncio.gather(a(), b(), c())
...     print(f'Result: {result}')
>>>
>>>
>>> asyncio.run(main())
a: started
b: started
c: started
b: finished
a: finished
c: finished
Result: ['a', 'b', 'c']


Run as Completed
----------------
* ``asyncio.as_completed(aws, *, timeout=None)``
* Run awaitable objects in the ``aws`` iterable concurrently
* Return an iterator of coroutines
* Each coroutine returned can be awaited to get the earliest next result from the iterable of the remaining awaitables
* Raises ``asyncio.TimeoutError`` if the timeout occurs before all Futures are done

>>> async def a():
...     print('a: started')
...     await asyncio.sleep(0.2)
...     print('a: finished')
...     return 'a'
>>>
>>> async def b():
...     print('b: started')
...     await asyncio.sleep(0.1)
...     print('b: finished')
...     return 'b'
>>>
>>> async def c():
...     print('c: started')
...     await asyncio.sleep(0.3)
...     print('c: finished')
...     return 'c'
>>>
>>>
>>> async def main():
...     todo = [a(), b(), c()]
...     for coro in asyncio.as_completed(todo):
...         result = await coro
...         print(result)
>>>
>>>
>>> asyncio.run(main())  # doctest: +SKIP
a: started
c: started
b: started
b: finished
b
a: finished
a
c: finished
c


Run in Threads
--------------
* coroutine ``asyncio.to_thread(func, /, *args, **kwargs)``
* Asynchronously run function func in a separate thread.
* Any ``*args`` and ``**kwargs`` supplied for this function are directly passed to func.
* Return a coroutine that can be awaited to get the eventual result of func.
* This coroutine function is intended to be used for executing IO-bound functions/methods that would otherwise block the event loop if they were ran in the main thread.

>>> import asyncio
>>> import time
>>>
>>>
>>> def work():
...     print(f'Work started {time.strftime("%X")}')
...     time.sleep(2)  # Blocking
...     print(f'Work done at {time.strftime("%X")}')
>>>
>>>
>>> async def main():
...     print(f'Started main at {time.strftime("%X")}')
...     await asyncio.gather(
...         asyncio.to_thread(work),
...         asyncio.sleep(1))
...     print(f'Finished main at {time.strftime("%X")}')
>>>
>>>
>>> asyncio.run(main())  # doctest: +SKIP
Started main at 22:53:40
Work started 22:53:40
Work done at 22:53:42
Finished main at 22:53:42

Due to the GIL, ``asyncio.to_thread()`` can typically only be used to make
IO-bound functions non-blocking. However, for extension modules that
release the GIL or alternative Python implementations that don't have one,
``asyncio.to_thread()`` can also be used for CPU-bound functions.
