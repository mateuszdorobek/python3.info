Core Operators
==============
* ``=`` - equals
* ``!=`` - not equals
* ``>`` - greater then
* ``>=`` - greater or equal to
* ``<`` - less then
* ``<=`` - less or equal to
* ``between()`` - in between two values or dates
* Use ``!=`` and ``==`` instead ``is`` and ``is not``
* There is no ``in`` and ``not in`` operator overload


SetUp
-----
>>> from sqlalchemy import create_engine, MetaData, Table, Column
>>> from sqlalchemy import Integer, String, Date, Numeric, Enum
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


Attributes
----------
>>> astronaut.c.firstname
Column('firstname', String(length=50), table=<astronaut>, nullable=False)


Operators
---------
>>> astronaut.c.firstname == 'Mark'  # doctest: +ELLIPSIS
<sqlalchemy.sql.elements.BinaryExpression object at 0x...>

>>> expression = (astronaut.c.firstname == 'Mark')
>>>
>>> expression.operator
<built-in function eq>
>>>
>>> expression.left
Column('firstname', String(length=50), table=<astronaut>, nullable=False)
>>>
>>> expression.right  # doctest: +ELLIPSIS
BindParameter('%(... firstname)s', 'Mark', type_=String(length=50))
>>>
>>> print(expression)
astronaut.firstname = :firstname_1

Bound Parameters are generated from the Python expression. It prevents from
SQL injection attacks. Bound parameter sanitization and escaping is typically
done by the database driver. Bounds parameters allows also for caching.

>>> expression = (astronaut.c.firstname == 'Mark')
>>> compiled = expression.compile()
>>>
>>> compiled.string
'astronaut.firstname = :firstname_1'
>>>
>>> compiled.params
{'firstname_1': 'Mark'}


Conjunction Options
-------------------
ColumnElements are the basic building block of SQL statement objects. To
compose more complex criteria, ``and_()`` and ``or_()`` for example provide
the basic conjunctions of AND and OR. [#ytSQLAlchemy20]_

>>> from sqlalchemy import and_, or_
>>>
>>> criteria = or_(
...     astronaut.c.firstname == 'Mark',
...     astronaut.c.firstname == 'Melissa',
... )
>>>
>>> print(criteria)
astronaut.firstname = :firstname_1 OR astronaut.firstname = :firstname_2

>>> criteria = and_(
...     astronaut.c.lastname == 'Watney',
...     or_(astronaut.c.firstname == 'Mark',
...         astronaut.c.firstname == 'Melissa'),
... )
>>>
>>> print(criteria)
astronaut.lastname = :lastname_1 AND (astronaut.firstname = :firstname_1 OR astronaut.firstname = :firstname_2)


Comparison Operators
--------------------
* ``=`` - equals
* ``!=`` - not equals
* ``>`` - greater then
* ``>=`` - greater or equal to
* ``<`` - less then
* ``<=`` - less or equal to
* ``between()`` - in between two values or dates

>>> criteria = and_(
...     astronaut.c.id >= 5,
...     astronaut.c.firstname != 'Mark',
...     astronaut.c.born.between('1994-10-01', '1994-10-31'),
... )
>>>
>>> print(criteria)
astronaut.id >= :id_1 AND astronaut.firstname != :firstname_1 AND astronaut.born BETWEEN :born_1 AND :born_2


Null Checking
-------------
* Note ``!=`` and ``==`` instead ``is`` and ``is not``
* You can easily overload ``!=`` and ``==`` operators

Compare to None produce ``IS NULL`` / ``IS NOT NULL``

>>> criteria = and_(
...     astronaut.c.firstname != None,
...     astronaut.c.agency == None,
... )
>>>
>>> print(criteria)
astronaut.firstname IS NOT NULL AND astronaut.agency IS NULL


Numerical Operators
-------------------
* Operators may also be type sensitive.
* ``+`` with numbers means 'addition'.

>>> criteria = astronaut.c.id + 5
>>>
>>> print(criteria)
astronaut.id + :id_1


String Operators
----------------
``+`` with strings means 'concatenation'.

>>> criteria = astronaut.c.firstname + 'Jr.'
>>>
>>> print(criteria)
astronaut.firstname || :firstname_1


Membership Operators
--------------------
* Note, there is no ``in`` and ``not in`` operator overload

The ``IN`` operator generates a special placeholder that will be filled in
when the statement is executed.

>>> criteria = astronaut.c.firstname.in_(['Mark', 'Melissa', 'Rick'])
>>>
>>> print(criteria)
astronaut.firstname IN (__[POSTCOMPILE_firstname_1])

When it is executed, bound parameters are generated:

>>> result = criteria.compile(compile_kwargs={'render_postcompile': True})
>>>
>>> print(result)
astronaut.firstname IN (:firstname_1_1, :firstname_1_2, :firstname_1_3)

When given an empty collection, the placeholder generates a SQL subquery
that represents an 'empty set'. This is due to that every database has a
different syntax to search for an 'empty set'.

>>> criteria = astronaut.c.firstname.in_([])
>>> result = criteria.compile(compile_kwargs={'render_postcompile': True})
>>>
>>> print(result)
astronaut.firstname IN (NULL) AND (1 != 1)


References
----------
.. [#ytSQLAlchemy20] Bayer, Mike. SQLAlchemy 2.0 - The One-Point-Four-Ening 2021. Year: 2022. Retrieved: 2022-01-26. URL: https://www.youtube.com/watch?v=1Va493SMTcY
