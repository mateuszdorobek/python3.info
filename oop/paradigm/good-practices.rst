Good Engineering Practises
==========================


Code Language
-------------
* ``import this`` - The Zen of Python, by Tim Peters
* Readability counts.
* Special cases aren't special enough to break the rules.
* Although practicality beats purity.
* If the implementation is hard to explain, it's a bad idea.
* In US: The states are **not administrative** divisions of the country, in that their powers and responsibilities are in no way assigned to them from above by federal legislation or the Constitution; rather they exercise all powers of government not delegated to the federal government by the Constitution.
* Political divisions of the United States are the various recognized governing entities that together form the United States – states, the District of Columbia, territories and Indian reservations.
* https://en.wikipedia.org/wiki/Administrative_division
* https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country
* https://en.wikipedia.org/wiki/Administrative_division

>>> class Obywatel:
...     def get_wojewodztwo(self):
...         pass
...
...     def get_powiat(self):
...         pass
...
...     def get_gmina(self):
...         pass

>>> class Citizen:
...     def get_voivodeship(self):
...         pass
...
...     def get_state(self):
...         pass
...
...     def get_county(self):
...         pass
...
...     def get_ceremonial_county(self):
...         pass
...
...     def get_metropolitan_county(self):
...         pass
...
...     def get_nonmetropolitan_county(self):
...         pass
...
...     def get_district(self):
...         pass
...
...     def get_civil_parish(self):
...         pass
...

>>> class Obywatel:
...     def get_PESEL(self):
...         pass
...
...     def get_NIP(self):
...         pass


>>> class Citizen:
...     def get_SSN(self):
...         ...
...
...     def get_VATEU(self):
...         pass

>>> class Obywatel:
...     def get_NIP(self):
...         pass
...
...     def get_PESEL(self):
...         pass

>>> class Citizen:
...     def get_VATEU(self):
...         pass

Stdnum https://github.com/arthurdejong/python-stdnum/tree/master/stdnum

Objects and instances
---------------------
Creating string instance:

``''`` is just a syntactic sugar:

>>> name1 = 'Mark Watney'
>>> name2 = str('Mark Watney')
>>> name1 == name2
True

>>> name = 'Mark Watney'
>>> name.upper()
'MARK WATNEY'

>>> str.upper('Mark Watney')
'MARK WATNEY'

Use case:

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...
...     def say_hello(self):
...         print(f'My name... {self.firstname} {self.lastname}')
>>>
>>>
>>> astro = Astronaut('Jose', 'Jimenez')
>>> astro.say_hello()
My name... Jose Jimenez
>>>
>>> Astronaut.say_hello()
Traceback (most recent call last):
TypeError: Astronaut.say_hello() missing 1 required positional argument: 'self'
>>>
>>> Astronaut.say_hello(astro)
My name... Jose Jimenez


Tell - don't ask
----------------
* Tell-Don't-Ask is a principle that helps people remember that object-orientation is about bundling data with the functions that operate on that data.
* It reminds us that rather than asking an object for data and acting on that data, we should instead tell an object what to do.
* This encourages to move behavior into an object to go with the data.

Bad:

>>> class Light:
...     status = 'off'
>>>
>>>
>>> light = Light()
>>> light.status = 'on'
>>> light.status = 'off'

Good:

>>> class Light:
...     status = 'off'
...
...     def switch_on(self):
...         self.status = 'on'
...
...     def switch_off(self):
...         self.status = 'off'
>>>
>>>
>>> light = Light()
>>> light.switch_on()
>>> light.switch_off()

Bad:

>>> class Hero:
...     health: int = 10
>>>
>>>
>>> hero = Hero()
>>>
>>> while hero.health > 0:
...     hero.health -= 2

Good:

>>> class Hero:
...     health: int = 10
...
...     def is_alive(self):
...         return self.health > 0
...
...     def take_damage(self, damage):
...         self.health -= damage
>>>
>>>
>>> hero = Hero()
>>>
>>> while hero.is_alive():
...     hero.take_damage(2)


Setters, Getters, Deleters
--------------------------
* Java way: setters, getters, deleters
* Python way: properties, reflection, descriptors
* More information in `Protocol Property`
* More information in `Protocol Reflection`
* More information in `Protocol Descriptor`
* In Python you prefer direct attribute access

Accessing class fields using setter and getter:

>>> class Astronaut:
...     _name: str
...
...     def set_name(self, name):
...         self._name = name
...
...     def get_name(self):
...         return self._name
>>>
>>>
>>> astro = Astronaut()
>>> astro.set_name('Mark Watney')
>>> result = astro.get_name()
>>> print(result)
Mark Watney

Problem with setters and getters:

>>> class Point:
...     _x: int
...     _y: int
...
...     def get_x(self):
...         return self._x
...
...     def set_x(self, value):
...         self._x = value
...
...     def del_x(self):
...         del self._x
...
...     def get_y(self):
...         return self._y
...
...     def set_y(self, value):
...         self._x = value
...
...     def del_y(self):
...         del self._y

Rationale for Setters and Getters:

>>> class Temperature:
...     kelvin: int
...
...     def set_kelvin(self, kelvin):
...         if kelvin < 0:
...             raise ValueError('Kelvin cannot be negative')
...         else:
...             self._kelvin = kelvin
...
>>>
>>> t = Temperature()
>>> t.set_kelvin(-1)
Traceback (most recent call last):
ValueError: Kelvin cannot be negative

Rationale for Setters and Getters `habitatOS <https://https://www.astronaut.center/habitatOS>`_ Z-Wave sensor admin:

>>> #doctest: +SKIP
...
... from django.contrib import admin
... from habitat._common.admin import HabitatAdmin
... from habitat.sensors.models import ZWaveSensor
...
...
... @admin.register(ZWaveSensor)
... class ZWaveSensorAdmin(HabitatAdmin):
...     change_list_template = 'sensors/change_list_charts.html'
...     list_display = ['mission_date', 'mission_time', 'type', 'device', 'value', 'unit']
...     list_filter = ['created', 'type', 'unit', 'device']
...     search_fields = ['^date', 'device']
...     ordering = ['-datetime']
...
...     def get_list_display(self, request):
...         list_display = self.list_display
...         if request.user.is_superuser:
...             list_display = ['earth_datetime'] + list_display
...         return list_display


Collections Abstract Base Classes
---------------------------------
* Source: https://docs.python.org/dev/library/collections.abc.html#collections-abstract-base-classes

========================== ====================== ======================= ====================================================
ABC                        Inherits from          Abstract Methods        Mixin Methods
========================== ====================== ======================= ====================================================
:class:`Container`                                ``__contains__``
:class:`Hashable`                                 ``__hash__``
:class:`Iterable`                                 ``__iter__``
:class:`Iterator`          :class:`Iterable`      ``__next__``            ``__iter__``
:class:`Reversible`        :class:`Iterable`      ``__reversed__``
:class:`Generator`         :class:`Iterator`      ``send``, ``throw``     ``close``, ``__iter__``, ``__next__``
:class:`Sized`                                    ``__len__``
:class:`Callable`                                 ``__call__``
:class:`Collection`        :class:`Sized`,        ``__contains__``,
                           :class:`Iterable`,     ``__iter__``,
                           :class:`Container`     ``__len__``

:class:`Sequence`          :class:`Reversible`,   ``__getitem__``,        ``__contains__``, ``__iter__``, ``__reversed__``,
                           :class:`Collection`    ``__len__``             ``index``, and ``count``

:class:`MutableSequence`   :class:`Sequence`      ``__getitem__``,        Inherited :class:`Sequence` methods and
                                                  ``__setitem__``,        ``append``, ``reverse``, ``extend``, ``pop``,
                                                  ``__delitem__``,        ``remove``, and ``__iadd__``
                                                  ``__len__``,
                                                  ``insert``

:class:`ByteString`        :class:`Sequence`      ``__getitem__``,        Inherited :class:`Sequence` methods
                                                  ``__len__``

:class:`Set`               :class:`Collection`    ``__contains__``,       ``__le__``, ``__lt__``, ``__eq__``, ``__ne__``,
                                                  ``__iter__``,           ``__gt__``, ``__ge__``, ``__and__``, ``__or__``,
                                                  ``__len__``             ``__sub__``, ``__xor__``, and ``isdisjoint``

:class:`MutableSet`        :class:`Set`           ``__contains__``,       Inherited :class:`Set` methods and
                                                  ``__iter__``,           ``clear``, ``pop``, ``remove``, ``__ior__``,
                                                  ``__len__``,            ``__iand__``, ``__ixor__``, and ``__isub__``
                                                  ``add``,
                                                  ``discard``

:class:`Mapping`           :class:`Collection`    ``__getitem__``,        ``__contains__``, ``keys``, ``items``, ``values``,
                                                  ``__iter__``,           ``get``, ``__eq__``, and ``__ne__``
                                                  ``__len__``

:class:`MutableMapping`    :class:`Mapping`       ``__getitem__``,        Inherited :class:`Mapping` methods and
                                                  ``__setitem__``,        ``pop``, ``popitem``, ``clear``, ``update``,
                                                  ``__delitem__``,        and ``setdefault``
                                                  ``__iter__``,
                                                  ``__len__``


:class:`MappingView`       :class:`Sized`                                 ``__len__``
:class:`ItemsView`         :class:`MappingView`,                          ``__contains__``,
                           :class:`Set`                                   ``__iter__``
:class:`KeysView`          :class:`MappingView`,                          ``__contains__``,
                           :class:`Set`                                   ``__iter__``
:class:`ValuesView`        :class:`MappingView`,                          ``__contains__``, ``__iter__``
                           :class:`Collection`
:class:`Awaitable`                                ``__await__``
:class:`Coroutine`         :class:`Awaitable`     ``send``, ``throw``     ``close``
:class:`AsyncIterable`                            ``__aiter__``
:class:`AsyncIterator`     :class:`AsyncIterable` ``__anext__``           ``__aiter__``
:class:`AsyncGenerator`    :class:`AsyncIterator` ``asend``, ``athrow``   ``aclose``, ``__aiter__``, ``__anext__``
========================== ====================== ======================= ====================================================

.. todo:: Make this table more readable


.. todo:: Assignments
