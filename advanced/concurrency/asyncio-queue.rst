AsyncIO Queue
=============


Rationale
---------
* ``asyncio`` queues are designed to be similar to classes of the ``queue`` module.
* Although ``asyncio`` queues are not thread-safe, they are designed to be used specifically in async/await code.
* Note that methods of asyncio queues don't have a timeout parameter; use`` asyncio.wait_for()`` function to do queue operations with a timeout.


FIFO Queue
----------
* FIFO Queue - First In, First Out
* class ``asyncio.Queue(maxsize=0)``
* If maxsize is less than or equal to zero, the queue size is infinite.
* Unlike the standard library threading queue, the size of the queue is always known and can be returned by calling the qsize() method.
* ``maxsize`` - Number of items allowed in the queue.
* ``empty()`` - Return True if the queue is empty, False otherwise.
* ``full()`` - Return True if there are maxsize items in the queue.
* coroutine ``get()`` - Remove and return an item from the queue. If queue is empty, wait until an item is available.
* ``get_nowait()`` - Return an item if one is immediately available, else raise QueueEmpty.
* coroutine ``join()`` - Block until all items in the queue have been received and processed.
* coroutine ``put(item)`` - Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
* ``put_nowait(item)`` - Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
* ``qsize()`` - Return the number of items in the queue.
* ``task_done()`` - Indicate that a formerly enqueued task is complete.


Priority Queue
--------------
* class ``asyncio.PriorityQueue``
* Retrieves entries in priority order (lowest first).
* Entries are typically tuples of the form (priority_number, data).


LIFO Queue
----------
* LIFO Queue - Last In, First Out
* class ``asyncio.LifoQueue``
* Retrieves most recently added entries first.


Exceptions
----------
* exception ``asyncio.QueueEmpty`` - Raised when ``get_nowait()`` method is called on an empty queue.
* exception ``asyncio.QueueFull`` - Raised when ``put_nowait()`` method is called on a queue that has reached its maxsize.


Example
-------
.. code-block:: python

    import asyncio
    import random
    import time


    async def worker(name, queue):
        while True:
            # Get a "work item" out of the queue.
            sleep_for = await queue.get()

            # Sleep for the "sleep_for" seconds.
            await asyncio.sleep(sleep_for)

            # Notify the queue that the "work item" has been processed.
            queue.task_done()

            print(f'{name} has slept for {sleep_for:.2f} seconds')


    async def main():
        # Create a queue that we will use to store our "workload".
        queue = asyncio.Queue()

        # Generate random timings and put them into the queue.
        total_sleep_time = 0
        for _ in range(20):
            sleep_for = random.uniform(0.05, 1.0)
            total_sleep_time += sleep_for
            queue.put_nowait(sleep_for)

        # Create three worker tasks to process the queue concurrently.
        tasks = []
        for i in range(3):
            task = asyncio.create_task(worker(f'worker-{i}', queue))
            tasks.append(task)

        # Wait until the queue is fully processed.
        started_at = time.monotonic()
        await queue.join()
        total_slept_for = time.monotonic() - started_at

        # Cancel our worker tasks.
        for task in tasks:
            task.cancel()
        # Wait until all worker tasks are cancelled.
        await asyncio.gather(*tasks, return_exceptions=True)

        print('====')
        print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
        print(f'total expected sleep time: {total_sleep_time:.2f} seconds')


    asyncio.run(main())
    # worker-0 has slept for 0.26 seconds
    # worker-0 has slept for 0.41 seconds
    # worker-1 has slept for 0.89 seconds
    # worker-2 has slept for 0.98 seconds
    # worker-0 has slept for 0.59 seconds
    # worker-0 has slept for 0.09 seconds
    # worker-0 has slept for 0.11 seconds
    # worker-2 has slept for 0.53 seconds
    # worker-1 has slept for 0.91 seconds
    # worker-1 has slept for 0.21 seconds
    # worker-0 has slept for 0.87 seconds
    # worker-2 has slept for 0.86 seconds
    # worker-2 has slept for 0.11 seconds
    # worker-2 has slept for 0.23 seconds
    # worker-0 has slept for 0.53 seconds
    # worker-1 has slept for 0.89 seconds
    # worker-0 has slept for 0.53 seconds
    # worker-0 has slept for 0.10 seconds
    # worker-2 has slept for 0.86 seconds
    # worker-1 has slept for 0.82 seconds
    # ====
    # 3 workers slept in parallel for 3.74 seconds
    # total expected sleep time: 10.79 seconds
