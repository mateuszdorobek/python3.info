"""
* Assignment: RE Syntax Quantifier
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Define `result: str` with regular expression to find:
       a. times (hours and minutes)
       b. dates in US long format
       c. durations in text
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z wyrażeniem regularnym aby wyszukać:
       a. czasy (godziny z minutami)
       b. daty w formacie amerykańskim długim
       c. okresy
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
    ['20:17', '02:56']

    >>> result = re.findall(result_b, TEXT)
    >>> pprint(result, compact=True, width=72)
    ['July 20, 1969', 'July 21, 1969']

    >>> result = re.findall(result_c, TEXT)
    >>> pprint(result, compact=True, width=72)
    ['6 hours 39 minutes', '2 hours 31 minutes', '21 hours 36 minutes']

"""

import re

TEXT = """Apollo 11 was the American spaceflight that first landed
humans on the Moon. Commander (CDR) Neil Armstrong and lunar module
pilot (LMP) Buzz Aldrin landed the Apollo Lunar Module (LM) Eagle on
July 20, 1969 at 20:17 UTC, and Armstrong became the first person
to step (EVA) onto the Moon's surface (EVA) 6 hours 39 minutes later,
on July 21, 1969 at 02:56:15 UTC. Aldrin joined him 19 minutes later.
They spent 2 hours 31 minutes exploring the site they had named Tranquility
Base upon landing. Armstrong and Aldrin collected 47.5 pounds (21.5 kg)
of lunar material to bring back to Earth as pilot Michael Collins (CMP)
flew the Command Module (CM) Columbia in lunar orbit, and were on the
Moon's surface for 21 hours 36 minutes before lifting off to rejoin
Columbia."""


# Find all times in text
# Example: '20:17', '02:56'
# Note: define only regex pattern (str), not re.findall(...)
# type: str
result_a = ...

# Find all dates in US long format
# Example: 'July 20, 1969', 'July 21, 1969'
# Note: define only regex pattern (str), not re.findall(...)
# type: str
result_b = ...

# Find all durations in text
# Example: '6 hours 39 minutes', '2 hours 31 minutes', '21 hours 36 minutes'
# Note: define only regex pattern (str), not re.findall(...)
# type: str
result_c = ...

# Solution
result_a = r'[0-9]+:[0-9]+'
result_b = r'[A-Z][a-z]+ [0-9]+, [0-9]+'
result_c = r'[0-9]+ hours [0-9]+ minutes'
