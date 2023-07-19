.. testsetup::

    # doctest: +SKIP_FILE


Model Define
============
* Models inherits from ``Base``
* Models represents objects in a database
* They are the most important entity in the project


SetUp
-----
>>> from sqlalchemy import create_engine
>>> from sqlalchemy.orm import sessionmaker, declarative_base
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>>
>>> engine = create_engine(DATABASE)
>>> session = sessionmaker(bind=engine).__call__()
>>> Base = declarative_base()


Good practices
--------------
* Model, View, Controller Pattern (MVC)
* Fat Model, thin controller, thin view (best)
* Thin model, fat controller, thin view (bad)
* Thin model, thin controller, fat view (worst)
* Model name should be the same as database table name


Table Specification
-------------------
* Models uses ``__tablename__`` class attribute to specify reflected table
* You can use legacy database to work on (database was created in the past
  now we use models to reflect the schema in order to query it)
* Preferable is to use declarative SQLAlchemy database and table creation
* Use only models and migrations to alter and version schema

>>> class User(Base):
...     __tablename__ = 'user'


Column Specification
--------------------
>>> from sqlalchemy import Column, String, Integer

>>> class User(Base):
...     __tablename__ = 'user'
...
...     username = Column(String)
...     password = Column(String)


Initializer
-----------
* Initializer is an ``__init__()`` method
* All models has default initializer method
* You can create initializer explicitly, which will overload the default one

>>> class User(Base):
...     __tablename__ = 'user'
...     username = Column(String, primary_key=True)
...     password = Column(String)

SQLAlchemy applies a default initializer (``__init__``) method, to all
mapped classes that don't explicitly have their own ``__init__`` method.
The behavior of this method is such that it provides a convenient keyword
constructor that will accept as optional keyword arguments all the
attributes that are named. The constructor also applies to imperative
mappings [#sqlalchemyConstructor]_.

Note, that this must be keyword arguments. Positional argument won't work.


Stringification
---------------
* ``__str__()`` method
* ``__repr__()`` method


Create Schema
-------------
In order to create tables in database you have to call ``create_all()`` method
of ``Base.metadata`` object and pass engine instance.

>>> Base.metadata.create_all(engine)


Create Model Instances
----------------------
In order to create object simply instantiate it passing proper arguments.
Creating instances will not modify anything in a database. If you want to store
information in database you have to commit manually.

If any constraints will fail, the ``IntegrityError`` exception will be raised.
This may happen for example if field should have unique values (like username)
and we create two users with the same username.

Creating objects:

>>> mark = User('Mark', 'Watney')
>>> session.add(mark)
>>> session.commit()

You can also create two objects within one session (transaction). Mind, that
both of those objects will be saved to database in the same time, as soon as
the ``.commit()`` method is called.

>>> mark = User('Mark', 'Watney')
>>> melissa = User('Melissa', 'Lewis')
>>>
>>> session.add(mark)
>>> session.add(melissa)
>>>
>>> session.commit()


Use Case - 0x01
---------------
>>> from sqlalchemy import create_engine
>>> from sqlalchemy import Column, String, Integer
>>> from sqlalchemy.orm import sessionmaker, declarative_base
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>>
>>> engine = create_engine(DATABASE)
>>> session = sessionmaker(bind=engine).__call__()
>>> Base = declarative_base()
>>>
>>>
>>> class User(Base):
...     __tablename__ = 'user'
...     username = Column(String, primary_key=True)
...     password = Column(String)
>>>
>>>
>>> Base.metadata.create_all(engine)
>>>
>>>
>>> mark = User(firstname='Mark', lastname='Watney')
>>> melissa = User(firstname='Melissa', lastname='Lewis')
>>>
>>> session.add(mark)
>>> session.add(melissa)
>>>
>>> session.commit()


References
----------
.. [#sqlalchemyConstructor] https://docs.sqlalchemy.org/en/stable/orm/mapping_styles.html#default-constructor
