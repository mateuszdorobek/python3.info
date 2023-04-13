.. testsetup::

    # doctest: +SKIP_FILE


Query Limit
===========
* First
* Last
* Limit
* Offset
* Slice

First
-----
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.first

>>> results = Valuation.query.filter_by(..).order_by(sqlalchemy.desc(Valuation.date)).first()


Last
----
* No last method

>>> results = Valuation.query.filter_by(..).order_by(sqlalchemy.desc(Valuation.date)).all()
>>> first_valuation = results[0]
>>> last_valuation = results[-1]


Limit
-----
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.limit


Offset
------
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.offset


Slice
-----
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.slice
