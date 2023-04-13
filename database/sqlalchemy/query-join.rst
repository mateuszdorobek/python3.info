.. testsetup::

    # doctest: +SKIP_FILE


Query Join
==========
* Join
* Select From
* Multiple Joins
* Outer Join
* Reset Join Point

>>> q = session.query(User).\
...         join(User.addresses).\
...         filter(Address.email_address.like('%@aol.com')).\
...         options(contains_eager(User.addresses)).\
...         populate_existing()


Join
----
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.join

>>> q = session.query(User).join(User.addresses)

.. code-block:: sql

    SELECT user.id, user.name
    FROM user JOIN address ON user.id = address.user_id


Select From
-----------
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.select_from


Multiple Joins
--------------
* the order in which each call to the join() method occurs is important.

>>> q = (
...     select(User).
...     join(User.orders).
...     join(Order.items).
...     join(Item.keywords))


Outer Join
----------
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.outerjoin


Reset Join Point
----------------
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.reset_joinpoint


Use Case - 0x01
---------------
>>> q = session.query(User).join(Address, User.id==Address.user_id)
>>> q = session.query(User).join(Address, User.addresses)


Use Case - 0x02
---------------
>>> a1 = aliased(Address)
>>> a2 = aliased(Address)
>>>
>>> q = session.query(User).\
...         join(a1, User.addresses).\
...         join(a2, User.addresses).\
...         filter(a1.email_address=='ed@foo.com').\
...         filter(a2.email_address=='ed@bar.com')


Use Case - 0x03
---------------
>>> a1 = aliased(Address)
>>> a2 = aliased(Address)
>>>
>>> q = session.query(User).\
...         join(User.addresses.of_type(a1)).\
...         join(User.addresses.of_type(a2)).\
...         filter(a1.email_address == 'ed@foo.com').\
...         filter(a2.email_address == 'ed@bar.com')


Use Case - 0x04
---------------
>>> q = session.query(User).join(
...     User.addresses.and_(Address.email_address != 'foo@bar.com')
... )


Use Case - 0x05
---------------
>>> subq = session.query(Address).\
...     filter(Address.email_address == 'ed@foo.com').\
...     subquery()
>>>
>>> q = session.query(User).join(
...     subq, User.id == subq.c.user_id
... )


Further Reading
---------------
* https://docs.sqlalchemy.org/en/stable/orm/loading_relationships.html
* https://docs.sqlalchemy.org/en/stable/orm/loading_relationships.html#lazy-loading
* https://docs.sqlalchemy.org/en/stable/orm/loading_relationships.html#joined-eager-loading
* https://docs.sqlalchemy.org/en/stable/orm/loading_relationships.html#subquery-eager-loading
* https://docs.sqlalchemy.org/en/stable/orm/loading_relationships.html#select-in-loading
* https://docs.sqlalchemy.org/en/stable/orm/loading_relationships.html#what-kind-of-loading-to-use
* https://docs.sqlalchemy.org/en/stable/orm/loading_relationships.html#wildcard-loading-strategies
* https://docs.sqlalchemy.org/en/stable/orm/loading_relationships.html#relationship-loader-api
