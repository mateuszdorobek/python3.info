.. testsetup::

    # doctest: +SKIP_FILE


Dragon ADR Init Name
====================
* ADR - Architecture Design Records


Problem
-------
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
>>> class Dragon:
...     def __init__(self, name: str, /) -> None: ...
>>>
>>>
>>> dragon = Dragon('Wawelski')

Pros and Cons:

* Easy to use
* Verbose enough
