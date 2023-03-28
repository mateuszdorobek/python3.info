JSON Object
===========

SetUp
-----
>>> from pprint import pprint
>>> from dataclasses import dataclass
>>> import json


Encode Object
-------------
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
>>>
>>> DATA = User('Mark', 'Watney')
>>>
>>> data = vars(DATA)
>>> result = json.dumps(data)
>>>
>>> print(result)
{"firstname": "Mark", "lastname": "Watney"}


Decode Object
-------------
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
>>>
>>> DATA = """{
...   "firstname": "Mark",
...   "lastname": "Watney"
... }"""
>>>
>>> data = json.loads(DATA)
>>> result = User(**data)
>>>
>>> print(result)
User(firstname='Mark', lastname='Watney')


Object Encoder
--------------
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
>>>
>>> DATA = User('Mark', 'Watney')
>>>
>>>
>>> def encoder(obj):
...     return vars(obj)
>>>
>>>
>>> result = json.dumps(DATA, default=encoder)
>>> print(result)
{"firstname": "Mark", "lastname": "Watney"}


Object Decoder
--------------
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
>>>
>>> DATA = """{
...   "firstname": "Mark",
...   "lastname": "Watney"
... }"""
>>>
>>>
>>> def decoder(data):
...     return User(**data)
>>>
>>>
>>> result =  json.loads(DATA, object_hook=decoder)
>>> print(result)
User(firstname='Mark', lastname='Watney')


Encode Object with Relation
---------------------------
>>> @dataclass
... class Group:
...     gid: int
...     name: str
>>>
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     groups: list[Group]
>>>
>>>
>>> DATA = [
...     User('Mark', 'Watney', groups=[
...         Group(gid=1, name='users')]),
...     User('Melissa', 'Lewis', groups=[
...         Group(gid=1, name='users'),
...         Group(gid=2, name='admins')]),
...     User('Rick', 'Martinez', groups=[]),
... ]
>>>
>>>
>>> def encoder(obj):
...     data = {'_clsname': obj.__class__.__name__}
...     return data | vars(obj)
>>>
>>>
>>> result = json.dumps(DATA, default=encoder, indent=2)
>>> print(result)
[
  {
    "_clsname": "User",
    "firstname": "Mark",
    "lastname": "Watney",
    "groups": [
      {
        "_clsname": "Group",
        "gid": 1,
        "name": "users"
      }
    ]
  },
  {
    "_clsname": "User",
    "firstname": "Melissa",
    "lastname": "Lewis",
    "groups": [
      {
        "_clsname": "Group",
        "gid": 1,
        "name": "users"
      },
      {
        "_clsname": "Group",
        "gid": 2,
        "name": "admins"
      }
    ]
  },
  {
    "_clsname": "User",
    "firstname": "Rick",
    "lastname": "Martinez",
    "groups": []
  }
]


Decode
------
Encoding nested objects with relations to JSON:

>>> @dataclass
... class Group:
...     gid: int
...     name: str
>>>
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...     role: str
...     groups: list[Group]
>>>
>>>
>>> DATA = (
...     '[{"_clsname":"User","firstname":"Mark","lastname":"Watney","rol'
...     'e":"user","groups":[{"_clsname":"Group","gid":1,"name":"users"}'
...     ']},{"_clsname":"User","firstname":"Melissa","lastname":"Lewis",'
...     '"role":"admin","groups":[{"_clsname":"Group","gid":1,"name":"us'
...     'ers"},{"_clsname":"Group","gid":2,"name":"admins"}]},{"_clsname'
...     '":"User","firstname":"Rick","lastname":"Martinez","role":"guest'
...     '","groups":[]}]'
... )
>>>
>>>
>>> def decoder(obj):
...     clsname = obj.pop('_clsname')
...     cls = globals()[clsname]
...     return cls(**obj)
>>>
>>>
>>> result = json.loads(DATA, object_hook=decoder)
>>> pprint(result, width=72)
[User(firstname='Mark',
      lastname='Watney',
      role='user',
      groups=[Group(gid=1, name='users')]),
 User(firstname='Melissa',
      lastname='Lewis',
      role='admin',
      groups=[Group(gid=1, name='users'), Group(gid=2, name='admins')]),
 User(firstname='Rick', lastname='Martinez', role='guest', groups=[])]


Use Case - 0x01
---------------
>>> import json
>>> from dataclasses import dataclass, field
>>> from pprint import pprint
>>>
>>>
>>> @dataclass
... class Group:
...     gid: int
...     name: str
>>>
>>> @dataclass
... class User:
...     lastname: str
...     firstname: str
...     groups: list[Group]
>>>
>>>
>>> DATA = [
...     User('Mark', 'Watney', groups=[
...         Group(gid=1, name='users')]),
...     User('Melissa', 'Lewis', groups=[
...         Group(gid=1, name='users'),
...         Group(gid=2, name='admins')]),
...     User('Rick', 'Martinez', groups=[]),
... ]

>>> class Encoder(json.JSONEncoder):
...     def default(self, obj):
...         data = vars(obj)
...         data['_clsname'] = obj.__class__.__name__
...         return data
>>>
>>>
>>> result = json.dumps(DATA, cls=Encoder)
>>> pprint(result, width=72)
('[{"lastname": "Mark", "firstname": "Watney", "groups": [{"gid": 1, '
 '"name": "users", "_clsname": "Group"}], "_clsname": "User"}, '
 '{"lastname": "Melissa", "firstname": "Lewis", "groups": [{"gid": 1, '
 '"name": "users", "_clsname": "Group"}, {"gid": 2, "name": "admins", '
 '"_clsname": "Group"}], "_clsname": "User"}, {"lastname": "Rick", '
 '"firstname": "Martinez", "groups": [], "_clsname": "User"}]')

>>> class Decoder(json.JSONDecoder):
...     def __init__(self):
...         super().__init__(object_hook=self.default)
...
...     def default(self, data: dict) -> dict:
...         clsname = data.pop('_clsname')
...         cls = globals()[clsname]
...         return cls(**data)
>>>
>>>
>>> result = json.loads(result, cls=Decoder)
>>> pprint(result, width=72)
[User(lastname='Mark',
      firstname='Watney',
      groups=[Group(gid=1, name='users')]),
 User(lastname='Melissa',
      firstname='Lewis',
      groups=[Group(gid=1, name='users'), Group(gid=2, name='admins')]),
 User(lastname='Rick', firstname='Martinez', groups=[])]


Assignments
-----------
.. literalinclude:: assignments/json_object_a.py
    :caption: :download:`Solution <assignments/json_object_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/json_object_b.py
    :caption: :download:`Solution <assignments/json_object_b.py>`
    :end-before: # Solution
