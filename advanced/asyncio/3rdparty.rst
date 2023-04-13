AsyncIO 3rd Party
=================


Unsync
------
* Library decides which to run, thread, asyncio or sync

.. code-block:: console

    $ pip install unsync

.. code-block:: python

    @unsync
    def my_function():
        pass


Twisted
-------
* Old project

.. code-block:: console

    $ pip install twisted


Gevent
------
* Actively maintained
* Greenlets (micro-threads running inside one thread)

.. code-block:: console

    $ pip install gevent


Tornado
-------
* Actively maintained
* Web framework and asynchronous networking library
* Open-sourced by Facebook after acquisition of FriendFeed


Curio
-----
* Coroutine-based library for concurrent Python systems programming
* Provides standard programming abstractions such as tasks, sockets, files, locks and queues
* Works on POSIX and Windows


Trio
----
* Python library for async concurrency and I/O
* Focussed on usability and correctness
* Introduced nursery (task groups)


UVLoop
------
* The ultimate loop implementation for UNIXes (run this on production)

.. code-block:: console

    $ pip install uvloop

>>> # doctest: +SKIP
... import uvloop
...
... uvloop.install()
...
... loop = asyncio.new_event_loop()
... loop
<uvloop.Loop running=False closed=False debug=False>
