SQL Insert
==========


Insert Values
-------------
.. code-block:: sql

    INSERT INTO astronauts
    VALUES ('Mark', 'Watney');


Insert Values to Columns
------------------------
.. code-block:: sql

    INSERT INTO astronauts (firstname, lastname)
    VALUES ('Mark', 'Watney');

.. code-block:: sql

    INSERT INTO astronauts (lastname, firstname)
    VALUES ('Watney', 'Mark');


Insert to Autoincrement Column
------------------------------
.. code-block:: sql

    INSERT INTO astronauts (id, firstname, lastname)
    VALUES (NULL, 'Mark', 'Watney');


Prepared statements
-------------------
For sequences (list, tuple, set):

.. code-block:: sql

    INSERT INTO astronauts (firstname, lastname)
    VALUES (?, ?);

For mappings (dict):

.. code-block:: sql

    INSERT INTO astronauts
    VALUES (NULL, :firstname, :lastname);
