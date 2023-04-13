Normalization About
===================
* Entities - rows in database
* Attributes - columns in database
* Normalization is what gives data meaning
* NF - Normal Form
* In order to be in 3rd normal form, you need to be in 1st and 2nd NF
* Core basics: 1st, 2nd, 3rd
* Exceptions: 4th, 5th
* 1st: atomic values, unique identifiers (PK), columns with same type
* 2nd: all data must depend on the Primary Key
* 3rd: PK define all Non-Key columns, those can't depend on any other Key
* 4th: No multi-valued dependencies


Glossary
--------
.. glossary::

    normalization
        Database normalization is the process of structuring a database,
        usually a relational database, in accordance with a series of
        so-called normal forms in order to reduce data redundancy and
        improve data integrity. Normalization entails organizing the columns
        (attributes) and tables (relations) of a database to ensure that
        their dependencies are properly enforced by database integrity
        constraints. It is accomplished by applying some formal rules either
        by a process of synthesis (creating a new database design) or
        decomposition (improving an existing database design). A relational
        database relation is often described as 'normalized' if it meets
        third normal form. [#WikipediaDatabaseNormalization]_ [#Codd1972]_

    NF
        Normal Form

    Entity
    Entities
        Rows in database

    Attributes
        Columns in database

    Table
        Database Table


Recap
-----
.. figure:: img/normalform-1st,2nd,3rd.png

    Image credit: [#Lowgren2021]_

References
----------
.. [#WikipediaDatabaseNormalization] Database normalization. https://en.wikipedia.org/wiki/Database_normalization

.. [#Lowgren2021]
   Lowgren, Jesper.
   Database Normalization 1NF 2NF 3NF.
   Year: 2021.
   Retrieved: 2022-02-05.
   URL: https://www.youtube.com/watch?v=SK4H5tTT6-M

.. [#Codd1972] Codd, E. F. Further Normalization of the Data Base Relational Model. (Presented at Courant Computer Science Symposia Series 6, Data Base Systems, New York City, May 24–25, 1971.) IBM Research Report RJ909 (August 31, 1971). Republished in Randall J. Rustin (ed.), Data Base Systems: Courant Computer Science Symposia Series 6. Prentice-Hall, 1972.
