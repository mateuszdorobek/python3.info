AsyncIO Sleep
=============
* Coroutine ``asyncio.sleep(delay, result=None)``
* Delay can be int or float
* Block for delay seconds.
* If result is provided, it is returned to the caller when the coroutine completes
* Delay is not guaranteed
* It means that this is at least X number of seconds
* This us due, that after that time of delay, there might still be an other function running
* This does not interrupt or preempt

The ``asyncio.sleep()`` function is a utility function that is used to pause
a coroutine for a specified amount of time.

The ``asyncio.sleep()`` function is similar to the ``time.sleep()`` function
in Python's standard library, but it is designed for use with asynchronous
code. When a coroutine calls asyncio.sleep(), it yields control to the event
loop, allowing other coroutines to run while it is paused.

Here is an example of how to use ``asyncio.sleep()``:

>>> import asyncio
>>>
>>> async def my_coroutine():
...     print("Coroutine started.")
...     await asyncio.sleep(0.5)
...     print("Coroutine resumed.")
...     await asyncio.sleep(1.0)
...     print("Coroutine complete.")
>>>
>>> asyncio.run(my_coroutine())
Coroutine started.
Coroutine resumed.
Coroutine complete.

In this example, the ``my_coroutine`` function is a coroutine that prints a
message, sleeps for 0.5 second using ``asyncio.sleep()``, prints another
message, sleeps for an additional 1.0 second using ``asyncio.sleep()``,
and then prints a final message.

When the program is run, the ``my_coroutine`` function is executed using
``asyncio.run()``. The first message is printed immediately, followed
by a pause of 0.5 seconds. After the pause, the second message is printed,
followed by another pause of 1.0 seconds. Finally, the third message is
printed, and the coroutine is complete.

The ``asyncio.sleep()`` function is a useful tool for implementing asynchronous
code in Python. It allows coroutines to pause for a specified amount of time
without blocking the event loop, allowing other coroutines to run in the
meantime.


Example
-------
>>> import asyncio
>>>
>>>
>>> async def main():
...     result = await asyncio.sleep(0.5, 'done')
...     print(result)
>>>
>>>
>>> asyncio.run(main())
done
