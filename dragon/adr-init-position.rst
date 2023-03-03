.. testsetup::

    # doctest: +SKIP_FILE


Dragon ADR Init Position
========================
* ADR - Architecture Design Records


Problem
-------
* Set Dragon's initial position to x=50, y=120


Option 1
--------
>>> dragon = Dragon('Wawelski', 50, 120)

* Good: easy to use
* Bad: not explicit enough
* Bad: requires knowledge of API to answer what are those numbers
* Bad: It does suggest, that x and y are some parameters to texture (for example width and height of a texture image, or gold and hit points)
* Decision: rejected, not explicit

Problems:

>>> dragon = Dragon('Wawelski', 0, 0)
>>> dragon = Dragon('Wawelski', None, None)
>>> dragon = Dragon('Wawelski', 'img/dragon/alive.png', 50, 120)

>>> current = Point(1, 2)                   # ok
>>> current = GPSPoint(1, 2)                # maybe

>>> knn = KNearestNeighbors(3)              # ok
>>> knn = KNearestNeighbors(3, [1,2,3])     # bad


Option 2
--------
>>> dragon = Dragon('Wawelski', x=50, y=120)

* Good: easy to use
* Good: short argument names
* Good: verbose in this example
* Good: you can assign ``None`` by default to set default point
* Good: extensible, easy to add ``z`` with default value ``0``
* Bad: It does suggest, that x and y are some parameters to texture (for example width and height of a texture image)
* Decision: rejected, not explicit enough

Problem:

>>> dragon = Dragon('Wawelski', x=0, y=0)
>>> dragon = Dragon('Wawelski', x=None, y=None)
>>> dragon = Dragon('Wawelski', texture='img/dragon/alive.png', x=50, y=120)

>>> current = Point(x=1, y=2)                   # ok
>>> current = GPSPoint(...)                     # both longitude and latitude starts with letter "l"

>>> knn = KNearestNeighbors(k=3)                # ok
>>> knn = KNearestNeighbors(k=3, w=[1,2,3])     # bad

.. figure:: img/knn.png


Option 3
--------
>>> dragon = Dragon('Wawelski', posx=50, posy=120)
>>> dragon = Dragon('Wawelski', pos_x=50, pos_y=120)

* Good: simple, easy to use
* Good: you can assign ``None`` by default to set default point
* Good: extensible, easy to add ``pos_z`` with default value ``0``
* Bad: not verbose
* Decision: rejected, not explicit enough

Example:

>>> dragon = Dragon('Wawelski', posx=0, posy=0)         # maybe, bad
>>> dragon = Dragon('Wawelski', pos_x=None, pos_y=None) # maybe, bad

Problem:

>>> current = Point(x=1, y=2)                   # ok
>>> current = GPSPoint(lon=1, lat=2)            # ok


>>> knn = KNearestNeighbors(k=3, wgt=[1,2,3])           # bad


Option 4
--------
>>> dragon = Dragon('Wawelski', positionx=50, positiony=120)
>>> dragon = Dragon('Wawelski', positionX=50, positionY=120)

* Good: simple, easy to use
* Good: you can assign ``None`` by default to set default point
* Good: extensible, easy to add ``positionZ`` with default value ``0``
* Decision: candidate, but names could be better

Example:

>>> current = Point(x=1, y=2)                        # ok
>>> current = GPSPoint(longitude=1, latitude=2)      # ok

>>> knn = KNearestNeighbors(k=3, weights=[1,2,3])    # ok

Problem:

>>> df.plot(kind='line', subplots=True, color='grey', sharey=True)  # bad


Option 5
--------
>>> dragon = Dragon('Wawelski', position_x=50, position_y=120)

* Good: simple, easy to use
* Good: you can assign ``None`` by default to set initial point
* Good: extensible, easy to add ``position_z`` with default value ``0``
* Good: backward compatible
* Decision: candidate

Example:

>>> df.plot(kind='line', sub_plots=True, color='grey', share_y=True)      # ok
>>> df.plot(kind='line', sub_plots=True, color='grey', share_y_axis=True) # ok
>>> df.plot(kind='line', sub_plots=True, color='grey', share_axis_y=True) # ok


Option 6
--------
>>> dragon = Dragon('Wawelski', pos=(50, 120))
>>> dragon = Dragon('Wawelski', pos=[50, 120])

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: simple, easy to use
* Good: you can assign ``None`` to set default ``pos``
* Good: can set only one axis to ``None``
* Good: always has to pass both ``x`` and ``y`` coordinates together
* Bad: always has to pass both ``x`` and ``y`` coordinates together
* Bad: you have to know that first is ``x`` and second is ``y``
* Bad: order is important, you cannot change it
* Bad: unpacking
* Bad: not extensible, ``pos`` will always be 2D
* Decision: rejected, not extensible

Problem:

>>> dragon = Dragon('Wawelski', pos=[0, 0])         # ok
>>> dragon = Dragon('Wawelski', pos=[None, 0])      # maybe
>>> dragon = Dragon('Wawelski', pos=[0, None])      # maybe
>>> dragon = Dragon('Wawelski', pos=[None, None])   # maybe

* ``pattern = r'[\(\[(\s*?:\d+|None\s*)\s*,\s*(\s*?:\d+|None\s*)[\)\]]'``


Option 7
--------
>>> dragon = Dragon('Wawelski', position=(50, 120))
>>> dragon = Dragon('Wawelski', position=[50, 120])

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: simple, easy to use
* Good: you can assign ``None`` to set default ``position``
* Good: can set only one axis to ``None``
* Good: always has to pass both ``x`` and ``y`` coordinates together
* Bad: always has to pass both ``x`` and ``y`` coordinates together
* Bad: you have to know that first is ``x`` and second is ``y``
* Bad: order is important, you cannot change it
* Bad: unpacking
* Bad: not extensible, ``position`` will always be 2D
* Decision: rejected, not extensible

Problem:

>>> dragon = Dragon('Wawelski', position=[0, 0])         # ok
>>> dragon = Dragon('Wawelski', position=[None, 0])      # maybe
>>> dragon = Dragon('Wawelski', position=[0, None])      # maybe
>>> dragon = Dragon('Wawelski', position=[None, None])   # maybe

* ``pattern = r'[\(\[(\s*?:\d+|None\s*)\s*,\s*(\s*?:\d+|None\s*)[\)\]]'``

Example:

>>> pt = (50, 120)
>>>
>>> pt[0], pt[1]
(50, 120)


Option 8
--------
>>> dragon = Dragon('Wawelski', posxy=(50, 120))
>>> dragon = Dragon('Wawelski', pos_xy=(50, 120))
>>> dragon = Dragon('Wawelski', position_xy=(50, 120))

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: simple, easy to use
* Good: you can assign ``None`` by default to set default ``position``
* Good: always has to pass both ``x`` and ``y``
* Bad: always has to pass both ``x`` and ``y``
* Bad: you have to know that first is ``x`` and second is ``y``
* Bad: order is important
* Bad: unpacking
* Bad: not extensible, ``position_xy`` will always be 2D
* Decision: rejected, not extensible

Problem:

* ``pattern = r'[\(\[(\s*?:\d+|None\s*)\s*,\s*(\s*?:\d+|None\s*)[\)\]]'``

Example:

>>> pt = (50, 120)
>>>
>>> pt[0], pt[1]
(50, 120)


Option 9
--------
>>> dragon = Dragon('Wawelski', pos={'x':50, 'y':120})
>>> dragon = Dragon('Wawelski', position={'x':50, 'y':120})

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: you can assign ``None`` by default to set default point
* Good: order is not important
* Good: always has to pass both ``x`` and ``y``
* Good: possible to extend to 3D with refactoring
* Good: easier to refactor than tuple - ``pattern = r'\{"x":\d+, "y":\d+\}'``
* Bad: always has to pass both ``x`` and ``y``
* Bad: unpacking
* Bad: not extensible, ``position`` will always be 2D
* Decision: rejected, not extensible

Problem:

* ``pattern = r'\{\s*"x"\s*:\s*(?:\d+|None)\s*,\s*"y"\s*:\s*(?:\d+|None)\s*\}'``

Example:

>>> pt = {'x':50, 'y':120}
>>>
>>> pt['x']
50
>>> pt['y']
120


Option 10
---------
>>> from collections import namedtuple
>>>
>>>
>>> Point = namedtuple('Point', ['x', 'y'])
>>>
>>> dragon = Dragon('Wawelski', Point(50, 120))
>>> dragon = Dragon('Wawelski', Point(x=50, y=120))
>>> dragon = Dragon('Wawelski', position=Point(50, 120))
>>> dragon = Dragon('Wawelski', position=Point(x=50, y=120))

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: simple, easy to use
* Good: always has to pass both ``x`` and ``y``
* Good: possible to extend to 3D (Python will crash if ``z`` not found)
* Good: keyword argument is not required, class name is verbose enough
* Good: lightweight, in the end this is a tuple
* Bad: always has to pass both ``x`` and ``y``
* Bad: not extensible, ``position`` will always be 2D
* Decision: rejected, could be done better

Example:

>>> pt = Point(x=50, y=120)
>>>
>>> pt[0], pt[1]
(50, 120)
>>>
>>> pt.x, pt.y
(50, 120)


Option 11
---------
>>> from typing import NamedTuple
>>>
>>>
>>> class Point(NamedTuple):
...     x: int
...     y: int
>>>
>>>
>>> dragon = Dragon('Wawelski', Point(50, 120))
>>> dragon = Dragon('Wawelski', Point(x=50, y=120))
>>> dragon = Dragon('Wawelski', position=Point(50, 120))
>>> dragon = Dragon('Wawelski', position=Point(x=50, y=120))

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: simple, easy to use
* Good: verbose
* Good: you can assign ``None`` by default to set default ``position``
* Good: very easy to extend to 3D
* Good: keyword argument is not required, class name is verbose enough
* Good: lightweight, in the end this is a tuple
* Decision: candidate

Example:

>>> pt = Point(x=50, y=120)
>>>
>>> pt[0], pt[1]
(50, 120)
>>>
>>> pt.x, pt.y
(50, 120)


Option 12
---------
>>> from typing import TypedDict
>>>
>>>
>>> class Point(TypedDict):
...     x: int
...     y: int
>>>
>>>
>>> pt1 = Point(x=50, y=120)
>>> pt2: Point = {'x': 50, 'y': 120}
>>>
>>> dragon = Dragon('Wawelski', position=pt1)
>>> dragon = Dragon('Wawelski', position=pt2)

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: simple
* Good: you can assign ``position=None`` by default to set default ``position``
* Good: relatively easy to extend to 3D
* Good: keyword argument is not required, class name is verbose enough
* Bad: ``TypeDict`` does not support default values
* Decision: rejected, better than dict, does not support default values

Future:

* API will change in Python 3.11
* Will include ``Required`` and ``NotRequired``
* Re-evaluate then

Example:

>>> pt = Point(x=50, y=120)
>>>
>>> pt['x']
50
>>> pt['y']
120


Option 13
---------
>>> from typing import TypedDict, Required, NotRequired
>>>
>>>
>>> class Point(TypedDict):
...     x: Required[int]
...     y: Required[int]
...     z: NotRequired[int]
>>>
>>>
>>> pt1 = Point(x=50, y=120)
>>> pt2: Point = {'x': 50, 'y': 120}
>>>
>>> dragon = Dragon('Wawelski', position=pt1)
>>> dragon = Dragon('Wawelski', position=pt2)

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: simple
* Good: you can assign ``position=None`` by default to set default ``position``
* Good: relatively easy to extend to 3D
* Good: keyword argument is not required, class name is verbose enough
* Bad: ``TypeDict`` does not support default values
* Decision: rejected, does not support default values

Future:

* API will change in Python 3.11
* Will include ``Required`` and ``NotRequired``
* Re-evaluate then

Example:

>>> pt = Point(x=50, y=120)
>>>
>>> pt['x']
50
>>> pt['y']
120


Option 14
---------
>>> class Point:
...     x: int
...     y: int
...
...     def __init__(self, x: int = 0, y: int = 0) -> None:
...         self.x = x
...         self.y = y
>>>
>>>
>>> dragon = Dragon('Wawelski', Point(50, 120))
>>> dragon = Dragon('Wawelski', Point(x=50, y=120))
>>> dragon = Dragon('Wawelski', position=Point(50, 120))
>>> dragon = Dragon('Wawelski', position=Point(x=50, y=120))

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: very common pattern
* Good: easy to use
* Good: faster than dataclasses
* Good: more explicit than ``dataclass``
* Good: easy to extend to 3D
* Good: can set default values
* Good: keyword argument is not required, class name is verbose enough
* Bad: allows creation of not existing attributes
* Bad: allows for attribute mutation
* Decision: maybe, has some limitation

Example:

>>> pt = Point(x=1, y=2)
>>>
>>> pt.x, pt.y
(1, 2)
>>>
>>> pt.x = 10            # ok
>>> pt.y = 20            # ok
>>> pt.notexisting = 30  # ok


Option 15
---------
>>> class Point:
...     __slots__ = ('x', 'y')
...     x: int
...     y: int
...
...     def __init__(self, x: int = 0, y: int = 0) -> None:
...         self.x = x
...         self.y = y
>>>
>>>
>>> dragon = Dragon('Wawelski', Point(50, 120))
>>> dragon = Dragon('Wawelski', Point(x=50, y=120))
>>> dragon = Dragon('Wawelski', position=Point(50, 120))
>>> dragon = Dragon('Wawelski', position=Point(x=50, y=120))

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: common pattern
* Good: easy to use
* Good: more explicit than ``dataclass``
* Good: easy to extend to 3D
* Good: can set default values
* Good: keyword argument is not required, class name is verbose enough
* Bad: too complex for now
* Bad: allows for attribute mutation
* Decision: maybe, too complex for now

Example:

>>> pt = Point(x=1, y=2)
>>>
>>> pt.x, pt.y
(1, 2)
>>>
>>> pt.x = 10             # ok
>>> pt.y = 20             # ok
>>> pt.notexisting = 30   # error


Option 16
---------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Point:
...     x: int
...     y: int
>>>
>>>
>>> dragon = Dragon('Wawelski', Point(50, 120))
>>> dragon = Dragon('Wawelski', Point(x=50, y=120))
>>> dragon = Dragon('Wawelski', position=Point(50, 120))
>>> dragon = Dragon('Wawelski', position=Point(x=50, y=120))

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: simple, easy to use
* Good: verbose
* Good: you can assign ``None`` to set default ``position``
* Good: very easy to extend to 3D
* Good: keyword argument is not required, class name is verbose enough
* Bad: allows creation of not existing attributes
* Bad: allows for attribute mutation
* Decision: maybe, has some limitation

Example:

>>> pt = Point(x=1, y=2)
>>>
>>> pt.x, pt.y
(1, 2)
>>>
>>> pt.x = 10             # ok
>>> pt.y = 20             # ok
>>> pt.notexisting = 30   # ok


Option 17
---------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(frozen=True, slots=True)
... class Point:
...     x: int = 0
...     y: int = 0
>>>
>>>
>>> dragon = Dragon('Wawelski', Point(50, 120))
>>> dragon = Dragon('Wawelski', Point(x=50, y=120))
>>> dragon = Dragon('Wawelski', position=Point(50, 120))
>>> dragon = Dragon('Wawelski', position=Point(x=50, y=120))

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: simple, easy to use
* Good: verbose
* Good: you can assign ``None`` by default to set default ``position``
* Good: very easy to extend to 3D
* Good: keyword argument is not required, class name is verbose enough
* Good: is faster and leaner than simple dataclass
* Good: does not allow for attribute mutation
* Good: does not allow for attribute creation
* Bad: more complicated than mutable dataclasses
* Decision: candidate

Example:

>>> pt = Point(x=1, y=2)
>>>
>>> pt.x, pt.y
(1, 2)
>>>
>>> pt.x = 10             # error
>>> pt.y = 20             # error
>>> pt.notexisting = 30   # error


Decision
--------
>>> dragon = Dragon('Wawelski', position_x=50, position_y=120)

* Good: simple
* Good: explicit
* Good: verbose
* Good: extensible

Re-evaluate in future:

>>> dragon = Dragon('Wawelski', position=Point(x=50, y=120))

* Choices: ``NameTuple``, ``dataclass(frozen=True, slots=True)``
* Good: explicit
* Good: verbose
* Good: extensible
* Bad: to complicated for now
