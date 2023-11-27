.. testsetup:: # doctest: +SKIP_FILE


ADR Dragon Health Init
======================
* Dragon when created has random health from 50 to 100


Option 1
--------
>>> dragon = Dragon('Name')
>>> dragon.health = randint(50,100)

Pros and Cons:

* Good: code is readable
* Good: easy to use
* Good: can use ``@property`` for validation if needed
* Bad: requires knowledge of an API
* Bad: violates encapsulation (OOP Principle)
* Decision: rejected, violates encapsulation


Option 2
--------
>>> dragon = Dragon('Name')

Pros and Cons:

* Good: easy to use
* Bad: less verbose than keyword arguments
* Decision: candidate

Example:

>>> dragon = Dragon('Name')
>>> assert dragon.health in range(50,101)

>>> dragon = Dragon('Name')
>>> assert 50 <= dragon.health <= 100

>>> from random import seed; seed(0)
>>>
>>> dragon = Dragon('Name')
>>> dragon.health
74


Option 3
--------
>>> dragon = Dragon('Name')

Pros and Cons:

* Good: easy to use
* Bad: less verbose than keyword arguments
* Decision: candidate

Example:

>>> dragon = Dragon('Name')
>>> assert dragon._health in range(50,101)

>>> dragon = Dragon('Name')
>>> assert 50 <= dragon._health <= 100

>>> from random import seed; seed(0)
>>>
>>> dragon = Dragon('Name')
>>> dragon._health
74


Option 4
--------
>>> dragon = Dragon('Name', randint(50,100))

Pros and Cons:

* Good: easy to use
* Bad: not explicit enough
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected, violates Tell, Don't Ask


Option 5
--------
>>> dragon = Dragon('Name', health=randint(50,100))

Pros and Cons:

* Good: easy to use
* Good: explicit enough
* Bad: we were asked to generate health randomly
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected, violates Tell, Don't Ask


Option 6
--------
>>> dragon = Dragon('Name', 50, 100)

Pros and Cons:

* Good: easy to use
* Bad: less verbose than keyword arguments
* Bad: requires knowledge of API to answer what is this number
* Decision: rejected, requires knowledge of API


Option 7
--------
>>> dragon = Dragon('Name', health_min=50, health_max=100)

Pros and Cons:

* Good: easy to use
* Good: more verbose than positional arguments
* Bad: requires knowledge of API
* Decision: candidate


Option 8
--------
>>> dragon = Dragon('Name')
>>> dragon.health_min = 50
>>> dragon.health_max = 100
>>> dragon.init_health()

Pros and Cons:

* Good: code is readable
* Good: can use ``@property`` for validation if needed
* Bad: requires knowledge of API
* Bad: violates encapsulation (OOP Principle)
* Decision: rejected, violates encapsulation


Option 9
--------
>>> dragon = Dragon('Name')
>>> dragon.HEALTH_MIN = 50
>>> dragon.HEALTH_MAX = 100
>>> dragon.init_health()

Pros and Cons:

* Good: code is readable
* Good: can use ``@property`` for validation if needed
* Bad: requires knowledge of API
* Bad: violates encapsulation (OOP Principle)
* Decision: rejected, violates encapsulation


Option 10
---------
>>> class Dragon:
...     HEALTH_MIN = 50
...     HEALTH_MAX = 100
>>>
>>> dragon = Dragon('Name')

Pros and Cons:

* Good: code is readable
* Good: easy to use
* Good: can use ``@property`` for validation if needed
* Decision: candidate

Implementation:

>>> class Dragon:
...     HEALTH_MIN = 50
...     HEALTH_MAX = 100
...
...     def __init__(name):
...         self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)


Decision
--------
>>> class Dragon:
...     HEALTH_MIN = 50
...     HEALTH_MAX = 100
>>>
>>> dragon = Dragon('Name')

Rationale:

* Code is readable
* Easy to use
* Easy to modify
* Can use ``@property`` for validation if needed

Implementation:

>>> class Dragon:
...     HEALTH_MIN = 50
...     HEALTH_MAX = 100
...
...     def __init__(name):
...         self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)

Tests:

>>> from random import seed; seed(0)

>>> Dragon.HEALTH_MIN
50
>>> Dragon.HEALTH_MAX
100

>>> dragon = Dragon('Name')
>>> dragon.health
74
