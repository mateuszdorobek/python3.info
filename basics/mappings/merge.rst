Mapping Merge
=============


Update Method
-------------
>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>> new = {
...    'chemist': 'Alex Vogel',
...    'surgeon': 'Chris Beck',
...    'engineer': 'Beth Johanssen'}
>>>
>>>
>>> crew.update(new)
>>> print(crew)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'pilot': 'Rick Martinez',
 'chemist': 'Alex Vogel',
 'surgeon': 'Chris Beck',
 'engineer': 'Beth Johanssen'}


Merge Operator
--------------
* Merge (``|``) and update (``|=``) operators have been added to the built-in dict class.
* Since Python 3.9: :pep:`584` -- Add Union Operators To dict

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>> new = {
...     'chemist': 'Alex Vogel',
...     'surgeon': 'Chris Beck',
...     'engineer': 'Beth Johanssen'}
>>>
>>>
>>> everyone = crew | new
>>>
>>> print(crew)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'pilot': 'Rick Martinez'}
>>>
>>> print(new)  # doctest: +NORMALIZE_WHITESPACE
{'chemist': 'Alex Vogel',
 'surgeon': 'Chris Beck',
 'engineer': 'Beth Johanssen'}
>>>
>>> print(everyone)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'pilot': 'Rick Martinez',
 'chemist': 'Alex Vogel',
 'surgeon': 'Chris Beck',
 'engineer': 'Beth Johanssen'}


Increment Merge Operator
------------------------
>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>> new = {
...     'chemist': 'Alex Vogel',
...     'surgeon': 'Chris Beck',
...     'engineer': 'Beth Johanssen'}
>>>
>>>
>>> crew |= new
>>>
>>> print(crew)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'pilot': 'Rick Martinez',
 'chemist': 'Alex Vogel',
 'surgeon': 'Chris Beck',
 'engineer': 'Beth Johanssen'}
>>>
>>> print(new)  # doctest: +NORMALIZE_WHITESPACE
{'chemist': 'Alex Vogel',
 'surgeon': 'Chris Beck',
 'engineer': 'Beth Johanssen'}


.. todo:: Assignment with merging dict using |
.. todo:: Assignment with merging dict using |=
.. todo:: Assignment with merging dict using update()

