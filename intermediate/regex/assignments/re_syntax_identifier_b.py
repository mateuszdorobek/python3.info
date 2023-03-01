"""
* Assignment: RE Syntax Identifier
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define `result: str` with regular expression to find:
        a. whitespace characters
        b. non-whitespace characters
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z wyrażeniem regularnym aby wyszukać:
        a. białe-znaki
        b. nie-białe-znaki
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
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\n', ' ', ' ', ' ', ' ', ' ',
     ' ', ' ', ' ', ' ', ' ', '\\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
     ' ', ' ', ' ', '\\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
     ' ', '\\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
     '\\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\n',
     ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\n', ' ',
     ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\n', ' ', ' ', ' ', ' ',
     ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\n', ' ', ' ', ' ', ' ', ' ',
     ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\n', ' ', ' ', ' ', ' ', ' ', ' ',
     ' ', ' ', ' ', ' ', ' ', '\\n']

    >>> result = re.findall(result_b, TEXT)
    >>> pprint(result, compact=True, width=72)
    ['A', 'p', 'o', 'l', 'l', 'o', '1', '1', 'w', 'a', 's', 't', 'h', 'e',
     'A', 'm', 'e', 'r', 'i', 'c', 'a', 'n', 's', 'p', 'a', 'c', 'e', 'f',
     'l', 'i', 'g', 'h', 't', 't', 'h', 'a', 't', 'f', 'i', 'r', 's', 't',
     'l', 'a', 'n', 'd', 'e', 'd', 'h', 'u', 'm', 'a', 'n', 's', 'o', 'n',
     't', 'h', 'e', 'M', 'o', 'o', 'n', '.', 'C', 'o', 'm', 'm', 'a', 'n',
     'd', 'e', 'r', '(', 'C', 'D', 'R', ')', 'N', 'e', 'i', 'l', 'A', 'r',
     'm', 's', 't', 'r', 'o', 'n', 'g', 'a', 'n', 'd', 'l', 'u', 'n', 'a',
     'r', 'm', 'o', 'd', 'u', 'l', 'e', 'p', 'i', 'l', 'o', 't', '(', 'L',
     'M', 'P', ')', 'B', 'u', 'z', 'z', 'A', 'l', 'd', 'r', 'i', 'n', 'l',
     'a', 'n', 'd', 'e', 'd', 't', 'h', 'e', 'A', 'p', 'o', 'l', 'l', 'o',
     'L', 'u', 'n', 'a', 'r', 'M', 'o', 'd', 'u', 'l', 'e', '(', 'L', 'M',
     ')', 'E', 'a', 'g', 'l', 'e', 'o', 'n', 'J', 'u', 'l', 'y', '2', '0',
     't', 'h', ',', '1', '9', '6', '9', 'a', 't', '2', '0', ':', '1', '7',
     'U', 'T', 'C', ',', 'a', 'n', 'd', 'A', 'r', 'm', 's', 't', 'r', 'o',
     'n', 'g', 'b', 'e', 'c', 'a', 'm', 'e', 't', 'h', 'e', 'f', 'i', 'r',
     's', 't', 'p', 'e', 'r', 's', 'o', 'n', 't', 'o', 's', 't', 'e', 'p',
     '(', 'E', 'V', 'A', ')', 'o', 'n', 't', 'o', 't', 'h', 'e', 'M', 'o',
     'o', 'n', "'", 's', 's', 'u', 'r', 'f', 'a', 'c', 'e', '(', 'E', 'V',
     'A', ')', '6', 'h', 'o', 'u', 'r', 's', '3', '9', 'm', 'i', 'n', 'u',
     't', 'e', 's', 'l', 'a', 't', 'e', 'r', ',', 'o', 'n', 'J', 'u', 'l',
     'y', '2', '1', 's', 't', ',', '1', '9', '6', '9', 'a', 't', '0', '2',
     ':', '5', '6', ':', '1', '5', 'U', 'T', 'C', '.', 'A', 'l', 'd', 'r',
     'i', 'n', 'j', 'o', 'i', 'n', 'e', 'd', 'h', 'i', 'm', '1', '9', 'm',
     'i', 'n', 'u', 't', 'e', 's', 'l', 'a', 't', 'e', 'r', '.', 'T', 'h',
     'e', 'y', 's', 'p', 'e', 'n', 't', '2', 'h', 'o', 'u', 'r', 's', '3',
     '1', 'm', 'i', 'n', 'u', 't', 'e', 's', 'e', 'x', 'p', 'l', 'o', 'r',
     'i', 'n', 'g', 't', 'h', 'e', 's', 'i', 't', 'e', 't', 'h', 'e', 'y',
     'h', 'a', 'd', 'n', 'a', 'm', 'e', 'd', 'T', 'r', 'a', 'n', 'q', 'u',
     'i', 'l', 'i', 't', 'y', 'B', 'a', 's', 'e', 'u', 'p', 'o', 'n', 'l',
     'a', 'n', 'd', 'i', 'n', 'g', '.', 'A', 'r', 'm', 's', 't', 'r', 'o',
     'n', 'g', 'a', 'n', 'd', 'A', 'l', 'd', 'r', 'i', 'n', 'c', 'o', 'l',
     'l', 'e', 'c', 't', 'e', 'd', '4', '7', '.', '5', 'p', 'o', 'u', 'n',
     'd', 's', '(', '2', '1', '.', '5', 'k', 'g', ')', 'o', 'f', 'l', 'u',
     'n', 'a', 'r', 'm', 'a', 't', 'e', 'r', 'i', 'a', 'l', 't', 'o', 'b',
     'r', 'i', 'n', 'g', 'b', 'a', 'c', 'k', 't', 'o', 'E', 'a', 'r', 't',
     'h', 'a', 's', 'p', 'i', 'l', 'o', 't', 'M', 'i', 'c', 'h', 'a', 'e',
     'l', 'C', 'o', 'l', 'l', 'i', 'n', 's', '(', 'C', 'M', 'P', ')', 'f',
     'l', 'e', 'w', 't', 'h', 'e', 'C', 'o', 'm', 'm', 'a', 'n', 'd', 'M',
     'o', 'd', 'u', 'l', 'e', '(', 'C', 'M', ')', 'C', 'o', 'l', 'u', 'm',
     'b', 'i', 'a', 'i', 'n', 'l', 'u', 'n', 'a', 'r', 'o', 'r', 'b', 'i',
     't', ',', 'a', 'n', 'd', 'w', 'e', 'r', 'e', 'o', 'n', 't', 'h', 'e',
     'M', 'o', 'o', 'n', "'", 's', 's', 'u', 'r', 'f', 'a', 'c', 'e', 'f',
     'o', 'r', '2', '1', 'h', 'o', 'u', 'r', 's', '3', '6', 'm', 'i', 'n',
     'u', 't', 'e', 's', 'b', 'e', 'f', 'o', 'r', 'e', 'l', 'i', 'f', 't',
     'i', 'n', 'g', 'o', 'f', 'f', 't', 'o', 'r', 'e', 'j', 'o', 'i', 'n',
     'C', 'o', 'l', 'u', 'm', 'b', 'i', 'a', '.']
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

# Find all whitespace characters in text
# Example: '\n', ' '
# type: str
result_a = ...

# Find all non-whitespace characters in text
# Example: "'", '(', ')', ',', '.', '0', '1', '2', '3', '4', '5', '6', ...
# type: str
result_b = ...

# Solution
result_a = r'\s'
result_b = r'\S'
