"""
* Assignment: RE Syntax Qualifier
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: str` with regular expression to find:
        a. all digits and uppercase letters
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z wyrażeniem regularnym aby wyszukać:
        a. wszystkie cyfry i duże litery
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

    >>> result = re.findall(result, TEXT)
    >>> pprint(result, compact=True, width=72)
    ['A', '1', '1', 'A', 'M', 'C', 'C', 'D', 'R', 'N', 'A', 'L', 'M', 'P',
     'B', 'A', 'A', 'L', 'M', 'L', 'M', 'E', 'J', '2', '0', '1', '9', '6',
     '9', '2', '0', '1', '7', 'U', 'T', 'C', 'A', 'E', 'V', 'A', 'M', 'E',
     'V', 'A', '6', '3', '9', 'J', '2', '1', '1', '9', '6', '9', '0', '2',
     '5', '6', '1', '5', 'U', 'T', 'C', 'A', '1', '9', 'T', '2', '3', '1',
     'T', 'B', 'A', 'A', '4', '7', '5', '2', '1', '5', 'E', 'M', 'C', 'C',
     'M', 'P', 'C', 'M', 'C', 'M', 'C', 'M', '2', '1', '3', '6', 'C']
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

# Find all digits and uppercase letters in text
# Example: 'A', '1', '1', 'A', 'M', 'C', 'C', 'D', 'R', ...
# Note: define only regex pattern (str), not re.findall(..., TEXT)
# type: str
result = ...

# Solution
result = r'[A-Z0-9]'
