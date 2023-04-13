Func Numeric
============
* ``array_agg`` - Support for the ARRAY_AGG function
* ``count`` - The ANSI COUNT aggregate function. With no arguments, emits ``COUNT *``
* ``cube`` - Implement the CUBE grouping operation
* ``cume_dist`` - Implement the cume_dist hypothetical-set aggregate function
* ``dense_rank`` - Implement the dense_rank hypothetical-set aggregate function
* ``max`` - The SQL MAX() aggregate function
* ``min`` - The SQL MIN() aggregate function
* ``mode`` - Implement the mode ordered-set aggregate function
* ``percent_rank`` - Implement the percent_rank hypothetical-set aggregate function
* ``percentile_cont`` - Implement the percentile_cont ordered-set aggregate function
* ``percentile_disc`` - Implement the percentile_disc ordered-set aggregate function
* ``random`` - The RANDOM() SQL function
* ``rank`` - Implement the rank hypothetical-set aggregate function
* ``sum`` - The SQL SUM() aggregate function


About
-----
.. csv-table:: SQL and Generic Functions
    :widths: 20,80
    :header: "Object", "Name Description"

    "``array_agg``",             "Support for the ARRAY_AGG function"
    "``count``",                 "The ANSI COUNT aggregate function. With no arguments, emits COUNT *"
    "``cube``",                  "Implement the CUBE grouping operation"
    "``cume_dist``",             "Implement the cume_dist hypothetical-set aggregate function"
    "``dense_rank``",            "Implement the dense_rank hypothetical-set aggregate function"
    "``max``",                   "The SQL MAX() aggregate function"
    "``min``",                   "The SQL MIN() aggregate function"
    "``mode``",                  "Implement the mode ordered-set aggregate function"
    "``percent_rank``",          "Implement the percent_rank hypothetical-set aggregate function"
    "``percentile_cont``",       "Implement the percentile_cont ordered-set aggregate function"
    "``percentile_disc``",       "Implement the percentile_disc ordered-set aggregate function"
    "``random``",                "The RANDOM() SQL function"
    "``rank``",                  "Implement the rank hypothetical-set aggregate function"
    "``sum``",                   "The SQL SUM() aggregate function"


Count
-----
* https://docs.sqlalchemy.org/en/stable/core/functions.html#sqlalchemy.sql.functions.count

>>> from sqlalchemy import func
>>> from sqlalchemy import distinct

Count User records, without sing a subquery:

>>> session.query(func.count(User.id))  # doctest: +SKIP

Return count of user 'id' grouped by 'name':

>>> session.query(func.count(User.id)).\
...         group_by(User.name)  # doctest: +SKIP

Count distinct 'name' values:

>>> session.query(func.count(distinct(User.name)))  # doctest: +SKIP
