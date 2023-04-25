Operator Contains
=================
* ``in`` - contains
* ``y in x`` - will call "contains" on object x (``x.__contains__(y)``)


Example
-------
>>> class Crew:
...     def __init__(self):
...         self.members = []
...
...     def __iadd__(self, astronaut):
...         self.members.append(astronaut)
...         return self
...
...     def __contains__(self, astronaut):
...         for member in self.members:
...             if member == astronaut:
...                 return True
...         return False
>>>
>>>
>>> ares3 = Crew()
>>> ares3 += 'Mark Watney'
>>> ares3 += 'Melissa Lewis'
>>> ares3 += 'Rick Martinez'
>>>
>>>
>>> 'Mark Watney' in ares3
True
>>>
>>> 'Alex Vogel' in ares3
False


Assignments
-----------
.. literalinclude:: assignments/operator_contains_a.py
    :caption: :download:`Solution <assignments/operator_contains_a.py>`
    :end-before: # Solution
