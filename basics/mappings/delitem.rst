Mapping DelItem
===============


Pop Method
----------
>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez',
...    'chemist': 'Alex Vogel',
...    'surgeon': 'Chris Beck',
...    'engineer': 'Beth Johanssen'}
>>>
>>>
>>> left_alone_on_mars = crew.pop('botanist')
>>>
>>> print(left_alone_on_mars)
Mark Watney
>>>
>>> print(crew)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'pilot': 'Rick Martinez',
 'chemist': 'Alex Vogel',
 'surgeon': 'Chris Beck',
 'engineer': 'Beth Johanssen'}


Popitem Method
--------------
>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>>
>>> last = crew.popitem()
>>>
>>> print(last)
('pilot', 'Rick Martinez')
>>>
>>> print(crew)
{'commander': 'Melissa Lewis', 'botanist': 'Mark Watney'}


Del Keyword
-----------
>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>>
>>> del crew['pilot']
>>>
>>> print(crew)
{'commander': 'Melissa Lewis', 'botanist': 'Mark Watney'}


.. todo:: Assignment with delitem
.. todo:: Assignment with .clear()
.. todo:: Assignment with .pop()
.. todo:: Assignment with .popitem()
