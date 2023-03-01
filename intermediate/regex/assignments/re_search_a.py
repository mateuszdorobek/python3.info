"""
* Assignment: RE Search Astronauts
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Use `re.search()` to get start and end position in `TEXT`:
        a. Define `a: tuple[int,int]` for 'Neil Armstrong'
        b. Define `b: tuple[int,int]` for 'Buzz Aldrin'
        c. Define `c: tuple[int,int]` for 'Michael Collins'
        d. Define `d: tuple[int,int]` for 'July 21 at 02:56 UTC'
        e. Define `e: tuple[int,int]` for 'Tranquility Base'
        f. Define `f: tuple[int,int]` for 'Mark Watney'
    2. For each element return tuple i.e. `(10, 20)`
    3. If element is not present in `TEXT` assign `None`
    4. Run doctests - all must succeed

Polish:
    1. Użyj `re.search()` aby dostać pozycję startu i końca w `TEXT`:
        a. Zdefiniuj `a: tuple[int,int]` dla 'Neil Armstrong'
        b. Zdefiniuj `b: tuple[int,int]` dla 'Buzz Aldrin'
        c. Zdefiniuj `c: tuple[int,int]` dla 'Michael Collins'
        d. Zdefiniuj `d: tuple[int,int]` dla 'July 21 at 02:56 UTC'
        e. Zdefiniuj `e: tuple[int,int]` dla 'Tranquility Base'
        f. Zdefiniuj `f: tuple[int,int]` dla 'Mark Watney'
    2. Dla każdego ciągu znaków zwracaj tuple np. `(10, 20)`
    3. Jeżeli ciąg znaków nie jest obecny w `TEXT` przypisz `None`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `re.Match.span()`

References:
    [1] Wikipedia: Apollo 11
        URL: https://en.wikipedia.org/wiki/Apollo_11
        Year: 2019
        Retrieved: 2019-12-14

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(a) is tuple, 'a must be a tuple'
    >>> assert type(b) is tuple, 'b must be a tuple'
    >>> assert type(c) is tuple, 'c must be a tuple'
    >>> assert type(d) is tuple, 'd must be a tuple'
    >>> assert type(e) is tuple, 'e must be a tuple'
    >>> assert f is None, 'f must be a None'

    >>> assert len(a) == 2, 'a must be a tuple with two elements'
    >>> assert len(b) == 2, 'b must be a tuple with two elements'
    >>> assert len(c) == 2, 'c must be a tuple with two elements'
    >>> assert len(d) == 2, 'd must be a tuple with two elements'
    >>> assert len(e) == 2, 'e must be a tuple with two elements'

    >>> assert all(type(x) is int for x in a), 'a must be a tuple[int,int]'
    >>> assert all(type(x) is int for x in b), 'b must be a tuple[int,int]'
    >>> assert all(type(x) is int for x in c), 'c must be a tuple[int,int]'
    >>> assert all(type(x) is int for x in d), 'd must be a tuple[int,int]'
    >>> assert all(type(x) is int for x in e), 'e must be a tuple[int,int]'

    >>> a
    (78, 92)
    >>> b
    (116, 127)
    >>> c
    (562, 577)
    >>> d
    (326, 346)
    >>> e
    (761, 777)
"""

import re


TEXT = ("Apollo 11 was the spaceflight that first landed humans on the Moon. "
        "Commander Neil Armstrong and lunar module pilot Buzz Aldrin formed "
        "the American crew that landed the Apollo Lunar Module Eagle on "
        "July 20, 1969, at 20:17 UTC. Armstrong became the first person to "
        "step onto the lunar surface six hours and 39 minutes later on "
        "July 21 at 02:56 UTC; Aldrin joined him 19 minutes later. They spent "
        "about two and a quarter hours together outside the spacecraft, "
        "and they collected 47.5 pounds (21.5 kg) of lunar material to bring "
        "back to Earth. Command module pilot Michael Collins flew the command "
        "module Columbia alone in lunar orbit while they were on the Moon's "
        "surface. Armstrong and Aldrin spent 21 hours, 36 minutes on the "
        "lunar surface at a site they named Tranquility Base before lifting "
        "off to rejoin Columbia in lunar orbit. ")


# use re.search() to get 'Neil Armstrong' a (start, end) position or None
# type: tuple[int,int] | None
a = ...

# use re.search() to get 'Buzz Aldrin' a (start, end) position or None
# type: tuple[int,int] | None
b = ...

# use re.search() to get 'Michael Collins' a (start, end) position or None
# type: tuple[int,int] | None
c = ...

# use re.search() to get 'July 21 at 02:56 UTC' a (start, end) position or None
# type: tuple[int,int] | None
d = ...

# use re.search() to get 'Tranquility Base' a (start, end) position or None
# type: tuple[int,int] | None
e = ...

# use re.search() to get 'Mark Watney' a (start, end) position or None
# type: tuple[int,int] | None
f = ...


# Solution
def search(pattern):
    if r := re.search(pattern, TEXT):
        return r.span()

a = search('Neil Armstrong')
b = search('Buzz Aldrin')
c = search('Michael Collins')
d = search('July 21 at 02:56 UTC')
e = search('Tranquility Base')
f = search('Mark Watney')
