.. testsetup::

    # doctest: +SKIP_FILE


Schema Reflection
=================
* SQLAlchemy allows for database reflection

SQLAlchemy tool ``Automap`` does the reflection of database and figures out
how to do the mapping dynamically.

There is third-party tool ``sqlacodegen`` that generates the files (Python
code) for you based on introspected tables. This is more robust solution.

.. glossary::

    Reflection
        Loading Table objects based on reading from an existing database.


Reflection
----------
"Reflection" refers to loading Table objects based on reading from an
existing database. In order to create a reflection, first create empty
metadata object:

>>> metadata2 = MetaData()

And then use it to introspect the database table:

>>> with engine.connect() as db:
...     astronauts = Table('astronauts', metadata2, autoload_with=db)

The reflected object is filled in with all the columns and constraints and is
ready to use.

>>> print(astronauts.c)  # doctest: +ELLIPSIS
<sqlalchemy.sql.base.ImmutableColumnCollection object at 0x...>

>>> print(astronauts.primary_key)
PrimaryKeyConstraint(Column('id', INTEGER(), table=<astronaut>, primary_key=True, nullable=False))

>>> print(select(astronauts))
SELECT astronaut.id, astronaut.firstname, astronaut.lastname, astronaut.born, astronaut.height, astronaut.weight, astronaut.agency
FROM astronaut


Inspection
----------
Information about a database at a more specific level is available using the
``Inspector`` object. Inspector will work with an engine or a connection.
[#ytSQLAlchemy20]_

First import the inspector:

>>> from sqlalchemy import inspect

Attach it to the engine:

>>> inspector = inspect(engine)

You can query the database to get all tables:

>>> inspector.get_table_names()
['astronaut']

Or get information about columns:

>>> inspector.get_columns('astronaut')  # doctest: +NORMALIZE_WHITESPACE
[{'name': 'id', 'type': INTEGER(), 'nullable': False, 'default': None, 'autoincrement': 'auto', 'primary_key': 1},
 {'name': 'firstname', 'type': VARCHAR(length=50), 'nullable': False, 'default': None, 'autoincrement': 'auto', 'primary_key': 0},
 {'name': 'lastname', 'type': VARCHAR(length=50), 'nullable': False, 'default': None, 'autoincrement': 'auto', 'primary_key': 0},
 {'name': 'born', 'type': DATE(), 'nullable': True, 'default': None, 'autoincrement': 'auto', 'primary_key': 0},
 {'name': 'height', 'type': INTEGER(), 'nullable': True, 'default': None, 'autoincrement': 'auto', 'primary_key': 0},
 {'name': 'weight', 'type': NUMERIC(precision=3, scale=2), 'nullable': True, 'default': None, 'autoincrement': 'auto', 'primary_key': 0},
 {'name': 'agency', 'type': VARCHAR(length=9), 'nullable': True, 'default': None, 'autoincrement': 'auto', 'primary_key': 0}]

Or constraints:

>>> inspector.get_foreign_keys('astronaut')
[]

Currently supported constraints:

    * FOREIGNKEY
    * UNIQUE
    * CHECK

Currently not supported:

    * Functional Indexes (PostgreSQL)
    * EXCLUDE (PostgreSQL)


Reflecting an Entire Schema
---------------------------
The ``MetaData`` object also includes a feature that will reflect all the
tables in particular schema at once. [#ytSQLAlchemy20]_

>>> metadata3 = MetaData()
>>>
>>> with engine.connect() as db:
...     metadata3.reflect(db)

Note, that this will produce a lot of database queries. The Tables objects
are then in the metadata.tables collection:

>>> metadata3.tables  # doctest: +NORMALIZE_WHITESPACE
FacadeDict({
    'published': Table('published', MetaData(),
                    Column('pub_id', INTEGER(), table=<published>, primary_key=True, nullable=False),
                    Column('pub_timestamp', Date(), table=<published>),
                    Column('story_id', INTEGER(), ForeignKey('story.story_id'), table=<published>),
                    Column('version_id', INTEGER(), ForeignKey('story.version_id'), table=<published>), schema=None),
    'story': Table('story', MetaData(),
                    Column('story_id', INTEGER(), table=<story>, primary_key=True, nullable=False),
                    Column('version_id', INTEGER(), table=<story>, primary_key=True, nullable=False),
                    Column('headline', VARCHAR(length=100), table=<story>, nullable=False),
                    Column('body', TEXT(), table=<story>), schema=None),
    'users': Table('users', MetaData(),
                    Column('uid', INTEGER(), table=<users>, primary_key=True, nullable=False),
                    Column('firstname', VARCHAR(), table=<users>, nullable=False),
                    Column('lastname', VARCHAR(), table=<users>, nullable=False), schema=None)})

>>> story = metadata3.tables['story']
>>> published = metadata3.tables['published']

>>> story  # doctest: +NORMALIZE_WHITESPACE
Table('story', MetaData(),
      Column('story_id', INTEGER(), table=<story>, primary_key=True, nullable=False),
      Column('version_id', INTEGER(), table=<story>, primary_key=True, nullable=False),
      Column('headline', VARCHAR(length=100), table=<story>, nullable=False),
      Column('body', TEXT(), table=<story>), schema=None)

>>> published  # doctest: +NORMALIZE_WHITESPACE
Table('published', MetaData(),
      Column('pub_id', INTEGER(), table=<published>, primary_key=True, nullable=False),
      Column('pub_timestamp', DATE(), table=<published>),
      Column('story_id', INTEGER(), ForeignKey('story.story_id'), table=<published>),
      Column('version_id', INTEGER(), ForeignKey('story.version_id'), table=<published>), schema=None)

This is useful if you have an existing database and you want to write
queries against it.

>>> query = select(story).join(published)
>>> print(query)
SELECT story.story_id, story.version_id, story.headline, story.body
FROM story JOIN published ON story.story_id = published.story_id AND story.version_id = published.version_id


References
----------
.. [#ytSQLAlchemy20] Bayer, Mike. SQLAlchemy 2.0 - The One-Point-Four-Ening 2021. Year: 2022. Retrieved: 2022-01-26. URL: https://www.youtube.com/watch?v=1Va493SMTcY
