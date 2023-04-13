SQLite3 Connect
===============
* File database - persistent storage
* In-memory - very fast, but volatile
* sqlite3.connect() -> connection
* connection.close()


In-Memory Database
------------------
* Useful for tests, development and demonstrations
* Very fast (do not write any data to disk)
* Remember to close connection

Connection to in-memory database:

>>> import sqlite3
>>>
>>>
>>> db = sqlite3.connect(':memory:')
>>> db.close()


File Database
-------------
* Connection will create file if not exists
* Remember to close connection

Connection to database file:

>>> import sqlite3
>>>
>>>
>>> db = sqlite3.connect('/tmp/database.sqlite3')
>>> db.close()


Context Managers
----------------
* Prefer using context manager
* No need to remember about closing connection
* Prepare your data and statements before connection
* Works with either in-memory or file database

>>> import sqlite3
>>>
>>>
>>> DATABASE = ':memory:'
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     pass


Debug
-----
* ``conn.set_trace_callback(print)``
* Registers trace_callback to be called for each SQL statement that is actually executed by the SQLite backend.
* The only argument passed to the callback is the statement (as string) that is being executed.

>>> import sqlite3
>>>
>>>
>>> DATABASE = ':memory:'
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     db.set_trace_callback(print)
