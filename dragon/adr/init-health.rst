.. testsetup:: # doctest: +SKIP_FILE


ADR Dragon Init Health
======================
* Smok ma punkty życia (losowa liczba od 50 do 100)


Option 1
--------
>>> dragon = Dragon('Name')

Pros and Cons:

* Good: easy to use
* Bad: less verbose than keyword arguments
* Decision: candidate

Example:

>>> dragon = Dragon('Name')


Option 2
--------
>>> dragon = Dragon('Name', 75)

Pros and Cons:

* Good: easy to use
* Bad: not explicit enough
* Bad: requires knowledge of API to answer what is this number
* Decision: rejected, not explicit enough


Option 2
--------
>>> dragon = Dragon('Name', health=75)

Pros and Cons:

* Good: easy to use
* Good: explicit enough
* Bad: we were asked to generate health randomly
* Decision: rejected, we were asked to generate health randomly


Option 2
--------
>>> dragon = Dragon('Name', 50, 100)

Pros and Cons:

* Good: easy to use
* Good: more verbose than positional arguments
* Bad: too verbose for such simple example
* Decision: rejected, too verbose for such simple example


Option 2
--------
>>> dragon = Dragon('Name', health_min=50, health_max=100)

Pros and Cons:

* Good: easy to use
* Good: more verbose than positional arguments
* Bad: too verbose for such simple example
* Decision: rejected, too verbose for such simple example


Option 3
--------
>>> dragon = Dragon('Name')
>>> dragon.health_min = 50
>>> dragon.health_max = 100

Pros and Cons:

* Good: easy to use
* Good: more verbose than positional arguments
* Bad: too verbose for such simple example
* Decision: rejected, too verbose for such simple example

Pros and Cons:

* Good: code is readable
* Good: can use ``@property`` for validation if needed
* Bad: violates encapsulation (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected, violates OOP principles


Decision
--------
>>> dragon = Dragon('Wawelski')

Pros and Cons:

* Good: Easy to use
* Good: Verbose enough

Implementation:

>>> class Dragon:
...     name: str
...
...     def __init__(self, name: str, /) -> None: ...
