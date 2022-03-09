OOP Static and Dynamic Attrs
============================


Static Fields
-------------
* Fields created on class
* Must have default values
* Share state

Static Fields:

>>> class Astronaut:
...     agency = 'NASA'
>>>
>>>
>>> watney = Astronaut()
>>> jimenez = Astronaut()
>>>
>>> print(watney.agency)
NASA
>>>
>>> print(jimenez.agency)
NASA
>>>
>>> print(Astronaut.agency)
NASA


Dynamic Fields
--------------
* Fields created on instance
* Do not share state
* By convention initialized in ``__init__()``
* You can also initialize on living object directly

Dynamic fields:

>>> class Astronaut:
...     def __init__(self, agency='NASA'):
...         self.agency = agency
>>>
>>>
>>> watney = Astronaut()
>>> twardowski = Astronaut()
>>>
>>> print(watney.agency)
NASA
>>>
>>> print(twardowski.agency)
NASA
>>>
>>> print(Astronaut.agency)
Traceback (most recent call last):
AttributeError: type object 'Astronaut' has no attribute 'agency'


Static vs. Dynamic Fields
-------------------------
Static vs. Dynamic fields:

>>> class Astronaut:
...     agency = 'NASA'
>>>
>>>
>>> watney = Astronaut()
>>> twardowski = Astronaut()
>>> ivanovic = Astronaut()
>>>
>>> # Print field
>>> print(watney.agency)
NASA
>>> print(twardowski.agency)
NASA
>>> print(ivanovic.agency)
NASA
>>> print(Astronaut.agency)
NASA
>>>
>>> # Change field on a class
>>> Astronaut.agency = 'ESA'
>>>
>>> # Print field
>>> print(watney.agency)
ESA
>>> print(twardowski.agency)
ESA
>>> print(ivanovic.agency)
ESA
>>> print(Astronaut.agency)
ESA
>>>
>>> # Change field on the instance
>>> ivanovic.agency = 'Roscosmos'
>>>
>>> # Print field
>>> print(watney.agency)
ESA
>>> print(twardowski.agency)
ESA
>>> print(ivanovic.agency)
Roscosmos
>>> print(Astronaut.agency)
ESA
>>>
>>> # Change field on a class
>>> Astronaut.agency = 'POLSA'
>>>
>>> # Print field
>>> print(watney.agency)
POLSA
>>> print(twardowski.agency)
POLSA
>>> print(ivanovic.agency)
Roscosmos
>>> print(Astronaut.agency)
POLSA


Static or Dynamic?
------------------
Static Fields:

>>> class Astronaut:
...     firstname = ...
...     lastname = ...

Dynamic Fields:

>>> class Cosmonaut:
...     def __init__(self):
...         self.firstname = ...
...         self.lastname = ...

Dynamic Fields:

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class GaganYatri:
...     firstname: str = ...
...     lastname: list = ...

Dynamic Fields:

>>> class Taikonaut:
...     pass
>>>
>>> t = Taikonaut()
>>> t.firstname = ...
>>> t.lastname = ...

Static Fields:

>>> class Taikonaut:
...     pass
>>>
>>> Taikonaut.firstname = ...
>>> Taikonaut.lastname = ...


.. todo:: Assignments
