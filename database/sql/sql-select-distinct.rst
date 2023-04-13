SQL Select Distinct
===================
* Unique values


Distinct
--------
.. code-block:: sql

    SELECT DISTINCT agency
    FROM astronauts;


Alias
-----
.. code-block:: sql

    SELECT DISTINCT agency AS ag
    FROM astronauts;


With Query
----------
.. code-block:: sql

    SELECT DISTINCT agency
    FROM astronauts
    WHERE location = 'Europe';
