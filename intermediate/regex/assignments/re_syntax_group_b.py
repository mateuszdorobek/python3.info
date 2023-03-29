"""
* Assignment: RE Syntax Group
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define `result: str` with regular expression
       to find duration values
    2. Use positional group
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z wyrażeniem regularnym
       aby wyszukać wartości okresów
    2. Użyj grup pozycyjnych
    3. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] Authors: Wikipedia contributors
        Title: Apollo 11
        Publisher: Wikipedia
        Year: 2019
        Retrieved: 2019-12-14
        URL: https://en.wikipedia.org/wiki/Apollo_11

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> result = re.findall(result, TEXT)
    >>> pprint(result, compact=True, width=20)
    [('6', '39'),
     ('2', '31'),
     ('21', '36')]
"""

import re

TEXT = """Apollo 11 was the American spaceflight that first landed
humans on the Moon. Commander (CDR) Neil Armstrong and lunar module
pilot (LMP) Buzz Aldrin landed the Apollo Lunar Module (LM) Eagle on
July 20th, 1969 at 20:17 UTC, and Armstrong became the first person
to step (EVA) onto the Moon's surface (EVA) 6 hours 39 minutes later,
on July 21st, 1969 at 02:56:15 UTC. Aldrin joined him 19 minutes later.
They spent 2 hours 31 minutes exploring the site they had named Tranquility
Base upon landing. Armstrong and Aldrin collected 47.5 pounds (21.5 kg)
of lunar material to bring back to Earth as pilot Michael Collins (CMP)
flew the Command Module (CM) Columbia in lunar orbit, and were on the
Moon's surface for 21 hours 36 minutes before lifting off to rejoin
Columbia."""

# Find all duration values, use positional groups
# Example: [('6', '39'), ('2', '31'), ('21', '36')]
# Note: define only regex pattern (str), not re.findall(...)
# type: str
result = ...

# Solution
result = r'(?P<hours>[0-9]+) hours (?P<minutes>[0-9]+) minutes'
