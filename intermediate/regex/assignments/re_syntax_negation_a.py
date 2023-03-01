"""
* Assignment: RE Syntax Negation
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Define `result: str` with regular expression to find:
        a. non-digits
        b. non-lowercase-letters
        c. non-uppercase-letters
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z wyrażeniem regularnym aby wyszukać:
        a. nie-cyfry
        b. nie-małe-litery
        c. nie-duże-litery
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
    ['\\n', ' ', "'", '(', ')', ',', '.', ':', 'A', 'B', 'C', 'D', 'E', 'J',
     'L', 'M', 'N', 'P', 'R', 'T', 'U', 'V', 'a', 'b', 'c', 'd', 'e', 'f',
     'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
     'u', 'w', 'x', 'y', 'z']

    >>> result = re.findall(result_b, TEXT)
    >>> result = sorted(set(result))
    >>> pprint(result, compact=True, width=72)
    ['\\n', ' ', "'", '(', ')', ',', '.', '0', '1', '2', '3', '4', '5', '6',
     '7', '9', ':', 'A', 'B', 'C', 'D', 'E', 'J', 'L', 'M', 'N', 'P', 'R',
     'T', 'U', 'V']

    >>> result = re.findall(result_c, TEXT)
    >>> result = sorted(set(result))
    >>> pprint(result, compact=True, width=72)
    ['\\n', ' ', "'", '(', ')', ',', '.', '0', '1', '2', '3', '4', '5', '6',
     '7', '9', ':', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']
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

# Find all non-digits
# Example: '\n', ' ', "'", '(', ')', ',', '.', ':'
# type: str
result_a = ...

# Find all non-lowercase-letters
# Example: '\n', ' ', "'", '(', ')', ',', '.', '0', '1', '2', '3', ...
# type: str
result_b = ...

# Find all non-uppercase-letters
# Example: '\n', ' ', "'", '(', ')', ',', '.', '0', '1', '2', '3', ...
# type: str
result_c = ...

# Solution
result_a = r'[^0-9]'
result_b = r'[^a-z]'
result_c = r'[^A-Z]'
