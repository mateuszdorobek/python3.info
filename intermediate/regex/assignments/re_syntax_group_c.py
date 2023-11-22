"""
* Assignment: RE Syntax Group
* Complexity: medium
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Define `result: str` with regular expression to find:
        a. all duration values, SKIP durations without hours
        b. all duration values, DO NOT SKIP durations without hours
    2. Use named group
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z wyrażeniem regularnym aby wyszukać:
       a. wszystkie okresy czasowe, POMIŃ okresy bez godzin
       b. wszystkie okresy czasowe, NIE POMIJAJ okresów bez godzin
    2. Użyj grup nazwanych
    3. Uruchom doctesty - wszystkie muszą się powieść

Hits:
    * Use non-capturing group

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

    >>> result_a = re.finditer(result_a, TEXT)
    >>> result_a = [x.groupdict() for x in result_a]
    >>> pprint(result_a, compact=True, width=50)
    [{'hours': '6', 'minutes': '39'},
     {'hours': '2', 'minutes': '31'},
     {'hours': '21', 'minutes': '36'}]

    >>> result_b = re.finditer(result_b, TEXT)
    >>> result_b = [x.groupdict() for x in result_b]
    >>> pprint(result_b, compact=True, width=50)
    [{'hours': '6', 'minutes': '39'},
     {'hours': None, 'minutes': '19'},
     {'hours': '2', 'minutes': '31'},
     {'hours': '21', 'minutes': '36'}]
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

# Find all duration values, use named groups
# SKIP durations without hours: 19 minutes later
# Example: [{'hours': '6', 'minutes': '39'}, {'hours': '2', 'minutes': '31'}]
# Note: define only regex pattern (str), not re.findall(...)
# type: str
result_a = r''

# Find all duration values, use named groups
# DO NOT SKIP durations without hours: 19 minutes later
# Example: [{'hours': '6', 'minutes': '39'}, {'hours': None, 'minutes': '19'}]
# Hint: Use non-capturing group
# Note: define only regex pattern (str), not re.findall(...)
# type: str
result_b = r''

# Solution
result_a = '(?P<hours>\d+) hours (?P<minutes>\d+) minutes'
result_b = '(?:(?P<hours>\d+) hours)? (?P<minutes>\d+) minutes'
