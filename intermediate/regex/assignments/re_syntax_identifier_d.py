"""
* Assignment: RE Syntax Patterns
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Use regular expressions find in text:
        a. all two-letter conjunctives (two-letter words)
        b. all three-letter conjunctives (three-letter words)
        c. all conjunctives (both two- and three-letter words)
        d. all acronyms (standalone words with two or three uppercase letters)
    2. Run doctests - all must succeed

Polish:
    1. Użyj wyrażeń regularnych wyszukiwania w tekście:
        a. wszystkie dwu literowe spójniki (dwu-literowe słowa)
        b. wszystkie trzy literowe spójniki (trzy literowe słow)
        c. wszystkie spójniki (zarówno dwu jak i trzy literowe słowa)
        d. wszystkie akronimy (słowa pisane dwoma lub trzemi dużymi literami)
    2. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * `re.findall()`

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

    >>> pprint(result_a, compact=True, width=72)
    ['on', 'on', 'at', 'to', 'on', 'at', 'kg', 'of', 'to', 'to', 'as', 'in',
     'on', 'to']

    >>> pprint(result_b, compact=True, width=72)
    ['was', 'the', 'the', 'and', 'the', 'and', 'the', 'the', 'him', 'the',
     'had', 'and', 'the', 'and', 'the', 'for', 'off']

    >>> pprint(result_c, compact=True, width=72)
    ['was', 'the', 'on', 'the', 'and', 'the', 'on', 'at', 'and', 'the',
     'to', 'the', 'on', 'at', 'him', 'the', 'had', 'and', 'kg', 'of', 'to',
     'to', 'as', 'the', 'in', 'and', 'on', 'the', 'for', 'off', 'to']

    >>> pprint(result_d, compact=True, width=72)
    ['CDR', 'LMP', 'LM', 'UTC', 'EVA', 'EVA', 'UTC', 'CMP', 'CM']
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


# Find all two-letter conjunctives in text (two-letter words)
# Example: 'on', 'on', 'at', 'to', ...
# type: list[str]
result_a = ...


# Find all three-letter conjunctives in text (three-letter words)
# Example: 'was', 'the', 'the', 'and', ...
# type: list[str]
result_b = ...


# Find all conjunctives in text (both two- and three-letter words)
# Example: 'was', 'the', 'on', 'the', 'and', ...
# type: list[str]
result_c = ...

# Find all acronyms in text (standalone words with two or three uppercase letters)
# Example: 'CDR', 'LMP', 'LM', 'UTC', 'EVA', 'EVA', 'UTC', 'CMP', 'CM'
# type: list[str]
result_d = ...


# Solution
result_a = re.findall(r'\b[a-z]{2}\b', TEXT)
result_b = re.findall(r'\b[a-z]{3}\b', TEXT)
result_c = re.findall(r'\b[a-z]{2,3}\b', TEXT)
result_d = re.findall(r'\b[A-Z]{2,3}\b', TEXT)
