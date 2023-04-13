Case Study
==========


SetUp
-----
>>> from sqlalchemy import Table, Column, MetaData, select
>>> from sqlalchemy import String, Enum, Integer, Time, Date, DateTime
>>> from sqlalchemy import create_engine
>>> from sqlalchemy import select, distinct, func
>>>
>>>
>>> DATABASE = 'sqlite:///space.db'
>>> engine = create_engine(DATABASE)
>>> Model = MetaData()
>>>
>>>
>>> def debug(query):
...     compiled = query.compile(engine, compile_kwargs={'literal_binds': True})
...     print(compiled)
>>>
>>>
>>> apollo11 = Table('apollo11', Model,
...     Column('id', Integer, primary_key=True),
...     Column('datetime', DateTime),
...     Column('date', Date),
...     Column('time', Time),
...     Column('met', Integer, comment='Mission Elapsed Time'),
...     Column('category', Enum('CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG')),
...     Column('event', String(255)),
... )


SQLAlchemy ORM
--------------
>>> important_categories = (
...     select(distinct(apollo11.c.category)).
...     group_by(apollo11.c.category).
...     having(func.count(apollo11.c.category) < 50).
...     order_by(apollo11.c.category.asc()).
...     limit(5).
...     offset(0)
... ).cte('important_categories')
>>>
>>> query = (
...     select(apollo11.c.datetime.label('dt'),
...            apollo11.c.category,
...            apollo11.c.event).
...
...     where((apollo11.c.category != 'DEBUG')
...         & (apollo11.c.date >= '1969-07-16')
...         & (apollo11.c.date <= '1969-07-24')
...         & ((apollo11.c.date == '1969-07-20') | (apollo11.c.date == '1969-07-21'))
...         & (apollo11.c.datetime.between('1969-07-20 20:17:41', '1969-07-21 15:00'))
...         & (apollo11.c.event.like('%CDR%'))
...         & (apollo11.c.category != None)
...         & (~apollo11.c.category.in_(['DEBUG', 'INFO']))
...         & (apollo11.c.category.in_(['CRITICAL', 'ERROR']))
...         & (apollo11.c.category.in_(important_categories))).
...
...     order_by(apollo11.c.category.desc(),
...              apollo11.c.date.asc().nullsfirst(),
...              apollo11.c.time.asc().nullslast()).
...
...     limit(30).
...     offset(0)
... )
>>>
>>>
>>> debug(query)  # doctest: +NORMALIZE_WHITESPACE
WITH important_categories
  AS (SELECT DISTINCT apollo11.category AS anon_1
      FROM apollo11
      GROUP BY apollo11.category
      HAVING count(apollo11.category) < 50
      ORDER BY apollo11.category ASC
      LIMIT 5
      OFFSET 0)
SELECT apollo11.datetime AS dt,
       apollo11.category,
       apollo11.event
FROM apollo11
WHERE apollo11.category != 'DEBUG'
  AND apollo11.date >= '1969-07-16'
  AND apollo11.date <= '1969-07-24'
  AND (apollo11.date = '1969-07-20' OR apollo11.date = '1969-07-21')
  AND apollo11.datetime BETWEEN '1969-07-20 20:17:41' AND '1969-07-21 15:00'
  AND apollo11.event LIKE '%CDR%'
  AND apollo11.category IS NOT NULL
  AND (apollo11.category NOT IN ('DEBUG', 'INFO'))
  AND apollo11.category IN ('CRITICAL', 'ERROR')
  AND apollo11.category IN (SELECT important_categories.anon_1 FROM important_categories)
ORDER BY apollo11.category DESC,
         apollo11.date ASC NULLS FIRST,
         apollo11.time ASC NULLS LAST
LIMIT 30
OFFSET 0


Raw SQL
-------
.. code-block:: sql

    WITH important_categories AS (

        SELECT DISTINCT(category)
        FROM apollo11
        GROUP BY category
        HAVING COUNT(category) < 50
        ORDER BY category ASC
        LIMIT 5
        OFFSET 0

    )

    SELECT datetime AS dt,
           category,
           event

    FROM apollo11

    WHERE category != 'DEBUG'
      AND date >= '1969-07-16'
      AND date <= '1969-07-24'
      AND (date == '1969-07-20' OR date == '1969-07-21')
      AND datetime BETWEEN '1969-07-20 20:17:41' AND '1969-07-21 15:00'
      AND event LIKE '%CDR%'
      AND category IS NOT NULL
      AND category NOT IN ('DEBUG', 'INFO')
      AND category IN ('CRITICAL', 'ERROR')
      AND category IN important_categories
      AND category IN (

        SELECT DISTINCT(category)
        FROM apollo11
        GROUP BY category
        HAVING COUNT(category) < 50
        ORDER BY category ASC
        LIMIT 5
        OFFSET 0

      ) -- CRITICAL, ERROR


    ORDER BY category DESC,
             date ASC NULLS FIRST,
             time ASC NULLS LAST

    LIMIT 30
    OFFSET 0;
