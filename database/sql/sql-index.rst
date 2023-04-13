SQL Index
=========
* Used to create and retrieve data from the database very quickly
* Analog to notebook calendar tabs

.. figure:: img/sql-index-notebookcalendar.png


Index Types
-----------
* Column Index
* Multi Column Index
* Partial Index
* Functional Index
* Binary Index


SQL Syntax
----------
.. code-block:: sql

    CREATE INDEX astronaut_agency_index
    ON astronaut (agency);


If Not Exists
-------------
* ``IF NOT EXISTS``

.. code-block:: sql

    CREATE INDEX IF NOT EXISTS astronaut_agency_index
    ON astronaut (agency);


Unique Index
------------
* ``UNIQUE``

.. code-block:: sql

    CREATE UNIQUE INDEX IF NOT EXISTS astronaut_agency_index
    ON astronaut (agency);
