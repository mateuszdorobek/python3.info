"""
* Assignment: RE Syntax Quantifier
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

TODO: This assignment is not ready yet.

English:
    1. Use regular expressions find in text
    2. Run doctests - all must succeed

Polish:
    1. Użyj wyrażeń regularnych wyszukiwania w tekście
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
    ['11', '20', '1969', '20', '17', '6', '39', '21', '1969', '02', '56',
     '15', '19', '2', '31', '47', '5', '21', '5', '21', '36']

    >>> pprint(result_b, compact=True, width=72)
    ['47.5', '21.5']
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

# Find all integers in text (as long as possible)
# Example: '11', '20', '1969', ...
# type: list[str]
result_a = ...


# Find all floats in text
# Example: '47.5', '21.5'
# type: list[str]
result_b = ...


# Solution
result_a = re.findall(r'[0-9]+', TEXT)
result_b = re.findall(r'[0-9]+\.[0-9]+', TEXT)
