Theory Object-Relational Mapping
================================
* ORM - Object-relational mapping
* Converts (`map`) between objects in code and database tables (`relations`)
* Declarative - First define model, which then maps to the database tables

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
