AsyncIO Debug
=============
* By default asyncio runs in production mode
* Asyncio has a debug mode which can be enabled
* More verbose message you can achieve by using ``PYTHONASYNCIODEBUG=1`` and ``PYTHONTRACEMALLOC=1`` environment variables
* Also ``python3 -X dev -X tracemalloc=5 myfile.py``


Debug
-----
* By default asyncio runs in production mode
* Asyncio has a debug mode which can be enabled

.. code-block:: console

    $ PYTHONMALLOC=debug PYTHONASYNCIODEBUG=1 python3 -X dev -X tracemalloc=5 myfile.py

Asyncio has a debug mode which can be enabled by:

    * Setting the ``PYTHONASYNCIODEBUG`` environment variable to 1.
    * Using the Python Development Mode.
    * Passing ``debug=True`` to ``asyncio.run()``.
    * Calling ``loop.set_debug()``.

In addition to enabling the debug mode, consider also:

    * setting the log level of the asyncio logger to ``logging.basicConfig(level=logging.DEBUG)``
    * configuring the warnings module to display ``ResourceWarning`` warnings. One way of doing that is by using the ``-W`` default command line option.

When the debug mode is enabled:

    * ``asyncio`` checks for coroutines that were not awaited and logs them; this mitigates the 'forgotten await' pitfall.
    * Many non-threadsafe asyncio APIs (such as ``loop.call_soon()`` and ``loop.call_at()`` methods) raise an exception if they are called from a wrong thread.
    * The execution time of the I/O selector is logged if it takes too long to perform an I/O operation.
    * Callbacks taking longer than 100ms are logged.
    * The ``loop.slow_callback_duration`` attribute can be used to set the minimum execution duration in seconds that is considered 'slow'.


Introspection
-------------
* ``asyncio.current_task(loop=None)`` - Return the currently running Task instance, or None if no task is running.
* ``asyncio.all_tasks(loop=None)`` -  Return a set of not yet finished Task objects run by the loop.
* If loop is ``None``, ``get_running_loop()`` is used for getting current loop.


Further Reading
---------------
* https://docs.python.org/3/library/devmode.html
* https://docs.python.org/3/library/asyncio-dev.html#debug-mode
