SQL Select Order By
===================


Order By
--------
.. code-block:: sql

    SELECT *
    FROM astronauts
    ORDER BY lastname;


Ascending
---------
* From smallest to biggest
* ``ASC``

.. code-block:: sql

    SELECT *
    FROM astronauts
    ORDER BY lastname ASC;


Descending
----------
* From biggest to smallest
* ``DESC``

.. code-block:: sql

    SELECT *
    FROM astronauts
    ORDER BY lastname DESC;


Multiple
--------
* When first criteria is the same

.. code-block:: sql

    SELECT *
    FROM astronauts
    ORDER BY lastname ASC, firstname DESC;


Empty
-----
* ``NULLS FIRST``
* ``NULLS LAST``

.. code-block:: sql

    SELECT *
    FROM astronauts
    ORDER BY mission NULLS FIRST;

.. code-block:: sql

    SELECT *
    FROM astronauts
    ORDER BY mission ASC NULLS LAST;
