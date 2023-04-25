OOP Object Relations
====================
* ORM - Object-relational mapping
* Converts (`map`) between objects in code and database tables (`relations`)
* Declarative - First define model, which then maps to the database tables
* ``pickle`` - has relations
* ``json`` - has relations
* ``csv`` - non-relational format

Object–relational mapping (ORM, O/RM, and O/R mapping tool) in computer
science is a programming technique for converting data between incompatible
type systems using object-oriented programming languages. This creates, in
effect, a 'virtual object database' that can be used from within the
programming language. There are both free and commercial packages available
that perform object–relational mapping, although some programmers opt to
construct their own ORM tools [#wikipediaORM]_.

In object-oriented programming, data-management tasks act on objects that
are almost always non-scalar values. For example, consider an address book
entry that represents a single person along with zero or more phone numbers
and zero or more addresses. This could be modeled in an object-oriented
implementation by a 'Person object' with an attribute/field to hold each
data item that the entry comprises: the person's name, a list of phone
numbers, and a list of addresses. The list of phone numbers would itself
contain 'PhoneNumber objects' and so on. Each such address-book entry is
treated as a single object by the programming language (it can be
referenced by a single variable containing a pointer to the object, for
instance). Various methods can be associated with the object, such as
methods to return the preferred phone number, the home address, and so on
[#wikipediaORM]_.

By contrast, many popular database products such as SQL database management
systems (DBMS) are not object-oriented and can only store and manipulate
scalar values such as integers and strings organized within tables. The
programmer must either convert the object values into groups of simpler
values for storage in the database (and convert them back upon retrieval),
or only use simple scalar values within the program. Object–relational
mapping implements the first approach [#hibernateORM]_.

The heart of the problem involves translating the logical representation of
the objects into an atomized form that is capable of being stored in the
database while preserving the properties of the objects and their
relationships so that they can be reloaded as objects when needed. If this
storage and retrieval functionality is implemented, the objects are said to
be persistent [#wikipediaORM]_.

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
        database relation is often described as "normalized" if it meets
        third normal form. [#WikipediaDatabaseNormalization]_ [#Codd1972]_

    big-data
        Big data is a field that treats ways to analyze, systematically
        extract information from, or otherwise deal with data sets that are
        too large or complex to be dealt with by traditional data-processing
        application software. Data with many fields (columns) offer greater
        statistical power, while data with higher complexity (more
        attributes or columns) may lead to a higher false discovery rate.
        Big data analysis challenges include capturing data, data storage,
        data analysis, search, sharing, transfer, visualization, querying,
        updating, information privacy, and data source. Big data was
        originally associated with three key concepts: volume, variety, and
        velocity. The analysis of big data presents challenges in sampling,
        and thus previously allowing for only observations and sampling.
        Therefore, big data often includes data with sizes that exceed the
        capacity of traditional software to process within an acceptable
        time and value. [#WikipediaBigData]_

    retention
        Data retention defines the policies of persistent data and records
        management for meeting legal and business data archival requirements.
        In the field of telecommunications, data retention generally refers
        to the storage of call detail records (CDRs) of telephony and
        internet traffic and transaction data (IPDRs) by governments and
        commercial organisations. In the case of government data retention,
        the data that is stored is usually of telephone calls made and
        received, emails sent and received, and websites visited. Location
        data is also collected. [#WikipediaDataRetention]_

    relation
        In relational database theory, a relation, as originally defined by
        E. F. Codd, [#Codd1972]_ is a set of tuples (d1, d2, ..., dn), where
        each element dj is a member of Dj, a data domain. Codd's original
        definition notwithstanding, and contrary to the usual definition in
        mathematics, there is no ordering to the elements of the tuples of a
        relation. Instead, each element is termed an attribute value. An
        attribute is a name paired with a domain (nowadays more commonly
        referred to as a type or data type). An attribute value is an
        attribute name paired with an element of that attribute's domain,
        and a tuple is a set of attribute values in which no two distinct
        elements have the same name. Thus, in some accounts, a tuple is
        described as a function, mapping names to values.
        [#WikipediaRelation]_

    consistency
        Consistency (or Correctness) in database systems refers to the
        requirement that any given database transaction must change affected
        data only in allowed ways. Any data written to the database must be
        valid according to all defined rules, including constraints,
        cascades, triggers, and any combination thereof. This does not
        guarantee correctness of the transaction in all ways the application
        programmer might have wanted (that is the responsibility of
        application-level code) but merely that any programming errors
        cannot result in the violation of any defined database constraints.
        [#Date2012]_ [#WikipediaConsistency]_

    integrity
        Data integrity is the maintenance of, and the assurance of, data
        accuracy and consistency over its entire life-cycle and is a
        critical aspect to the design, implementation, and usage of any
        system that stores, processes, or retrieves data. The term is broad
        in scope and may have widely different meanings depending on the
        specific context – even under the same general umbrella of
        computing. It is at times used as a proxy term for data quality,
        while data validation is a prerequisite for data integrity. Data
        integrity is the opposite of data corruption. The overall intent of
        any data integrity technique is the same: ensure data is recorded
        exactly as intended (such as a database correctly rejecting mutually
        exclusive possibilities). Moreover, upon later retrieval, ensure the
        data is the same as when it was originally recorded. In short, data
        integrity aims to prevent unintentional changes to information. Data
        integrity is not to be confused with data security, the discipline
        of protecting data from unauthorized parties. [#Boritz2011]_
        [#WikipediaDataIntegrity]_

    SQL
    Structured Query Language
        Domain-specific language used in programming and designed for
        managing data held in a relational database management system
        (RDBMS), or for stream processing in a relational data stream
        management system (RDSMS). It is particularly useful in handling
        structured data, i.e. data incorporating relations among entities
        and variables. [#WikipediaSQL]_ [#RFC6922]_

    RDBMS
        Relational Database Management System
        https://en.wikipedia.org/wiki/Relational_database#RDBMS

    RDSMS
        Relational Data Stream Management System
        https://en.wikipedia.org/wiki/Relational_data_stream_management_system

    SELECT
        SQL language operation to retrieve data from the database

    INSERT
        SQL language operation to put data to the database

    UPDATE
        SQL language operation to modify data in the database

    JOIN
        SQL language operation to retrieve data from the database from
        multiple tables and merge them

    DBA
        DataBase Administrator


Pros
----
Compared to traditional techniques of exchange between an object-oriented
language and a relational database, ORM often reduces the amount of code
that needs to be written. [#Barry1998]_


Cons
----
Disadvantages of ORM tools generally stem from the high level of abstraction
obscuring what is actually happening in the implementation code. Also, heavy
reliance on ORM software has been cited as a major factor in producing
poorly designed databases. [#Lorenz2017]_


References
----------
.. [#wikipediaORM] https://en.wikipedia.org/wiki/Object–relational_mapping
.. [#hibernateORM] What is Object/Relational Mapping?. Hibernate Overview. JBOSS Hibernate. Retrieved: 2011-04-19. URL: https://hibernate.org/orm/what-is-an-orm/
.. [#Barry1998] Barry, Douglas and Stanienda, Torsten. Solving the Java Object Storage Problem. Computer, vol. 31, no. 11, pp. 33-40, Nov. 1998, http://www2.computer.org/portal/web/csdl/doi/10.1109/2.730734 , Excerpt at http://www.service-architecture.com/object-relational-mapping/articles/transparent_persistence_vs_jdbc_call-level_interface.html. Lines of code using O/R are only a fraction of those needed for a call-level interface (1:4). For this exercise, 496 lines of code were needed using the ODMG Java Binding compared to 1,923 lines of code using JDBC.
.. [#Lorenz2017] Lorenz, M and Rudolph, J.P. and Hesse, G. and Uflacker, M. and Plattner, H. Object–Relational Mapping Revisited - A Quantitative Study on the Impact of Database Technology on O/R Mapping Strategies. Hawaii International Conference on System Sciences (HICSS), 4877-4886 (DOI:10.24251/hicss.2017.592). Year: 2017.
.. [#WikipediaDatabaseNormalization] Database normalization. Wikipedia. Year: 2021. Retrieved: 2021-12-16. URL: https://en.wikipedia.org/wiki/Database_normalization
.. [#WikipediaSQL] SQL. Wikipedia. Year: 2021. Retrieved: 2021-12-16. URL: https://en.wikipedia.org/wiki/SQL
.. [#RFC6922] Shafranovich, Y. The application/sql Media Type. Internet Engineering Task Force (IETF). Year: 2013. Retrieved: 2021-12-16. URL: https://datatracker.ietf.org/doc/html/rfc6922
.. [#Codd1972] Codd, E. F. "Further Normalization of the Data Base Relational Model". (Presented at Courant Computer Science Symposia Series 6, "Data Base Systems", New York City, May 24–25, 1971.) IBM Research Report RJ909 (August 31, 1971). Republished in Randall J. Rustin (ed.), Data Base Systems: Courant Computer Science Symposia Series 6. Prentice-Hall, 1972.
.. [#WikipediaBigData] Big data. Wikipedia. Year: 2021. Retrieved: 2021-12-16. URL: https://en.wikipedia.org/wiki/Big_data
.. [#WikipediaDataRetention] Data retention. Wikipedia. Year: 2021. Retrieved: 2021-12-16. URL: https://en.wikipedia.org/wiki/Data_retention
.. [#WikipediaRelation] Relation (database). Wikipedia. Year: 2021. Retrieved: 2021-12-16. URL: https://en.wikipedia.org/wiki/Relation_(database)
.. [#WikipediaConsistency] Consistency. Wikipedia. Year: 2021. Retrieved: 2021-12-16. URL: https://en.wikipedia.org/wiki/Consistency_(database_systems)
.. [#WikipediaDataIntegrity] Data Integrity. Wikipedia. Year: 2021. Retrieved: 2021-12-16. URL: https://en.wikipedia.org/wiki/Data_integrity
.. [#Boritz2011] Boritz, J. "IS Practitioners' Views on Core Concepts of Information Integrity". International Journal of Accounting Information Systems. Elsevier. Archived from the original on 5 October 2011. Retrieved 12 August 2011.
.. [#Date2012] Date, C. J. "SQL and Relational Theory: How to Write Accurate SQL Code 2nd edition", O'reilly Media, Inc., 2012, pg. 180.


Assignments
-----------
.. literalinclude:: assignments/database_orm_a.py
    :caption: :download:`Solution <assignments/database_orm_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/database_orm_b.py
    :caption: :download:`Solution <assignments/database_orm_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/database_orm_c.py
    :caption: :download:`Solution <assignments/database_orm_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/database_orm_d.py
    :caption: :download:`Solution <assignments/database_orm_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/database_orm_e.py
    :caption: :download:`Solution <assignments/database_orm_e.py>`
    :end-before: # Solution

.. literalinclude:: assignments/database_orm_f.py
    :caption: :download:`Solution <assignments/database_orm_f.py>`
    :end-before: # Solution
