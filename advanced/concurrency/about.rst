About
=====
* Latency problem - time from the user action to the appearance of the first UI element user can interact with
* General rule for frontend frameworks - don't block the foreground, let the long running operations to run in background, and leave the user interface interactive
* Concurrency and Parallelism

CPU-bound Concurrency:

    * Using Queues and Multiprocessing
    * Using Futures and Multiprocessing

I/O-bound Concurrency:

    * Using Queues and Threading
    * Using Futures and Threading

.. figure:: img/concurrency-about-techniques.png

    Source: Michael Kennedy [#Kennedy2019]_


Classification of concurrency problems
--------------------------------------
* Martelli Model of Scalability
* 1 core: Single thread and single process
* 2-8 cores: Multiple threads and multiple processes
* 9+ cores: Distributed processing

Martelli's observation: As time goes on, the second category becomes less common and relevant.
Single cores become more powerful. Big datasets grow ever larger [to use 2-8 cores].

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


Process
-------
#. Co to jest proces?
#. Ile czasu trwa tworzenie procesów?
#. Kto zarządza procesami?
#. Ile może być równoległych procesów?
#. Co to jest ``nice``
#. Jak komunikować się między procesami?

#. Procesy są w pełni niezależne między sobą.
#. Nie trzeba stawiać locków, bo nie wchodzą sobie w grę
#. Działanie jednego nie wpływa na drugi
#. Pamięć jest odseparowana
#. Wadą procesów jest brak komunikacji (dlatego potrzebne są metody IPC, np. pickle)
#. Bardzo duży koszt związany z komunikacją i serializacją


Thread
------
#. Co to jest wątek?
#. Ile czasu trwa tworzenie wątków?
#. Kto zarządza wątkami?
#. Ile może być równoległych wątków?
#. Ile wątków może być w ramach jednego procesu?
#. Jak komunikować się między wątkami?
#. Czy współdzielenie pamięci przez wątki jest dobre czy złe?

* Zaletą wątków jest to, że mają współdzielony stan
* Jeden wątek może zapisać kod do pamięci a drugi odczytać bez narzutu komunikacyjnego
* Wadą jest również współdzielony stan i race condition
* Ideą wątków jest tani dostęp do współdzielonej pamięci, tylko trzeba wszędzie wstawiać locki
* Run very fast, but hard to get correct
* It's insanely difficult to create large multi-threaded programs with multiple locks
* Even if you lock resource, there is no protection if other parts of the system do not even try to acquire the lock
* Threads switch preemptively
* Preemptively means that the thread manager decides to switch tasks for you (you don't have to explicitly say to do so). Programmer has to do very little.
* This is convenient because you don't need to add explicit code to cause a task switch
* The cost of this convenience is that you have to assume a switch can happen at any time
* Accordingly, critical sections have to be a guarded with locks
* The limit on threads is total CPU power minus the cost of tasks switches and synchronization overhead

Source: [#Hettinger2017]_


Async
-----
* Running asynchronously: 3s + 1s + 1s = bit over 3s [execution time]
* Async is the future of programming

* Objective: Maximize the usage of a single thread
* Objective: handling I/O asynchronously
* Objective: enabling concurrent code using coroutines

* Advantage: Async will fill the gaps, otherwise wasted on waiting for I/O
* Advantage: You control when tasks switches occur, so locks and other synchronization are no longer needed
* Advantage: Cost task switches is incredibly low. Calling a pure Python function has more overhead than restarting a generator or awaitable
* Advantage: Function builds stack each time it's called, whereas async uses generators underneath, which already has stack created
* Advantage: Async is the cheapest way to task switch
* Advantage: In terms of speed async servers blows threaded servers in means of thousands
* Advantage: Async is very cheap in means of resources
* Advantage: Async world has a huge ecosystem of support tools
* Advantage: Coding is easier to get right, than threads

* Disadvantage: Async switches cooperatively, so you do need to add explicit code ``yield`` or ``await`` to cause a task to switch
* Disadvantage: Everything you do need a non-blocking version (for example ``open()``)
* Disadvantage: Increased learning curve
* Disadvantage: Create event loop, acquire, crate non-blocking versions of your code
* Disadvantage: You think you know Python, there is a second half to learn (async)


Sync vs Async
-------------
.. figure:: img/asyncio-sequence-sync.png

    Source: Michael Kennedy [#Kennedy2019]_

.. figure:: img/asyncio-sequence-async.png

    Source: Michael Kennedy [#Kennedy2019]_


Threads vs Processes
--------------------
#. Czym się różnią wątki od procesów?
#. Ile może być wątków przetwarzanych równolegle na procesorze czterordzeniowym (z i bez Hyper Threading)?
#. Ile może być procesów przetwarzanych równolegle na procesorze czterordzeniowym (z i bez Hyper Threading)?
#. Jak na wątki i procesy wpływa GIL?


Threads vs Async
----------------
* Threads are about workers and async is about tasks
* Async maximizes CPU utilization because it has less overhead than threads.
* Threading typically works with existing code and tools as long as locks are added around critical sections
* For complex systems, async is much easier to get right than threads with locks
* Threads require very little tooling (locks and queues)
* Async needs a great deal of tooling (futures, event loops, and non-blocking version of just about everything.

Source: [#Hettinger2017]_


Context Switching
-----------------
* Threads, thread manager does it automatically for you
* In Async, you specify places to context switch
* Time consuming
* Za każdym razem kiedy robisz ``print()`` kod automatycznie wykonuje Context Switch


Testing
-------
* In concurrent programs (threading, multiprocessing) testing can hide bugs and errors
* Some lines of code works so fast, that it requires million runs to make errors to appear
* But if you put ``sleep()`` than errors will show up
* In Internet of Things (IoT) I'd prefer to stand in front of a car which has code written in async way, than a threaded way
* Async is profoundly easier to debug and get it right

Source: [#Hettinger2017]_


Rules
-----
#. If step A and B must be run sequentially, put them in the same thread
#. If there is several parallel threads launched and you want to be sure that all are complete, just ``join()`` all of the threads. It's called "barrier". Example: Several programmers make improvements to the website, they has to merge their work, before releasing website to the public.
#. Daemon thread is a service worker, a task which never suppose to finish (by infinite loop). Instead you ``join()`` on the queue itself. It waits until all the requested tasks are marked as being done. Example: a printer sits in the office, it waits for documents, when document arrives, printer prints it, and wait for another job, printer never finish
#. Sometimes you need global variable to communicate between functions (this is the reason behind the threading).
#. In single threaded programs global variables works
#. In multi-threaded programs, mutable global state is a disaster. The better solution is to uses a ``threading.local()`` that is global WITHIN a thread but not without (thread has local copy of this variable). Example: ``decimal.Decimal`` has this.
#. Never try to kill a thread from something external to that thread. You never know if that thread is holding a lock. Python doesn't provide direct mechanism for kill threads externally; however, you can do it using ctypes, but that is a recipe for a deadlock.
#. Reason for threads is a shared state. When you have shared state, you've got race conditions. And you manage this race conditions through a locks. You acquire a lock, do stuff and release. What if you get killed, between acquire and release. You never know if this thread acquired a lock. If you kill it, it will become a deadlock for all other threads. That's the reason why there is no API for killing a thread.
#. For large systems when you need to isolate parts of the running code, use processes, because you can kill them.

Source: [#Hettinger2017]_


References
----------
.. [#Hettinger2017] Hettinger, Raymond. Keynote on Concurrency. PyBay 2017. https://youtu.be/9zinZmE3Ogk?t=1243

.. [#Kennedy2019] Kennedy, M. Demystifying Python's Async and Await Keywords. Publisher: JetBrainsTV. Year: 2019. Retrieved: 2022-03-10. URL: https://www.youtube.com/watch?v=F19R_M4Nay4
