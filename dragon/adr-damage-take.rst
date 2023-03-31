.. testsetup:: # doctest: +SKIP_FILE


Dragon ADR Damage Take
======================
* Make 10 points damage to the dragon
* Make 5 points damage to the dragon
* Make 3 points damage to the dragon
* Make 2 points damage to the dragon
* Make 15 points damage to the dragon
* Make 25 points damage to the dragon
* Make 75 points damage to the dragon


Option 1
--------
>>> dragon.set_damage(DMG)

Pros and Cons:

* Good: easy to use
* Good: clear intent
* Good: encapsulation
* Bad: the name indicates a setter of a ``damage`` attribute
* Bad: not Pythonic way
* Decision: rejected, method name indicates something else


Option 2
--------
>>> dragon.wound(DMG)       # dragon  -> enemy
>>> dragon.hurt(DMG)        # dragon <-  enemy
>>> dragon.hit(DMG)         # dragon <-> enemy
>>> dragon.damage(DMG)      # dragon  -> enemy

Pros and Cons:

* Bad: Indication of direction is too weak ``dragon <-> enemy``
* Decision: rejected, indication of direction is too weak

Example:

>>> dragon.hit(10)  # bad, dragon make or take 10 damage?

Rationale:

.. code-block:: text

    dragon --> enemy
    dragon  -> enemy
    dragon <-> enemy
    dragon <-  enemy
    dragon <-- enemy


Option 3
--------
>>> dragon.hurt_self(DMG)
>>> dragon.receive_damage(DMG)

Pros and Cons:

* Good: Explicit relation ``dragon --> enemy``
* Good: Consistent with ``deal_damage()``
* Bad: ``hurt_self()`` is too use-case specific
* Bad: Inconsistent with ``make_damage()``
* Decision: rejected, method names are too use-case specific

Example:

>>> dragon.hurt_self(DMG)
>>> chair.hurt_self(DMG)
>>> barrel.hurt_self(DMG)

>>> dragon.receive_damage(DMG)
>>> chair.receive_damage(DMG)
>>> barrel.receive_damage(DMG)


Option 4
--------
>>> dragon.take_damage(DMG)

Pros and Cons:

* Good: Explicit relation ``dragon --> enemy``
* Good: Consistent with ``make_damage()``
* Decision: candidate

Example:

>>> dragon.take_damage(DMG)
>>> chair.take_damage(DMG)
>>> barrel.take_damage(DMG)


Option 5
--------
>>> dragon.health - DMG
>>> dragon.health -= DMG

Pros and Cons:

* Good: simple
* Good: can use ``@property`` for validation if needed
* Bad: requires knowledge of API
* Bad: violates encapsulation
* Decision: rejected, violates encapsulation


Option 6
--------
>>> dragon.health - Damage(20)
>>> dragon.health -= Damage(20)

Pros and Cons:

* Good: simple
* Good: can use ``@property`` for validation if needed
* Bad: requires knowledge of API
* Bad: violates encapsulation
* Decision: rejected, violates encapsulation


Option 7
--------
>>> dragon - DMG
>>> dragon -= DMG

Pros and Cons:

* Good: simple
* Good: can use ``.__sub__()`` for validation if needed
* Bad: requires knowledge of API
* Decision: rejected, not explicit and requires knowledge of API


Option 8
--------
>>> dragon - Damage(20)
>>> dragon -= Damage(20)

Pros and Cons:

* Good: simple
* Good: can use ``.__sub__()`` for validation if needed
* Bad: requires knowledge of API
* Decision: rejected, not explicit and requires knowledge of API


Option 9
--------
>>> dragon < Damage(20)
>>> dragon <= Damage(20)
>>> dragon << Damage(20)

Pros and Cons:

* Good: simple
* Good: can use ``.__lt__()``, ``.__le__()`` for validation if needed
* Bad: requires knowledge of API
* Decision: rejected, not explicit and requires knowledge of API


Decision
--------
>>> class Dragon:
...     def take_damage(damage: int, /) -> None: ...
>>>
>>>
>>> dragon.take_damage(DMG)

Pros and Cons:

* Good: provides encapsulation
* Good: easy to use
* Good: explicit relation ``dragon --> enemy``
