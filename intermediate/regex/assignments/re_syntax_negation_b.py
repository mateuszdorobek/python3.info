"""
* Assignment: RE Syntax Negation
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Use regular expressions find in text:
        a. non-letters
        b. non-digits and non-letters
    2. Run doctests - all must succeed

Polish:
    1. Użyj wyrażeń regularnych wyszukiwania w tekście:
        a. nie-litery
        b. nie-cyfry i nie-litery
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
    >>> result = sorted(set(result))
    >>> pprint(result, compact=True, width=72)
    ['\\n', ' ', "'", '(', ')', ',', '.', '0', '1', '2', '3', '4', '5', '6',
     '7', '9', ':']

    >>> result = re.findall(result_b, TEXT)
    >>> result = sorted(set(result))
    >>> pprint(result, compact=True, width=72)
    ['\\n', ' ', "'", '(', ')', ',', '.', ':']
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

# Find all non-letters
# Example: '\n', ' ', "'", '(', ')', ',', '.', ':'
# type: str
result_a = ...

# Find all non-digits and non-letters
# Example: '\n', ' ', "'", '(', ')', ',', '.', ':'
# type: str
result_b = ...

# Solution
result_a = r'[^a-zA-Z]'
result_b = r'[^a-zA-Z0-9]'
