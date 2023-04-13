Core Text
=========


>>> from sqlalchemy import update


SetUp
-----
>>> from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
>>> from sqlalchemy import Integer, String, Date, Numeric, Enum
>>> from sqlalchemy import select
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
>>> mission = Table('mission', metadata,  # one to many relationship
...     Column('id', Integer, primary_key=True),
...     Column('astronaut_id', ForeignKey('astronaut.id'), nullable=False),
...     Column('year', Integer, nullable=False),
...     Column('name', String(50), nullable=False),
... )
>>>
>>> ASTRONAUTS = [
...     {'firstname': 'Mark', 'lastname': 'Watney'},
...     {'firstname': 'Melissa', 'lastname': 'Lewis'},
...     {'firstname': 'Rick', 'lastname': 'Martinez'},
... ]
>>>
>>> MISSIONS = [
...     {'astronaut_id': 1, 'year': 2035, 'name': 'Ares3'},
...     {'astronaut_id': 2, 'year': 2030, 'name': 'Ares1'},
...     {'astronaut_id': 2, 'year': 2035, 'name': 'Ares3'},
...     {'astronaut_id': 3, 'year': 2035, 'name': 'Ares3'},
... ]
>>>
>>> with engine.begin() as db:
...     metadata.create_all(db)
...     result = db.execute(astronaut.insert(), ASTRONAUTS)
...     result = db.execute(mission.insert(), MISSIONS)


Constructs
----------
* SQL Expression language constructs: select, where, join, ...
* Composability - we can build and rearrange SQL using Python objects
* Database agnosticism - query will run on lots of different backends
* Support for refactoring

>>> from sqlalchemy import select
>>>
>>>
>>> query = select(astronaut)
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> result.all()  # doctest: +NORMALIZE_WHITESPACE
[(1, 'Mark', 'Watney', None, None, None, None, None),
 (2, 'Melissa', 'Lewis', None, None, None, None, None),
 (3, 'Rick', 'Martinez', None, None, None, None, None)]


Text
----
* If you have perfect query - use ``text()``
* Usually for more complex queries that's very specific
* It can be changed to SQL constructs later if needed
* Works with the ORM too

>>> from sqlalchemy import text
>>>
>>>
>>> query = text('SELECT * FROM astronaut')
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> result.all()  # doctest: +NORMALIZE_WHITESPACE
[(1, 'Mark', 'Watney', None, None, None, None, None),
 (2, 'Melissa', 'Lewis', None, None, None, None, None),
 (3, 'Rick', 'Martinez', None, None, None, None, None)]

Note, use bound parameters for variables that change (user input) in oder to
avoid SQL injection. Do not ever concatenate user input to SQL queries!


References
----------
.. [#ytSQLAlchemy20] Bayer, Mike. SQLAlchemy 2.0 - The One-Point-Four-Ening 2021. Year: 2022. Retrieved: 2022-01-26. URL: https://www.youtube.com/watch?v=1Va493SMTcY
