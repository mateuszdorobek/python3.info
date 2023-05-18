Comprehension Dict
==================


Syntax
------
Short syntax:

>>> {x:None for x in range(0,5)}
{0: None, 1: None, 2: None, 3: None, 4: None}

Long syntax:

>>> dict((x,None) for x in range(0,5))
{0: None, 1: None, 2: None, 3: None, 4: None}


Example
-------
>>> {x:x for x in range(0,5)}
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

>>> {x:None for x in range(0,5)}
{0: None, 1: None, 2: None, 3: None, 4: None}

>>> {None:x for x in range(0,5)}
{None: 4}


Dict Collision
--------------
Recap information about dict keys collision. Duplicating items are overridden
by the latter:

>>> data = {
...     'commander': 'Mark Watney',
...     'commander': 'Melissa Lewis',
... }
>>>
>>> data
{'commander': 'Melissa Lewis'}

While generating ``dict`` with unique keys, there are no collisions:

>>> {x:None for x in range(0,5)}
{0: None, 1: None, 2: None, 3: None, 4: None}

Although when generating ``dict`` with constant key, it will be overridden
by the last one:

>>> {None:x for x in range(0,5)}
{None: 4}


Modify Key/Values
-----------------
Modify keys:

>>> {x+10:x for x in range(0,5)}
{10: 0, 11: 1, 12: 2, 13: 3, 14: 4}

Modify values:

>>> {x:x+10 for x in range(0,5)}
{0: 10, 1: 11, 2: 12, 3: 13, 4: 14}

Modify keys and values:

>>> {x+10:x+10 for x in range(0,5)}
{10: 10, 11: 11, 12: 12, 13: 13, 14: 14}


Dict Reversal
-------------
Swap ``dict`` keys with values.

Algorithm:

>>> DATA = {
...     'mlewis': 'Melissa Lewis',
...     'mwatney': 'Mark Watney',
...     'rmartinez': 'Rick Martinez',
... }
>>>
>>>
>>> result = {}
>>>
>>> for username, user in DATA.items():
...     result[user] = username
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
{'Melissa Lewis': 'mlewis',
 'Mark Watney': 'mwatney',
 'Rick Martinez': 'rmartinez'}

Dict comprehension:

>>> DATA = {
...     'mlewis': 'Melissa Lewis',
...     'mwatney': 'Mark Watney',
...     'rmartinez': 'Rick Martinez',
... }
>>>
>>>
>>> result = {user:username for username,user in DATA.items()}
>>> result = {v:k for k,v in DATA.items()}
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
{'Melissa Lewis': 'mlewis',
 'Mark Watney': 'mwatney',
 'Rick Martinez': 'rmartinez'}


Dict Reversal Collision
-----------------------
>>> DATA = {'a': 1, 'b': 2}
>>>
>>>
>>> {v:k for k,v in DATA.items()}
{1: 'a', 2: 'b'}

Value collision while reversing ``dict``:

>>> DATA = {'a': 1, 'b': 2, 'c': 2}
>>>
>>> {v:k for k,v in DATA.items()}
{1: 'a', 2: 'c'}


Use Case - 0x01
---------------
*  Even or Odd

>>> result = {}
>>>
>>> for x in range(0,5):
...     is_even = (x % 2 == 0)
...     result.update({x: is_even})
>>>
>>> print(result)
{0: True, 1: False, 2: True, 3: False, 4: True}

>>> {x: (x%2==0) for x in range(0,5)}
{0: True, 1: False, 2: True, 3: False, 4: True}


Assignments
-----------
.. literalinclude:: assignments/comprehension_dict_a.py
    :caption: :download:`Solution <assignments/comprehension_dict_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/comprehension_dict_b.py
    :caption: :download:`Solution <assignments/comprehension_dict_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/comprehension_dict_c.py
    :caption: :download:`Solution <assignments/comprehension_dict_c.py>`
    :end-before: # Solution
