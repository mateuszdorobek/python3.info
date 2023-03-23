Mapping Items
=============
* Key-Value Pairs



Get Key-Value Pairs
-------------------
In Python 2, the methods ``items()``, ``keys()`` and ``values()`` used to
"take a snapshot" of the dictionary contents and return it as a list. It
meant that if the dictionary changed while you were iterating over the list,
the contents in the list would not change. In Python 3, these methods return
a view object whose contents change dynamically as the dictionary changes.
Therefore, in order for the behavior of iterations over the result of these
methods to remain consistent with previous versions, an additional call to
``list()` has to be performed in Python 3 to "take a snapshot" of the view
object contents [#Hamidi2017]_.

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez',
... }
>>>
>>>
>>> crew.items()
dict_items([('commander', 'Melissa Lewis'), ('botanist', 'Mark Watney'), ('pilot', 'Rick Martinez')])
>>>
>>> list(crew.items())  # doctest: +NORMALIZE_WHITESPACE
[('commander', 'Melissa Lewis'),
 ('botanist', 'Mark Watney'),
 ('pilot', 'Rick Martinez')]


References
----------
.. [#Hamidi2017] Frédéric Hamidi. Why does Python 3 need dict.items to be wrapped with list()? Retrieved: 2021-02-28. URL: https://stackoverflow.com/a/17695716


Assignments
-----------
.. literalinclude:: assignments/mapping_items_a.py
    :caption: :download:`Solution <assignments/mapping_items_a.py>`
    :end-before: # Solution
