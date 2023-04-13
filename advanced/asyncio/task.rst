AsyncIO Task
============
* ``asyncio.create_task(coro, *, name=None)``
* Tasks are used to schedule coroutines concurrently
* Wrap the ``coro`` coroutine into a ``Task`` and schedule its execution
* ``Task`` can be used to cancel execution
* ``Task`` can be awaited until it is complete
* The task is executed in the loop returned by ``get_running_loop()``
* ``RuntimeError`` is raised if there is no running loop in current thread
* Tasks are used to run coroutines in event loops
* If a coroutine awaits on a Future, the Task suspends the execution of the coroutine and waits for the completion of the Future
* When the Future is done, the execution of the wrapped coroutine resumes
* Manual instantiation of ``Tasks`` is discouraged
* Use the high-level ``asyncio.create_task()`` function to create Tasks

Tasks are used to run coroutines in event loops. If a coroutine awaits on a
Future, the Task suspends the execution of the coroutine and waits for the
completion of the Future. When the Future is done, the execution of the
wrapped coroutine resumes.

Event loops use cooperative scheduling: an event loop runs one Task at a
time. While a Task awaits for the completion of a Future, the event loop
runs other Tasks, callbacks, or performs IO operations.

Use the high-level asyncio.create_task() function to create Tasks, or the
low-level loop.create_task() or ensure_future() functions. Manual
instantiation of Tasks is discouraged.


SetUp
-----
>>> import asyncio


Example
-------
>>> async def work():
...     return 'done'
>>>
>>>
>>> async def main():
...     task = asyncio.create_task(work())
...     result = await task
...     print(result)
>>>
>>>
>>> asyncio.run(main())
done


Example
-------
>>> async def a():
...     print('a: started')
...     await asyncio.sleep(1)
...     print('a: finished')
...     return 'a'
>>>
>>> async def b():
...     print('b: started')
...     await asyncio.sleep(0.5)
...     print('b: finished')
...     return 'b'
>>>
>>> async def c():
...     print('c: started')
...     await asyncio.sleep(1.5)
...     print('c: finished')
...     return 'c'
>>>
>>>
>>> async def main():
...     t1 = asyncio.create_task(a())
...     t2 = asyncio.create_task(b())
...     t3 = asyncio.create_task(c())
...     await t1
...     await t2
...     await t3
>>>
>>>
>>> asyncio.run(main())
a: started
b: started
c: started
b: finished
a: finished
c: finished


Selected Task Methods
---------------------
* class ``asyncio.Task(coro, *, loop=None, name=None)`` - A Future-like object that runs a Python coroutine. Not thread-safe.
* method ``asyncio.Task.cancel(msg=None)`` - Request the Task to be cancelled. This arranges for a ``CancelledError`` exception to be thrown into the wrapped coroutine on the next cycle of the event loop.
* method ``asyncio.Task.cancelled()`` - Return ``True`` if the ``Task`` is cancelled.
* method ``asyncio.Task.done()`` - Return ``True`` if the ``Task`` is done.
* method ``asyncio.Task.result()`` - Return the result of the ``Task``. If the result isn't yet available, raise ``InvalidStateError``.
* method ``asyncio.Task.exception()`` - Return the exception of the ``Task``
* method ``asyncio.Task.add_done_callback(callback, *, context=None)`` - Add a callback to be run when the ``Task`` is done.
* method ``asyncio.Task.remove_done_callback(callback)`` - Remove callback from the callbacks list.
* method ``asyncio.Task.set_name(value)`` - Set the name of the ``Task``.
* method ``asyncio.Task.get_name()`` - Return the name of the ``Task``.


Introspection
-------------
* ``asyncio.current_task(loop=None)`` - Return the currently running Task instance, or None if no task is running.
* ``asyncio.all_tasks(loop=None)`` -  Return a set of not yet finished Task objects run by the loop.
* If loop is ``None``, ``get_running_loop()`` is used for getting current loop.
