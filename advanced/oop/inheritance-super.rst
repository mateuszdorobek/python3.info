OOP Inheritance Super
=====================


Super
-----
* Order is important
* Raymond Hettinger - Super considered super! - PyCon 2015 [#Hettinger2015]_

>>> class Account:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
...         self.groups = []
>>>
>>>
>>> class User(Account):
...     def __init__(self):
...         super().__init__()
...         self.groups = ['admins']
>>>
>>>
>>> mark = User()
>>> print(vars(mark))
{'firstname': 'Mark', 'lastname': 'Watney', 'groups': ['admins']}

>>> class Account:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
...         self.groups = []
>>>
>>>
>>> class User(Account):
...     def __init__(self):
...         self.groups = ['admins']
...         super().__init__()
>>>
>>>
>>> mark = User()
>>> print(vars(mark))
{'groups': [], 'firstname': 'Mark', 'lastname': 'Watney'}


Init and Multiple Inheritance
-----------------------------
Multiple inheritance in Python needs to be cooperative. That is,
the two parent classes need to be aware of the possibility that
each other exist (though they don't need to know any of each other's
details). Then whichever parent is named first can call the other
parent's ``__init__`` method. That's how super works, it always calls
the next class in the MRO (the method resolution order) of the instance
being operated on.

>>> class HasPosition:
...     def __init__(self):
...         self.x = 0
...         self.y = 0
>>>
>>> class HasHealth:
...     def __init__(self):
...         self.health = 100
>>>
>>>
>>> class Hero(HasPosition, HasHealth):
...     def __init__(self, name):
...         self.name = name
...         super().__init__()
>>>
>>>
>>> mark = Hero('Mark Watney')
>>> vars(mark)
{'name': 'Mark Watney', 'x': 0, 'y': 0}

>>> class HasPosition:
...     def __init__(self):
...         self.x = 0
...         self.y = 0
>>>
>>> class HasHealth:
...     def __init__(self):
...         self.health = 100
>>>
>>>
>>> class Hero(HasPosition, HasHealth):
...     def __init__(self, name):
...         self.name = name
...         super().__init__()
...         super().super().__init__()
>>>
>>>
>>> mark = Hero('Mark Watney')
Traceback (most recent call last):
AttributeError: 'super' object has no attribute 'super'

>>> class HasPosition:
...     def __init__(self):
...         self.x = 0
...         self.y = 0
>>>
>>> class HasHealth:
...     def __init__(self):
...         self.health = 100
>>>
>>>
>>> class Hero(HasPosition, HasHealth):
...     def __init__(self, name):
...         self.name = name
...         x = super()
...         print('Obj:', x)
...         print('Type:', type(x))
...         print('Vars:', vars(x))
...         print('Dir:', dir(x))
>>>
>>> mark = Hero('Mark Watney')
Obj: <super: <class 'Hero'>, <Hero object>>
Type: <class 'super'>
Vars: {'name': 'Mark Watney'}
Dir: ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__self_class__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__thisclass__', 'name']


Init Subclass
-------------
>>> class HasPosition:
...     def __init_subclass__(cls, **kwargs):
...         super().__init_subclass__(**kwargs)
...         cls.position_x = 0
...         cls.position_y = 0
>>>
>>>
>>> class HasHealth:
...     def __init_subclass__(cls, **kwargs):
...         super().__init_subclass__(**kwargs)
...         cls.health = 100
>>>
>>>
>>> class Hero(HasPosition, HasHealth):
...     def __init__(self, name):
...         self.name = name
>>>
>>>
>>> vars(Hero)  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
mappingproxy({'__module__': '__main__',
              '__init__': <function Hero.__init__ at 0x...>,
              '__doc__': None,
              'health': 100,
              'position_x': 0,
              'position_y': 0})
>>>
>>>
>>> hero = Hero('Mark')
>>> vars(hero)
{'name': 'Mark'}

Init subclass can also take keyword arguments:

>>> class Account:
...     def __init_subclass__(cls, /, group, **kwargs):
...         super().__init_subclass__(**kwargs)
...         cls.group = group
>>>
>>>
>>> class User(Account, group='admins'):
...     pass


Use Case - 0x01
---------------
>>> x = True
>>>
>>>
>>> type(x)
<class 'bool'>
>>>
>>> bool.mro()
[<class 'bool'>, <class 'int'>, <class 'object'>]
>>>
>>>
>>> isinstance(True, bool)
True
>>>
>>> isinstance(True, int)
True
>>>
>>> isinstance(True, object)
True


References
----------
.. [#Hettinger2015] Hettinger R. Super considered super!. PyCon 2015. Year: 2020. Retrieved: 2022-07-13. URL: https://www.youtube.com/watch?v=EiOglTERPEo
