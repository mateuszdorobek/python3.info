Regex RE Split
==============
* ``re.split()``
* Split text by pattern


Example
-------
Usage of ``re.split()``:

>>> import re
>>>
>>>
>>> DATA = 'Baked Beans And Spam'
>>> PATTERN = r'\s[a-z]{3}\s'
>>>
>>> re.split(PATTERN, DATA, flags=re.IGNORECASE)
['Baked Beans', 'Spam']


Use Case - 0x01
---------------
* Making a Phonebook

>>> import re
>>>
>>>
>>> TEXT = """Pan Twardowski: 834.345.1254 Polish Space Agency
...
... Mark Watney: 892.345.3428 Johnson Space Center
... Matt Kowalski: 925.541.7625 Kennedy Space Center
...
...
... Melissa Lewis: 548.326.4584 Bajkonur, Kazakhstan"""
>>>
>>> entries = re.split(r'\n+', TEXT)
>>> print(entries)  # doctest: +NORMALIZE_WHITESPACE
['Pan Twardowski: 834.345.1254 Polish Space Agency',
 'Mark Watney: 892.345.3428 Johnson Space Center',
 'Matt Kowalski: 925.541.7625 Kennedy Space Center',
 'Melissa Lewis: 548.326.4584 Bajkonur, Kazakhstan']
>>>
>>> result = [re.split(r':?\s', entry, maxsplit=3) for entry in entries]
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[['Pan', 'Twardowski', '834.345.1254', 'Polish Space Agency'],
 ['Mark', 'Watney', '892.345.3428', 'Johnson Space Center'],
 ['Matt', 'Kowalski', '925.541.7625', 'Kennedy Space Center'],
 ['Melissa', 'Lewis', '548.326.4584', 'Bajkonur, Kazakhstan']]


Assignments
-----------
.. literalinclude:: assignments/re_split_a.py
    :caption: :download:`Solution <assignments/re_split_a.py>`
    :end-before: # Solution
