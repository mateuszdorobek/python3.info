SQL Select From
===============
.. figure:: img/sql-select.png


All Columns
-----------
.. code-block:: sql

    SELECT * FROM astronauts;


Selected Columns
----------------
.. code-block:: sql

    SELECT firstname, lastname
    FROM astronauts;


Column Name Aliases
-------------------
.. code-block:: sql

    SELECT firstname AS fname,
           lastname AS lname
    FROM astronauts;

.. code-block:: sql

    SELECT firstname,
           lastname,
           previous_job as career
    FROM astronauts;
