"""
* Assignment: OOP Init Define
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Create one class `Hello`
    2. At initialization instance print `hello world`
    3. Do not store any values
    4. Run doctests - all must succeed

Polish:
    1. Stwórz jedną klasę `Hello`
    2. Przy inicjalizacji instancja wypisuje `hello world`
    3. Nie przechowuj żadnych informacji
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result = Hello()
    hello world
    >>> vars(result)
    {}
"""


# Solution
class Hello:
    def __init__(self):
        print('hello world')
