.. testsetup::

    # doctest: +SKIP_FILE


Query Order By
==============
* Order By
* Ascending
* Descending
* Nulls first


Order By
--------
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.order_by

>>> results = Valuation.query.all().order_by(sqlalchemy.desc(Valuation.date)).all()
