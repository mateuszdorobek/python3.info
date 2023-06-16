AsyncIO Shield
==============
* Shielding from Cancellation
* Awaitable ``asyncio.shield(aw)``
* Protect an awaitable object from being cancelled.

In Python, asyncio is a module that provides tools for writing asynchronous
code using coroutines. The ``asyncio.shield()`` function is a utility function
that is used to protect a coroutine from being cancelled.

When a coroutine is cancelled in Python, it raises a ``CancelledError ``
exception. This can be problematic if the coroutine is in the middle of
performing an important task that should not be interrupted. The asyncio
``.shield()`` function can be used to prevent the coroutine from being
cancelled until it has completed its task.

Here is an example of how to use ``asyncio.shield()``:

>>> import asyncio
>>>
>>> async def my_coroutine():
...     await asyncio.sleep(1)
...     print('Task complete')
>>>
>>> async def main():
...     task = asyncio.create_task(my_coroutine())
...     await asyncio.sleep(0.5)
...     asyncio.shield(task)
...     print('Task shielded')
>>>
>>> asyncio.run(main())
Task shielded

In this example, the ``my_coroutine`` function is a coroutine that sleeps for
1 second and then prints "Task complete!". The ``main`` function creates a
task from ``my_coroutine`` and then sleeps for 0.5 second before calling
``asyncio.shield()`` on the task. The ``print`` statement after
``asyncio.shield()`` is executed immediately, while the coroutine continues
to run in the background.

If the coroutine were to be cancelled before it completes its task, the
``asyncio.shield()`` function would prevent the cancellation from occurring
until the task is finished. This ensures that the task is completed even if
the coroutine is cancelled prematurely.


Example
-------
>>> import asyncio
>>>
>>>
>>> async def work():
...     return 'done'
>>>
>>>
>>> async def main():
...     try:
...         res = await asyncio.shield(work())
...     except asyncio.CancelledError:
...         res = None
>>>
>>>
>>> asyncio.run(main())
