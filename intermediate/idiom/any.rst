Idiom Any
=========
* Return True if any element of the iterable is true.
* If the iterable is empty, return False.
* Built-in (evaluated)

>>> DATA = [True, False, True]
>>>
>>> any(DATA)
True


Solution
--------
>>> def any(iterable):
...     if not iterable:
...         return False
...     for element in iterable:
...         if element:
...             return True
...     return False


Use Case - 0x01
---------------
>>> any(x for x in range(0,5))
True


Use Case - 0x02
---------------
>>> USERS = [
...     {'is_admin': True,  'name': 'Mark Watney'},
...     {'is_admin': True,  'name': 'Melisa Lewis'},
...     {'is_admin': False, 'name': 'Rick Martinez'},
...     {'is_admin': True,  'name': 'Alex Vogel'},
...     {'is_admin': False, 'name': 'Beth Johanssen'},
...     {'is_admin': False, 'name': 'Chris Beck'},
... ]
>>>
>>>
>>> if any(user['is_admin'] for user in USERS):
...     print('At least one person is an administrator')
... else:
...     print('There are no administrators')
At least one person is an administrator
