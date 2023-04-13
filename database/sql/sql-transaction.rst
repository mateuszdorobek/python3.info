SQL Transaction
===============
* Any command that accesses the database will automatically start a transaction
* Automatically started transactions are committed when the last SQL statement finishes
* Transactions can be started manually using the BEGIN command.
* Transactions usually persist until the next COMMIT or ROLLBACK command.
* ACID - four standard properties
* Atomicity
* Consistency
* Isolation
* Durability

Any command that accesses the database (basically, any SQL command, except
a few PRAGMA statements) will automatically start a transaction if one is
not already in effect. Automatically started transactions are committed
when the last SQL statement finishes. [#sqlitetranaction]_

Transactions can be started manually using the BEGIN command. Such
transactions usually persist until the next COMMIT or ROLLBACK command.
But a transaction will also ROLLBACK if the database is closed or if an
error occurs and the ROLLBACK conflict resolution algorithm is specified.
See the documentation on the ON CONFLICT clause for additional information
about the ROLLBACK conflict resolution algorithm. [#sqlitetranaction]_


ACID
----
Transactions have the following four standard properties, usually referred
to by the acronym ACID.

**Atomicity**

Ensures that all operations within the work unit are completed
successfully; otherwise, the transaction is aborted at the point of
failure and previous operations are rolled back to their former state.

Transactions are often composed of multiple statements. Atomicity
guarantees that each transaction is treated as a single 'unit', which
either succeeds completely, or fails completely: if any of the statements
constituting a transaction fails to complete, the entire transaction fails
and the database is left unchanged. An atomic system must guarantee
atomicity in each and every situation, including power failures, errors
and crashes.


**Consistency**

Ensures that the database properly changes states upon a successfully
committed transaction.

Consistency ensures that a transaction can only bring the database from
one valid state to another, maintaining database invariants: any data
written to the database must be valid according to all defined rules,
including constraints, cascades, triggers, and any combination thereof.
This prevents database corruption by an illegal transaction, but does not
guarantee that a transaction is correct.


**Isolation**

Enables transactions to operate independently of and transparent
to each other.

Transactions are often executed concurrently (e.g., reading and writing
to multiple tables at the same time). Isolation ensures that concurrent
execution of transactions leaves the database in the same state that
would have been obtained if the transactions were executed sequentially.
Isolation is the main goal of concurrency control; depending on the method
used, the effects of an incomplete transaction might not even be visible
to other transactions.


**Durability**

Ensures that the result or effect of a committed transaction persists
in case of a system failure.

Durability guarantees that once a transaction has been committed, it will
remain committed even in the case of a system failure (e.g., power outage
or crash). This usually means that completed transactions (or their
effects) are recorded in non-volatile memory.


Source: [#sqlitetranaction]_ [#tutorialspoint]_


Begin
-----
* Starts a transaction
* ``BEGIN`` or ``BEGIN TRANSACTION``

.. code-block:: sql

    BEGIN;

    DELETE FROM astronauts
    WHERE agency = 'NASA';

    -- COMMIT or ROLLBACK;

.. figure:: img/sql-transaction-begin.png


Rollback
--------
* Perform a revert of all operations

.. code-block:: sql

    BEGIN;
    DELETE FROM astronauts WHERE agency = 'NASA';
    ROLLBACK;

.. figure:: img/sql-transaction-rollback.png


Commit
------
* Executes all operations
* ``COMMIT`` or ``END TRANSACTION``

.. code-block:: sql

    BEGIN;
    DELETE FROM astronauts WHERE agency = 'NASA';
    COMMIT;

.. figure:: img/sql-transaction-commit.png


Example
-------
.. code-block:: sql

    BEGIN;
    INSERT INTO astronauts VALUES (1, 'Mark', 'Watney');
    INSERT INTO astronauts VALUES (2, 'Melissa', 'Lewis');
    DELETE FROM astronauts WHERE agency = 'ESA';
    ROLLBACK;


References
----------
.. [#sqlitetranaction] https://www.sqlite.org/lang_transaction.html
.. [#tutorialspoint] https://www.tutorialspoint.com/sqlite/sqlite_transactions.htm
