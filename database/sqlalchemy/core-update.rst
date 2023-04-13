Core Update
===========


>>> from sqlalchemy import update


SetUp
-----
>>> from sqlalchemy import create_engine, MetaData, Table, Column
>>> from sqlalchemy import Integer, String, Date, Numeric, Enum
>>> from sqlalchemy import update
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
>>> ASTRONAUTS = [
...     {'firstname': 'Mark', 'lastname': 'Watney'},
...     {'firstname': 'Melissa', 'lastname': 'Lewis'},
...     {'firstname': 'Rick', 'lastname': 'Martinez'},
... ]
>>>
>>> with engine.begin() as db:
...     metadata.create_all(db)
...     result = db.execute(astronaut.insert(), ASTRONAUTS)


Update Statement
----------------
>>> query = (
...     update(astronaut).
...     values(firstname='Alex', lastname='Vogel').
...     where(astronaut.c.id == 3)
... )
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)


Update Object
-------------
Like ``INSERT``, it can also generate the ``SET`` clause based ont the given
parameters:

>>> query = (
...     update(astronaut).
...     where(astronaut.c.id == 3)
... )
>>>
>>> data = {'firstname': 'Alex', 'lastname': 'Vogel'}
>>>
>>> with engine.begin() as db:
...     result = db.execute(query, data)


Update Expression
-----------------
* SQL Expression

>>> query = (
...     update(astronaut).
...     values(lastname=astronaut.c.firstname + '' + astronaut.c.lastname).
...     where(astronaut.c.id == 3)
... )
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)

Note, that this example does not have any sense and it is used only to
demonstrate the capability of the framework.


References
----------
.. [#ytSQLAlchemy20] Bayer, Mike. SQLAlchemy 2.0 - The One-Point-Four-Ening 2021. Year: 2022. Retrieved: 2022-01-26. URL: https://www.youtube.com/watch?v=1Va493SMTcY
