.. testsetup::

    # doctest: +SKIP_FILE


Query Filter
============
* Filter
* Filter By
* Where


Filter
------
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.filter


Filter By
---------
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.filter_by


Where
-----
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.where

>>> shrew = Animal(u'shrew')
>>> shrew[u'cuteness'] = 5
>>> shrew[u'weasel-like'] = False
>>> shrew[u'poisonous'] = True
>>>
>>> session.add(shrew)
>>> session.flush()
>>>
>>> q = (session.query(Animal).
...      filter(Animal.facts.any(
...        and_(AnimalFact.key == u'weasel-like',
...             AnimalFact.value == True))))
>>> print('weasel-like animals', q.all())
