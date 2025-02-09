.. testsetup:: # doctest: +SKIP_FILE


ADR Dragon Position Init
========================
* Set Dragon's initial position to x=50, y=100


Option 1
--------
>>> dragon = Dragon('Wawelski', 50, 100)

Pros and Cons:

* Good: easy to use
* Bad: not explicit enough
* Bad: requires knowledge of API to answer what are those numbers
* Bad: It can suggest, that `x` and `y` are gold and hit points
* Bad: It can suggest, that `x` and `y` are width and height of an `texture`
* Bad: Not extensible to 3D
* Decision: rejected, not explicit

Example:

>>> dragon = Dragon('Wawelski', 50, 100)
>>> dragon = Dragon('Wawelski', 50, 100, 0)

Problem:

>>> dragon = Dragon('Wawelski', 50, 100)  # health or position?

>>> dragon = Dragon('Wawelski', None, None)  # 2D
>>> dragon = Dragon('Wawelski', None, None, None)  # 3D

>>> dragon = Dragon('Wawelski', 50, 100, 'img/dragon/alive.png')  # 2D
>>> dragon = Dragon('Wawelski', 50, 100, 'img/dragon/alive.png', 0)  # 3D


Use Case:

>>> pt = Point(1, 2)

>>> knn = KNearestNeighbors(3)  # ok
>>> knn = KNearestNeighbors(3, [0.75, 0.50, 0.25])  # bad


.. figure:: img/ml-knn-1.png
.. figure:: img/ml-knn-2.png
.. figure:: img/ml-knn-3.png
.. figure:: img/ml-knn-4.png
.. figure:: img/ml-knn-5.png
.. figure:: img/ml-knn-6.png
.. figure:: img/ml-knn-7.png
.. figure:: img/ml-knn-8.png
.. figure:: img/ml-knn-9.png


Option 2
--------
>>> dragon = Dragon('Wawelski', x=50, y=100)

Pros and Cons:

* Good: easy to use
* Good: short argument names
* Good: verbose in this example
* Good: you can assign ``None`` by default to set default point
* Good: extensible, easy to add ``z`` with default value ``0``
* Good: Extensible to 3D
* Bad: It can suggest, that `x` and `y` are gold and hit points
* Bad: It can suggest, that `x` and `y` are width and height of an `texture`
* Decision: rejected, not explicit enough

Example:

>>> dragon = Dragon('Wawelski', x=0, y=0)
>>> dragon = Dragon('Wawelski', x=0, y=0, z=0)

>>> dragon = Dragon('Wawelski', t='img/dragon/alive.png', x=0, y=0)
>>> dragon = Dragon('Wawelski', t='img/dragon/alive.png', x=0, y=0, z=0)

>>> dragon = Dragon('Wawelski', x=None, y=None)
>>> dragon = Dragon('Wawelski', t='img/dragon/alive.png', x=None, y=None)
>>> dragon = Dragon('Wawelski', t='img/dragon/alive.png', x=None, y=None, z=None)

Use Case:

>>> pt = Point(x=1, y=2)

>>> knn = KNearestNeighbors(k=3)  # ok
>>> knn = KNearestNeighbors(k=3, w=[0.75, 0.50, 0.25])  # bad


Option 3
--------
>>> dragon = Dragon('Wawelski', posx=50, posy=100)

Pros and Cons:

* Good: simple, easy to use
* Good: you can assign ``None`` by default to set default point
* Good: extensible, easy to add ``posz`` with default value ``0``
* Good: Extensible to 3D
* Bad: not verbose
* Decision: rejected, not explicit enough

Example:

>>> dragon = Dragon('Wawelski', posx=0, posy=0)  # maybe, bad
>>> dragon = Dragon('Wawelski', posx=0, posy=0, posz=0)  # maybe, bad

Use Case:

>>> pt = Point(coordx=1, coordy=2)  # bad, overkill

>>> knn = KNearestNeighbors(k=3, wgt=[0.75, 0.50, 0.25])  # maybe, bad


Option 4
--------
>>> dragon = Dragon('Wawelski', positionx=50, positiony=100)

Pros and Cons:

* Good: simple, easy to use
* Good: you can assign ``None`` by default to set default point
* Good: extensible, easy to add ``positionz`` with default value ``0``
* Good: Extensible to 3D
* Bad: CamelCase `positionX` and `positionY` does not conform to PEP-8
* Decision: candidate, but names could be better

Example:

>>> dragon = Dragon('Wawelski', positionx=0, positiony=0)  # maybe
>>> dragon = Dragon('Wawelski', positionx=0, positiony=0, positionz=0)  # maybe
>>> dragon = Dragon('Wawelski', positionx=0, positiony=0, positionz=0, texture='img/dragon/alive.png')  # maybe

Use Case:

>>> knn = KNearestNeighbors(k=3, weights=[0.75, 0.50, 0.25])  # ok

>>> df.plot(kind='line', subplots=True, color='grey', sharey=True)  # bad


Option 5
--------
>>> dragon = Dragon('Wawelski', position_x=50, position_y=100)

Pros and Cons:

* Good: simple, easy to use
* Good: you can assign ``None`` by default to set initial point
* Good: extensible, easy to add ``position_z`` with default value ``0``
* Good: backward compatible
* Good: Extensible to 3D
* Decision: candidate

>>> dragon = Dragon('Wawelski', position_x=0, position_y=0)  # ok
>>> dragon = Dragon('Wawelski', position_x=0, position_y=0, position_z=0)  # ok
>>> dragon = Dragon('Wawelski', position_x=0, position_y=0, position_z=0, texture='img/dragon/alive.png')  # ok

Use Case:

>>> df.plot(kind='line', subplots=True, color='grey', share_y=True)       # ok
>>> df.plot(kind='line', subplots=True, color='grey', share_y_axis=True)  # ok
>>> df.plot(kind='line', subplots=True, color='grey', share_axis_y=True)  # ok
>>> df.plot(kind='line', sub_plots=True, color='grey', share_axis_y=True) # ok, overkill

Implementation:

>>> class Dragon:
...     def __init__(self, name, position_x, position_y):
...         ...

>>> class Dragon:
...     def __init__(self, name, position_x, position_y, position_z=0):
...         ...


Option 6
--------
>>> dragon = Dragon('Wawelski', (50, 100))
>>> dragon = Dragon('Wawelski', [50, 100])
>>> dragon = Dragon('Wawelski', position=(50, 100))
>>> dragon = Dragon('Wawelski', position=[50, 100])

Pros and Cons:

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
* Bad: could be refactored to 3D using regexp: ``pattern = r'[\(\]]\s*(?:\d+|None)\s*,\s*(?:\d+|None)\s*[\)\]]'``
* Decision: rejected, not extensible

Example:

>>> dragon = Dragon('Wawelski', (0, 0))              # bad
>>> dragon = Dragon('Wawelski', (0, 0, 0))           # bad
>>> dragon = Dragon('Wawelski', [0, 0])              # bad
>>> dragon = Dragon('Wawelski', [0, 0, 0])           # bad

>>> dragon = Dragon('Wawelski', position=(0, 0))     # maybe
>>> dragon = Dragon('Wawelski', position=(0, 0, 0))  # maybe
>>> dragon = Dragon('Wawelski', position=[0, 0])     # maybe
>>> dragon = Dragon('Wawelski', position=[0, 0, 0])  # maybe

>>> dragon = Dragon('Wawelski', (None, None))                   # bad
>>> dragon = Dragon('Wawelski', (None, None, None))             # bad
>>> dragon = Dragon('Wawelski', position=(None, None))          # bad, maybe
>>> dragon = Dragon('Wawelski', position=(None, None, None))    # bad, maybe

>>> pt = (None, None)
>>> pt = (None, None, None)

>>> pt = (50, 100)
>>> pt = (50, 100, 0)
>>> pt = [50, 100]
>>> pt = [50, 100, 0]

Use Case:

>>> np.random.randint(0, 10, (3, 3))  # bad
>>> np.random.randint(0, 10, size=(3, 3))  # ok
>>> np.random.randint(0, 10, rows=3, cols=3)  # ok, for 2D and 3D, not for ndim

>>> pt = (50, 100)
>>>
>>> pt[0], pt[1]
(50, 100)

>>> x, y = (50, 100)
>>>
>>> x, y
(50, 100)


Option 7
--------
>>> dragon = Dragon('Wawelski', {'x':50, 'y':100})
>>> dragon = Dragon('Wawelski', position={'x':50, 'y':100})

Pros and Cons:

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: you can assign ``None`` by default to set default point
* Good: order is not important
* Good: always has to pass both ``x`` and ``y``
* Good: possible to extend to 3D with refactoring
* Good: easier to refactor than tuple - ``pattern = r'\{\s*['"][xy]['"]\s*:\s*(?:\d+|None)\s*,\s*['"][xy]['"]\s*:\s*(?:\d+|None)\s*\}'``
* Bad: always has to pass both ``x`` and ``y``
* Bad: unpacking
* Bad: not extensible, ``position`` will always be 2D
* Decision: rejected, not extensible

Example:

>>> dragon = Dragon('Wawelski', {'x':0, 'y':0})         # bad, maybe
>>> dragon = Dragon('Wawelski', {'x':0, 'y':0, 'z':0})  # bad, maybe

>>> dragon = Dragon('Wawelski', position={'x':0, 'y':0})         # maybe
>>> dragon = Dragon('Wawelski', position={'x':0, 'y':0, 'z':0})  # maybe

>>> dragon = Dragon('Wawelski', {'x':None, 'y':None})                     # bad, maybe
>>> dragon = Dragon('Wawelski', {'x':None, 'y':None, 'z':None})           # bad, maybe
>>> dragon = Dragon('Wawelski', position={'x':None, 'y':None})            # bad, maybe
>>> dragon = Dragon('Wawelski', position={'x':None, 'y':None, 'z':None})  # bad, maybe

>>> pt = {'x':None, 'y':None}
>>> pt = {'x':None, 'y':None, 'z':None}

>>> pt = {'x':50, 'y':100}
>>> pt = {'x':50, 'y':100, 'z':0}

Use Case:

>>> pt = {'x':50, 'y':100}
>>>
>>> pt['x']
50
>>> pt['y']
100


Option 8
---------
>>> from collections import namedtuple
>>>
>>>
>>> Position = namedtuple('Point', ['x', 'y'])
>>>
>>> dragon = Dragon('Wawelski', Position(50, 100))
>>> dragon = Dragon('Wawelski', Position(x=50, y=100))
>>> dragon = Dragon('Wawelski', position=Position(50, 100))
>>> dragon = Dragon('Wawelski', position=Position(x=50, y=100))

Pros and Cons:

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: simple, easy to use
* Good: always has to pass both ``x`` and ``y``
* Good: possible to extend to 3D (Python will crash if ``z`` not found)
* Good: keyword argument is not required, class name is verbose enough
* Good: lightweight, in the end this is a tuple
* Bad: always has to pass both ``x`` and ``y``
* Bad: not extensible, ``position`` will always be 2D
* Decision: rejected, could be done better

Use Case:

>>> Point = namedtuple('Point', ['x', 'y'])
>>> pt = Point(x=50, y=100)
>>>
>>> pt[0], pt[1]
(50, 100)
>>>
>>> pt.x, pt.y
(50, 100)


Option 9
--------
>>> from typing import NamedTuple
>>>
>>>
>>> class Position(NamedTuple):
...     x: int
...     y: int
>>>
>>> dragon = Dragon('Wawelski', Position(50, 100))
>>> dragon = Dragon('Wawelski', Position(x=50, y=100))
>>> dragon = Dragon('Wawelski', position=Position(50, 100))
>>> dragon = Dragon('Wawelski', position=Position(x=50, y=100))

Pros and Cons:

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: simple, easy to use
* Good: verbose
* Good: you can assign ``None`` by default to set default ``position``
* Good: very easy to extend to 3D
* Good: keyword argument is not required, class name is verbose enough
* Good: lightweight, in the end this is a `tuple`
* Decision: candidate

Use Case:

>>> pt = Point(x=50, y=100)
>>>
>>> pt[0], pt[1]
(50, 100)
>>>
>>> pt.x, pt.y
(50, 100)


Option 10
---------
>>> from typing import TypedDict
>>>
>>>
>>> class Position(TypedDict):
...     x: int
...     y: int
>>>
>>> dragon = Dragon('Wawelski', Position(x=50, y=100))
>>> dragon = Dragon('Wawelski', position=Position(x=50, y=100))

Pros and Cons:

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: simple
* Good: you can assign ``position=None`` by default to set default ``position``
* Good: relatively easy to extend to 3D
* Good: keyword argument is not required, class name is verbose enough
* Bad: ``TypeDict`` does not support default values
* Decision: rejected, does not support default values

Use Case:

>>> class Point(TypedDict):
...     x: int
...     y: int
>>>
>>> pt = Point(x=50, y=100)
>>>
>>> pt['x']
50
>>> pt['y']
100


Option 11
---------
>>> from typing import TypedDict, Required, NotRequired
>>>
>>>
>>> class Position(TypedDict):
...     x: Required[int]
...     y: Required[int]
...     z: NotRequired[int]
>>>
>>> dragon = Dragon('Wawelski', Position(x=50, y=100))
>>> dragon = Dragon('Wawelski', position=Position(x=50, y=100))

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: simple
* Good: you can assign ``position=None`` by default to set default ``position``
* Good: relatively easy to extend to 3D
* Good: keyword argument is not required, class name is verbose enough
* Bad: today we need to make decision, that game will eventually be 3D
* Bad: ``TypeDict`` does not support default values
* Decision: rejected, does not support default values

Use Case:

>>> pt = Point(x=50, y=100)
>>>
>>> pt['x']
50
>>> pt['y']
100


Option 12
---------
>>> class Position:
...     x: int
...     y: int
...
...     def __init__(self, x: int = 0, y: int = 0) -> None:
...         self.x = x
...         self.y = y
>>>
>>>
>>> dragon = Dragon('Wawelski', Position(50, 100))
>>> dragon = Dragon('Wawelski', Position(x=50, y=100))
>>> dragon = Dragon('Wawelski', position=Position(50, 100))
>>> dragon = Dragon('Wawelski', position=Position(x=50, y=100))

Pros and Cons:

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

Use Case:

>>> pt = Point(x=1, y=2)
>>>
>>> pt.x, pt.y
(1, 2)
>>>
>>> pt.x = 10            # ok
>>> pt.y = 20            # ok
>>> pt.notexisting = 30  # ok


Option 13
---------
>>> class Position:
...     __slots__ = ('x', 'y')
...     x: int
...     y: int
...
...     def __init__(self, x: int = 0, y: int = 0) -> None:
...         self.x = x
...         self.y = y
>>>
>>> dragon = Dragon('Wawelski', Position(50, 100))
>>> dragon = Dragon('Wawelski', Position(x=50, y=100))
>>> dragon = Dragon('Wawelski', position=Position(50, 100))
>>> dragon = Dragon('Wawelski', position=Position(x=50, y=100))

Pros and Cons:

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: common pattern
* Good: easy to use
* Good: more explicit than ``dataclass``
* Good: easy to extend to 3D
* Good: can set default values
* Good: keyword argument is not required, class name is verbose enough
* Good: slots make class lighter and faster
* Bad: too complex for now
* Bad: allows for attribute mutation
* Decision: maybe, too complex for now

Use Case:

>>> pt = Point(x=1, y=2)
>>>
>>> pt.x, pt.y
(1, 2)
>>>
>>> pt.x = 10             # ok
>>> pt.y = 20             # ok
>>> pt.notexisting = 30   # error


Option 14
---------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Position:
...     x: int
...     y: int
>>>
>>> dragon = Dragon('Wawelski', Position(50, 100))
>>> dragon = Dragon('Wawelski', Position(x=50, y=100))
>>> dragon = Dragon('Wawelski', position=Position(50, 100))
>>> dragon = Dragon('Wawelski', position=Position(x=50, y=100))

Pros and Cons:

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: simple, easy to use
* Good: verbose
* Good: you can assign ``None`` to set default ``position``
* Good: very easy to extend to 3D
* Good: keyword argument is not required, class name is verbose enough
* Bad: allows creation of not existing attributes
* Bad: allows for attribute mutation
* Decision: maybe, has some limitation

Use Case:

>>> pt = Point(x=1, y=2)
>>>
>>> pt.x, pt.y
(1, 2)
>>>
>>> pt.x = 10             # ok
>>> pt.y = 20             # ok
>>> pt.notexisting = 30   # ok


Option 15
---------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(slots=True)
... class Position:
...     x: int = 0
...     y: int = 0
>>>
>>> dragon = Dragon('Wawelski', Position(50, 100))
>>> dragon = Dragon('Wawelski', Position(x=50, y=100))
>>> dragon = Dragon('Wawelski', position=Position(50, 100))
>>> dragon = Dragon('Wawelski', position=Position(x=50, y=100))

Pros and Cons:

* Good: data is stored together (``x`` and ``y`` coordinates)
* Good: simple, easy to use
* Good: verbose
* Good: you can assign ``None`` by default to set default ``position``
* Good: very easy to extend to 3D
* Good: keyword argument is not required, class name is verbose enough
* Good: is faster and leaner than simple dataclass
* Good: does not allow for new attribute creation
* Good: slots make class lighter and faster
* Bad: more complicated than mutable dataclasses
* Decision: candidate

Use Case:

>>> pt = Point(x=1, y=2)
>>>
>>> pt.x, pt.y
(1, 2)
>>>
>>> pt.x = 10             # ok
>>> pt.y = 20             # ok
>>> pt.notexisting = 30   # error


Decision
--------
>>> dragon = Dragon('Wawelski', position_x=50, position_y=100)

Rationale:

* Simple
* Explicit
* Verbose
* Extensible

Implementation:

>>> class Dragon:
...     position_x: int
...     position_y: int
...
...     def __init__(name: str, /, *, position_x: int, position_y: int) -> None:
...         ...


Future
------
>>> dragon = Dragon('Wawelski', Position(x=50, y=100))

Reconsider:

* ``NameTuple``
* ``dataclass(slots=True)``

Rationale:

* Explicit
* Verbose
* Extensible

Implementation:

>>> class Dragon:
...     position: Position
...
...     def __init__(name: str, /, *, position: Position) -> None:
...         ...
