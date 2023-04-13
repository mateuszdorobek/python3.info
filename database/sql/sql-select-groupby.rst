SQL Select Group By
===================


Group By
--------
.. code-block:: sql

    SELECT
        firstname,
        lastname,
        agency
    FROM astronauts
    GROUP BY agency;


Having
------
.. code-block:: sql

    SELECT
        firstname,
        lastname,
        agency,
        COUNT(id) as headcount
    FROM astronauts
    GROUP BY agency
    HAVING COUNT(headcount) > 5;


Use Case - 0x01
---------------
.. code-block:: sql

    SELECT
        message,
        level,
        COUNT(level) AS count
    FROM logs
    WHERE
        (datetime <= '1969-07-18' OR datetime >= '1969-07-20')
        AND message LIKE 'Max__%'
        AND level IN (
            SELECT DISTINCT(level) FROM logs
        )
    GROUP BY level
    HAVING count > 5
    ORDER BY datetime DESC
    LIMIT 5;
