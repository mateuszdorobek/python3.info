Model Column
============
* ``name=None``
* ``type_=None``
* ``autoincrement='auto'``
* ``default=None``
* ``doc=None``
* ``key=name``
* ``index=None``
* ``info=None``
* ``nullable=True``
* ``onupdate=None``
* ``primary_key=False``
* ``server_default=None``
* ``server_onupdate=None``
* ``quote=None``
* ``unique=None``
* ``system=False``
* ``comment=None``

* Documentation [#sqlalchemyColumn]_


Define Column
-------------
>>> from sqlalchemy import Column, String, Integer

Use a type with arguments:

>>> Column('username', String(50))
Column('username', String(length=50), table=None)

Use no arguments:

>>> Column('age', Integer)
Column('age', Integer(), table=None)

Parameters
----------
.. csv-table:: Parameters
    :widths: 10,10,80
    :header: "Parameter", "Default", "Description"

    "``name``",            "``None``",   "The name of this column as represented in the database. This argument may be the first positional argument, or specified via keyword"
    "``type_``",           "``None``",   "The column's type, indicated using an instance which subclasses TypeEngine. The type argument may be the second positional argument or specified by keyword"
    "``autoincrement``",   "``'auto'``", "Set up 'auto increment' semantics for an integer primary key column with no foreign key dependencies. Other values include True (force this column to have auto-increment semantics for a composite primary key as well), False (this column should never have auto-increment semantics), and the string 'ignore_fk' (special-case for foreign key columns, see below)"
    "``default``",         "``None``",   "Scalar, Python callable, or ColumnElement expression representing the default value for this column, which will be invoked upon insert if this column is otherwise not specified in the VALUES clause of the insert"
    "``doc``",             "``None``",   "Optional String that can be used by the ORM or similar to document attributes on the Python side"
    "``key``",             "``name``",   "An optional string identifier which will identify this Column object on the Table. When a key is provided, this is the only identifier referencing the Column within the application, including ORM attribute mapping; the name field is used only when rendering SQL"
    "``index``",           "``None``",   "When True, indicates that a Index construct will be automatically generated for this Column"
    "``info``",            "``None``",   "Optional data dictionary which will be populated into the SchemaItem.info attribute of this object"
    "``nullable``",        "``True``",   "When set to False, will cause the 'NOT NULL' phrase to be added when generating DDL for the column. When True, will normally generate nothing (in SQL this defaults to 'NULL'), except in some very specific backend-specific edge cases where 'NULL' may render explicitly"
    "``onupdate``",        "``None``",   "A scalar, Python callable, or ClauseElement representing a default value to be applied to the column within UPDATE statements, which will be invoked upon update if this column is not present in the SET clause of the update"
    "``primary_key``",     "``False``",  "If True, marks this column as a primary key column. Multiple columns can have this flag set to specify composite primary keys"
    "``server_default``",  "``None``",   "Server DEFAULT value for already existing column"
    "``server_onupdate``", "``None``",   "Database-side default generation function, such as a trigger"
    "``quote``",           "``None``",   "Force quoting of this column's name on or off, corresponding to True or False"
    "``unique``",          "``None``",   "When True, and the Column.index parameter is left at its default value of False which will result in a 'UNIQUE CONSTRAINT' clause referring to this column being included in the CREATE TABLE statement"
    "``system``",          "``False``",  "When True, indicates this is a 'system' column, that is a column which is automatically made available by the database, and should not be included in the columns list for a CREATE TABLE statement"
    "``comment``",         "``None``",   "Optional string that will render an SQL comment on table creation"

Examples:

>>> field = Column('id', Integer, key='user_id', primary_key=True, autoincrement=True)
>>> field = Column('username', String(30), nullable=False, unique=True, index=True)
>>> field = Column('password', String(30), nullable=False)
>>> field = Column('email', String(60), unique=True),


Use Case - 0x01
---------------
>>> from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey
>>> from sqlalchemy import create_engine
>>>
>>>
>>> metadata = MetaData()
>>>
>>> user = Table('user', metadata,
...     Column('user_id', Integer, primary_key=True),
...     Column('user_name', String(16), nullable=False),
...     Column('email_address', String(60), key='email'),
...     Column('nickname', String(50), nullable=False)
... )
>>>
>>> user_prefs = Table('user_prefs', metadata,
...     Column('pref_id', Integer, primary_key=True),
...     Column('user_id', Integer, ForeignKey('user.user_id'), nullable=False),
...     Column('pref_name', String(40), nullable=False),
...     Column('pref_value', String(100))
... )
>>>
>>>
>>> engine = create_engine('sqlite:///:memory:')
>>>
>>> with engine.begin() as conn:
...     metadata.create_all(engine)


Use Case - 0x02
---------------
>>> from sqlalchemy.orm import deferred
>>> from sqlalchemy import Integer, String, Text, BLOB, Column
>>> from sqlalchemy.orm import declarative_base
>>>
>>> Base = declarative_base()
>>>
>>>
>>> class Book(Base):
...     __tablename__ = 'book'
...
...     book_id = Column(Integer, primary_key=True)
...     title = Column(String(200), nullable=False)
...     summary = Column(String(2000))
...     excerpt = deferred(Column(Text))
...     photo = deferred(Column(BLOB))


Use Case - 0x03
---------------
>>> from sqlalchemy.orm import deferred
>>> from sqlalchemy import Integer, String, Text, BLOB, Column
>>> from sqlalchemy.orm import declarative_base
>>>
>>> Base = declarative_base()
>>>
>>>
>>> class Book(Base):
...     __tablename__ = 'book'
...
...     book_id = Column(Integer, primary_key=True)
...     title = Column(String(200), nullable=False)
...     summary = Column(String(2000))
...     excerpt = deferred(Column(Text))
...     photo1 = deferred(Column(BLOB), group='photos')
...     photo2 = deferred(Column(BLOB), group='photos')
...     photo3 = deferred(Column(BLOB), group='photos')


References
----------
.. [#sqlalchemyColumn] https://docs.sqlalchemy.org/en/stable/core/metadata.html#sqlalchemy.schema.Column.__init__
