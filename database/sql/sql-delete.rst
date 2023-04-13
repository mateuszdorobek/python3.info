SQL Delete
==========
* Write your statement starting with ``--`` after you're done, make sure
  there is no mistake, then remove comment and execute
* https://www.youtube.com/watch?v=1aEqd4bl6Bs


Delete One
----------
* Removes data from table
* Leaves table structure intact
* Can be narrowed down by a ``WHERE``

.. code-block:: sql

    DELETE FROM astronauts
    WHERE id = 1;


Delete Many
-----------
* Removes data from table
* Leaves table structure intact
* Can be narrowed down by a ``WHERE``

.. code-block:: sql

    DELETE FROM astronauts
    WHERE agency = 'NASA';


Delete Query
------------
* Removes data from table
* Leaves table structure intact
* Can be narrowed down by a ``WHERE``

.. code-block:: sql

    DELETE FROM astronauts
    WHERE firstname = 'Mark'
    AND lastname = 'Watney';


Truncate
--------
* Removes all the data
* Leaves table structure intact

.. code-block:: sql

    TRUNCATE TABLE astronauts;


Drop
----
* Removes all the data
* Removes table too

.. code-block:: sql

    DROP TABLE astronauts;
