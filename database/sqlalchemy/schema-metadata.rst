.. testsetup::

    # doctest: +SKIP_FILE


Schema Metadata
===============


Use Case - 0x01
---------------
>>> from sqlalchemy import MetaData
>>> from sqlalchemy import Table, Column
>>> from sqlalchemy import Integer, String
>>> from sqlalchemy import select
>>>
>>>
>>> metadata = MetaData()
>>>
>>> users = Table('users', metadata,
...     Column('id', Integer, primary_key=True),
...     Column('firstname', String(50), nullable=False),
...     Column('lastname', String(50), nullable=False),
... )

>>> users  # doctest: +NORMALIZE_WHITESPACE
Table('users', MetaData(), Column('id', Integer(), table=<users>,
      primary_key=True, nullable=False), Column('firstname', String(length=50),
      table=<users>, nullable=False), Column('lastname', String(length=50),
      table=<users>, nullable=False), schema=None)

>>> users.name
'users'
>>>
>>> users.primary_key
PrimaryKeyConstraint(Column('id', Integer(), table=<users>, primary_key=True, nullable=False))

Associative array of columns. Bit looking like a dict, but not quite.

>>> users.c  # doctest: +ELLIPSIS
<sqlalchemy.sql.base.ImmutableColumnCollection object at 0x...>

>>> users.c.values()  # doctest: +NORMALIZE_WHITESPACE
[Column('id', Integer(), table=<users>, primary_key=True, nullable=False),
 Column('firstname', String(length=50), table=<users>, nullable=False),
 Column('lastname', String(length=50), table=<users>, nullable=False)]

You can query each column separately about all metadata:

>>> users.c.firstname
Column('firstname', String(length=50), table=<users>, nullable=False)
>>>
>>> users.c.firstname.name
'firstname'
>>>
>>> users.c.firstname.type
String(length=50)

Table metadata is used to generate SQL statements:

>>> print(select(users))
SELECT users.id, users.firstname, users.lastname
FROM users


Schema Generation
-----------------
Table and MetaData objects can be used to generate a schema in database;
MetaData features the ``create_all()`` method. [#ytSQLAlchemy20]_

>>> from sqlalchemy import create_engine
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE)
>>>
>>> with engine.begin() as db:
...     metadata.create_all(db)


Use Case - 0x01
---------------
* SQLite does not have Enums

>>> from sqlalchemy import MetaData
>>> from sqlalchemy import create_engine
>>> from sqlalchemy import Table, Column
>>> from sqlalchemy import Integer, String, Date, Numeric, Enum
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE)
>>> metadata = MetaData()
>>>
>>> astronaut = Table('astronaut', metadata,
...     Column('id', Integer, primary_key=True),
...     Column('firstname', String(50), nullable=False),
...     Column('lastname', String(50), nullable=False),
...     Column('born', Date),
...     Column('height', Integer),
...     Column('weight', Numeric(3,2)),
...     Column('agency', Enum('NASA', 'ESA', 'POLSA')),
... )
>>>
>>>
>>> with engine.begin() as db:
...     astronaut.create(db)
>>>
>>>
>>> metadata.tables.keys()
dict_keys(['astronaut'])
>>>
>>> metadata.tables['astronaut']  # doctest: +NORMALIZE_WHITESPACE
Table('astronaut', MetaData(),
      Column('id', Integer(), table=<astronaut>, primary_key=True, nullable=False),
      Column('firstname', String(length=50), table=<astronaut>, nullable=False),
      Column('lastname', String(length=50), table=<astronaut>, nullable=False),
      Column('born', Date(), table=<astronaut>),
      Column('height', Integer(), table=<astronaut>),
      Column('weight', Numeric(precision=3, scale=2), table=<astronaut>),
      Column('agency', Enum('NASA', 'ESA', 'POLSA'), table=<astronaut>), schema=None)


Use Case - 0x02
---------------
Table metadata also allows for constraints and indexes. ``ForeignKey``
is used to link one column to a remote primary key. Note we can omit
the datatype for a ``ForeignKey`` column [#ytSQLAlchemy20]_.

>>> from sqlalchemy import MetaData
>>> from sqlalchemy import create_engine
>>> from sqlalchemy import Table, Column
>>> from sqlalchemy import Integer, String, Date, Numeric, Enum, ForeignKey
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE)
>>> metadata = MetaData()
>>>
>>> astronauts = Table('astronauts', metadata,
...     Column('id', Integer, primary_key=True),
...     Column('firstname', String(50), nullable=False),
...     Column('lastname', String(50), nullable=False),
...     Column('born', Date),
...     Column('height', Integer),
...     Column('weight', Numeric(3,2)),
...     Column('agency', Enum('NASA', 'ESA', 'POLSA')),
... )
>>>
>>> missions = Table('missions', metadata,
...     Column('id', Integer, primary_key=True),
...     Column('astronaut_id', ForeignKey('astronauts.id'), nullable=False),
...     Column('year', Integer, nullable=False),
...     Column('name', String(100), nullable=False),
... )
>>>
>>>
>>> with engine.begin() as db:
...     astronauts.create(db)
...     missions.create(db)


Use Case - 0x03
---------------
``ForeignKey`` is a shortcut for ``ForeignKeyConstraint`` which should be
used for composite references. [#ytSQLAlchemy20]_

>>> from sqlalchemy import ForeignKeyConstraint
>>> from sqlalchemy import Table, Column
>>> from sqlalchemy import Text, Integer, String, Date
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE)
>>> metadata = MetaData()
>>>
>>> story_table = Table('story', metadata,
...     Column('story_id', Integer, primary_key=True),
...     Column('version_id', Integer, primary_key=True),
...     Column('headline', String(100), nullable=False),
...     Column('body', Text),
... )
>>>
>>> published_table = Table('published', metadata,
...     Column('pub_id', Integer, primary_key=True),
...     Column('pub_timestamp', Date, nullable=True),
...     Column('story_id', Integer),
...     Column('version_id', Integer),
...     ForeignKeyConstraint(
...         ['story_id', 'version_id'],
...         ['story.story_id', 'story.version_id'],
...     ),
... )

``create_all()`` by default checks for tables existing already.

>>> with engine.begin() as db:
...     metadata.create_all(db)


References
----------
.. [#ytSQLAlchemy20] Bayer, Mike. SQLAlchemy 2.0 - The One-Point-Four-Ening 2021. Year: 2022. Retrieved: 2022-01-26. URL: https://www.youtube.com/watch?v=1Va493SMTcY
