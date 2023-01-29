Connection DSN
==============
* DSN - Database Source Name
* Format: ``db://user:password@host:port/database?opt1=val1&opt2=val2``
* :rfc:`1738` -- Uniform Resource Locators (URL) [#RFC1738]_

Different database drivers use different connection parameters (arguments to
the ``.connect()`` method. SQLAlchemy uses consistent URL format (DSN) known
from JDBC or ODBC connections.


Data Source Name
----------------
* the name of the data source
* the location of the data source
* the name of a database driver which can access the data source
* a user ID for data access (if required)
* a user password for data access (if required)

.. glossary::

    DSN
    Data Source Name
    Database Source Name
        A string that has an associated data structure used to describe a
        connection to a data source [#wikipediaDataSourceName]_

Most commonly used in connection with ODBC, DSNs also exist for JDBC and for
other data access mechanisms. The term often overlaps with "connection
string". Most systems do not make a distinction between DSNs or connection
strings and the term can often be used interchangeably
[#wikipediaDataSourceName]_.

DSN attributes may include, but are not limited to:

    * the name of the data source
    * the location of the data source
    * the name of a database driver which can access the data source
    * a user ID for data access (if required)
    * a user password for data access (if required)

The system administrator of a client machine generally creates a separate
DSN for each relevant data source.

Example:

>>> DATABASE = 'postgresql://myusername:mypassword@myhost:5432/mydatabase'


SQLite3
-------
* https://docs.sqlalchemy.org/en/stable/dialects/sqlite.html
* Supported versions 3.12+
* In-memory mode
* File mode

Drivers:

    * `pysqlite <https://docs.python.org/library/sqlite3.html>`_ (same driver as the Python sqlite3 stdlib module)
    * `aiosqlite <https://pypi.org/project/aiosqlite/>`_
    * `pysqlcipher <https://pypi.org/project/sqlcipher3/>`_ (no longer maintained)

In-memory database does not store on disk (useful for tests):

>>> DATABASE = 'sqlite:///'
>>> DATABASE = 'sqlite:///:memory:'
>>> DATABASE = 'sqlite+pysqlite:///:memory:'

File connection using relative path (note 3 slashes):

>>> DATABASE = 'sqlite:///myfile.db'
>>> DATABASE = 'sqlite+pysqlite:///myfile.db'

File connection using absolute path (note 4 slashes for unix, backslash for Windows):

>>> DATABASE = 'sqlite:////path/to/myfile.db'
>>> DATABASE = 'sqlite:///C:\\path\\to\\myfile.db'

Modern versions of SQLite support an alternative system of connecting using a
driver level URI, which has the advantage that additional driver-level
arguments can be passed including options such as 'read only'. The SQLite-level
'URI' is kept as the 'database' portion of the SQLAlchemy url (that is,
following a slash):

>>> DATABASE = 'sqlite:///file:path/to/myfile.db?uri=true&mode=ro'
>>> DATABASE = 'sqlite:///file:path/to/myfile.db?uri=true&mode=ro&check_same_thread=true&timeout=10&nolock=1'

Aiosqlite:

>>> DATABASE = 'sqlite+aiosqlite:///myfile.db'

.. note:: Async connections require ``create_async_engine``

SQLite does not have built-in DATE, TIME, or DATETIME types, and pysqlite
does not provide out of the box functionality for translating values
between Python datetime objects and a SQLite-supported format.


PostgreSQL
----------
* https://docs.sqlalchemy.org/en/stable/dialects/postgresql.html
* Supported versions 9.6+

Drivers:

    * `psycopg2 <https://pypi.org/project/psycopg2/>`_ (recommended)
    * `pg8000 <https://pypi.org/project/pg8000/>`_
    * `asyncpg <https://magicstack.github.io/asyncpg/>`_
    * `psycopg2cffi <https://pypi.org/project/psycopg2cffi/>`_
    * `py-postgresql <https://python.projects.pgfoundry.org/>`_ (deprecated, not tested in CI/CD)
    * `pygresql <https://www.pygresql.org/>`_ (deprecated, not tested in CI/CD)

Default driver:

>>> DATABASE = 'postgresql://myusername:mypassword@myhost:5432/mydatabase'

Psycopg2 using TCP/IP:

>>> DATABASE = 'postgresql+psycopg2://myusername:mypassword@myhost:5432/mydatabase'
>>> DATABASE = 'postgresql+psycopg2://myusername:mypassword@myhost:5432/mydatabase?sslmode=require'
>>> DATABASE = 'postgresql+psycopg2://'  # use PG_... environment variables for connections

Psycopg2 using Unix socket:

>>> DATABASE = 'postgresql+psycopg2://myusername:mypassword@/mydatabase'  # by default socket in /tmp
>>> DATABASE = 'postgresql+psycopg2://myusername:mypassword@/mydatabase?host=/var/lib/postgresql' # specify socket location
>>> DATABASE = 'postgresql+psycopg2://myusername:mypassword@/mydatabase?host=HostA:port1&host=HostB&host=HostC'  # fallback hosts

Pg8000 driver:

>>> DATABASE = 'postgresql+pg8000://myusername:mypassword@myhost:5432/mydatabase'

PostgreSQL async [#sqlalchemyPostgresql]_, [#githubAsyncpg]_:

>>> DATABASE = 'postgresql+asyncpg://myusername:mypassword@myhost:5432/mydatabase'
>>> DATABASE = 'postgresql+asyncpg://myusername:mypassword@myhost:5432/mydatabase?async_fallback=true'
>>> DATABASE = 'postgresql+asyncpg://myusername:mypassword@myhost:5432/mydatabase?prepared_statement_cache_size=500'
>>> DATABASE = 'postgresql+asyncpg://myusername:mypassword@myhost:5432/mydatabase?prepared_statement_cache_size=0'

.. note:: Async connections require ``create_async_engine``

Psycopg2cffi (implemented with cffi layer for portability):

>>> DATABASE = 'postgresql+psycopg2cffi://myusername:mypasswordword@myhost:5432/mydatabase'


MySQL and MariaDB
-----------------
* https://docs.sqlalchemy.org/en/stable/dialects/mysql.html
* MariaDB is an open-source fork of MySQL (after it was bought by Oracle)
* SQLAlchemy supports MySQL and all modern versions of MariaDB
* Minimum MySQL version supported is now 5.0.2

Drivers:

    * `mysqlclient <https://pypi.org/project/mysqlclient/>`_ (recommended)
    * `PyMySQL <https://pymysql.readthedocs.io/>`_ (recommended)
    * `mysqlconnector <https://pypi.org/project/mysql-connector-python/>`_ (not tested in CI/CD)
    * `asyncmy <https://github.com/long2ice/asyncmy>`_ (new)
    * `aiomysql <https://github.com/aio-libs/aiomysql>`_ (unmaintained, not tested in CI/CD)
    * `CyMySQL <https://github.com/nakagami/CyMySQL>`_ (not tested in CI/CD)
    * `OurSQL <https://packages.python.org/oursql/>`_ (deprecated)
    * `PyODBC <https://pypi.org/project/pyodbc/>`_ (not tested in CI/CD)

MySQL connection:

>>> DATABASE = 'mysql://myusername:mypassword@myhost:3306/mydatabase'

MySQL connection using PyMSQL driver:

>>> DATABASE = 'mysql+pymysql://myusername:mypassword@myhost/mydatabase:3306?charset=utf8mb4'

The MariaDB variant of MySQL retains fundamental compatibility with MySQL's
protocols however the development of these two products continues to diverge
To connect to a MariaDB database, no changes to the database URL are
required:

>>> DATABASE = 'mysql+pymysql://myusername:mypassword@myhost/mydatabase:3306?charset=utf8mb4'

Upon first connect, the SQLAlchemy dialect employs a server version
detection scheme that determines if the backing database reports as
MariaDB. Based on this flag, the dialect can make different choices in
those of areas where its behavior must be different.

MariaDB-Only Mode:

>>> DATABASE = 'mariadb+pymysql://myusername:mypassword@myhost/mydatabase:3306?charset=utf8mb4'

MySQL connection using mysqldb driver:

>>> DATABASE = 'mysql+mysqldb://myusername:mypassword@myhost/mydatabase:3306?charset=utf8mb4&binary_prefix=true'

>>> DATABASE = (
...     'mysql+mysqldb://myusername:mypassword@myhost:3306/mydatabase'
...     '?ssl_ca=/home/myusername/client-ssl/ca.pem'
...     '&ssl_cert=/home/myusername/client-ssl/client-cert.pem'
...     '&ssl_key=/home/myusername/client-ssl/client-key.pem'
... )

>>> DATABASE = (
...     'mysql+pymysql://myusername:mypassword@myhost:3306/mydatabase'
...     '?ssl_ca=/home/myusername/client-ssl/ca.pem'
...     '&ssl_cert=/home/myusername/client-ssl/client-cert.pem'
...     '&ssl_key=/home/myusername/client-ssl/client-key.pem'
...     '&ssl_check_hostname=false'
... )

With Google Cloud SQL:

>>> DATABASE = 'mysql+mysqldb://root@/mydatabase?unix_socket=/cloudsql/<projectid>:<instancename>'

Asyncmy:

>>> DATABASE = 'mysql+asyncmy://myusername:mypassword@myhost:3306/mydatabase?charset=utf8mb4'

.. note:: Async connections require ``create_async_engine``


Oracle
------
* https://docs.sqlalchemy.org/en/stable/dialects/oracle.html
* Supported versions 11+

Drivers:

    * cx-Oracle (recommended)

Default driver connection:

>>> DATABASE = 'oracle://myusername:mypassword@myhost:1521/mydatabase'

Cx-Oracle driver connection:

>>> DATABASE = 'oracle+cx_oracle://myusername:mypassword@myhost'
>>> DATABASE = 'oracle+cx_oracle://myusername:mypassword@myhost:1521/mydatabase'
>>> DATABASE = 'oracle+cx_oracle://myusername:mypassword@myhost:1521/?encoding=UTF-8&nencoding=UTF-8'
>>> DATABASE = 'oracle+cx_oracle://myusername:mypassword@myhost:1521/?encoding=UTF-8&nencoding=UTF-8&service_name=myservice'
>>> DATABASE = 'oracle+cx_oracle://myusername:mypassword@myhost:1521/?encoding=UTF-8&nencoding=UTF-8&mode=SYSDBA&events=true'
>>> DATABASE = 'oracle+cx_oracle://myusername:mypassword@myhost:1521/mydatabase?encoding=UTF-8&nencoding=UTF-8'


MSSQL
-----
* https://docs.sqlalchemy.org/en/stable/dialects/mssql.html
* Supported versions 2012+
* pymssql is currently not included in SQLAlchemy's continuous integration (CI) testing.

Drivers:

    * `PyODBC <https://pypi.org/project/pyodbc/>`_ (recommended)
    * `mxODBC <https://www.egenix.com/>`_ (deprecated)
    * `pymssql <http://www.pymssql.org>`_ (not tested in CI/CD)

PyODBC:

>>> DATABASE = 'mssql+pyodbc://myusername:mypassword@myhost'
>>> DATABASE = 'mssql+pyodbc://myusername:mypassword@myhost?driver=ODBC+Driver+13+for+SQL+Server;'
>>> DATABASE = 'mssql+pyodbc://myusername:mypassword@myhost:49242/mydatabase?driver=ODBC+Driver+17+for+SQL+Server'
>>> DATABASE = 'mssql+pyodbc://myusername:mypassword@myhost:49242/mydatabase?driver=ODBC+Driver+17+for+SQL+Server&authentication=ActiveDirectoryIntegrated'

PyMSSQL:

>>> DATABASE = 'mssql+pymssql://myusername:mypassword@myhost/mydatabase'
>>> DATABASE = 'mssql+pymssql://myhost'


URL Create
----------
>>> from sqlalchemy.engine import URL
>>>
>>>
>>> DATABASE = URL.create(
...     drivername='mssql+pyodbc',
...     username='myusername',
...     password='mypassword',
...     host='myhost',
...     port=49242,
...     database='mydatabase',
...     query={
...         'driver': 'ODBC Driver 17 for SQL Server',
...         'authentication': 'ActiveDirectoryIntegrated',
...     },
... )
>>>
>>> print(DATABASE)
mssql+pyodbc://myusername:***@myhost:49242/mydatabase?authentication=ActiveDirectoryIntegrated&driver=ODBC+Driver+17+for+SQL+Server


Good Practice
-------------
* Split configuration parameter from its call
* Place configuration in separate file which can be imported


References
----------
.. [#sqlalchemyPostgresql] https://docs.sqlalchemy.org/en/stable/dialects/postgresql.html
.. [#githubAsyncpg] https://magicstack.github.io/asyncpg/
.. [#wikipediaDataSourceName] https://en.wikipedia.org/wiki/Data_source_name
.. [#RFC1738] Berners-Lee, T. Uniform Resource Locators (URL). Year: 1994. Retrieved: 2022-02-22. URL: https://datatracker.ietf.org/doc/html/rfc1738
