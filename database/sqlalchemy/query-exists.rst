.. testsetup::

    # doctest: +SKIP_FILE


Query Exists
============
* Exist


Exists
------
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.exists

>>> q = session.query(User).filter(User.name == 'fred')
>>> session.query(q.exists())

.. code-block:: sql

    SELECT EXISTS (
        SELECT 1 FROM users WHERE users.name = :name_1
    ) AS anon_1

>>> session.query(User.id).filter(q.exists()).scalar()

>>> from sqlalchemy import literal
>>> session.query(literal(True)).filter(q.exists()).scalar()
