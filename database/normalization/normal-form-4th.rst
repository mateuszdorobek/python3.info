4th Normal Form
===============
* No multi-valued dependencies


Problem
-------
.. csv-table:: astronauts
    :header: id (PK), firstname, lastname, email

    1, Melissa, Lewis, mlewis@nasa.gov
    1, Melissa, Lewis, mlewis@gmail.com
    2, Mark, Watney, mwatney@nasa.gov
    3, Rick, Martinez, rmartinez@nasa.gov

Note, that Melissa has two emails: work email mlewis@nasa.gov and private
email mlewis@gmail.com.


Solution
--------
.. csv-table:: astronauts
    :header: id (PK), firstname, lastname

    1, Melissa, Lewis
    2, Mark, Watney
    3, Rick, Martinez

.. csv-table:: astronaut_emails
    :header: id (PK), email, astronaut_id (FK)

    1, mlewis@nasa.gov, 1
    2, mlewis@gmail.com, 1
    3, mwatney@nasa.gov, 2
    4, rmartinez@nasa.gov, 3
