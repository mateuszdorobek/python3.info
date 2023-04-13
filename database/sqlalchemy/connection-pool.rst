Connection Pool
===============
* Establishing a new database connection is time consuming
* Connection Pool - a collection of connections, which lives longer than requests
* Establish several connections at the beginning
* Add them to the so called 'connection pool'
* Use them for request processing
* After request is process the connection is returned to the pool

Normally the database connection would be established as soon as the request
comes in and would thrive until disconnection on request processing end.
Establishing a new database connection involves in three-way handshake (for
TCP/IP connections) which can take a lot of time. Having connections which
lives longer than requests improves performance. Trick here is to establish
several parallel connections at the beginning, add them to the so called
'connection pool' and add use them for request processing. As soon as
request does not need the connection it releases it back to the pool.

A connection pool is a standard technique used to maintain long running
connections in memory for efficient re-use, as well as to provide management
for the total number of connections an application might use simultaneously.
Particularly for server-side web applications, a connection pool is the
standard way to maintain a 'pool' of active database connections in memory
which are reused across requests. [#sqlalchemyDocPooling]_

SQLAlchemy includes several connection pool implementations which integrate
with the ``Engine``. They can also be used directly for applications that
want to add pooling to an otherwise plain DBAPI approach.
[#sqlalchemyDocPooling]_


Usage
-----
The Engine returned by the ``create_engine()`` function in most cases has a
``QueuePool`` integrated, pre-configured with reasonable pooling defaults:

>>> from sqlalchemy import create_engine
>>>
>>>
>>> DATABASE = 'postgresql://myusername:mypassword@myhost:5432/mydatabase'
>>>
>>> engine = create_engine(DATABASE, pool_size=20, max_overflow=0)

Note, that SQLite 'memory' databases maintain their entire dataset within
the scope of a single connection.

All SQLAlchemy pool implementations have in common that none of them
'pre create' connections - all implementations wait until first use before
creating a connection.

This is why it's perfectly fine for ``create_engine()`` to default to using
a ``QueuePool`` of size five without regard to whether or not the
application really needs five connections queued up - the pool would only
grow to that size if the application actually used five connections
concurrently, in which case the usage of a small pool is an entirely
appropriate default behavior. [#sqlalchemyDocPooling]_


Parameters
----------
* ``echo_pool=False``
* ``max_overflow=10``
* ``pool=None``
* ``poolclass=None``
* ``pool_logging_name``
* ``pool_pre_ping=True``
* ``pool_recycle=-1``
* ``pool_reset_on_return='rollback'``
* ``pool_size=5``
* ``pool_timeout=30``
* ``pool_use_lifo=False``

``echo_pool=False``
    If ``True``, the connection pool will log informational output such as
    when connections are invalidated as well as when connections are
    recycled to the default log handler, which defaults to ``sys.stdout``
    for output. If set to the string "debug", the logging will include pool
    checkouts and checkins. Direct control of logging is also available
    using the standard Python logging module.

``max_overflow=10``
    The number of connections to allow in connection pool "overflow", that
    is connections that can be opened above and beyond the pool_size
    setting, which defaults to five. this is only used with ``QueuePool``.

``pool=None``
    An already-constructed instance of ``Pool``, such as a ``QueuePool``
    instance. If non-None, this pool will be used directly as the underlying
    connection pool for the engine, bypassing whatever connection parameters
    are present in the URL argument. For information on constructing
    connection pools manually.

``poolclass=None``
    A ``Pool`` subclass, which will be used to create a connection pool
    instance using the connection parameters given in the URL. Note this
    differs from pool in that you don't actually instantiate the pool in
    this case, you just indicate what type of pool to be used.

``pool_logging_name``
    String identifier which will be used within the "name" field of logging
    records generated within the ``sqlalchemy.pool`` logger. Defaults to a
    hexstring of the object's id.

``pool_pre_ping=True``
    Boolean, if ``True`` will enable the connection pool "pre-ping" feature
    that tests connections for liveness upon each checkout.

``pool_recycle=-1``
    This setting causes the pool to recycle connections after the given
    number of seconds has passed. It defaults to -1, or no timeout. For
    example, setting to 3600 means connections will be recycled after one
    hour. Note that MySQL in particular will disconnect automatically if no
    activity is detected on a connection for eight hours (although this is
    configurable with the MySQLDB connection itself and the server
    configuration as well).

``pool_reset_on_return='rollback'``
    Set the ``Pool.reset_on_return`` parameter of the underlying Pool
    object, which can be set to the values ``"rollback"``, ``"commit"``, or
    ``None``.

``pool_size=5``
    The number of connections to keep open inside the connection pool. This
    used with ``QueuePool`` as well as ``SingletonThreadPool``. With
    ``QueuePool``, a pool_size setting of 0 indicates no limit; to disable
    pooling, set ``poolclass=NullPool`` instead.

``pool_timeout=30``
    Number of seconds to wait before giving up on getting a connection from
    the pool. This is only used with ``QueuePool``. This can be a float but
    is subject to the limitations of Python time functions which may not be
    reliable in the tens of milliseconds.

``pool_use_lifo=False``
    if ``True`` causes the pool's "queue" behavior to instead be
    that of a "stack", e.g. the last connection to be returned to the pool
    is the first one to be used on the next request. In contrast to the
    pool's long- standing behavior of first-in-first-out, which produces a
    round-robin effect of using each connection in the pool in series, lifo
    mode allows excess connections to remain idle in the pool, allowing
    server-side timeout schemes to close these connections out. Using LIFO,
    a server-side timeout scheme can reduce the number of connections used
    during non- peak periods of use. When planning for server-side
    timeouts, ensure that a recycle or pre-ping strategy is in use to
    gracefully handle stale connections.


Pool Implementations
--------------------
The ``poolclass`` argument accepts a class imported from the
``sqlalchemy.pool`` module. Example pools are as follows:

``AssertionPool``
    Pool that allows at most one checked out connection at any given time.

``NullPool``
    Pool which does not pool connections.

``QueuePool``
    Pool that imposes a limit on the number of open connections.

``SingletonThreadPool``
    Pool that maintains one connection per thread.

``StaticPool``
    Pool of exactly one connection, used for all requests.

Usage:

>>> from sqlalchemy.pool import QueuePool
>>>
>>>
>>> engine = create_engine(DATABASE, poolclass=QueuePool)


Keep Alive
----------
The connection pool has the ability to refresh individual connections as
well as its entire set of connections, setting the previously pooled
connections as 'invalid'. A common use case is allow the connection pool to
gracefully recover when the database server has been restarted, and all
previously established connections are no longer functional. There are two
approaches to this: pessimistic and optimistic [#sqlalchemyDocPooling]_.

The pessimistic approach refers to emitting a test statement on the SQL
connection at the start of each connection pool checkout, to test that the
database connection is still viable. Typically, this is a simple statement
like ``SELECT 1``, but may also make use of some DBAPI-specific method to
test the connection for liveness. The approach adds a small bit of overhead
to the connection checkout process, however is otherwise the most simple and
reliable approach to completely eliminating database errors due to stale
pooled connections. The calling application does not need to be concerned
about organizing operations to be able to recover from stale connections
checked out from the pool. It is critical to note that the pre-ping approach
does not accommodate for connections dropped in the middle of transactions
or other SQL operations. If the database becomes unavailable while a
transaction is in progress, the transaction will be lost and the database
error will be raised [#sqlalchemyDocPooling]_.

>>> engine = create_engine(DATABASE, pool_pre_ping=True)

The 'pre ping' feature will normally emit SQL equivalent to ``SELECT 1``
each time a connection is checked out from the pool; if an error is raised
that is detected as a 'disconnect' situation, the connection will be
immediately recycled, and all other pooled connections older than the
current time are invalidated, so that the next time they are checked out,
they will also be recycled before use. This statement is not logged in the
SQL echo output, and will not show up in SQLAlchemy's engine logging
[#sqlalchemyDocPooling]_.

When pessimistic handling is not employed, as well as when the database is
shutdown and/or restarted in the middle of a connection's period of use
within a transaction, the other approach to dealing with stale / closed
connections is to let SQLAlchemy handle disconnects as they occur, at which
point all connections in the pool are invalidated, meaning they are assumed
to be stale and will be refreshed upon next checkout. This behavior assumes
the Pool is used in conjunction with a Engine. The Engine has logic which
can detect disconnection events and refresh the pool automatically. When the
Connection attempts to use a DBAPI connection, and an exception is raised
that corresponds to a 'disconnect' event, the connection is invalidated. The
Connection then calls the ``Pool.recreate()`` method, effectively
invalidating all connections not currently checked out so that they are
replaced with new ones upon next checkout [#sqlalchemyDocPooling]_.

An additional setting that can augment the 'optimistic' approach is to set
the pool recycle parameter. This parameter prevents the pool from using a
particular connection that has passed a certain age, and is appropriate for
database backends such as MySQL that automatically close connections that
have been stale after a particular period of time [#sqlalchemyDocPooling]_:

>>> engine = create_engine(DATABASE, pool_recycle=3600)

Above, any DBAPI connection that has been open for more than one hour will
be invalidated and replaced, upon next checkout. Note that the invalidation
only occurs during checkout [#sqlalchemyDocPooling]_.


Further Reading
---------------
* http://docs.sqlalchemy.org/en/latest/core/pooling.html


References
----------
.. [#sqlalchemyDocPooling] http://docs.sqlalchemy.org/en/latest/core/pooling.html
