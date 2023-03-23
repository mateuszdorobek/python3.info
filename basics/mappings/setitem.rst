Mapping SetItem
===============
* Adds if value not exist
* Updates if value exist


Set Item Method
---------------
>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>>
>>> crew['chemist'] = 'Alex Vogel'
>>> print(crew)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'pilot': 'Rick Martinez',
 'chemist': 'Alex Vogel'}

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>>
>>> crew['commander'] = 'Alex Vogel'
>>> print(crew)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Alex Vogel',
 'botanist': 'Mark Watney',
 'pilot': 'Rick Martinez'}


Update Method
-------------
>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>>
>>> crew.update(chemist='Alex Vogel')
>>> print(crew)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'pilot': 'Rick Martinez',
 'chemist': 'Alex Vogel'}

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>>
>>> crew.update(commander='Alex Vogel')
>>> print(crew)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Alex Vogel',
 'botanist': 'Mark Watney',
 'pilot': 'Rick Martinez'}


.. todo:: Assignment with dict set item using []
.. todo:: Assignment with dict set item using update()
