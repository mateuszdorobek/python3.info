.. testsetup:: # doctest: +SKIP_FILE


ADR Dragon Position Get
=======================
* Get Dragon position


Option 1
--------
>>> dragon.position_x
1
>>> dragon.position_y
2

Pros and Cons:

* Good: easy to use
* Good: arguments are explicit
* Good: can use ``@property`` for validation if needed
* Bad: violates encapsulation (OOP Principle)
* Decision: rejected, violates encapsulation


Option 2
--------
>>> dragon.position
(1, 2)

>>> dragon.position
{'x':1, 'y':2}

>>> dragon.position
Position(x=1, y=2)

Pros and Cons:

* Good: easy to use
* Good: arguments are explicit
* Good: can use ``@property`` for validation if needed
* Bad: violates encapsulation (OOP Principle)
* Decision: rejected, violates encapsulation


Option 3
--------
>>> dragon.position.x
1
>>> dragon.position.y
2

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
* Bad: violates encapsulation (OOP Principle)
* Decision: rejected, violates encapsulation and Python convention (PEP 20)


Option 4
--------
>>> dragon.get_position()
(1, 2)

>>> dragon.get_position()
{'x':1, 'y':2}

>>> dragon.get_position()
Position(x=1, y=2)

Pros and Cons:

* Good: easy to use
* Good: encapsulation
* Good: easy to add validation if needed
* Good: easy to extend to 3D - add parameter with default value ``0``
* Bad: arguments are implicit, require knowledge of an API what are the values provided as arguments
* Decision: maybe, could be done better


Option 6
--------
>>> dragon.get('position_x')
1
>>> dragon.get('position_y')
2

Pros and Cons:

* Good: easy to use
* Good: arguments are explicit
* Good: easy to add validation if needed
* Bad: ``get()`` is too generic and allows for abuse
* Bad: encapsulation is in question
* Decision: rejected, possibility of abuse


Option 7
--------
>>> dragon.get('position_x', 'position_y')
(1, 2)

>>> dragon.get('position_x', 'position_y')
{'position_x':1, 'position_y':2}

Pros and Cons:

* Good: easy to use
* Good: arguments are explicit
* Good: easy to add validation if needed
* Bad: ``get()`` is too generic and allows for abuse
* Bad: encapsulation is in question
* Decision: rejected, possibility of abuse


Decision
--------
>>> dragon.get_position()

Rationale:

* Easy to use
* Provides encapsulation
* Extensible, easy to refactor to 3D

Implementation:

>>> class Dragon:
...     def get_position(self) -> tuple[int,int]:
...         ...
