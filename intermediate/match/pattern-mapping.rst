Match Mapping
=============
* https://peps.python.org/pep-0622/#mapping-patterns

A mapping pattern looks like ``{"user": u, "emails": [*es]}``. It
matches mappings with at least the set of provided keys, and if all the
sub-patterns match their corresponding values. It binds whatever the
sub-patterns bind while matching with the values corresponding to the
keys. Adding **rest at the end of the pattern to capture extra items
is allowed.

SetUp:

>>> def login_user(firstname, lastname): ...
>>> def login_admin(firstname, lastname): ...

Usage:

>>> user = {'role': 'admin', 'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> match user:
...     case {'role': 'admin', 'firstname': firstname, 'lastname': lastname}:
...         login_admin(firstname, lastname)
...
...     case {'role': 'user', 'firstname': firstname, 'lastname': lastname}:
...         login_user(firstname, lastname)


Args, Kwargs
------------
>>> user = {'role': 'admin', 'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> match user:
...     case {'role': 'admin', **data}:  login_admin(**data)
...     case {'role': 'user', **data}:   login_user(**data)
