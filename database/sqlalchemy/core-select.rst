Core Select
===========
* Method chaining
* Note the dot ``.`` at the end of the select line

>>> from sqlalchemy import select


SetUp
-----
>>> from sqlalchemy import create_engine, MetaData, Table, Column
>>> from sqlalchemy import Integer, String, Date, Numeric, Enum
>>> from sqlalchemy import select, or_
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
...     astronaut.create(db)
...     result = db.execute(astronaut.insert(), ASTRONAUTS)


Select All Columns
------------------
>>> query = select(astronaut)
>>>
>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
SELECT astronaut.id, astronaut.firstname, astronaut.lastname, astronaut.agency, astronaut.born, astronaut.age, astronaut.height, astronaut.weight
FROM astronaut


Select Specified Columns
------------------------
>>> query = select(astronaut.c.firstname, astronaut.c.lastname)
>>>
>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
SELECT astronaut.firstname, astronaut.lastname
FROM astronaut


Where Clause
------------
>>> query = (
...     select(astronaut.c.firstname, astronaut.c.lastname).
...     where(astronaut.c.firstname == 'Mark')
... )
>>>
>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
SELECT astronaut.firstname, astronaut.lastname
FROM astronaut
WHERE astronaut.firstname = :firstname_1


Where OR
--------
>>> query = (
...     select(astronaut.c.firstname, astronaut.c.lastname).
...     where(or_(astronaut.c.firstname == 'Mark',
...               astronaut.c.firstname == 'Melissa'))
... )
>>>
>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
SELECT astronaut.firstname, astronaut.lastname
FROM astronaut
WHERE astronaut.firstname = :firstname_1 OR astronaut.firstname = :firstname_2

>>> query = (
...     select(astronaut.c.firstname, astronaut.c.lastname).
...     where((astronaut.c.firstname == 'Mark')
...         | (astronaut.c.firstname == 'Melissa'))
... )
>>>
>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
SELECT astronaut.firstname, astronaut.lastname
FROM astronaut
WHERE astronaut.firstname = :firstname_1 OR astronaut.firstname = :firstname_2


Where AND
---------
* Multiple ``where()`` clauses are automatically joined by ``AND``

>>> query = (
...     select(astronaut.c.firstname, astronaut.c.lastname).
...     where(astronaut.c.firstname == 'Mark').
...     where(astronaut.c.lastname == 'Watney')
... )
>>>
>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
SELECT astronaut.firstname, astronaut.lastname
FROM astronaut
WHERE astronaut.firstname = :firstname_1 AND astronaut.lastname = :lastname_1

>>> query = (
...     select(astronaut.c.firstname, astronaut.c.lastname).
...     where((astronaut.c.firstname == 'Mark')
...         & (astronaut.c.lastname == 'Watney'))
... )
>>>
>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
SELECT astronaut.firstname, astronaut.lastname
FROM astronaut
WHERE astronaut.firstname = :firstname_1 AND astronaut.lastname = :lastname_1


Order By
--------
>>> query = (
...     select(astronaut.c.firstname, astronaut.c.lastname).
...     order_by(astronaut.c.lastname)
... )
>>>
>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
SELECT astronaut.firstname, astronaut.lastname
FROM astronaut
ORDER BY astronaut.lastname


References
----------
.. [#ytSQLAlchemy20] Bayer, Mike. SQLAlchemy 2.0 - The One-Point-Four-Ening 2021. Year: 2022. Retrieved: 2022-01-26. URL: https://www.youtube.com/watch?v=1Va493SMTcY
