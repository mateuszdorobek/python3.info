"""
* Assignment: RE Syntax Identifier
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define `result: str` with regular expression to find:
        a. all conjunctives (both two- and three-letter words)
        b. all acronyms (standalone words with two or three uppercase letters)
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z wyrażeniem regularnym aby wyszukać:
        a. wszystkie spójniki (zarówno dwu jak i trzy literowe słowa)
        b. wszystkie akronimy (słowa pisane dwoma lub trzemi dużymi literami)
    2. Uruchom doctesty - wszystkie muszą się powieść

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

    >>> result = re.findall(result_a, TEXT)
    >>> pprint(result, compact=True, width=72)
    ['was', 'the', 'on', 'the', 'and', 'the', 'on', 'at', 'and', 'the',
     'to', 'the', 'on', 'at', 'him', 'the', 'had', 'and', 'kg', 'of', 'to',
     'to', 'as', 'the', 'in', 'and', 'on', 'the', 'for', 'off', 'to']

    >>> result = re.findall(result_b, TEXT)
    >>> pprint(result, compact=True, width=72)
    ['CDR', 'LMP', 'LM', 'UTC', 'EVA', 'EVA', 'UTC', 'CMP', 'CM']
"""

import re

TEXT = """Apollo 11 was the American spaceflight that first landed
humans on the Moon. Commander (CDR) Neil Armstrong and lunar module
pilot (LMP) Buzz Aldrin landed the Apollo Lunar Module (LM) Eagle on
July 20th, 1969 at 20:17 UTC, and Armstrong became the first person
to step (EVA) onto the Moon's surface (EVA) 6 hours 39 minutes later,
on July 21st, 1969 at 02:56:15 UTC. Aldrin joined him 19 minutes later.
They spent 2 hours 31 minutes exploring the site they had named
Tranquility Base upon landing. Armstrong and Aldrin collected 47.5 pounds
(21.5 kg) of lunar material to bring back to Earth as pilot Michael Collins
(CMP) flew the Command Module (CM) Columbia in lunar orbit, and were on the
Moon's surface for 21 hours 36 minutes before lifting off to rejoin
Columbia."""

# Find all conjunctives in text (standalone both two- and three-letter words)
# Example: 'was', 'the', 'on', 'the', 'and', ...
# Note: define only regex pattern (str), not re.findall(...)
# type: str
result_a = ...

# Find all acronyms in text (standalone words with two or three uppercase letters)
# Example: 'CDR', 'LMP', 'LM', 'UTC', 'EVA', 'EVA', 'UTC', 'CMP', 'CM'
# Note: define only regex pattern (str), not re.findall(...)
# type: str
result_b = ...

# Solution
result_a = r'\b[a-z][a-z]\b|\b[a-z][a-z][a-z]\b'
result_b = r'\b[A-Z][A-Z]\b|\b[A-Z][A-Z][A-Z]\b'
