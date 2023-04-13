SQLite3 About
=============
* The most popular database in the world
* File database with
* Open Source (Public Domain license), written in C
* It is only 699 KiB
* Supports for SQL-92 standard (Postgres flavor)
* SQLite3 is built in in Python
* It is used by mobile apps on iOS, Android, etc.
* Almost every app has it's own sqlite3 database
* Almost every web browser (on desktop) uses SQLite3 database
* https://sqlitebrowser.org/


Limits
------
* Maximum database size: 281 terabytes
* Maximum number of rows in a table: 2**64 (1.8e+19)
* Maximum number of columns in a table: 2000
* Maximum Number Of Tables In A Schema: 2147483646 (a little over 2 billion)
* Maximum BLOB size: 2147483647 (2**31 - 1)
* Maximum bytes of SQL statement: 1,000,000,000
* Maximum tables in a join: 64 tables
* Maximum number of arguments on a function: 127
* Maximum number of terms in a compound select statement: 500
* Maximum length of a LIKE or GLOB pattern: 50000
* Only partially provides triggers
* Cannot write to views
* https://sqlite.org/limits.html


Installation
------------
1. Download from https://sqlite.org/download.html
2. Extract archive
3. Add ``sqlite`` executable to ``PATH``:

    * Linux, macOS, etc:
      move ``sqlite`` executable to ``/usr/local/bin/``

    * Windows (proper way):
      Add folder with extracted ``sqlite`` executable to ``%path%``
      directory by following instruction [#pybookinstall]_

    * Windows (simple way):
      If you have GIT installed, move ``sqlite`` executable
      to ``C:\Program Files\Git\cmd``


Verification
------------
To check if Sqlite3 is already installed run in Console/Terminal/CMD:

.. code-block:: console

    $ sqlite3 --version


DB API v2
---------
.. code-block:: python

    sqlite3.connect(...) -> connection
    connection.execute(...) -> result
    connection.executemany(...) -> list[result]
    connection.fetchmany(...) -> list[result]
    connection.fetchone(...) -> result
    connection.cursor(...) -> cursor
    connection.commit(...)
    connection.close()


Command-line interface
----------------------
* New in version 3.12

The sqlite3 module can be invoked as a script in order to provide a simple
SQLite shell. Type .quit or CTRL-D to exit the shell.

.. code-block:: text

    -h, --help
    Print CLI help.

    -v, --version
    Print underlying SQLite library version.



References
----------
.. [#pybookinstall] https://python3.info/install.html
