Collections Defaultdict
=======================

`defaultdict` is a subclass of the built-in `dict` class in Python. It
overrides one method and adds one writable instance variable. The
`defaultdict` class is used when you want to create a dictionary with
default values for keys that have not been set yet.

The default value is specified as a parameter when creating the
`defaultdict`. If a key is not found in the dictionary, instead of a
`KeyError` being thrown, a new entry is created. The type of this new entry
is specified by the argument of `defaultdict`.

Here's an example:

>>> from collections import defaultdict
>>>
>>> d = defaultdict(int)
>>> d['a'] += 1
>>> d['b'] += 2
>>> d['c']  # returns 0, since it was not set yet
0

In this example, we create a `defaultdict` with a default value of 0. We
then set the values of keys 'a' and 'b'. When we try to access the value of
key 'c', which was not set yet, it returns the default value of 0.


SetUp
-----
>>> from collections import defaultdict


Example
-------
>>> data = defaultdict(str)
>>>
>>>
>>> data
defaultdict(<class 'str'>, {})
>>>
>>> data['firstname'] = 'Mark'
>>> data['firstname']
'Mark'
>>>
>>> data['lastname']
''
>>>
>>> data
defaultdict(<class 'str'>, {'firstname': 'Mark', 'lastname': ''})


Empty Values
------------
>>> data = defaultdict(lambda: None)
>>>
>>> data['latin_name']

>>> from types import NoneType
>>>
>>> data = defaultdict(NoneType)
>>>
>>> data['latin_name']
>>> data
defaultdict(<class 'NoneType'>, {'latin_name': None})


Dict to Defaultdict
-------------------
>>> PLATYPUS = {'english_name': 'Platypus'}
>>>
>>> data = defaultdict(NoneType, **PLATYPUS)
>>>
>>> data['english_name']
'Platypus'
>>>
>>> data['latin_name']
