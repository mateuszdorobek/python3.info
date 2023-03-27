Idiom Iter
==========

Range
-----
>>> for i in range(0,3):
...     print(i)
0
1
2


Enumerate
---------
>>> months = ['January', 'February', 'March']
>>>
>>> for i, month in enumerate(months, start=1):
...     print(f'{i=}, {month=}')
i=1, month='January'
i=2, month='February'
i=3, month='March'


Zip
---
>>> roles = ['botanist', 'commander', 'pilot']
>>> names = ['Mark Watney', 'Melissa Lewis', 'Rick Martinez']
>>>
>>> for role, name in zip(roles, names):
...     print(f'{role=}, {name=}')
role='botanist', name='Mark Watney'
role='commander', name='Melissa Lewis'
role='pilot', name='Rick Martinez'
