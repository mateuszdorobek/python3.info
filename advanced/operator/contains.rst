Operator Contains
=================
* ``in`` - contains
* ``y in x`` - will call "contains" on object x (``x.__contains__(y)``)


Example
-------
>>> class Group:
...     def __init__(self):
...         self.members = []
...
...     def __iadd__(self, user):
...         self.members.append(user)
...         return self
...
...     def __contains__(self, user):
...         return user in self.members
>>>
>>>
>>> admins = Group()
>>> admins += 'mwatney'
>>> admins += 'mlewis'
>>> admins += 'rmartinez'
>>>
>>> admins.members
['mwatney', 'mlewis', 'rmartinez']
>>>
>>> 'mwatney' in admins
True
>>>
>>> 'avogel' in admins
False


Implementation
--------------
>>> class Group:
...     def __init__(self):
...         self.members = []
...
...     def __iadd__(self, user):
...         self.members.append(user)
...         return self
...
...     def __contains__(self, user):
...         for member in self.members:
...             if member == user:
...                 return True
...         return False
>>>
>>>
>>> admins = Group()
>>> admins += 'mwatney'
>>> admins += 'mlewis'
>>> admins += 'rmartinez'
>>>
>>> admins.members
['mwatney', 'mlewis', 'rmartinez']
>>>
>>> 'mwatney' in admins
True
>>>
>>> 'avogel' in admins
False


Assignments
-----------
.. literalinclude:: assignments/operator_contains_a.py
    :caption: :download:`Solution <assignments/operator_contains_a.py>`
    :end-before: # Solution
