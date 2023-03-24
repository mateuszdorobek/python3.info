OOP Class Instance
==================
* Definition: instance - object created from class
* Instances are objects
* Convention: ``snake_case`` names
* Convention: Two newlines between class and instances

.. glossary::

    instance
    object
        Computer software entity created from a class.


Class vs Instance
-----------------
.. figure:: img/oop-classes-class.jpg

    Class. Source: [#class]_

.. figure:: img/oop-classes-instances.jpg

    Instances. Source: [#instances]_


One Class, One Instance
-----------------------
One class and one instance:

>>> class User:
...     pass
...
>>> mark = User()


One Class, Many Instances
-------------------------
One class and three instances:

>>> class User:
...     pass
>>>
>>>
>>> mark = User()
>>> melissa = User()
>>> rick = User()


Many Classes, Many Instances
----------------------------
Two classes and six instances. One instance of an ``Admin`` class, and
five instances of ``User`` class:

>>> class User:
...     pass
...
>>> class Admin:
...     pass
...
>>>
>>> melissa = Admin()
>>> mark = User()
>>> rick = User()
>>> alex = User()
>>> beth = User()
>>> chris = User()


Naming Convention
-----------------
>>> first_name = str()
>>> last_name = str()
>>>
>>> firstname = str()
>>> lastname = str()
>>>
>>> fname = str()
>>> lname = str()

>>> class User:
...     pass
...
>>>
>>> mark_watney = User()
>>> melissa_lewis = User()
>>>
>>> markwatney = User()
>>> melissalewis = User()
>>>
>>> mwatney = User()
>>> mlewis = User()


Type vs Isinstance
------------------
>>> class User:
...     pass
>>>
>>> mark = User()

>>> isinstance(mark, User)
True

>>> type(mark)
<class '__main__.User'>

>>> type(mark) is User
True
>>>
>>> mark is User
False


Use Case - 0x01
---------------
>>> x = int()
>>> y = int()
>>>
>>> x
0
>>> y
0

>>> class Int:
...     pass
...
>>> x = Int()
>>> y = Int()


Use Case - 0x02
---------------
>>> x = int()
>>> y = float()
>>>
>>> x
0
>>> y
0.0

>>> class Int:
...     pass
...
>>> class Float:
...     pass
...
>>> x = int()
>>> y = float()


Use Case - 0x03
---------------
>>> a = int()
>>> b = float()
>>> c = bool()
>>> d = str()
>>> e = list()
>>> f = tuple()
>>> g = set()
>>> h = dict()


Use Case - 0x04
---------------
>>> class Astronaut:
...     pass
>>>
>>>
>>> mark = Astronaut()
>>> melissa = Astronaut()
>>> rick = Astronaut()
>>> alex = Astronaut()
>>> beth = Astronaut()
>>> chris = Astronaut()


Use Case - 0x05
---------------
>>> class AstronautPilot:
...     pass
...
>>> class AstronautScientist:
...     pass
...
>>> class AstronautEngineer:
...     pass
...
>>> class AstronautMedic:
...     pass
>>>
>>>
>>>
>>> mark_watney = AstronautScientist()
>>> melissa_lewis = AstronautEngineer()
>>> rick_martinez = AstronautPilot()
>>> alex_vogel = AstronautScientist()
>>> beth_johanssen = AstronautEngineer()
>>> chris_beck = AstronautMedic()


References
----------
.. [#class] http://makieta.pl/12344-thickbox_default/faller-130803-blok-z-wielkiej-plyty-skala-h0.jpg
.. [#instances] https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Os_Rusa_Poznań_RB1.jpg/1200px-Os_Rusa_Poznań_RB1.jpg


Assignments
-----------
.. literalinclude:: assignments/oop_class_instance_a.py
    :caption: :download:`Solution <assignments/oop_class_instance_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_class_instance_b.py
    :caption: :download:`Solution <assignments/oop_class_instance_b.py>`
    :end-before: # Solution
