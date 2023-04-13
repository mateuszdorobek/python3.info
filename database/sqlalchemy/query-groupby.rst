.. testsetup::

    # doctest: +SKIP_FILE


Query Group By
==============
* Group By
* Having


Group By
--------
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.group_by


Having
------
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.having

>>> q = session.query(User.id).\
...             join(User.addresses).\
...             group_by(User.id).\
...             having(func.count(Address.id) > 2)
