.. testsetup::

    # doctest: +SKIP_FILE


Query Count
===========
* Count
* https://docs.sqlalchemy.org/en/stable/faq/sessions.html#faq-query-deduplicating

It is important to note that the value returned by count() is not the same
as the number of ORM objects that this Query would return from a method
such as the .all() method. The Query object, when asked to return full
entities, will deduplicate entries based on primary key, meaning if the
same primary key value would appear in the results more than once, only one
object of that primary key would be present. This does not apply to a query
that is against individual columns.


Count
-----
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.count


Use Case - 0x01
---------------
Count User records, without sing a subquery

>>> from sqlalchemy import func
>>>
>>>
>>> query = select(func.count(User.id))
>>>
>>> with session.begin() as db:
...     result = db.execute(query)


Use Case - 0x02
---------------
Return count of user 'id' grouped by 'name'

>>> from sqlalchemy import func
>>>
>>>
>>> query = (
...     select(func.count(User.id)).
...     group_by(User.name))
>>>
>>> with session.begin() as db:
...     result = db.execute(query)


Use Case - 0x02
---------------
Count distinct 'name' values

>>> from sqlalchemy import func
>>> from sqlalchemy import distinct
>>>
>>>
>>> query = (
...     select(func.count(distinct(User.id)).
...     group_by(User.name)))
>>>
>>> with session.begin() as db:
...     result = db.execute(query)
