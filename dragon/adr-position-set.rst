.. testsetup:: # doctest: +SKIP_FILE


Dragon ADR Position Set
=======================
* Set new position to x=10, y=20


Option 1
--------
>>> dragon.fly(10, 20)
>>> dragon.teleport(10, 20)

Pros and Cons:

* Good: easy to use
* Good: encapsulation
* Good: easy to add validation if needed
* Good: easy to extend to 3D - add parameter with default value ``0``
* Bad: method names are too use-case specific
* Bad: arguments are implicit, require knowledge of an API what are the values provided as arguments
* Decision: rejected, too use-case specific names

Example:

>>> dragon.fly(10, 20)     # does the same, but different name
>>> hero.walk(10, 20)      # does the same, but different name
>>> snake.slide(10, 20)    # does the same, but different name

Use Case:

>>> locmem.store()
>>> locmem.retrieve()
>>> database.insert()
>>> database.select()
>>> filesystem.write()
>>> filesystem.read()


Option 2
--------
>>> dragon.set_position(10, 20)

Pros and Cons:

* Good: easy to use
* Good: encapsulation
* Good: easy to add validation if needed
* Good: easy to extend to 3D - add parameter with default value ``0``
* Bad: arguments are implicit, require knowledge of an API what are the values provided as arguments
* Decision: maybe, could be done better


Option 3
--------
>>> dragon.set_position_xy(10, 20)

Pros and Cons:

* Good: verbose
* Good: does not require knowledge of an API what are the values provided as arguments
* Good: easy to use
* Good: encapsulation
* Good: easy to add validation if needed
* Bad: name ``set_position_xy()`` ties to 2D point
* Decision: rejected, ties to 2D point

Example:

>>> dragon.set_position_xy(10, 20)
>>> dragon.set_position_xyz(10, 20, 30)


Option 4
--------
>>> dragon.set_position(x=10, y=20)

Pros and Cons:

* Good: easy to use
* Good: arguments are explicit
* Good: encapsulation
* Good: easy to add validation if needed
* Good: easy to extend to 3D - add parameter with default value ``0``
* Decision: candidate

Example:

>>> dragon.set_position(x=10, y=20)
>>> dragon.set_position(x=10, y=20, z=30)


Option 5
--------
>>> dragon.set(position_x=10, position_y=20)

Pros and Cons:

* Good: easy to use
* Good: arguments are explicit
* Good: easy to add validation if needed
* Bad: ``set()`` is too generic and allows for abuse
* Bad: encapsulation is in question
* Decision: rejected, possibility of abuse

Example:

>>> dragon.set(position_x=10, position_y=20)
>>> dragon.set(health=50)
>>> dragon.set(gold=100)
>>> dragon.set(damage=10)
>>> dragon.set(name='Wawelski')


Option 6
--------
>>> dragon.position_x = 10
>>> dragon.position_y = 20
>>> dragon.position_x, dragon.position_y = 10, 20

Pros and Cons:

* Good: easy to use
* Good: arguments are explicit
* Good: can use ``@property`` for validation if needed
* Bad: violates abstraction (OOP Principle)
* Bad: violates encapsulation (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected, violates OOP principles

Use Case:

>>> knn = KNearestNeighbors()
>>> knn.k = 3


Option 7
---------
>>> dragon.position.x = 10
>>> dragon.position.y = 20

>>> dragon.position.x, dragon.position.y = 10, 20

Pros and Cons:

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

Use Case:

>>> knn = KNearestNeighbors()
>>> knn.params.k = 3
>>> knn.params.w = [1, 2, 3]


Option 8
--------
>>> dragon.position = (10, 20)

Pros and Cons:

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

Use Case:

>>> knn = KNearestNeighbors()
>>> knn.parameters = (3, [1, 2, 3])


Option 9
---------
>>> dragon.position = Position(x=10, y=20)

Pros and Cons:

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

Use Case:

>>> knn = KNearestNeighbors()
>>> knn.parameters = Params(k=3, w=[1, 2, 3])


Option 10
---------
>>> dragon.position @ Position(x=10, y=20)

Pros and Cons:

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

Use Case:

>>> knn = KNearestNeighbors()
>>> knn << Params(k=3, w=[1, 2, 3])


Decision
--------
>>> class Dragon:
...     def set_position(self, *, x: int, y: int) -> None:
...         ...
>>>
>>>
>>> dragon.set_position(x=10, y=20)

Pros and Cons:

* Good: easy to use
* Good: arguments are explicit
* Good: provides encapsulation
* Good: easy to add validation if needed
* Good: extensible, easy to refactor to 3D
