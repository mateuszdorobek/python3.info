OOP Inheritance Patterns
========================
* No Inheritance
* Single Inheritance
* Multilevel Inheritance
* Multiple Inheritance (with mixin classes)

.. glossary::

    single inheritance
        One class inherits from one other class. Has one parent.

    multilevel inheritance
        One class inherits from other class, and yet another class inherits
        from it. This creates hierarchical structure.

    multiple inheritance
    mixin classes
        One class derives from several other classes at once.


Starting Point
--------------
>>> class Car:
...     pass
...
>>> class Truck:
...     pass
...
...
>>> maluch = Car()
>>> scania = Truck()


No Inheritance
--------------
>>> class Car:
...     def engine_start(self): ...
...     def engine_stop(self): ...
...
>>> class Truck:
...     def engine_start(self): ...
...     def engine_stop(self): ...
...
...
>>> maluch = Car()
>>> maluch.engine_start()
>>> maluch.engine_stop()
>>>
>>> scania = Truck()
>>> scania.engine_start()
>>> scania.engine_stop()


Single Inheritance
------------------
>>> class Vehicle:
...     def engine_start(self): ...
...     def engine_stop(self): ...
...
>>> class Car(Vehicle):
...     pass
...
>>> class Truck(Vehicle):
...     pass
...
...
>>> maluch = Car()
>>> maluch.engine_start()
>>> maluch.engine_stop()
>>>
>>> scania = Truck()
>>> scania.engine_start()
>>> scania.engine_stop()

Next:

>>> class Vehicle:
...     def engine_start(self): ...
...     def engine_stop(self): ...
...     def window_open(self): ...
...     def window_close(self): ...
...
>>> class Car(Vehicle):
...     pass
...
>>> class Truck(Vehicle):
...     pass
...
>>> maluch = Car()
>>> maluch.engine_start()
>>> maluch.engine_stop()
>>> maluch.window_open()
>>> maluch.window_close()
>>>
>>> scania = Truck()
>>> scania.engine_start()
>>> scania.engine_stop()
>>> scania.window_open()
>>> scania.window_close()

Problem:

>>> class Vehicle:
...     def engine_start(self): ...
...     def engine_stop(self): ...
...     def window_open(self): ...
...     def window_close(self): ...
...
>>> class Car(Vehicle):
...     pass
...
>>> class Truck(Vehicle):
...     pass
...
>>> class Motorbike(Vehicle):
...     pass
...
...
>>> maluch = Car()
>>> maluch.engine_start()
>>> maluch.engine_stop()
>>> maluch.window_open()
>>> maluch.window_close()
>>>
>>> scania = Truck()
>>> scania.engine_start()
>>> scania.engine_stop()
>>> scania.window_open()
>>> scania.window_close()
>>>
>>> yamaha = Motorbike()
>>> yamaha.engine_start()
>>> yamaha.engine_stop()
>>> yamaha.window_open()  # motorbikes don't have windows
>>> yamaha.window_close()  # motorbikes don't have windows

Solution 1 - code duplication:

>>> class Vehicle:
...     def engine_start(self): ...
...     def engine_stop(self): ...
>>>
>>> class Car(Vehicle):
...     def window_open(self): ...
...     def window_close(self): ...
>>>
>>> class Truck(Vehicle):
...     def window_open(self): ...
...     def window_close(self): ...
>>>
>>> class Motorbike(Vehicle):
...     pass
>>>
>>>
>>> maluch = Car()
>>> maluch.engine_start()
>>> maluch.engine_stop()
>>> maluch.window_open()
>>> maluch.window_close()
>>>
>>> scania = Truck()
>>> scania.engine_start()
>>> scania.engine_stop()
>>> scania.window_open()
>>> scania.window_close()
>>>
>>> yamaha = Motorbike()
>>> yamaha.engine_start()
>>> yamaha.engine_stop()

Solution 2 - not implemented:

>>> class Vehicle:
...     def engine_start(self): ...
...     def engine_stop(self): ...
...     def window_open(self): ...
...     def window_close(self): ...
>>>
>>> class Car(Vehicle):
...     pass
>>>
>>> class Truck(Vehicle):
...     pass
>>>
>>> class Motorbike(Vehicle):
...     def window_open(self): raise NotImplementedError
...     def window_close(self): raise NotImplementedError
>>>
>>>
>>> maluch = Car()
>>> maluch.engine_start()
>>> maluch.engine_stop()
>>> maluch.window_open()
>>> maluch.window_close()
>>>
>>> scania = Truck()
>>> scania.engine_start()
>>> scania.engine_stop()
>>> scania.window_open()
>>> scania.window_close()
>>>
>>> yamaha = Motorbike()
>>> yamaha.engine_start()
>>> yamaha.engine_stop()
>>> yamaha.window_open()
Traceback (most recent call last):
NotImplementedError
>>> yamaha.window_close()
Traceback (most recent call last):
NotImplementedError


Multilevel Inheritance
----------------------
>>> class Vehicle:
...     def engine_start(self): ...
...     def engine_stop(self): ...
>>>
>>> class VehicleWithWindows(Vehicle):
...     def window_open(self): ...
...     def window_close(self): ...
>>>
>>> class Car(VehicleWithWindows):
...     pass
>>>
>>> class Truck(VehicleWithWindows):
...     pass
>>>
>>> class Motorbike(Vehicle):
...     pass
>>>
>>>
>>> maluch = Car()
>>> maluch.engine_start()
>>> maluch.engine_stop()
>>> maluch.window_open()
>>> maluch.window_close()
>>>
>>> scania = Truck()
>>> scania.engine_start()
>>> scania.engine_stop()
>>> scania.window_open()
>>> scania.window_close()
>>>
>>> yamaha = Motorbike()
>>> yamaha.engine_start()
>>> yamaha.engine_stop()

Problem - Passenger take/drop:
(let's assume that Truck cannot take passengers)

>>> class Vehicle:
...     def engine_start(self): ...
...     def engine_stop(self): ...
>>>
>>> class VehicleWithWindows(Vehicle):
...     def window_open(self): ...
...     def window_close(self): ...
>>>
>>> class Car(VehicleWithWindows):
...     def passenger_take(self): ...
...     def passenger_drop(self): ...
>>>
>>> class Truck(VehicleWithWindows):
...     pass
>>>
>>> class Motorbike(Vehicle):
...     def passenger_take(self): ...
...     def passenger_drop(self): ...
>>>
>>>
>>> maluch = Car()
>>> maluch.engine_start()
>>> maluch.engine_stop()
>>> maluch.window_open()
>>> maluch.window_close()
>>>
>>> scania = Truck()
>>> scania.engine_start()
>>> scania.engine_stop()
>>> scania.window_open()
>>> scania.window_close()
>>>
>>> yamaha = Motorbike()
>>> yamaha.engine_start()
>>> yamaha.engine_stop()


Multilevel Inheritance
----------------------
>>> class Vehicle:
...     def engine_start(self): ...
...     def engine_stop(self): ...
>>>
>>> class VehicleWithWindows(Vehicle):
...     def window_open(self): ...
...     def window_close(self): ...
>>>
>>> class VehicleWithPassengers(Vehicle):
...     def passenger_take(self): ...
...     def passenger_drop(self): ...
>>>
>>> class Car(VehicleWithWindows, VehicleWithPassengers):
...     pass
>>>
>>> class Truck(VehicleWithWindows):
...     pass
>>>
>>> class Motorbike(VehicleWithPassengers):
...     pass
>>>
>>>
>>>
>>> maluch = Car()
>>> maluch.engine_start()
>>> maluch.engine_stop()
>>> maluch.window_open()
>>> maluch.window_close()
>>> maluch.passenger_take()
>>> maluch.passenger_drop()
>>>
>>> scania = Truck()
>>> scania.engine_start()
>>> scania.engine_stop()
>>> scania.window_open()
>>> scania.window_close()
>>>
>>> yamaha = Motorbike()
>>> yamaha.engine_start()
>>> yamaha.engine_stop()
>>> yamaha.passenger_take()
>>> yamaha.passenger_drop()


Mixin Classes
-------------
>>> class Vehicle:
...     pass
>>>
>>> class HasEngine:
...     def engine_start(self): ...
...     def engine_stop(self): ...
>>>
>>> class HasWindows:
...     def window_open(self): ...
...     def window_close(self): ...
>>>
>>> class HasPassengers:
...     def passenger_take(self): ...
...     def passenger_drop(self): ...
>>>
>>>
>>> class Car(Vehicle, HasEngine, HasWindows, HasPassengers):
...     pass
>>>
>>> class Truck(Vehicle, HasEngine, HasWindows):
...     pass
>>>
>>> class Motorbike(Vehicle, HasEngine, HasPassengers):
...     pass
>>>
>>>
>>> maluch = Car()
>>> maluch.engine_start()
>>> maluch.engine_stop()
>>> maluch.window_open()
>>> maluch.window_close()
>>> maluch.passenger_take()
>>> maluch.passenger_drop()
>>>
>>> scania = Truck()
>>> scania.engine_start()
>>> scania.engine_stop()
>>> scania.window_open()
>>> scania.window_close()
>>>
>>> yamaha = Motorbike()
>>> yamaha.engine_start()
>>> yamaha.engine_stop()
>>> yamaha.passenger_take()
>>> yamaha.passenger_drop()


Use Case - 0x01
---------------
>>> class User:
...     pass
>>>
>>> class Admin:
...     pass
>>>
>>>
>>> mark = User()
>>> isinstance(mark, User)
True
>>> isinstance(mark, Admin)
False
>>>
>>>
>>> melissa = Admin()
>>> isinstance(melissa, User)
False
>>> isinstance(melissa, Admin)
True

Single Inheritance:

>>> class User:
...     pass
...
>>> class Admin(User):
...     pass
...
...
>>> mark = User()
>>> isinstance(mark, User)
True
>>> isinstance(mark, Admin)
False
>>>
>>>
>>> melissa = Admin()
>>> isinstance(melissa, User)
True
>>> isinstance(melissa, Admin)
True

Multilevel Inheritance:

>>> class User:
...     pass
...
>>> class Admin(User):
...     pass
...
>>> class SuperAdmin(Admin):
...     pass
>>>
>>>
>>> mark = User()
>>> isinstance(mark, User)
True
>>> isinstance(mark, Admin)
False
>>> isinstance(mark, SuperAdmin)
False
>>>
>>>
>>> melissa = Admin()
>>> isinstance(melissa, User)
True
>>> isinstance(melissa, Admin)
True
>>> isinstance(melissa, SuperAdmin)
False
>>>
>>>
>>> rick = SuperAdmin()
>>> isinstance(rick, User)
True
>>> isinstance(rick, Admin)
True
>>> isinstance(rick, SuperAdmin)
True

Multiple Inheritance:

>>> class CanEditSelf:
...     pass
>>>
>>> class CanEditUsers:
...     pass
>>>
>>> class CanEditAdmins:
...     pass
>>>
>>>
>>> class Account:
...     pass
>>>
>>> class User(Account, CanEditSelf):
...     pass
>>>
>>> class Admin(Account, CanEditSelf, CanEditUsers):
...     pass
>>>
>>> class SuperAdmin(Account, CanEditSelf, CanEditUsers, CanEditAdmins):
...     pass


Assignments
-----------
.. literalinclude:: assignments/oop_inheritance_patterns_a.py
    :caption: :download:`Solution <assignments/oop_inheritance_patterns_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_inheritance_patterns_b.py
    :caption: :download:`Solution <assignments/oop_inheritance_patterns_b.py>`
    :end-before: # Solution
