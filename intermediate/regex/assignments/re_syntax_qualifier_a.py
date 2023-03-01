"""
* Assignment: RE Syntax Qualifier
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Define `result: str` with regular expression to find:
        a. all digits
        b. all uppercase letters
        c. all lowercase letters
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z wyrażeniem regularnym aby wyszukać:
        a. wszystkie cyfry
        b. wszystkie duże litery
        c. wszystkie małe litery
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
    ['1', '1', '2', '0', '1', '9', '6', '9', '2', '0', '1', '7', '6', '3',
     '9', '2', '1', '1', '9', '6', '9', '0', '2', '5', '6', '1', '5', '1',
     '9', '2', '3', '1', '4', '7', '5', '2', '1', '5', '2', '1', '3', '6']

    >>> result = re.findall(result_b, TEXT)
    >>> pprint(result, compact=True, width=72)
    ['A', 'A', 'M', 'C', 'C', 'D', 'R', 'N', 'A', 'L', 'M', 'P', 'B', 'A',
     'A', 'L', 'M', 'L', 'M', 'E', 'J', 'U', 'T', 'C', 'A', 'E', 'V', 'A',
     'M', 'E', 'V', 'A', 'J', 'U', 'T', 'C', 'A', 'T', 'T', 'B', 'A', 'A',
     'E', 'M', 'C', 'C', 'M', 'P', 'C', 'M', 'C', 'M', 'C', 'M', 'C']

    >>> result = re.findall(result_c, TEXT)
    >>> pprint(result, compact=True, width=72)
    ['p', 'o', 'l', 'l', 'o', 'w', 'a', 's', 't', 'h', 'e', 'm', 'e', 'r',
     'i', 'c', 'a', 'n', 's', 'p', 'a', 'c', 'e', 'f', 'l', 'i', 'g', 'h',
     't', 't', 'h', 'a', 't', 'f', 'i', 'r', 's', 't', 'l', 'a', 'n', 'd',
     'e', 'd', 'h', 'u', 'm', 'a', 'n', 's', 'o', 'n', 't', 'h', 'e', 'o',
     'o', 'n', 'o', 'm', 'm', 'a', 'n', 'd', 'e', 'r', 'e', 'i', 'l', 'r',
     'm', 's', 't', 'r', 'o', 'n', 'g', 'a', 'n', 'd', 'l', 'u', 'n', 'a',
     'r', 'm', 'o', 'd', 'u', 'l', 'e', 'p', 'i', 'l', 'o', 't', 'u', 'z',
     'z', 'l', 'd', 'r', 'i', 'n', 'l', 'a', 'n', 'd', 'e', 'd', 't', 'h',
     'e', 'p', 'o', 'l', 'l', 'o', 'u', 'n', 'a', 'r', 'o', 'd', 'u', 'l',
     'e', 'a', 'g', 'l', 'e', 'o', 'n', 'u', 'l', 'y', 't', 'h', 'a', 't',
     'a', 'n', 'd', 'r', 'm', 's', 't', 'r', 'o', 'n', 'g', 'b', 'e', 'c',
     'a', 'm', 'e', 't', 'h', 'e', 'f', 'i', 'r', 's', 't', 'p', 'e', 'r',
     's', 'o', 'n', 't', 'o', 's', 't', 'e', 'p', 'o', 'n', 't', 'o', 't',
     'h', 'e', 'o', 'o', 'n', 's', 's', 'u', 'r', 'f', 'a', 'c', 'e', 'h',
     'o', 'u', 'r', 's', 'm', 'i', 'n', 'u', 't', 'e', 's', 'l', 'a', 't',
     'e', 'r', 'o', 'n', 'u', 'l', 'y', 's', 't', 'a', 't', 'l', 'd', 'r',
     'i', 'n', 'j', 'o', 'i', 'n', 'e', 'd', 'h', 'i', 'm', 'm', 'i', 'n',
     'u', 't', 'e', 's', 'l', 'a', 't', 'e', 'r', 'h', 'e', 'y', 's', 'p',
     'e', 'n', 't', 'h', 'o', 'u', 'r', 's', 'm', 'i', 'n', 'u', 't', 'e',
     's', 'e', 'x', 'p', 'l', 'o', 'r', 'i', 'n', 'g', 't', 'h', 'e', 's',
     'i', 't', 'e', 't', 'h', 'e', 'y', 'h', 'a', 'd', 'n', 'a', 'm', 'e',
     'd', 'r', 'a', 'n', 'q', 'u', 'i', 'l', 'i', 't', 'y', 'a', 's', 'e',
     'u', 'p', 'o', 'n', 'l', 'a', 'n', 'd', 'i', 'n', 'g', 'r', 'm', 's',
     't', 'r', 'o', 'n', 'g', 'a', 'n', 'd', 'l', 'd', 'r', 'i', 'n', 'c',
     'o', 'l', 'l', 'e', 'c', 't', 'e', 'd', 'p', 'o', 'u', 'n', 'd', 's',
     'k', 'g', 'o', 'f', 'l', 'u', 'n', 'a', 'r', 'm', 'a', 't', 'e', 'r',
     'i', 'a', 'l', 't', 'o', 'b', 'r', 'i', 'n', 'g', 'b', 'a', 'c', 'k',
     't', 'o', 'a', 'r', 't', 'h', 'a', 's', 'p', 'i', 'l', 'o', 't', 'i',
     'c', 'h', 'a', 'e', 'l', 'o', 'l', 'l', 'i', 'n', 's', 'f', 'l', 'e',
     'w', 't', 'h', 'e', 'o', 'm', 'm', 'a', 'n', 'd', 'o', 'd', 'u', 'l',
     'e', 'o', 'l', 'u', 'm', 'b', 'i', 'a', 'i', 'n', 'l', 'u', 'n', 'a',
     'r', 'o', 'r', 'b', 'i', 't', 'a', 'n', 'd', 'w', 'e', 'r', 'e', 'o',
     'n', 't', 'h', 'e', 'o', 'o', 'n', 's', 's', 'u', 'r', 'f', 'a', 'c',
     'e', 'f', 'o', 'r', 'h', 'o', 'u', 'r', 's', 'm', 'i', 'n', 'u', 't',
     'e', 's', 'b', 'e', 'f', 'o', 'r', 'e', 'l', 'i', 'f', 't', 'i', 'n',
     'g', 'o', 'f', 'f', 't', 'o', 'r', 'e', 'j', 'o', 'i', 'n', 'o', 'l',
     'u', 'm', 'b', 'i', 'a']

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

# Find all digits in text
# Example: '1', '1', '2', '0', '1', '9', '6', ...
# type: str
result_a = ...

# Find all uppercase letters in text
# Example: 'A', 'A', 'M', 'C', 'C', 'D', 'R', ...
# type: str
result_b = ...

# Find all lowercase letters in text
# Example: 'p', 'o', 'l', 'l', 'o', ...
# type: str
result_c = ...

# Solution
result_a = r'[0-9]'
result_b = r'[A-Z]'
result_c = r'[a-z]'
