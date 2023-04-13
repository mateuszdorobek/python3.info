Core Join
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


Select Multiple Tables
----------------------
* ``SELECT`` from more than one table
* This will render CARTESIAN JOIN
* This can crash systems if tables are big
* Since SQLAlchemy 1.4 library will warn on cartesian products

The ``select()`` construct will include in the ``FROM`` clause all those
tables that we mention in the columns clause or ``WHERE`` clause. By default,
they are separated by a coma [#ytSQLAlchemy20]_.

>>> query = select(astronaut.c.firstname, mission.c.name)
>>>
>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
SELECT astronaut.firstname, mission.name
FROM astronaut, mission

Selecting from multiple tables without relating them to each other produces
an effect known as 'cartesian product'. SQLAlchemy will usually warn when
this is detected during statement execution [#ytSQLAlchemy20]_.

>>> query = select(astronaut.c.firstname, mission.c.name)
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
... # SAWarning: SELECT statement has a cartesian product between FROM
... # element(s) "astronaut" and FROM element "mission".  Apply join
... # condition(s) between each element to resolve.
>>>
>>> result.all()  # doctest: +NORMALIZE_WHITESPACE
[('Mark', 'Ares3'),
 ('Mark', 'Ares1'),
 ('Mark', 'Ares3'),
 ('Mark', 'Ares3'),
 ('Melissa', 'Ares3'),
 ('Melissa', 'Ares1'),
 ('Melissa', 'Ares3'),
 ('Melissa', 'Ares3'),
 ('Rick', 'Ares3'),
 ('Rick', 'Ares1'),
 ('Rick', 'Ares3'),
 ('Rick', 'Ares3')]

Using warnings filter can turn Warning to Error. This is useful for a CI/CD
and a pre-production tests.

Generated SQL statement:

>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
SELECT astronaut.firstname, mission.name
FROM astronaut, mission


Join From
---------
* New in SQLAlchemy 1.4
* Have some additional features than ``join()``
* More explicitly
* Is better to start chain of joins

When we have more than one table mentioned, we want to relate them together,
which is most easily achieved using ``join_from()`` [#ytSQLAlchemy20]_.

>>> query = (
...     select(astronaut.c.firstname, mission.c.name).
...     join_from(astronaut, mission)
... )
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> result.all()  # doctest: +NORMALIZE_WHITESPACE
[('Mark', 'Ares3'),
 ('Melissa', 'Ares1'),
 ('Melissa', 'Ares3'),
 ('Rick', 'Ares3')]

Generated SQL statement:

>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
SELECT astronaut.firstname, mission.name
FROM astronaut JOIN mission ON astronaut.id = mission.astronaut_id


Join
----
* ``join()`` will infer the left hand side automatically
* Is better for continuing chain of joins

>>> query = (
...     select(astronaut.c.firstname, mission.c.name).
...     join(mission)
... )
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> result.all()  # doctest: +NORMALIZE_WHITESPACE
[('Mark', 'Ares3'),
 ('Melissa', 'Ares1'),
 ('Melissa', 'Ares3'),
 ('Rick', 'Ares3')]

Generated SQL statement:

>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
SELECT astronaut.firstname, mission.name
FROM astronaut JOIN mission ON astronaut.id = mission.astronaut_id


Join On
-------
* You can specify the column on which to perform a join
* Useful when there is several ``ForeignKey`` columns
* If SQLAlchemy cannot find join column automatically it throws an error

The ``ON`` clause of the ``JOIN`` is also inferred automatically from the
foreign key relationship of the involved tables. We may chose to express
this join condition explicitly, as would be needed if the join condition
were otherwise ambiguous [#ytSQLAlchemy20]_.

>>> query = (
...     select(astronaut.c.firstname, mission.c.name).
...     join(mission, astronaut.c.id == mission.c.astronaut_id)
... )
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> result.all()  # doctest: +NORMALIZE_WHITESPACE
[('Mark', 'Ares3'),
 ('Melissa', 'Ares1'),
 ('Melissa', 'Ares3'),
 ('Rick', 'Ares3')]

Generated SQL statement:

>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
SELECT astronaut.firstname, mission.name
FROM astronaut JOIN mission ON astronaut.id = mission.astronaut_id


Table Aliases
-------------
* Python will use object identity to distinguish objects

When a ``SELECT`` wants to refer to the same table more than once, a SQL alias
is used. This is available using the ``.alias()`` method, which returns a
unique Alias object representing that table with a particular SQL alias
[#ytSQLAlchemy20]_.

>>> m1 = mission.alias()
>>> m2 = mission.alias()
>>>
>>> query = (
...     select(astronaut.c.firstname, m1.c.name, m2.c.name).
...     join_from(astronaut, m1).
...     join_from(astronaut, m2).
...     where(m1.c.name == 'Ares1').
...     where(m2.c.name == 'Ares3')
... )
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> result.all()
[('Melissa', 'Ares1', 'Ares3')]

Note, using ``.join_from()``.

Use Case: When you want to get rows in two different context.

Generated SQL statement:

>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
SELECT astronaut.firstname, mission_1.name, mission_2.name AS name_1
FROM astronaut JOIN mission AS mission_1 ON astronaut.id = mission_1.astronaut_id JOIN mission AS mission_2 ON astronaut.id = mission_2.astronaut_id
WHERE mission_1.name = :name_2 AND mission_2.name = :name_3


Subqueries
----------
A subquery is used much like a table alias, except we start with a ``SELECT``
statement. We call the ``.subquery`` method of ``select()`` [#ytSQLAlchemy20]_.

The subquery object itself has .c attribute, and is used just like a table.

>>> subquery = (
...     select(astronaut.c.firstname, mission.c.name).
...     join(mission).
...     subquery()
... )
>>>
>>> query = (
...     select(subquery.c.firstname).
...     where(subquery.c.firstname == 'Mark')
... )
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> result.all()
[('Mark',)]

Generated SQL statement:

>>> print(subquery)  # doctest: +NORMALIZE_WHITESPACE
SELECT astronaut.firstname, mission.name
FROM astronaut JOIN mission ON astronaut.id = mission.astronaut_id
>>>
>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
SELECT anon_1.firstname
FROM (SELECT astronaut.firstname AS firstname, mission.name AS name
FROM astronaut JOIN mission ON astronaut.id = mission.astronaut_id) AS anon_1
WHERE anon_1.firstname = :firstname_1


Subqueries Group By
-------------------
* SQLAlchemy uses column correspondence
* It uses column names to identify implicit foreign keys
* Example: ``astronaut_id`` will be joined with ``astronaut.id``

With subqueries and coins we can compose more elaborate statements. This
subquery introduces the ``func`` and ``group_by`` connects [#ytSQLAlchemy20]_:

We use ``join()`` to link the ``subquery()`` with another ``select()``:

>>> from sqlalchemy import func
>>>
>>>
>>> subquery = (
...     select(mission.c.astronaut_id,
...            func.count(mission.c.id).label('count')).
...     group_by(mission.c.astronaut_id).
...     subquery()
... )
>>>
>>> query = (
...     select(astronaut.c.firstname, subquery.c.count).
...     join(subquery).
...     order_by(astronaut.c.firstname)
... )
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> result.all()
[('Mark', 1), ('Melissa', 2), ('Rick', 1)]

Note, that while using function from a ``func`` namespace, you should add a
label to it, because the function results doesn't have meaningful names.

Generated SQL statement:

>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
SELECT astronaut.firstname, anon_1.count
FROM astronaut JOIN (SELECT mission.astronaut_id AS astronaut_id, count(mission.id) AS count
FROM mission GROUP BY mission.astronaut_id) AS anon_1 ON astronaut.id = anon_1.astronaut_id ORDER BY astronaut.firstname


Common Table Expressions
------------------------
* CTE - Common Table Expressions
* Very popular PostgreSQL feature
* Could be used with ``SELECT``, ``UPDATE`` and ``DELETE``
* Like a Subquery, but not in the ``FROM`` clause
* It resides above query and uses syntax ``WITH``
* Allow recursive queries
* Can produce very optimized forms
* Postgres can optimize CTE better than subqueries
* In SQLAlchemy it is used exactly the same way as subqueries

Joining to a subquery can also be achieved using a CTE (Common Table
Expression). By calling ``cte()`` instead of ``subquery()``, we get a CTE
[#ytSQLAlchemy20]_:

We ``SELECT``/``JOIN`` to the CTE in exactly the same way as we did the
subquery:

>>> from sqlalchemy import func
>>>
>>>
>>> cte = (
...     select(mission.c.astronaut_id,
...            func.count(mission.c.id).label('count')).
...     group_by(mission.c.astronaut_id).
...     cte()
... )
>>>
>>> query = (
...     select(astronaut.c.firstname, cte.c.count).
...     join(cte).
...     order_by(astronaut.c.firstname)
... )
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> result.all()
[('Mark', 1), ('Melissa', 2), ('Rick', 1)]

Generated SQL statement:

>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
WITH anon_1 AS
(SELECT mission.astronaut_id AS astronaut_id, count(mission.id) AS count
FROM mission GROUP BY mission.astronaut_id)
 SELECT astronaut.firstname, anon_1.count
FROM astronaut JOIN anon_1 ON astronaut.id = anon_1.astronaut_id ORDER BY astronaut.firstname


Correlated Subqueries
---------------------
* A subquery in the columns clause or in the ``WHERE`` clause of the enclosing ``SELECT`` statement
* Should return exactly one row and one column
* Used as a column expression in bigger column query

A 'scalar subquery' returns exactly one row and one column. We indicate this
intent using the ``scalar_subquery()`` method after construction
[#ytSQLAlchemy20]_.

>>> from sqlalchemy import func
>>>
>>>
>>> corr = (
...     select(func.count(mission.c.id)).
...     where(astronaut.c.id == mission.c.astronaut_id).
...     scalar_subquery()
... )
>>>
>>> print(corr)  # doctest: +NORMALIZE_WHITESPACE
(SELECT count(mission.id) AS count_1
FROM mission, astronaut
WHERE astronaut.id = mission.astronaut_id)

The subquery here refers to two tables. Printing it alone, we can see both
tables in the ``FROM`` clause.

However, a scalar subquery will by default 'auto correlate' in a larger SQL
expression, omitting a ``FROM`` that is found in the immediate enclosing
``SELECT``.

>>> query = select(astronaut.c.firstname, corr)
>>>
>>> print(query)  # doctest: +NORMALIZE_WHITESPACE
SELECT astronaut.firstname, (SELECT count(mission.id) AS count_1
FROM mission
WHERE astronaut.id = mission.astronaut_id) AS anon_1
FROM astronaut


References
----------
.. [#ytSQLAlchemy20] Bayer, Mike. SQLAlchemy 2.0 - The One-Point-Four-Ening 2021. Year: 2022. Retrieved: 2022-01-26. URL: https://www.youtube.com/watch?v=1Va493SMTcY
