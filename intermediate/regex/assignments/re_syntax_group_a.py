"""
* Assignment: RE Syntax Patterns
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Use regular expressions find in text:
        a. all dates (month name followed by day number)
    2. Run doctests - all must succeed

Polish:
    1. Użyj wyrażeń regularnych wyszukiwania w tekście:
        a. wszyskie daty (miesiąc po którym jest dzień)
    2. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * `re.findall()`
    * After day there is an ordinal: st, nd, rd, th (you can use: ..)

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

    >>> pprint(result, compact=True)
    ['July 20', 'July 21']
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

# Find all dates (month name followed by day number)
# Note: after day there is an ordinal: st, nd, rd, th (you can use: ..)
# Example: 'July 20', 'July 21'
# type: list[str]
result = ...

# Solution
result = re.findall(r'([A-Z][a-z]+ \d{1,2}).., \d{4}', TEXT)
