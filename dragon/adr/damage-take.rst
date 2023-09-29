.. testsetup:: # doctest: +SKIP_FILE


ADR Dragon Damage Take
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
>>> dragon.set_health(DMG)

Pros and Cons:

* Good: easy to use
* Good: clear intent
* Good: encapsulation
* Bad: the name indicates a setter of a ``health`` attribute
* Bad: not Pythonic way
* Decision: rejected, method name indicates something else


Option 3
--------
>>> dragon.change_health(DELTA_HEALTH)

Pros and Cons:

* Good: easy to use
* Good: clear intent
* Good: encapsulation
* Bad: the name indicates a setter of a ``health`` attribute
* Bad: not Pythonic way
* Decision: rejected, method name indicates something else

Example:

>>> dragon.change_health(-10)  # Make 10 points damage to the dragon
>>> dragon.change_health(-5)  # Make 5 points damage to the dragon
>>> dragon.change_health(-3)  # Make 3 points damage to the dragon
>>> dragon.change_health(-2)  # Make 2 points damage to the dragon
>>> dragon.change_health(-15)  # Make 15 points damage to the dragon
>>> dragon.change_health(-25)  # Make 25 points damage to the dragon
>>> dragon.change_health(-75)  # Make 75 points damage to the dragon

Problem:

>>> dmg = hero.make_damage()
>>> result = dragon.health - dmg
>>>
>>> dragon.change_health(result)

Use Case:

>>> file.change_content('hello world')

.. figure:: img/designpatterns-telldontask-1.png


Option 4
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


Option 5
--------
>>> dragon.hurt_self(DMG)
>>> dragon.hurt_me(DMG)
>>> dragon.receive_damage(DMG)
>>> dragon.suffer_damage(DMG)

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


Option 6
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


Option 7
--------
>>> dragon.health - DMG
>>> dragon.health -= DMG

Pros and Cons:

* Good: simple
* Good: can use ``@property`` for validation if needed
* Bad: requires knowledge of API
* Bad: violates encapsulation
* Decision: rejected, violates encapsulation


Option 8
--------
>>> dragon.health - Damage(20)
>>> dragon.health -= Damage(20)

Pros and Cons:

* Good: simple
* Good: can use ``@property`` for validation if needed
* Bad: requires knowledge of API
* Bad: violates encapsulation
* Decision: rejected, violates encapsulation


Option 9
--------
>>> dragon - DMG
>>> dragon -= DMG

Pros and Cons:

* Good: simple
* Good: can use ``.__sub__()`` for validation if needed
* Bad: requires knowledge of API
* Decision: rejected, not explicit and requires knowledge of API


Option 10
---------
>>> dragon - Damage(20)
>>> dragon -= Damage(20)

Pros and Cons:

* Good: simple
* Good: can use ``.__sub__()`` for validation if needed
* Bad: requires knowledge of API
* Decision: rejected, not explicit and requires knowledge of API


Option 11
---------
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
>>> dragon.take_damage(DMG)

Pros and Cons:

* Good: provides encapsulation
* Good: easy to use
* Good: explicit relation ``dragon --> enemy``

Implementation:

>>> class Dragon:
...     def take_damage(damage: int, /) -> None: ...
