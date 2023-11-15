SQL Explain
===========

.. code-block:: sql

    ANALYZE users;

.. code-block:: sql

    EXPLAIN ANALYZE users;

.. code-block:: sql
    :caption: Not working in SQLite

    EXPLAIN SELECT firstname FROM users;

.. code-block:: sql
    :caption: Not working in SQLite

    EXPLAIN ANALYZE
    SELECT *
    FROM users;
