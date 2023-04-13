.. testsetup::

    # doctest: +SKIP_FILE


Query About
===========



Query
-----
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.__init__


With Session
------------
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.with_session


Select Columns
--------------
* https://docs.sqlalchemy.org/en/stable/orm/loading_columns.html#sqlalchemy.orm.defer
* https://docs.sqlalchemy.org/en/stable/orm/loading_columns.html#sqlalchemy.orm.deferred
* https://docs.sqlalchemy.org/en/stable/orm/loading_columns.html#sqlalchemy.orm.load_only

>>> from sqlalchemy.orm import defer
>>> from sqlalchemy.orm import undefer
>>>
>>> session.query(Book).options(
...     defer('*'), undefer('summary'), undefer('excerpt'))

A similar function is available with less verbosity by using the load_only()
option. This is a so-called exclusionary option which will apply deferred
behavior to all column attributes except those that are named:

>>> from sqlalchemy.orm import load_only
>>>
>>> session.query(Book).options(load_only(Book.summary, Book.excerpt))
