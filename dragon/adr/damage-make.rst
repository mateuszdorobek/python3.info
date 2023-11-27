.. testsetup:: # doctest: +SKIP_FILE


ADR Dragon Damage Make
======================
* Dragon makes damage


Option 1
--------
>>> dragon.get_damage()

Good:

* Easy use
* Readability
* Clear intent
* Easy to add validation if needed

Bad:

* Name ``get_damage()`` indicate a getter of ``damage`` attribute

Decision:

* rejected, bad method name


Option 2
--------
>>> dragon.attack()  # dragon  -> enemy
>>> dragon.hit()     # dragon <-> enemy
>>> dragon.hurt()    # dragon <-  enemy
>>> dragon.damage()  # dragon <-  enemy
>>> dragon.wound()   # dragon <-  enemy

Good:

* Indication of direction is too weak ``dragon <-> enemy``
* Not directed, all methods could mean making damage or receiving damage

Rationale:

Some method names has stronger emphasis on who is making damage to whom.
Consider this: ``dragon.hurt()`` - is that dragon who makes damage or takes
damage?

>>> dragon.make_damage()    # dragon --> enemy
>>> dragon.attack()         # dragon  -> enemy
>>> dragon.hit()            # dragon <-> enemy
>>> dragon.hurt()           # dragon <-  enemy
>>> dragon.take_damage()    # dragon <-- enemy

Decision:

* rejected, bad method names


Option 3
--------
>>> dragon.take_damage()    # dragon <-- enemy

Good:

* Simple

Bad:

* Relation is other way around ``dragon <-- enemy``

Decision:

* Rejected, relation is other way around


Option 4
--------
>>> dragon.deal_damage()    # dragon --> enemy
>>> dragon.hurt_someone()   # dragon --> enemy
>>> dragon.attack_enemy()   # dragon --> enemy

Good:

* Strong indication of direction ``dragon --> enemy``

Bad:

* ``hurt_someone()`` method name is too use-case specific

Example:

>>> dragon.attack_enemy()  # maybe
>>> magic_arrow.attack_enemy()  # bad
>>> explosion.attack_enemy()  # bad

Decision:

* Rejected, method names are too use-case specific


Option 5
--------
>>> dragon.make_damage()    # dragon --> enemy

Good:

* Strong indication of direction ``dragon --> enemy``
* Name indicates intent

Example:

>>> dragon.make_damage()
>>> magic_arrow.make_damage()
>>> explosion.make_damage()

Decision:

* Candidate


Option 6
--------
>>> dragon.make_damage(ENEMY)    # dragon --> enemy

Bad:

* Model-View-Controller (MVC)
* Each ENEMY will get different (random) damage

Decision:

* Rejected, violates Model-View-Controller (MVC)

Rationale:

>>> class BankAccount:
...     def transfer(self, destination_account, amount):
...         self.withdraw(amount)
...         destination_account.deposit(amount)

* Bad: this is not how bank transfers are done (especially between banks)
* Bad: other bank of will not share their source code with you, to make a transfer

>>> def swift_transfer(from_account, to_account, amount):  # controller
...     from_account.withdraw(amount)
...     to_account.deposit(amount)

.. figure:: img/dragon-firkraag-01.jpg
.. figure:: img/designpatterns-mvc-10.png
.. figure:: img/designpatterns-mvc-usecase-10.png


Option 7
--------
>>> hero.health -= dragon.damage()

Good:

* Simple
* Can use ``@property`` for validation if needed

Bad:

* Violates encapsulation

Decision:

* Decision: rejected, violates encapsulation


Option 8
--------
>>> dragon << Damage(20)

Good:

* Easy to use
* Using ``<<`` (lshift) it is easy to add validation

Bad:

* Require knowledge of an API
* Violates abstraction (OOP Principle)
* Violates encapsulation (OOP Principle)
* Violates Tell, Don't Ask (OOP Principle)

Decision:

* Rejected, violates OOP principles


Option 9
--------
>>> hero.wound(dragon.hit())

Bad:

* Readability
* Requires knowledge of API
* This is responsibility of a controller

Decision:

* Rejected, violates Model-View-Controller (MVC)


Decision
--------
>>> dmg = dragon.make_damage()

Rationale:

* Clear intent
* ``dragon --> enemy``
* Readability
* Encapsulation

Implementation:

>>> class Dragon:
...     def make_damage(self) -> int: ...
