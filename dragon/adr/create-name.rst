.. testsetup:: # doctest: +SKIP_FILE


ADR Dragon Create Name
======================
* Create dragon named "Wawelski"
* PL: Smok przy tworzeniu musi mieć nadane imię


Option 1
--------
>>> dragon = Dragon('Wawelski')

Good:

* Code is readable
* Easy to use
* Easy to understand

Bad:

* Less verbose than keyword arguments

Decision:

* Candidate


Option 2
--------
>>> dragon = Dragon(name='Wawelski')

Good:

* Code is readable
* Easy to use
* Easy to understand
* More verbose than positional arguments

Bad:

* Too verbose for such simple example

Decision:

* Rejected, too verbose for such simple case


Option 3
--------
>>> dragon = Dragon()
>>> dragon.name = 'Wawelski'

Good:

* Code is readable
* Easy to use
* Can use ``@property`` for validation if needed

Bad:

* Requires knowledge of an API
* Violates encapsulation (OOP Principle)

Decision:

* Rejected, violates encapsulation


Decision
--------
>>> dragon = Dragon('Wawelski')

Rationale:

* Readable
* Easy to use
* Easy to understand
* Verbose enough

Implementation:

>>> class Dragon:
...     name: str
...
...     def __init__(self, name: str, /) -> None: ...
