Migration About
===============



Migration Software
------------------
* Alembic
* Django Migrations
* Yoyo Database Migrations
* Migrate
* SOLAlchemy Migrate
* SQL Migration Runner
* Liquid Base
* FlywayDB


Lifecycle
---------
* Create Migration
* Run Forward (apply)
* Run Backward (rollback)


Alembic
-------
* Heavily relays on reflection

[alembic]
# path to migration scripts
script_location = h:migrations
# Edit the engine string for production
sqlalchemy.url: postgresql://hypothesis-h-prod-db.us-west-1.rds.amazonaws.com
:5432/h

Create:

.. code-block:: console

    $ alembic revision -m "create organization table"
    Generating h/migrations/versions/1975ea83b712_create_organization_table.py...done

Run forward:

.. code-block:: console

    $ alembic upgrade head
    INFO [alembic.context] Running upgrade None -> 1975ea836712


Use Cases
---------
* Create Table
* Alter Table
* Add Column
* Drop Column
* Rename Column
* Modify Data
