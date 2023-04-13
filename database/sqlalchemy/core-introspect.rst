Core Introspect
===============
* Introspection - getting information about the object internals


SetUp
-----
>>> from sqlalchemy import create_engine, MetaData, Table, Column, insert
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


Inspect
-------
Define database query:

>>> query = (
...     insert(astronaut).
...     values(firstname='Mark', lastname='Watney')
... )

We can inspect database query by printing the query:

>>> print(query)
INSERT INTO astronaut (firstname, lastname) VALUES (:firstname, :lastname)


Compile
-------
Define database query:

If we want to get to the lower level we can:

>>> query = (
...     insert(astronaut).
...     values(firstname='Mark', lastname='Watney')
... )
>>>
>>> sql = query.compile()

But mind, that all databases has different syntax, hence it is good idea to
pass the database engine instance to the compile method to set SQL language
flavor:

>>> query = (
...     insert(astronaut).
...     values(firstname='Mark', lastname='Watney')
... )
>>>
>>> sql = query.compile(engine)

Or we can set the flavor explicitly:

>>> from sqlalchemy.dialects import postgresql
>>>
>>>
>>> query = (
...     insert(astronaut).
...     values(firstname='Mark', lastname='Watney')
... )
>>>
>>> sql = query.compile(dialect=postgresql.dialect())


Introspection
-------------
Compiled object will have attributes:

>>> query = (
...     insert(astronaut).
...     values(firstname='Mark', lastname='Watney')
... )
>>>
>>> sql = query.compile(engine)
>>>
>>> print(sql.statement)
INSERT INTO astronaut (firstname, lastname) VALUES (:firstname, :lastname)
>>>
>>> print(sql.params)
{'firstname': 'Mark', 'lastname': 'Watney'}

However if you want to get the final version

>>> query = (
...     insert(astronaut).
...     values(firstname='Mark', lastname='Watney')
... )
>>>
>>> sql = query.compile(compile_kwargs={'literal_binds': True})
>>>
>>> print(sql)
INSERT INTO astronaut (firstname, lastname) VALUES ('Mark', 'Watney')
