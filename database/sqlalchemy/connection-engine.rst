Connection Engine
=================
* ``create_engine()`` builds a factory for database connections
* ``create_engine()`` uses Database Source Name (DSN) for configuration
* ``echo=True`` - if True, the Engine will log all statements to stdout
* ``future=True`` - v2.0 compatibility mode (works only in v1.4)
* Engine is lazily connected
* Engine object supports context managers ``with`` block
* ``engine.connect()`` method explicitly connects to the database


Glossary
--------
.. glossary::

    engine
        Provides a facade over the Python DBAPI. Used to create a lazy
        connection to the database.


Create Engine
-------------
Function ``create_engine()`` builds a factory for database connections. It
supports Database Source Name (DSN). In the following example we will
create a database connection factory to SQLite3 database using Python
builtin driver. The database works in memory, so it will not create any
files. Note that the connection is lazy, and creating an engine does not
implies connection to the database.

>>> from sqlalchemy import create_engine
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE)


Parameters
----------
* ``echo=True`` - if True, the Engine will log all statements to stdout
* ``future=True`` - v2.0 compatibility mode (works only in v1.4)
* Full List [#saDocsCreateEngine]_


2.x Style
---------
>>> from sqlalchemy import create_engine
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE)
>>>
>>> type(engine)
<class 'sqlalchemy.engine.base.Engine'>


Establishing Connection
-----------------------
Engine is lazily connected and does not connect on creating engine right
away. It does that in last possible moment (such as attribute access) or
on explicit ``.connect()`` method call.

>>> from sqlalchemy import create_engine
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE, future=True)
>>>
>>> with engine.connect() as db:
...     pass


Example
-------
>>> from sqlalchemy import create_engine
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE)
>>>
>>> with engine.connect() as db:
...     result = db.execute('SELECT * FROM users')  # doctest: +SKIP


Show Parameters
---------------
>>> from sqlalchemy import create_engine
>>>
>>>
>>> DATABASE = 'postgresql+psycopg2://mwatney:nasa@localhost:5432/ares3?charset=utf8'
>>>
>>> engine = create_engine(DATABASE)
>>> args, kwargs = engine.dialect.create_connect_args(engine.url)
>>>
>>> args
[]
>>>
>>> kwargs  # doctest: +NORMALIZE_WHITESPACE
{'host': 'localhost',
 'dbname': 'ares3',
 'user': 'mwatney',
 'password': 'nasa',
 'port': 5432,
 'charset': 'utf8'}


Further Reading
---------------
* https://docs.sqlalchemy.org/en/stable/core/engines.html#sqlalchemy.create_engine.params.connect_args


References
----------
.. [#saDocsCreateEngine]
   Author: SQLAlchemy authors and contributors.
   Title: Engine Creation API.
   Year: 2022.
   Retrieved: 2022-02-22.
   URL: https://docs.sqlalchemy.org/en/stable/core/engines.html#sqlalchemy.create_engine.params.connect_args
