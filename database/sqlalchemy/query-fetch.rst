Query Fetch
===========


SetUp
-----
>>> from sqlalchemy import create_engine, text
>>> from sqlalchemy import Column, String, Integer
>>> from sqlalchemy.ext.declarative import declarative_base
>>> from sqlalchemy.orm import sessionmaker
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>>
>>> engine = create_engine(DATABASE, future=True)
>>> Model = declarative_base()
>>>
>>>
>>> class User(Model):
...     __tablename__ = 'users'
...     uid = Column(Integer, autoincrement=True, primary_key=True)
...     firstname = Column(String, nullable=False)
...     lastname = Column(String, nullable=False)
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> Model.metadata.create_all(engine)
>>>
>>> with sessionmaker(engine).begin() as session:
...     session.add_all([
...         User('Mark', 'Watney'),
...         User('Melissa', 'Lewis'),
...         User('Rick', 'Martinez'),
...         User('Alex', 'Vogel'),
...         User('Beth', 'Johanssen'),
...         User('Chris', 'Beck'),
...     ])


Scalar
------
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.scalar
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.scalar_subquery


Value
-----
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.value


Values
------
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.values


Get
---
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.get


One
---
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.one


One or None
-----------
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.one_or_None


All
---
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.all

>>> query = text('SELECT * FROM users')
>>>
>>> with engine.begin() as db:
...     for row in db.execute(query).all():
...         print(row)
(1, 'Mark', 'Watney')
(2, 'Melissa', 'Lewis')
(3, 'Rick', 'Martinez')
(4, 'Alex', 'Vogel')
(5, 'Beth', 'Johanssen')
(6, 'Chris', 'Beck')
