Model Base
==========
* Used for reflecting database tables in our program
* Allows to manage and alter database tables
* Declarative base (recommended)
* Imperative (a.k.a. Classical) Mappings

SQLAlchemy historically features two distinct styles of mapper
configuration. The original mapping API is commonly referred to as
"classical" style, whereas the more automated style of mapping is known as
"declarative" style. SQLAlchemy now refers to these two mapping styles as
imperative mapping and declarative mapping. Both styles may be used
interchangeably, as the end result of each is exactly the same.
[#sqlalchemyMappings]_

.. glossary::

    base
        Model responsible for mapping objects with database


Declarative Base
----------------
The Declarative Mapping is the typical way that mappings are constructed in
modern SQLAlchemy. The most common pattern is to first construct a base
class using the ``declarative_base()`` function, which will apply the
declarative mapping process to all subclasses that derive from it. Below
features a declarative base which is then used in a declarative table
mapping [#sqlalchemyMappings]_:

>>> from sqlalchemy import Column
>>> from sqlalchemy import Integer, String
>>> from sqlalchemy.ext.declarative import declarative_base
>>>
>>>
>>> Base = declarative_base()
>>>
>>> class User(Base):
...     __tablename__ = 'user'
...
...     id = Column(Integer, primary_key=True)
...     username = Column(String)
...     password = Column(String)

Above, the ``declarative_base()`` callable returns a new base class from
which new classes to be mapped may inherit from, as above a new mapped
class ``User`` is constructed.


Imperative Base
---------------
* Imperative (a.k.a. Classical) Mappings
* Could be used to map pre-existing classes (od dataclasses) with Table

An imperative or classical mapping refers to the configuration of a mapped
class using the ``registry.map_imperatively()`` method, where the target
class does not include any declarative class attributes. The "map
imperative" style has historically been achieved using the ``mapper()``
function directly, however this function now expects that a
``sqlalchemy.orm.registry()`` is present [#sqlalchemyMappings]_.

>>> from sqlalchemy import Table, Column
>>> from sqlalchemy import Integer, String
>>> from sqlalchemy.orm import registry
>>>
>>>
>>> mapper_registry = registry()
>>>
>>> user_table = Table('user', mapper_registry.metadata,
...     Column('id', Integer, primary_key=True),
...     Column('firstname', String(50)),
...     Column('lastname', String(50)),
... )
>>>
>>> class User:
...     pass
>>>
>>> mapper_registry.map_imperatively(User, user_table)  # doctest: +ELLIPSIS
<Mapper at 0x...; User>

Information about mapped attributes, such as relationships to other classes,
are provided via the properties dictionary.


References
----------
.. [#sqlalchemyMappings] https://docs.sqlalchemy.org/en/stable/orm/mapping_styles.html#orm-declarative-mapping
