.. testsetup::

    # doctest: +SKIP_FILE


Query Execute
=============


SetUp
-----
>>> from sqlalchemy import create_engine
>>> from sqlalchemy import Column, String, Integer
>>> from sqlalchemy.ext.declarative import declarative_base
>>> from sqlalchemy.orm import sessionmaker
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>>
>>> engine = create_engine(DATABASE)
>>> db = sessionmaker(bind=engine).__call__()
>>> Model = declarative_base()
>>>
>>>
>>> class User(Model):
...     __tablename__ = 'user'
...     uid = Column(Integer, autoincrement=True, primary_key=True)
...     firstname = Column(String, nullable=False)
...     lastname = Column(String, nullable=False)
>>>
>>>
>>> Model.metadata.create_all(engine)
>>>
>>> db.add_all([
...     User('Mark', 'Watney'),
...     User('Melissa', 'Lewis'),
...     User('Rick', 'Martinez'),
...     User('Alex', 'Vogel'),
...     User('Beth', 'Johanssen'),
...     User('Chris', 'Beck'),
... ])
>>> db.commit()


Raw SQL Queries
---------------
>>> from sqlalchemy import text

>>> query = text('SELECT * FROM users')
>>>
>>> with engine.connect() as db:
...     result = db.execute(query).all()

>>> query = text("""SELECT *
...                 FROM users
...                 WHERE username=:username""")
>>>
>>> data = {'username': 'mwatney'}
>>>
>>> with engine.connect() as db:
...     result = db.execute(query).all()
...     print(result)


Transactions
------------
Lets define a query with some data:

>>> query = text("""INSERT INTO users (firstname, lastname)
...                 VALUES (:firstname, :lastname)""")
>>>
>>> data = {
...     'firstname': 'Pan',
...     'lastname': 'Twardowski',
... }


No autocommit at the library level. Always have to do it manually:

>>> with engine.connect() as db:
...     result = db.execute(query, data)
...     db.commit()

In SQLAlchemy there is an option to use context manager ``engine.begin()``
which already has transaction setup and no need to ``.commit()`` at the end
as of context manager will do it for you:

>>> query = text("""INSERT INTO users (firstname, lastname)
...                 VALUES (:firstname, :lastname)""")
>>> data = {'firstname': 'Pan', 'lastname': 'Twardowski'}
>>>
>>> with engine.begin() as db:
...     result = db.execute(query, data)

The above statement will commit transaction at the end of the ``with`` block
then release connection back to the connection pool. Moreover it will roll-back
automatically if there is an exception before re-throwing.


Savepoint
---------
If the transaction is ongoing, you can create a savepoint. Then if you rollback
transaction, you can discard the changes since savepoint, without loosing the
whole transaction.

This is particularly important for PostgreSQL. If you have ``IntegrityError``
in one of the inserted rows, it will rollback the whole transaction.

Let's define a query and data to use in following examples:

>>> query = text('UPDATE users SET lastname = :lastname')
>>> data = {'lastname': 'Twardowski'}

In order to create a savepoint, you have to use ``connection.begin_nested()``:

>>> with engine.connect() as db:
...     with db.begin():
...         savepoint = db.begin_nested()
...         result = db.execute(query, data)
...         savepoint.rollback()

You can use context manager syntax for savepoint:

>>> with engine.connect() as db:
...     with db.begin_nested() as savepoint:
...         result = db.execute(query, data)

This will commit transaction, or rollback if exception raises.

All savepoints has unique names which you can see in logs.
