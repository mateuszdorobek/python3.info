OOP Inheritance Patterns
========================
* no inheritance
* single inheritance
* multilevel inheritance
* multiple inheritance (mixin classes)

.. glossary::

    single inheritance
        One class inherits from one other class. Has one parent.

    multilevel inheritance
        One class inherits from other class, and yet another class inherits
        from it. This creates hierarchical structure.

    multiple inheritance
    mixin classes
        One class derives from several other classes at once.


No Inheritance
--------------
>>> class Vehicle:
...     pass
>>>
>>>
>>> class Car:
...     pass


Single Inheritance
------------------
>>> class Vehicle:
...     pass
>>>
>>>
>>> class Car(Vehicle):
...     pass


Multilevel Inheritance
----------------------
>>> class Vehicle:
...     pass
>>>
>>>
>>> class VehicleWithWindows(Vehicle):
...     pass
>>>
>>>
>>> class Car(VehicleWithWindows):
...     pass


Multiple Inheritance
--------------------
* ``HasEngine`` and ``HasWindows`` are Mixin Classes
* Such classes are usually called: ``EngineMixin``, ``WindowsMixin``

>>> class Vehicle:
...     pass
>>>
>>> class HasEngine:
...     pass
>>>
>>> class HasWindows:
...     pass
>>>
>>>
>>> class Car(Vehicle, HasEngine, HasWindows):
...     pass
...


Aggregation
-----------
>>> class Vehicle:
...     pass
...
>>> class Engine:
...     pass
...
>>> class Windows:
...     pass
...
>>>
>>> class Car(Vehicle):
...     parts = [Engine, Windows]


Composition
-----------
>>> class Vehicle:
...     pass
>>>
>>> class Engine:
...     pass
...
>>> class Windows:
...     pass
...
>>>
>>> class Car(Vehicle):
...     engine = Engine
...     windows = Windows


Why Composition?
----------------
>>> class Mother:
...     pass
>>>
>>> class Father:
...     pass
>>>
>>>
>>> class Child:
...     mother: Mother
...     father: Father
...
...     def __init__(self, mother=Mother, father=Father):
...         self.mother = mother()
...         self.father = father()

>>> class StepFather:
...     pass
>>>
>>> me = Child(father=StepFather)


Use Case - 0x01
---------------
Following example is simple and easy to understand, but not totally
accurate. Inheritance means, that a class is a specialized form of
its base. This results in a subclass being an instance of a superclass.
Which is weird when we think, that a ``Child`` might be its ``Parent``
in the same time.

No Inheritance:

>>> class Parent:
...     pass
>>>
>>>
>>> class Child:
...     pass

Single Inheritance:

>>> class Parent:
...     pass
>>>
>>>
>>> class Child(Parent):
...     pass


Multilevel Inheritance:

>>> class Grandparent:
...     pass
>>>
>>> class Parent(Grandparent):
...     pass
>>>
>>>
>>> class Child(Parent):
...     pass

Multiple Inheritance:

>>> class Mother:
...     pass
>>>
>>> class Father:
...     pass
>>>
>>>
>>> class Child(Mother, Father):
...     pass

Aggregation:

>>> class Mother:
...     pass
>>>
>>> class Father:
...     pass
>>>
>>> class Child:
...     parents = [Father, Mother]

Composition:

>>> class Mother:
...     pass
>>>
>>> class Father:
...     pass
>>>
>>> class Child:
...     mother = Mother
...     father = Father


Use Case - 0x02
---------------
>>> class Mother:
...     pass
>>>
>>> class Father:
...     pass
>>>
>>>
>>> class Child:
...     mother: Mother
...     father: Father
...
...     def __init__(self, mother=Mother, father=Father):
...         self.mother = mother()
...         self.father = father()


Use Case - 0x03
---------------
>>> class Vehicle:
...     engine: Engine
...     windows: Windows | None
>>>
>>> class Engine:
...     def engine_start(self): ...
...     def engine_stop(self): ...
...
>>> class Windows:
...     def window_open(self): ...
...     def window_close(self): ...
...
>>>
>>> class Car(Vehicle):
...     engine: Engine
...     windows: Windows
...
...     def __init__(self, windows=Windows, engine=Engine):
...         self.windows = windows()
...         self.engine = engine()
...
...     def engine_start(self):
...         if self.engine:
...             return self.engine.engine_start()
...
...     def engine_stop(self):
...         if self.engine:
...             return self.engine.engine_stop()
...
...     def window_open(self):
...         if self.windows:
...             return self.windows.windows_open()
...
...     def window_close(self):
...         if self.windows:
...             return self.windows.windows_close()


Use Case - 0x04
---------------
>>> class Encoder:
...     def encode(self, data):
...         ...
>>>
>>> class Decoder:
...     def decode(self, data):
...         ...
>>>
>>>
>>> class JSONSerializer:
...     encoder: Encoder
...     decoder: Decoder
...
...     def __init__(self,
...                  encoder: Encoder = Encoder,
...                  decoder: Decoder = Decoder,
...                  ) -> None:
...         self.encoder = encoder()
...         self.decoder = decoder()
...
...     def encode(self, data):
...        return self.encoder.encode(data)
...
...     def decode(self, data):
...         return self.decoder.decode(data)

Now, if you want to serialize your data, just create an instance
and call method ``.encode()`` on it.

>>> DATA = {'firstname': 'Mark', 'lastname': 'Watney'}
>>> json = JSONSerializer()
>>> result = json.encode(DATA)

If you want to use your better version of encoder (for example which
can encode ``datetime`` object. You can create a class which inherits
from default ``Encoder`` and overwrite ``.encode()`` method.

>>> class MyBetterEncoder(Encoder):
...     def encode(self, data):
...         ...
>>>
>>> DATA = {'firstname': 'Mark', 'lastname': 'Watney'}
>>> json = JSONSerializer(encoder=MyBetterEncoder)
>>> result = json.encode(DATA)


Use Case - 0x05
---------------
>>> from datetime import date
>>> import json

JSON dumps works well, we we don't have any exotic types:

>>> DATA = {'firstname': 'Mark', 'lastname': 'Watney'}
>>> json.dumps(DATA)
'{"firstname": "Mark", "lastname": "Watney"}'

When we introduce ``date`` object, JSON cannot serialize it:

>>> DATA = {'firstname': 'Mark', 'lastname': 'Watney', 'birthday': date(1969, 7, 21)}
>>> json.dumps(DATA)
Traceback (most recent call last):
TypeError: Object of type date is not JSON serializable

We can introduce ``MyEncoder`` and inject it into ``json.dumps()`` function:

>>> class MyEncoder(json.JSONEncoder):
...     def default(self, x):
...         if isinstance(x, date):
...             return x.isoformat()
...
>>>
>>> DATA = {'firstname': 'Mark', 'lastname': 'Watney', 'birthday': date(1969, 7, 21)}
>>> json.dumps(DATA, cls=MyEncoder)
'{"firstname": "Mark", "lastname": "Watney", "birthday": "1969-07-21"}'


Use Case - 0x06
---------------
Base classes:

>>> class Engine:
...     pass
>>>
>>> class Windows:
...     pass
>>>
>>> class Radio:
...     pass

Standard Classes:

>>> class StandardEngine(Engine):
...     pass
>>>
>>> class StandardWindows(Windows):
...     pass
>>>
>>> class StandardRadio(Radio):
...     pass

Define ``Vehicle`` using composition:

>>> class Vehicle:
...     engine: Engine
...     windows: Windows | None
...     radio: Radio | None
...
...     def __init__(self, engine=StandardEngine, windows=StandardWindows, radio=StandardRadio):
...         self.engine = engine()
...         self.windows = windows()
...         self.radio = radio()

Usage:

>>> class PoorEngine(Engine):
...     ...
>>>
>>> class ElectricEngine(Engine):
...     ...
>>>
>>> class SuperRadio(Radio):
...     ...
>>>
>>> mercedes = Vehicle()
>>> maluch = Vehicle(engine=PoorEngine)
>>> tesla = Vehicle(engine=ElectricEngine, radio=SuperRadio)

If not specified, car will use Standard part (such as ``StandardEngine``
or ``StandardRadio``). Thanks to composition we can override defaults.


Use Case - 0x07
---------------
>>> class Account:
...     def __init__(self, username):
...         self.username = username
>>>
>>> class User(Account):
...     pass
>>>
>>> class Admin(Account):
...     pass
>>>
>>>
>>> class Group:
...     members: list[Account] = [
...         User('mwatney'),
...         Admin('mlewis'),
...         User('rmartinez'),
...     ]


Use Case - 0x08
---------------
>>> import json
>>> import pickle
>>>
>>>
>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def to_json(self):
...         data = vars(self)
...         return json.dumps(data)
...
...     def to_pickle(self):
...         return pickle.dumps(self)
...
...     def to_csv(self):
...         values = tuple(vars(self).values())
...         return ','.join(values) + '\n'

>>> mark = User('Mark', 'Watney')
>>>
>>> mark.to_json()
'{"firstname": "Mark", "lastname": "Watney"}'
>>>
>>> mark.to_pickle()  # doctest: +SKIP
b'\x80\x04\x95D\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x04User\x94\x93\x94)\x81\x94}\x94(\x8c\tfirstname\x94\x8c\x04Mark\x94\x8c\x08lastname\x94\x8c\x06Watney\x94ub.'
>>>
>>> mark.to_csv()
'Mark,Watney\n'


Use Case - 0x09
---------------
>>> import json
>>> import pickle
>>>
>>>
>>> class Serializable:
...     def to_json(self):
...         data = vars(self)
...         return json.dumps(data)
...
...     def to_pickle(self):
...         return pickle.dumps(self)
...
...     def to_csv(self):
...         values = tuple(vars(self).values())
...         return ','.join(values) + '\n'

>>> class User(Serializable):
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> class Admin(Serializable):
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> class Group(Serializable):
...     def __init__(self, members):
...         self.members = members
...
...     def to_csv(self):
...         raise NotImplementedError

>>> mark = User('Mark', 'Watney')
>>>
>>> mark.to_json()
'{"firstname": "Mark", "lastname": "Watney"}'
>>>
>>> mark.to_pickle()  # doctest: +SKIP
b'\x80\x04\x95D\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x04User\x94\x93\x94)\x81\x94}\x94(\x8c\tfirstname\x94\x8c\x04Mark\x94\x8c\x08lastname\x94\x8c\x06Watney\x94ub.'
>>>
>>> mark.to_csv()
'Mark,Watney\n'


Use Case - 0x0A
---------------
>>> import json
>>> import pickle
>>>
>>>
>>> class JSONSerializable:
...     def to_json(self):
...         data = vars(self)
...         return json.dumps(data)
>>>
>>> class PickleSerializable:
...     def to_pickle(self):
...         return pickle.dumps(self)
>>>
>>> class CSVSerializable:
...     def to_csv(self):
...         values = tuple(vars(self).values())
...         return ','.join(values) + '\n'

>>> class User(JSONSerializable, PickleSerializable, CSVSerializable):
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> class Admin(JSONSerializable, PickleSerializable, CSVSerializable):
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> class Group(JSONSerializable, PickleSerializable):
...     def __init__(self, members):
...         self.members = members

>>> mark = User('Mark', 'Watney')
>>>
>>> mark.to_json()
'{"firstname": "Mark", "lastname": "Watney"}'
>>>
>>> mark.to_pickle()  # doctest: +SKIP
b'\x80\x04\x95D\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x04User\x94\x93\x94)\x81\x94}\x94(\x8c\tfirstname\x94\x8c\x04Mark\x94\x8c\x08lastname\x94\x8c\x06Watney\x94ub.'
>>>
>>> mark.to_csv()
'Mark,Watney\n'


Use Case - 0x0B
---------------
>>> import json
>>> import pickle
>>> from typing import Type
>>>
>>>
>>> class JSONSerializer:
...     @staticmethod
...     def to_json(instance):
...         fields = {k:v for k,v in vars(instance).items() if not k.startswith('_')}
...         return json.dumps(fields)
>>>
>>> class PickleSerializer:
...     @staticmethod
...     def to_pickle(instance):
...         fields = {k:v for k,v in vars(instance).items() if not k.startswith('_')}
...         return pickle.dumps(fields)
>>>
>>> class CSVSerializer:
...     @staticmethod
...     def to_csv(instance):
...         fields = {k:v for k,v in vars(instance).items() if not k.startswith('_')}
...         values = tuple(fields.values())
...         return ','.join(values) + '\n'
>>>
>>>
>>> class Serializable:
...     _json_serializer: Type[JSONSerializer] | None = None
...     _pickle_serializer: Type[PickleSerializer] | None = None
...     _csv_serializer: Type[CSVSerializer] | None = None
...
...     def to_json(self, cls=_json_serializer):
...         if cls is not None:
...             return cls.to_json(self)
...
...     def to_pickle(self, cls=_pickle_serializer):
...         if cls is not None:
...             return cls.to_pickle(self)
...
...     def to_csv(self, cls=_csv_serializer):
...         if cls is not None:
...             return cls.to_csv(self)

Groups are not CSV serializable:

>>> class Group(Serializable):
...     _json_serializer = JSONSerializer
...     _pickle_serializer = PickleSerializer
...     _csv_serializer = None
>>>
>>> class User(Serializable):
...     _json_serializer = JSONSerializer
...     _pickle_serializer = PickleSerializer
...     _csv_serializer = CSVSerializer
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname

Dump to JSON using default serializer:

>>> mark = User('Mark', 'Watney')
>>> mark.to_json()

Dump to JSON using custom serializer:

>>> class MyJSONSerializer(JSONSerializer):
...     @staticmethod
...     def to_json(instance):
...         ...
>>>
>>> mark = User('Mark', 'Watney')
>>> mark.to_json(cls=MyJSONSerializer)


Further Reading
---------------
* https://github.com/django/django/blob/main/django/views/generic/base.py
* https://github.com/pandas-dev/pandas/blob/main/pandas/core/frame.py
* https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/linear_model/_base.py#L533


Assignments
-----------
.. literalinclude:: assignments/oop_inheritance_patterns_a.py
    :caption: :download:`Solution <assignments/oop_inheritance_patterns_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_inheritance_patterns_b.py
    :caption: :download:`Solution <assignments/oop_inheritance_patterns_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_inheritance_patterns_c.py
    :caption: :download:`Solution <assignments/oop_inheritance_patterns_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_inheritance_patterns_d.py
    :caption: :download:`Solution <assignments/oop_inheritance_patterns_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_inheritance_patterns_e.py
    :caption: :download:`Solution <assignments/oop_inheritance_patterns_e.py>`
    :end-before: # Solution
