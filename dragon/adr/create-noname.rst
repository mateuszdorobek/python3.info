.. testsetup:: # doctest: +SKIP_FILE


ADR Dragon Create Noname
========================
* EN: Dragon on creation display error if it does not have name
* PL: Smok przy tworzeniu wyświetla błąd jeżeli nie ma imienia


Option 1
--------
>>> print('Dragon must have a name')
Dragon must have a name

Good:

* Easy to use

Bad:

* You should never print in a class
* Hard to catch programmatically
* Less verbose than exception

Example:

>>> dragon = Dragon()
Dragon must have a name

Decision:

* Rejected, hard to catch programmatically


Option 2
--------
>>> logging.error('Dragon must have a name')
ERROR:root:Dragon must have a name

Good:

* Easy to use
* Better than print

Bad:

* Hard to catch programmatically
* Less verbose than exception

Example:

>>> dragon = Dragon()
ERROR:root:Dragon must have a name

Decision:

* Rejected, hard to catch programmatically


Option 3
--------
>>> raise NameError('Dragon must have a name')
Traceback (most recent call last):
NameError: Dragon must have a name

Good:

* Easy to use
* Easy to understand
* Much better than print and logging
* Easy to catch programmatically
* Verbose

Bad:

* Requires default value for name, and later checking it

Example:

>>> dragon = Dragon()
Traceback (most recent call last):
NameError: Dragon must have a name

Implementation:

>>> class Dragon:
...     name: str
...
...     def __init__(self, name: str = Name) -> None:
...         if name is None:
...             raise NameError('Dragon must have a name')
...         self.name = name

Decision:

* Candidate


Option 4
--------
>>> dragon = Dragon()
Traceback (most recent call last):
TypeError: Dragon.__init__() missing 1 required positional argument: 'name'

Good:

* Easy to use
* Easy to understand
* Much better than print and logging
* Easy to catch programmatically
* Verbose
* Works out of the box
* Less code to maintain
* Standard Python message that all developers know

Bad:

* Very technical error message (not user friendly)

Example:

>>> dragon = Dragon()  # doctest: +ELLIPSIS
Traceback (most recent call last):
TypeError: ...

Implementation:

>>> class Dragon:
...     name: str
...
...     def __init__(self, name: str, /) -> None: ...

Decision:

* Candidate


Decision
--------
>>> dragon = Dragon()
Traceback (most recent call last):
TypeError: Dragon.__init__() missing 1 required positional argument: 'name'

Rationale:

* Easy to use and understand
* Easy to catch programmatically
* Works out of the box
* Standard Python message that all developers know
* Less code to maintain

Implementation:

>>> class Dragon:
...     def __init__(self, name: str, /) -> None: ...
