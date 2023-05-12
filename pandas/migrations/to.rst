DataFrame Export
================
* File paths works also with DATAs
* SQL functions uses SQLAlchemy, which supports many RDBMS


SetUp
-----
>>> import pandas as pd
>>>
>>> df = pd.DataFrame()


Most Frequently Used
--------------------
>>> # doctest: +SKIP
... df.to_csv()
... df.to_dict()
... df.to_excel()
... df.to_json()
... df.to_sql()


Other
-----
>>> # doctest: +SKIP
... df.to_clipboard()
... df.to_dense()
... df.to_feather()
... df.to_gbq()
... df.to_hdf()
... df.to_html()
... df.to_latex()
... df.to_msgpack()
... df.to_numpy()
... df.to_parquet()
... df.to_period()
... df.to_pickle()
... df.to_records()
... df.to_sparse()
... df.to_stata()
... df.to_string()
... df.to_timestamp()
... df.to_xarray()


Assignments
-----------
.. literalinclude:: assignments/pandas_tocsv_a.py
    :caption: :download:`Solution <assignments/pandas_tocsv_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_tojson_a.py
    :caption: :download:`Solution <assignments/pandas_tojson_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_topickle_a.py
    :caption: :download:`Solution <assignments/pandas_topickle_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_tosql_a.py
    :caption: :download:`Solution <assignments/pandas_tosql_a.py>`
    :end-before: # Solution
