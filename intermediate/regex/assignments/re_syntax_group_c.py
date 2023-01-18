"""
* Assignment: RE Syntax Patterns
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Use regular expressions find in text:
        a. durations in list[dict] format
           example: 6 hours 39 minutes -> [{'hours': '6', 'minutes': '39'}, ...]
    2. Run doctests - all must succeed

Polish:
    1. Użyj wyrażeń regularnych wyszukiwania w tekście:
        a. okresy w formacie list[dict]
           przykład: 6 hours 39 minutes -> [{'hours': '6', 'minutes': '39'}, ...]
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

    >>> pprint(result)
    [{'hours': '6', 'minutes': '39'},
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
They spent 2 hours 31 minutes exploring the site they had named Tranquility
Base upon landing. Armstrong and Aldrin collected 47.5 pounds (21.5 kg)
of lunar material to bring back to Earth as pilot Michael Collins (CMP)
flew the Command Module (CM) Columbia in lunar orbit, and were on the
Moon's surface for 21 hours 36 minutes before lifting off to rejoin
Columbia."""

# Extract duration values from text in list[dict] format
# Example: [{'hours': '6', 'minutes': '39'}, {'hours': '2', 'minutes': '31'}, ...]
# type: list[str]
result = ...

# Solution
pattern = r'(?P<hours>[0-9]+) hours (?P<minutes>[0-9]+) minutes'
result = [x.groupdict() for x in re.finditer(pattern, TEXT)]
