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

>>> dragon.fly(10, 20)
>>> dragon.walk(10, 20)    # code duplication
>>> hero.walk(10, 20)    # code duplication
>>> rock.slide(10, 20)   # code duplication


Option 2
--------
>>> dragon.fly(x=10, y=20)
>>> dragon.teleport(x=10, y=20)

* Good: easy to use
* Good: arguments are explicit
* Good: encapsulation
* Good: easy to add validation if needed
* Good: easy to extend to 3D - add parameter with default value ``0``
* Bad: method names are too use-case specific
* Decision: rejected, too use-case specific names

Problem:

>>> dragon.fly(x=10, y=20)
>>> dragon.walk(x=10, y=20)
>>> hero.walk(x=10, y=20)    # code duplication
>>> rock.slide(x=10, y=20)   # code duplication


Option 3
--------
>>> dragon.set_position(10, 20)

* Good: easy to use
* Good: encapsulation
* Good: easy to add validation if needed
* Good: easy to extend to 3D - add parameter with default value ``0``
* Bad: arguments are implicit, require knowledge of an API what are the values provided as arguments
* Decision: maybe, could be done better


Option 4
--------
>>> dragon.set_position_xy(10, 20)

* Good: verbose
* Good: does not require knowledge of an API what are the values provided as arguments
* Good: easy to use
* Good: encapsulation
* Good: easy to add validation if needed
* Bad: name ``set_position_xy()`` ties to 2D point
* Decision: rejected, ties to 2D point


Option 5
--------
>>> dragon.set_position(x=10, y=20)

* Good: easy to use
* Good: arguments are explicit
* Good: encapsulation
* Good: easy to add validation if needed
* Good: easy to extend to 3D - add parameter with default value ``0``
* Decision: candidate


Option 6
--------
>>> dragon.set(position_x=10, position_y=20)

* Good: easy to use
* Good: arguments are explicit
* Good: easy to add validation if needed
* Bad: ``set()`` is to generic
* Bad: possibility of abuse
* Bad: encapsulation is in question
* Decision: rejected, possibility of abuse

Problem:

>>> dragon.set(position_x=10, position_y=20)
>>> dragon.set(health=50)
>>> dragon.set(gold=100)
>>> dragon.set(name='Wawelski')


Option 7
--------
>>> dragon.x = 10
>>> dragon.y = 20

>>> dragon.x, dragon.y = 10, 20

* Good: easy to use
* Good: arguments are explicit
* Good: can use ``@property`` for validation if needed
* Bad: names ``x`` and ``y`` are weakly related to ``dragon``
* Bad: violates abstraction (OOP Principle)
* Bad: violates encapsulation (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected, violates OOP principles

Example:

>>> knn = KNearestNeighbors(k=3)
>>> knn.w = [1, 2, 3]


Option 8
--------
>>> dragon.position_x = 10
>>> dragon.position_y = 20

>>> dragon.position_x, dragon.position_y = 10, 20

* Good: easy to use
* Good: arguments are explicit
* Good: can use ``@property`` for validation if needed in future
* Bad: violates abstraction (OOP Principle)
* Bad: violates encapsulation (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected, violates OOP principles

Example:

>>> knn = KNearestNeighbors(k=3)
>>> knn.weights = [1, 2, 3]


Option 9
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


Option 10
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


Option 11
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


Option 12
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


Decision
--------
>>> dragon.set_position(x=10, y=20)

* Good: easy to use
* Good: arguments are explicit
* Good: provides encapsulation
* Good: easy to add validation if needed
* Good: extensible, easy to refactor to 3D
