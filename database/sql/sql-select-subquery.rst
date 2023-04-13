SQL Select Subquery
===================
* ``IN (SELECT ...)`` - subquery


Subqueries
----------
.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE agency IN (
        SELECT name FROM agencies);

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE career IN (
        SELECT name FROM job_names);

.. code-block:: sql

    SELECT *
    FROM logs
    WHERE level in (

        SELECT level
        FROM logs
        GROUP BY level
        HAVING COUNT(*) > 5

    );
