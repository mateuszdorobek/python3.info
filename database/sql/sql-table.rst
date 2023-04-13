SQL Table
=========
* Constraint ``UNIQUE``
* Constraint ``PRIMARY KEY``
* Constraint ``DEFAULT``
* Constraint ``NOT NULL``
* Auto-value ``NULL``
* Auto-value ``AUTOINCREMENT``
* Auto-value ``CURRENT_TIME``
* Auto-value ``CURRENT_DATE``
* Auto-value ``CURRENT_TIMESTAMP``
* Function ``STRFTIME()``, ``DATETIME()``


Create Table
------------
.. code-block:: sql

    CREATE TABLE astronauts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mycolumn01 INTEGER,
        mycolumn02 INTEGER UNIQUE,
        mycolumn03 REAL,
        mycolumn04 FLOAT,
        mycolumn05 TEXT,
        mycolumn06 CHAR(2),
        mycolumn07 VARCHAR(255),
        mycolumn08 DATE,
        mycolumn09 DATE DEFAULT CURRENT_DATE,
        mycolumn10 TIME,
        mycolumn11 TIME DEFAULT CURRENT_TIME,
        mycolumn12 DATETIME,
        mycolumn13 DATETIME DEFAULT NULL,
        mycolumn14 DATETIME DEFAULT (DATETIME('NOW', 'LOCALTIME')),
        mycolumn15 DATETIME DEFAULT (DATETIME('NOW', 'UTC')),
        mycolumn16 DATETIME DEFAULT (STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')),
        mycolumn17 TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

.. figure:: img/sql-create.png


Add Column
----------
.. code-block:: sql

    ALTER TABLE astronauts
    ADD mission_name TEXT;


Drop Column
-----------
* SQLite3 does not support dropping columns with ``ALTER TABLE``
* We have to do a workaround instead

    1. Create a new table with all the columns (and data)
       that we want to keep
    2. Drop the old table
    3. Rename the new table with the old name.

* Make sure you also take care of the Indexes and Views (if you have any)
* Perform a ``.schema astronauts`` BEFORE you drop the table
* Use this info to re-create the Indexes and Views after renaming the
  table back to its original name

.. code-block:: sql

    CREATE TABLE astronauts_temp AS (
        SELECT id, firstname, lastname, agency
        FROM astronauts);

    DROP TABLE astronauts;

    ALTER TABLE astronauts_temp RENAME TO astronauts;


Example
-------
.. code-block:: sql

    CREATE TABLE astronauts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT,
        lastname TEXT,
        agency TEXT);

.. code-block:: sql

    CREATE TABLE IF NOT EXISTS sensor_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datetime DATETIME DEFAULT (DATETIME('NOW', 'UTC')),
        device_id INTEGER,
        parameter TEXT,
        value REAL,
        unit TEXT);
