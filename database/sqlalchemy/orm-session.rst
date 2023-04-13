.. testsetup::

    # doctest: +SKIP_FILE


Connection Session
==================
* Session manages persistence operations for ORM-mapped objects
* 1.0 style (legacy)
* 2.0 style (with context managers)

.. glossary::

    session
        Manages persistence operations for ORM-mapped objects


SetUp
-----
>>> from sqlalchemy import create_engine
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE)


Sessionmaker
------------
* ``Session`` manages persistence operations for ORM-mapped objects

``sessionmaker`` acts as a factory for ``Session`` objects in the same way
as an ``Engine`` acts as a factory for ``Connection`` objects. In this way
it also includes a ``sessionmaker.begin()`` method, that provides a context
manager which both begins and commits a transaction, as well as closes out
the ``Session`` when complete, rolling back the transaction if any errors
occur.

Factory function ``sessionmaker()`` will return a **class**. In order to
create a session this class has to be called. There are several ways how to
do that. You can either capture the class from session maker, instantiate
it and then assign to identifier (variable) or you can do it step by step
having intermediate objects.

In order to use ``sessionmaker()`` you have to import it:

>>> from sqlalchemy.orm import sessionmaker


1.x Style
---------
To crate a session object simply use the ``sessionmaker()`` factory passing
(binding) an engine instance:

>>> Session = sessionmaker(bind=engine)
>>> session = Session()

Or you can simplify the expression by calling class right away:

>>> session = sessionmaker(bind=engine)()

Or using a bit more verbose, but explicit syntax:

>>> session = sessionmaker(bind=engine).__call__()


2.x Style
---------
Context manager on ``with`` block exit will commit transaction and close the
session automatically:

>>> from sqlalchemy.orm import Session
>>>
>>> with Session(engine) as session:
...     session.add(object1)
...     session.add(object2)
...     session.commit()


Transaction
-----------
>>> with Session(engine) as session:
...     session.begin()
...     try:
...         session.add(some_object)
...         session.add(some_other_object)
...     except:
...         session.rollback()
...         raise
...     else:
...         session.commit()

>>> with Session(engine) as session:
...     with session.begin():
...       session.add(some_object)
...       session.add(some_other_object)

>>> with Session(engine) as session, session.begin():
...     session.add(some_object)
...     session.add(some_other_object)


Example
-------
>>> from sqlalchemy import create_engine
>>> from sqlalchemy.orm import sessionmaker
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>>
>>> engine = create_engine(DATABASE)
>>> session = sessionmaker(bind=engine)
>>>
>>> with session.begin() as db:
...     result = db.execute('SELECT * FROM astronauts').all()
...
[(1, 'Melissa', 'Lewis', 805766400000),
 (2, 'Rick', 'Martinez', 822182400000),
 (3, 'Alex', 'Vogel', 784857600000),
 (4, 'Chris', 'Beck', 933552000000),
 (5, 'Beth', 'Johanssen', 822182400000),
 (6, 'Mark', 'Watney', 781920000000)]
