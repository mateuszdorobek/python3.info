Threading Synchronization
=========================
* Thread Synchronisation


.. figure:: img/threading-synchronization-lock-1.png

    Source: Langa, Ł. import asyncio: Learn Python's AsyncIO [#Langa2020]_

.. figure:: img/threading-synchronization-lock-2.png

    Source: Langa, Ł. import asyncio: Learn Python's AsyncIO [#Langa2020]_

.. figure:: img/threading-synchronization-lock-3.png

    Source: Langa, Ł. import asyncio: Learn Python's AsyncIO [#Langa2020]_


Problems
--------
* Lock Contention - when there is a shared resource which is wanted by many threads very often. Most of the threads will wait for access to that resource
* Lock Starvation - some threads are more lucky to get more access than the others. There are even some threads which didn't get a lock at all!
* Deadlock - You cannot access a lock to get a resource, because you haven't acquired a resource in the first place (example: the pharmacy won't sell you mask, because you are not wearing a mask)
* The more lock, the slower your program is and more memory it uses

.. figure:: img/threading-synchronization.png

    Source: Langa, Ł. import asyncio: Learn Python's AsyncIO [#Langa2020]_


Locks
-----
* Locks don't lock anything. They are just flags and can be ignored. It is a cooperative tool, not an enforced tool
* IIn general, locks should be considered a low level primitive that is difficult to reason about nontrivial examples. For more complex applications, you're almost always better of with using atomic message queues.
* The more locks you acquire at one time, the more you loose the advantages of concurrency

Source: [#Hettinger2017]_


GIL
---
* Global Interpreter Lock
* CPython has a lock for its internal shared global state
* One lock instead of hundreds smaller
* The unfortunate effect of GIL is that no more than one thread can run at a time
* For I/O bound applications, GIL doesn't present much of an issue
* For CPU bound applications, using threads makes the application speed worse
* Accordingly, that drives us to multiprocessing to gain more CPU cycles
* Larry Hastings, Gilectomy project - removed GIL, but Python slowed down

Source: [#Hettinger2017]_

.. figure:: img/threading-gil.png

    Source: Michael Kennedy [#Kennedy2019]_


Thread Local Storage
--------------------
* Operating system mechanism
* Limits global variables to be seen only by current thread
* You can keep data around, which are specifically not shared with other threads


Example
-------
.. code-block:: python

    from threading import Thread


    class MyThread(Thread):
        def run(self):
            print('hello')


    t1 = MyThread()
    t1.start()

    t2 = MyThread()
    t2.start()

    t1.join()
    t2.join()

.. code-block:: python

    from threading import Thread

    RUNNING = []


    class MyThread(Thread):
        def run(self):
            print('hello')


    t1 = MyThread()
    t1.start()
    RUNNING.append(t1)

    t2 = MyThread()
    t2.start()
    RUNNING.append(t2)

    for thread in RUNNING:
        thread.join()

.. code-block:: python

    from threading import Thread

    RUNNING = []


    class MyThread(Thread):
        def run(self):
            print('hello')


    def spawn(cls, count=1):
        for i in range(count):
            t = cls()
            t.start()
            RUNNING.append(t)


    spawn(MyThread, count=10)


    for thread in RUNNING:
        thread.join()


References
----------
.. [#Kennedy2019] Kennedy, M. Demystifying Python's Async and Await Keywords. Publisher: JetBrainsTV. Year: 2019. Retrieved: 2022-03-10. URL: https://www.youtube.com/watch?v=F19R_M4Nay4

.. [#Hettinger2017] Hettinger, Raymond. Keynote on Concurrency. PyBay 2017. https://youtu.be/9zinZmE3Ogk?t=1243

.. [#Langa2020] Langa, Ł. import asyncio: Learn Python's AsyncIO. Year: 2020. Retrieved: 2022-03-10. URL: https://www.youtube.com/playlist?list=PLhNSoGM2ik6SIkVGXWBwerucXjgP1rHmB
