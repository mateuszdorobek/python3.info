SQL Select Functions
====================


Sum
---
.. code-block:: sql

    SELECT SUM(experience)
    FROM astronauts
    WHERE agency = 'NASA';


Average
-------
.. code-block:: sql

    SELECT AVG(age)
    FROM astronauts
    WHERE agency = 'NASA';


Count
-----
.. code-block:: sql

    SELECT COUNT(id)
    FROM astronauts
    WHERE agency = 'NASA';

.. code-block:: sql

    SELECT COUNT(DISTINCT agency)
    FROM astronauts;

.. code-block:: sql

    SELECT COUNT(DISTINCT mission_name)
    FROM astronauts
    WHERE agency = 'NASA';
