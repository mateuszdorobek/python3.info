Read JSON
=========
* File paths works also with URLs
* File can be compressed with ``.gz``, ``.bz2``, ``.zip``, ``.xz``


Compressed
----------
* If the extension is ``.gz``, ``.bz2``, ``.zip``, and ``.xz``, the corresponding compression method is automatically selected

>>> df = pd.read_json('sample_file.zip', compression='zip')  # doctest: +SKIP
>>> df = pd.read_json('sample_file.gz', compression='infer')  # doctest: +SKIP


Assignments
-----------
.. literalinclude:: assignments/pandas_readjson_a.py
    :caption: :download:`Solution <assignments/pandas_readjson_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_readjson_b.py
    :caption: :download:`Solution <assignments/pandas_readjson_b.py>`
    :end-before: # Solution
