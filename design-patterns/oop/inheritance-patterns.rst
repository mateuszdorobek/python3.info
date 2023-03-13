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
...     def __init__(self, mother=Mother(), father=Father()):
...         self.mother = mother
...         self.father = father

>>> class StepFather:
...     pass
>>>
>>> me = Child(father=StepFather())


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

Aggregation:

>>> class Mother:
...     pass
>>>
>>> class Father:
...     pass
>>>
>>> class Child:
...     parents = [Father, Mother]


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
...     def __init__(self, mother=Mother(), father=Father()):
...         self.mother = mother
...         self.father = father


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
...     def __init__(self, windows=Windows(), engine=Engine()):
...         self.windows = windows
...         self.engine = engine
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
...                  encoder: Encoder = Encoder(),
...                  decoder: Decoder = Decoder(),
...                  ) -> None:
...         self.encoder = encoder
...         self.decoder = decoder
...
...     def encode(self, data):
...        return self.encoder.encode(data)
...
...     def decode(self, data):
...         return self.decoder.decode(data)
>>>
>>>
>>> DATA = {'firstname': 'Mark', 'lastname': 'Watney'}

Now, if you want to serialize your data, just create an instance
and call method ``.encode()`` on it.

>>> json = JSONSerializer()
>>> result = json.encode(DATA)

If you want to use your better version of encoder (for example which
can encode ``datetime`` object. You can create a class which inherits
from default ``Encoder`` and overwrite ``.encode()`` method.

>>> class MyBetterEncoder(Encoder):
...     def encode(self):
...         ...
>>>
>>> json = JSONSerializer(encoder=MyBetterEncoder)
>>> result = json.encode(DATA)


Use Case - 0x05
---------------
>>> from datetime import date
>>> import json

>>> DATA = {'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> json.dumps(DATA)
'{"firstname": "Mark", "lastname": "Watney"}'

>>> DATA = {'firstname': 'Mark', 'lastname': 'Watney', 'birthday': date(1969, 7, 21)}
>>>
>>> json.dumps(DATA)
Traceback (most recent call last):
TypeError: Object of type date is not JSON serializable

>>> class Encoder(json.JSONEncoder):
...     def default(self, x):
...         if isinstance(x, date):
...             return x.isoformat()
...
>>>
>>> DATA = {'firstname': 'Mark', 'lastname': 'Watney', 'birthday': date(1969, 7, 21)}
>>>
>>> json.dumps(DATA, cls=Encoder)
'{"firstname": "Mark", "lastname": "Watney", "birthday": "1969-07-21"}'


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
