Core Model
==========
* Models represents database entities (tables)
* Metadata represents connection between Python object and a database


SetUp
-----
Prepare connection:

>>> from sqlalchemy import create_engine
>>>
>>> engine = create_engine('sqlite:///:memory:', future=True)

Note, that we will use future flag to turn on the 2.0 compatibility mode.


Metadata
--------
Metadata represents connection between Python object and a database. In
order to create a Metadata object import it from sqlalchemy:

>>> from sqlalchemy import MetaData
>>>
>>> metadata = MetaData()


Database Model
--------------
>>> from sqlalchemy import  Table, Column
>>> from sqlalchemy import Integer, String, Date, Numeric, Enum
>>>
>>>
>>> astronaut = Table('astronaut', metadata,
...     Column('id', Integer, primary_key=True),
...     Column('firstname', String(50), nullable=False),
...     Column('lastname', String(50), nullable=False),
...     Column('born', Date),
...     Column('height', Integer),
...     Column('weight', Numeric(3,2)),
...     Column('agency', Enum('NASA', 'ESA', 'POLSA')),
... )


Execute
-------
Execute the statement to create database table:

>>> with engine.begin() as db:
...     astronaut.create(db)

SQLAlchemy core will generate and execute the following SQL statement. Note,
that the ``CREATE TABLE`` statement is inside of the transaction. This will
ensure database consistency and rollback if any problem occur (for example
database table with the same name already exists):

.. code-block:: sql

    BEGIN
    CREATE TABLE astronaut (
        id INTEGER NOT NULL,
        firstname VARCHAR(50) NOT NULL,
        lastname VARCHAR(50) NOT NULL,
        born DATE,
        height NUMERIC(3, 2),
        weight NUMERIC(3, 2),
        agency VARCHAR(9),
        PRIMARY KEY (id)
    )
    COMMIT


Recap
-----
>>> from sqlalchemy import create_engine, MetaData, Table, Column
>>> from sqlalchemy import Integer, String, Date, Numeric, Enum, Float
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
...     Column('height', Float(3,2)),
...     Column('weight', Float(3,2)),
... )
>>>
>>> with engine.begin() as db:
...     metadata.create_all(db)


Assignments
-----------
.. literalinclude:: assignments/model_data_a.py
    :caption: :download:`Solution <assignments/model_data_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/model_data_b.py
    :caption: :download:`Solution <assignments/model_data_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/model_data_c.py
    :caption: :download:`Solution <assignments/model_data_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/model_data_d.py
    :caption: :download:`Solution <assignments/model_data_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/model_data_e.py
    :caption: :download:`Solution <assignments/model_data_e.py>`
    :end-before: # Solution

.. literalinclude:: assignments/model_data_f.py
    :caption: :download:`Solution <assignments/model_data_f.py>`
    :end-before: # Solution

.. literalinclude:: assignments/model_data_g.py
    :caption: :download:`Solution <assignments/model_data_g.py>`
    :end-before: # Solution

.. literalinclude:: assignments/model_data_h.py
    :caption: :download:`Solution <assignments/model_data_h.py>`
    :end-before: # Solution
