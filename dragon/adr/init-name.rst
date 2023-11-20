.. testsetup:: # doctest: +SKIP_FILE


ADR Dragon Init Name
====================
* Create dragon named "Wawelski"


Option 1
--------
>>> dragon = Dragon('Wawelski')

Pros and Cons:

* Good: easy to use
* Bad: less verbose than keyword arguments
* Decision: candidate


Option 2
--------
>>> dragon = Dragon(name='Wawelski')

Pros and Cons:

* Good: easy to use
* Good: more verbose than positional arguments
* Bad: too verbose for such simple example
* Decision: rejected, too verbose for such simple example


Option 3
--------
>>> dragon = Dragon()
>>> dragon.name = 'Wawelski'

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
