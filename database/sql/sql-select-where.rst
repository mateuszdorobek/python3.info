SQL Select Where
================
* Order clauses to filter out the most data first!


Selection
---------
* ``=`` - equals
* ``!=`` - not equal
* ``<>`` - not equal
* ``>`` - greater then
* ``>=`` - greater or equal
* ``<`` - less than
* ``<=`` - less or equal

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE lastname = 'Watney';

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE agency != 'NASA';

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE age > 30;


Conjunction
-----------
* ``AND`` - conjunction

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE lastname = 'Watney'
    AND lastname = 'Mark';

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE age > 30
    AND age < 55;


Alternative
-----------
* ``OR`` - alternative

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE lastname = 'Watney'
    OR lastname = 'Lewis';


Contains
--------
* ``IN`` - contains
* ``NOT IN`` - not contains

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE career IN ('Pilot', 'Engineer', 'Scientist', 'Medical Doctor');

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE lastname NOT IN ('Watney', 'Lewis', 'Martinez');


Identity
--------
* ``IS`` - identity check
* ``IS NOT`` - negation of an identity check

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE mission IS NULL;

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE mission IS NOT NULL;


Like
----
* ``LIKE``
* ``%`` - Any character (many)
* ``_`` - Any character (one)

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE lastname LIKE 'Wat%';

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE lastname LIKE '%ney';

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE lastname LIKE '%tn%';

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE lastname LIKE 'Watne_';

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE lastname LIKE '_tn%';
