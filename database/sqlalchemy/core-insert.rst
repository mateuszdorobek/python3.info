Core Insert
===========
* ``insert()`` is a method of a Table object
* It could be also used as a object factory

>>> from sqlalchemy import insert


SetUp
-----
>>> from sqlalchemy import create_engine, MetaData, Table, Column
>>> from sqlalchemy import Integer, String, Date, Numeric, Enum
>>> from sqlalchemy import insert
>>>
>>>
>>> engine = create_engine('sqlite:///:memory:', future=True)
>>> metadata = MetaData()
>>>
>>> astronaut = Table('astronaut', metadata,
...     Column('id', Integer, primary_key=True),
...     Column('firstname', String(50), nullable=False),
...     Column('lastname', String(50), nullable=False),
...     Column('agency', Enum('NASA', 'ESA', 'POLSA')),
...     Column('born', Date),
...     Column('age', Integer),
...     Column('height', Numeric(3,2)),
...     Column('weight', Numeric(3,2)),
... )
>>>
>>> with engine.begin() as db:
...     metadata.create_all(db)


Insert Statement
----------------
We can insert data using the ``insert()`` construct:

>>> query = (
...     insert(astronaut).
...     values(firstname='Mark', lastname='Watney')
... )
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)

We can inspect the query object simply by printing it:

>>> print(query)
INSERT INTO astronaut (firstname, lastname) VALUES (:firstname, :lastname)


Insert Object
-------------
The ``insert()`` statement, when not given ``values()`` will generate the
``VALUES`` clause based on the list of parameters that are passed to
``execute()`` [#ytSQLAlchemy20]_.

Prepare data for insert and execute the query writing it to database:

>>> data = {'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> with engine.begin() as db:
...     result = db.execute(astronaut.insert(), data)


Insert List of Objects
----------------------
* Since 1.4/2.0 execute many is greatly improved for PostgreSQL

This format also accepts an 'executemany' style that DBAPI can optimize.
Prepare data for insert and execute the query writing it to database
[#ytSQLAlchemy20]_:

>>> data = [
...     {'firstname': 'Mark', 'lastname': 'Watney'},
...     {'firstname': 'Melissa', 'lastname': 'Lewis'},
...     {'firstname': 'Rick', 'lastname': 'Martinez'},
... ]
>>>
>>> with engine.begin() as db:
...     result = db.execute(astronaut.insert(), data)

Note, that this is the same ``.execute()`` method. SQLAlchemy will recognize
that the data is a ``list[dict]`` and will execute proper statements to the
database.


Recap
-----
* ``insert(table).values()``
* ``db.execute(table.insert(), data)``
* data can be a ``dict`` or ``list[dict]``


References
----------
.. [#ytSQLAlchemy20] Bayer, Mike. SQLAlchemy 2.0 - The One-Point-Four-Ening 2021. Year: 2022. Retrieved: 2022-01-26. URL: https://www.youtube.com/watch?v=1Va493SMTcY
