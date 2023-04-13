SQL Join
========
* Combine records from two or more tables in a database
* Combining fields from two tables by using values common to each

The SQL Joins clause is used to combine records from two or more tables
in a database. A JOIN is a means for combining fields from two tables
by using values common to each. [#sqljoin]_

.. figure:: img/sql-joins.png

.. figure:: img/sql-join-clause.png
.. figure:: img/sql-join-constraint.png
.. figure:: img/sql-join-operator.png


INNER JOIN
----------
* Returns rows when there is a match in both tables
* The most important and frequently used of the joins

The INNER JOIN creates a new result table by combining column values
of two tables (table1 and table2) based upon the join-predicate. The query
compares each row of table1 with each row of table2 to find all pairs
of rows which satisfy the join-predicate. When the join-predicate
is satisfied, column values for each matched pair of rows of A and B
are combined into a result row. [#sqljoininner]_

.. code-block:: sql

    SELECT *
    FROM astronauts
    INNER JOIN mission
    ON astronauts.id = mission.astronaut_id;

.. figure:: img/sql-innerjoin.gif


LEFT JOIN
---------
* Returns all rows from the left table, even if there are no matches
  in the right table

This means that if the ON clause matches 0 (zero) records in the right
table; the join will still return a row in the result, but with NULL
in each column from the right table. [#sqljoinleft]_

This means that a left join returns all the values from the left table,
plus matched values from the right table or NULL in case of no matching
join predicate. [#sqljoinleft]_

.. code-block:: sql

    SELECT *
    FROM astronauts
    LEFT JOIN mission
    ON astronauts.id = mission.astronaut_id;

.. figure:: img/sql-leftjoin.gif


RIGHT JOIN
----------
* Returns all rows from the right table, even if there are no matches
  in the left table

This means that if the ON clause matches 0 (zero) records in the left
table; the join will still return a row in the result, but with NULL
in each column from the left table. [#sqljoinright]_

This means that a right join returns all the values from the right table,
plus matched values from the left table or NULL in case of no matching
join predicate. [#sqljoinright]_

.. code-block:: sql

    SELECT *
    FROM astronauts
    RIGHT JOIN mission
    ON astronauts.id = mission.astronaut_id;

.. figure:: img/sql-rightjoin.gif


FULL JOIN
---------
* Combines the results of both left and right outer joins
* The joined table will contain all records from both the tables and fill
  in NULLs for missing matches on either side. [#sqljoinfull]_

.. code-block:: sql

    SELECT *
    FROM astronauts
    INNER JOIN mission
    ON astronauts.id = mission.astronaut_id;

.. figure:: img/sql-fulljoin.gif


OUTER JOIN
----------
.. code-block:: sql

    SELECT *
    FROM astronauts
    FULL OUTER JOIN mission
    ON astronauts.id = mission.astronaut_id;


SELF JOIN
---------
* Is used to join a table to itself as if the table were two tables
* Temporarily renaming at least one table in the SQL statement

.. code-block:: sql

    SELECT *
    FROM astronauts Astro1,
         astronauts Astro2
    WHERE Astro1.id != Astro2.id
    AND Astro1.agency = Astro2.agency
    ORDER BY Astro1.agency;


CARTESIAN JOIN
--------------
* Also known as ``CROSS JOIN``
* Returns the Cartesian product of the sets of records from the two
  or more joined tables.

Thus, it equates to an inner join where the join-condition always
evaluates to either True or where the join-condition is absent from
the statement. [#sqljoincartesian]_

.. code-block:: sql

    SELECT astronauts.firstname,
           astronauts.lastname,
           missions.name,
           missions.year
    FROM astronauts, missions;


References
----------
.. [#sqljoin] https://www.tutorialspoint.com/sql/sql-using-joins.htm
.. [#sqljoinleft] https://www.tutorialspoint.com/sql/sql-left-joins.htm
.. [#sqljoinright] https://www.tutorialspoint.com/sql/sql-right-joins.htm
.. [#sqljoinfull] https://www.tutorialspoint.com/sql/sql-full-joins.htm
.. [#sqljoinself] https://www.tutorialspoint.com/sql/sql-self-joins.htm
.. [#sqljoincartesian] https://www.tutorialspoint.com/sql/sql-cartesian-joins.htm
.. [#sqljoininner] https://www.tutorialspoint.com/sql/sql-inner-joins.htm
