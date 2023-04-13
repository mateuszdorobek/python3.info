SQL Update
==========


Update One
----------
.. code-block:: sql

    UPDATE astronauts SET
        agency = 'NASA'
    WHERE lastname = 'Watney';


Update Many Columns
-------------------
.. code-block:: sql

    UPDATE astronauts SET
        firstname = 'Mark',
        lastname = 'Watney',
        agency = 'NASA'
    WHERE id = 1;


Update Many Rows
----------------
.. code-block:: sql

    UPDATE astronauts SET
        mission = 'Ares 3'
    WHERE lastname IN ('Watney', 'Lewis', 'Martinez');
