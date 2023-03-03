.. testsetup::

    # doctest: +SKIP_FILE


Dragon ADR Position Set
=======================
* ADR - Architecture Design Records


Problem
-------
* Set new position to x=10, y=20


Option 1
--------
>>> dragon.fly(10, 20)
>>> dragon.teleport(10, 20)

* Good: easy to use
* Good: encapsulation
* Good: easy to add validation if needed
* Good: easy to extend to 3D - add parameter with default value ``0``
* Bad: method names are too use-case specific
* Bad: arguments are implicit, require knowledge of an API what are the values provided as arguments
* Decision: rejected, too use-case specific names

Problem:

>>> dragon.fly(10, 20)     # does the same, but different name
>>> hero.walk(10, 20)      # does the same, but different name
>>> snake.slide(10, 20)    # does the same, but different name


Option 2
--------
>>> def set_position(x, y, /):
...     pass
...
>>> dragon.set_position(10, 20)

* Good: easy to use
* Good: encapsulation
* Good: easy to add validation if needed
* Good: easy to extend to 3D - add parameter with default value ``0``
* Bad: arguments are implicit, require knowledge of an API what are the values provided as arguments
* Decision: maybe, could be done better


Option 3
--------
>>> def set_position_xy(x, y, /):
...     pass
...
>>> dragon.set_position_xy(10, 20)

* Good: verbose
* Good: does not require knowledge of an API what are the values provided as arguments
* Good: easy to use
* Good: encapsulation
* Good: easy to add validation if needed
* Bad: name ``set_position_xy()`` ties to 2D point
* Decision: rejected, ties to 2D point


Option 4
--------
>>> def set_position(*, x, y):
...     pass
...
>>> dragon.set_position(x=10, y=20)

* Good: easy to use
* Good: arguments are explicit
* Good: encapsulation
* Good: easy to add validation if needed
* Good: easy to extend to 3D - add parameter with default value ``0``
* Decision: candidate


Option 5
--------
>>> def set_position(**kwargs):
...     pass
...
>>> dragon.set(position_x=10, position_y=20)

* Good: easy to use
* Good: arguments are explicit
* Good: easy to add validation if needed
* Bad: ``set()`` is too generic and allows for abuse
* Bad: encapsulation is in question
* Decision: rejected, possibility of abuse

Problem:

>>> dragon.set(position_x=10, position_y=20)
>>> dragon.set(health=50)
>>> dragon.set(gold=100)
>>> dragon.set(name='Wawelski')


Option 6
--------
>>> dragon.x = 10
>>> dragon.y = 20
>>> dragon.x, dragon.y = 10, 20

>>> dragon.position_x = 10
>>> dragon.position_y = 20
>>> dragon.position_x, dragon.position_y = 10, 20

* Good: easy to use
* Good: arguments are explicit
* Good: can use ``@property`` for validation if needed
* Bad: names ``x`` and ``y`` are weakly related to ``dragon``
* Bad: violates abstraction (OOP Principle)
* Bad: violates encapsulation (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected, violates OOP principles

Problem:

>>> knn = KNearestNeighbors()
>>> knn.k = 3
>>> knn.w = [1, 2, 3]


Option 7
---------
>>> dragon.position.x = 10
>>> dragon.position.y = 20

>>> dragon.position.x, dragon.position.y = 10, 20

* Good: more or less easy to use (Simple is better than complex)
* Good: arguments are explicit
* Good: can use ``@property`` for validation if needed
* Good: namespace
* Good: more or less readable (Readability counts)
* Good: extensible, easy to refactor to 3D
* Bad: violates encapsulation - OOP good practices
* Bad: flat is better than nested (PEP 20)
* Bad: require knowledge of an API
* Bad: violates abstraction (OOP Principle)
* Bad: violates encapsulation (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected, violates OOP principles and Python convention (PEP 20)

Problem:

>>> knn = KNearestNeighbors()
>>> knn.params.k = 3
>>> knn.params.w = [1, 2, 3]


Option 8
--------
>>> dragon.position = (10, 20)

* Good: easy to use
* Good: can use ``@property`` for validation if needed
* Bad: arguments are implicit
* Bad: require knowledge of an API
* Bad: always 2D
* Bad: not extensible, hard to refactor to 3D
* Bad: violates abstraction (OOP Principle)
* Bad: violates encapsulation (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected, violates OOP principles

Problem:

>>> knn = KNearestNeighbors()
>>> knn.args = (3, [1, 2, 3])


Option 9
---------
>>> dragon.position = Point(x=10, y=20)

* Good: easy to use
* Good: can use ``@property`` for validation if needed
* Good: arguments are explicit
* Good: readability
* Bad: require knowledge of an API
* Bad: extensible, easy to refactor to 3D
* Bad: violates abstraction (OOP Principle)
* Bad: violates encapsulation (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected, violates OOP principles

Problem:

>>> knn = KNearestNeighbors()
>>> knn.args = Params(k=3, w=[1, 2, 3])


Option 10
---------
>>> dragon.position @ Point(x=10, y=20)

* Good: easy to use
* Good: using ``@`` (matmul) it is easy to validation
* Bad: ``@`` (at) makes sense only in English
* Bad: arguments are implicit
* Bad: require knowledge of an API
* Bad: always 2D
* Bad: not extensible, hard to refactor to 3D
* Bad: violates abstraction (OOP Principle)
* Bad: violates encapsulation (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected, violates OOP principles, misleading for non-English speakers

Problem:

>>> knn = KNearestNeighbors()
>>> knn << Params(k=3, w=[1, 2, 3])


Decision
--------
>>> dragon.set_position(x=10, y=20)

* Good: easy to use
* Good: arguments are explicit
* Good: provides encapsulation
* Good: easy to add validation if needed
* Good: extensible, easy to refactor to 3D
