AsyncIO Wait For
================
* ``asyncio.wait_for(aw, timeout: int|float|None)``
* Timeout - number of seconds to wait for
* If ``timeout=None``, block until the future completes
* ``wait_for()`` - when a timeout occurs: cancels the task and raises ``asyncio.TimeoutError``
* If aw is a coroutine it is automatically scheduled as a Task
* If the wait is cancelled, the future ``aw`` is also cancelled.


SetUp
-----
>>> import asyncio


Wait For
--------
* The function will wait until the future is actually cancelled
* Therefore the total wait time may exceed the timeout
* If an exception happens during cancellation, it is propagated
* If coroutine does not finish by then, rises ``TimeoutError``


>>> SECOND = 1
>>> MINUTE = 60 * SECOND
>>>
>>>
>>> async def hello():
...     while True:
...         print('hello')
...         await asyncio.sleep(MINUTE)
>>>
>>>
>>> async def main():
...     await asyncio.wait_for(hello(), SECOND)
>>>
>>>
>>> asyncio.run(main())  # doctest: +SKIP
waiting
waiting
waiting
asyncio.exceptions.CancelledError
<BLANKLINE>
During handling of the above exception, another exception occurred:
<BLANKLINE>
asyncio.exceptions.CancelledError
<BLANKLINE>
The above exception was the direct cause of the following exception:
<BLANKLINE>
asyncio.exceptions.TimeoutError


Handling Timeouts
-----------------
>>> SECOND = 1
>>> MINUTE = 60 * SECOND
>>>
>>>
>>> async def hello():
...     while True:
...         print('hello')
...         await asyncio.sleep(MINUTE)
>>>
>>>
>>> async def main():
...     try:
...         await asyncio.wait_for(hello(), SECOND)
...     except asyncio.TimeoutError:
...         print('Timeout')
>>>
>>>
>>> asyncio.run(main())
hello
Timeout


Handling Timeouts Concurrently
------------------------------
>>> SECOND = 1
>>> MINUTE = 60 * SECOND
>>>
>>>
>>> async def hello():
...     print('hello')
...     await asyncio.sleep(MINUTE)
>>>
>>>
>>> async def main():
...     todo = asyncio.gather(hello(), hello(), hello())
...     try:
...         await asyncio.wait_for(todo, timeout=SECOND)
...     except asyncio.TimeoutError:
...         print('Timeout')
>>>
>>>
>>> asyncio.run(main())
hello
hello
hello
Timeout


Handling Cancellation
---------------------
* If ``gather()`` is cancelled (ie. on timeout), all submitted awaitables (that have not completed yet) are also cancelled

>>> SECOND = 1
>>> MINUTE = 60 * SECOND
>>>
>>>
>>> async def hello():
...     print('hello')
...     try:
...         await asyncio.sleep(MINUTE)
...     except asyncio.CancelledError:
...         print('Cancelled')
>>>
>>>
>>> async def main():
...     todo = asyncio.gather(hello(), hello(), hello())
...     try:
...         await asyncio.wait_for(todo, timeout=SECOND)
...     except asyncio.TimeoutError:
...         print('Timeout')
>>>
>>>
>>> asyncio.run(main())
hello
hello
hello
Cancelled
Cancelled
Cancelled
Timeout



Further Reading
---------------
* Langa Ł. How Exception Groups Will Improve Error Handling in AsyncIO [#Langa2022]_


References
----------
.. [#Langa2022] Langa Ł. How Exception Groups Will Improve Error Handling in AsyncIO. Year: 2022. Retrieved: 2022-03-18. URL: https://www.youtube.com/watch?v=Lfe2zsGS0Js
