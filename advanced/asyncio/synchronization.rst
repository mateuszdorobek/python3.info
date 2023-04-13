AsyncIO Synchronization
=======================
* Synchronization Primitives
* Mutex Lock
* Condition Object
* Semaphore
* Event


Mutex Lock
----------
* Class ``asyncio.Lock()``
* Can be used to guarantee exclusive access to a shared resource
* Not thread-safe.

.. code-block:: python

    lock = asyncio.Lock()

    async with lock:
        # access shared state


Condition Object
----------------
* class ``asyncio.Condition(lock=None)``
* Not thread-safe.

.. code-block:: python

    cond = asyncio.Condition()

    async with cond:
        await cond.wait()


Semaphore
---------
* class ``asyncio.Semaphore(value=1)``
* Manages an internal counter which is decremented by each ``acquire()`` call and incremented by each ``release()`` call.
* The counter can never go below zero.
* When ``acquire()`` finds that it is zero, it blocks, waiting until some task calls ``release()``.

.. code-block:: python

    sem = asyncio.Semaphore(10)

    async with sem:
        # work with shared resource


Event
-----
* class ``asyncio.Event()``
* Can be used to notify multiple asyncio tasks that some event has happened.
* coroutine ``wait()`` - Wait until the event is set. If the event is set, return ``True`` immediately. Otherwise block until another task calls ``set()``.
* ``set()`` - Set the event. All tasks waiting for event to be set will be immediately awakened.
* ``clear()`` - Clear (unset) the event. Tasks awaiting on ``wait()`` will now block until the ``set()`` method is called again.
* ``is_set()`` - Return ``True`` if the event is set.

.. code-block:: python

    import asyncio


    async def listener(event):
        print(f'Waiting for event')
        await event.wait()
        print(f'Event processed')


    async def main():
        myevent = asyncio.Event()

        # Spawn a Task to wait until 'event' is set.
        handler = asyncio.create_task(listener(myevent))

        # Sleep for 1 second and set the event.
        await asyncio.sleep(1)
        myevent.set()

        # Wait until processing is complete
        await handler


    asyncio.run(main())
    # Waiting for event
    # Event processed
