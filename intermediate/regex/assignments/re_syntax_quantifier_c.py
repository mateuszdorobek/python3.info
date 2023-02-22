"""
* Assignment: RE Syntax Quantifier
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use regular expressions find in text
    2. Run doctests - all must succeed

Polish:
    1. Użyj wyrażeń regularnych wyszukiwania w tekście
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
    ['Apollo', 'American', 'Moon', 'Commander', 'Neil', 'Armstrong', 'Buzz',
     'Aldrin', 'Apollo', 'Lunar', 'Module', 'Eagle', 'July', 'Armstrong',
     'Moon', 'July', 'Aldrin', 'They', 'Tranquility', 'Base', 'Armstrong',
     'Aldrin', 'Earth', 'Michael', 'Collins', 'Command', 'Module',
     'Columbia', 'Moon', 'Columbia']

    >>> result = re.findall(result_b, TEXT)
    >>> pprint(result, compact=True, width=72)
    ['Neil Armstrong', 'Buzz Aldrin', 'Apollo Lunar', 'Michael Collins',
     'Command Module']

    >>> result = re.findall(result_c, TEXT)
    >>> pprint(result, compact=True, width=72)
    ['Apollo 11', 'July 20', 'July 21']

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


# Find all capitalized words
# Example: 'Apollo', 'Moon', 'Commander', 'Neil', 'Armstrong', ...
# type: str
result_a = ...

# Find all names (two capitalized words) in text
# Example: 'Neil Armstrong', 'Buzz Aldrin', 'Apollo Lunar', 'Tranquility Base', ...
# type: str
result_b = ...

# Find all names with numbers (capitalized word followed by number)
# Example: 'Apollo 11', 'July 20', 'July 21'
# type: str
result_c = ...


# Solution
result_a = r'[A-Z][a-z]+'
result_b = r'[A-Z][a-z]+ [A-Z][a-z]+'
result_c = r'[A-Z][a-z]+ [0-9]+'
