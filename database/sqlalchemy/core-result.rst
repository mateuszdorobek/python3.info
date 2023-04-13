Core Result
===========
* ``.all()``
* ``.first()``
* ``.one()`` - returns exactly one row
* ``.one_or_none()``


SetUp
-----
>>> from sqlalchemy import create_engine, MetaData, Table, Column
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
>>> ASTRONAUTS = [
...     {'firstname': 'Mark', 'lastname': 'Watney'},
...     {'firstname': 'Melissa', 'lastname': 'Lewis'},
...     {'firstname': 'Rick', 'lastname': 'Martinez'},
... ]
>>>
>>> with engine.begin() as db:
...     metadata.create_all(db)
...     result = db.execute(astronaut.insert(), ASTRONAUTS)


List[tuple]
-----------
* It will download all the data from database
* This technique is not particularly efficient for large databases

>>> query = select(astronaut.c.firstname, astronaut.c.lastname)
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[('Mark', 'Watney'),
 ('Melissa', 'Lewis'),
 ('Rick', 'Martinez')]


List[dict]
----------
* It will download all the data from database
* This technique is not particularly efficient for large databases

>>> query = select(astronaut.c.firstname, astronaut.c.lastname)
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> list(result.mappings())  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Mark', 'lastname': 'Watney'},
 {'firstname': 'Melissa', 'lastname': 'Lewis'},
 {'firstname': 'Rick', 'lastname': 'Martinez'}]


One
---
* Must be exactly one result, otherwise the exception is raised
* Exception ``MultipleResultsFound``

>>> query = (
...     select(astronaut.c.firstname, astronaut.c.lastname).
...     where(astronaut.c.lastname == 'Watney')
... )
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> result.one()
('Mark', 'Watney')


One or None
-----------
>>> query = (
...     select(astronaut.c.firstname, astronaut.c.lastname).
...     where(astronaut.c.lastname == 'Watney')
... )
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> result.one_or_none()
('Mark', 'Watney')


All
---
>>> query = select(astronaut.c.firstname, astronaut.c.lastname)
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> result.all()  # doctest: +NORMALIZE_WHITESPACE
[('Mark', 'Watney'),
 ('Melissa', 'Lewis'),
 ('Rick', 'Martinez')]


First
-----
* Fetches the first result from a cursor object
* ``CursorResult`` object has no attribute 'last'

>>> query = select(astronaut.c.firstname, astronaut.c.lastname)
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> result.first()
('Mark', 'Watney')


Columns
-------
Result objects now supports slicing at the result level. We can ``SELECT``
some rows, and change the ordering and/or presence of columns after the fact
using ``.columns()`` method [#ytSQLAlchemy20]_:

>>> query = (
...     select(astronaut).
...     order_by(astronaut.c.lastname)
... )
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> for lastname, firstname in result.columns('lastname', 'firstname'):
...     print(f'{lastname=}, {firstname=}')
...
lastname='Lewis', firstname='Melissa'
lastname='Martinez', firstname='Rick'
lastname='Watney', firstname='Mark'

Note, that the ``.columns()`` method defines the order for unpacked object.
It overwrites the default ordering from ``SELECT`` clause.


Scalars
-------
* When you have a row, but there is only one column that you care about
* We don't want the rows back, we want a list of values

A single column from the results can be delivered without using rows by
applying the ``.scalars()`` modifier. This accepts and optional column name,
or otherwise assumes the first column:

>>> query = (
...     select(astronaut.c.firstname).
...     order_by(astronaut.c.lastname)
... )
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> result.scalars('firstname').all()
['Melissa', 'Rick', 'Mark']

Note, that for performance reasons we narrowed down the ``SELECT`` clause
only to those values we want to receive.


References
----------
.. [#ytSQLAlchemy20] Bayer, Mike. SQLAlchemy 2.0 - The One-Point-Four-Ening 2021. Year: 2022. Retrieved: 2022-01-26. URL: https://www.youtube.com/watch?v=1Va493SMTcY
