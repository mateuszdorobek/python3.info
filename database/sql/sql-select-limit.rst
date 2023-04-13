SQL Select Limit
================


Limit Results
-------------
.. code-block:: sql

    SELECT *
    FROM astronauts
    LIMIT 5;


Pagination
----------
.. code-block:: sql

    SELECT *
    FROM astronauts
    LIMIT 0, 10;

.. code-block:: sql

    SELECT *
    FROM astronauts
    LIMIT 10, 10;

.. code-block:: sql

    SELECT *
    FROM astronauts
    LIMIT 20, 10;
