.. testsetup:: # doctest: +SKIP_FILE


Dragon ADR Init Name
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


Decision
--------
>>> dragon = Dragon('Wawelski')

Pros and Cons:

* Easy to use
* Verbose enough

Implementation:

>>> class Dragon:
...     def __init__(self, name: str, /) -> None: ...
