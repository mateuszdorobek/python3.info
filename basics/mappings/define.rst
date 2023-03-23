Mapping Define
==============
* ``dict`` are key-value storage (HashMap)
* Mutable - can add, remove, and modify items
* Since Python 3.7: ``dict`` keeps order of elements
* Before Python 3.7: ``dict`` order is not ensured!!


Syntax
------
* ``{}`` is used more often
* ``dict()`` is more readable
* Comma after last element is optional

>>> data = {}
>>> data = dict()

>>> data = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez',
... }

>>> data = dict(
...     commander='Melissa Lewis',
...     botanist='Mark Watney',
...     pilot='Rick Martinez',
... )


Duplicates
----------
Duplicating items are overridden by latter:

>>> data = {
...     'commander': 'Mark Watney',
...     'commander': 'Melissa Lewis',
... }
>>>
>>> data
{'commander': 'Melissa Lewis'}


Dict vs Set
-----------
* Both ``set`` and ``dict`` keys must be hashable
* Both ``set`` and ``dict`` uses the same ``{`` and ``}`` braces
* Despite similar syntax, they are different types

>>> data = {1, 2}
>>> type(data)
<class 'set'>
>>>
>>>
>>> data = {1: 2}
>>> type(data)
<class 'dict'>

>>> data = {1, 2, 3, 4}
>>> type(data)
<class 'set'>
>>>
>>>
>>> data = {1: 2, 3: 4}
>>> type(data)
<class 'dict'>

Empty ``dict`` and empty ``set``:

>>> data = {1: None}
>>> _ = data.pop(1)
>>>
>>> data
{}

>>> data = {1}
>>> _ = data.pop()
>>>
>>> data
set()


Length
------
>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>>
>>> len(crew)
3
>>>
>>> len(crew.keys())
3
>>>
>>> len(crew.values())
3
>>>
>>> len(crew.items())
3


Use Case - 0x1
--------------
* GIT - version control system

>>> git = {
...    'ce16a8ce': 'commit/1',
...    'cae6b510': 'commit/2',
...    '895444a6': 'commit/3',
...    'aef731b5': 'commit/4',
...    '4a92bc79': 'branch/master',
...    'b3bbd85a': 'tag/v1.0',
... }


Assignments
-----------
.. literalinclude:: assignments/mapping_define_a.py
    :caption: :download:`Solution <assignments/mapping_define_a.py>`
    :end-before: # Solution

.. todo:: Assignment with dict define
