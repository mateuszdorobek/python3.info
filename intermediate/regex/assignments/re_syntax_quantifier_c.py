"""
* Assignment: RE Syntax Patterns
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

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
    ['CDR', 'LMP', 'UTC', 'EVA', 'EVA', 'UTC', 'CMP']

    >>> pprint(result_b, compact=True, width=72)
    ['11', '20', '1969', '20', '17', '6', '39', '21', '1969', '02', '56',
     '15', '19', '2', '31', '47', '5', '21', '5', '21', '36']

    >>> pprint(result_c, compact=True, width=72)
    ['20:17', '02:56']

    >>> pprint(result_d, compact=True, width=72)
    ['47.5', '21.5']

    >>> pprint(result_e, compact=True, width=72)
    ['Apollo', 'American', 'Moon', 'Commander', 'Neil', 'Armstrong', 'Buzz',
     'Aldrin', 'Apollo', 'Lunar', 'Module', 'Eagle', 'July', 'Armstrong',
     'Moon', 'July', 'Aldrin', 'They', 'Tranquility', 'Base', 'Armstrong',
     'Aldrin', 'Earth', 'Michael', 'Collins', 'Command', 'Module',
     'Columbia', 'Moon', 'Columbia']

    >>> pprint(result_f, compact=True, width=72)
    ['Neil Armstrong', 'Buzz Aldrin', 'Apollo Lunar', 'Michael Collins',
     'Command Module']

    >>> pprint(result_g, compact=True, width=72)
    ['Apollo 11', 'July 20', 'July 21']

    >>> pprint(result_h, compact=True, width=72)
    []

    >>> pprint(result_i, compact=True, width=72)
    ['6 hours 39 minutes', '2 hours 31 minutes', '21 hours 36 minutes']

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


# Find all three letter acronyms in text (standalone word with three capitalized letters)
# Example: 'CDR', 'LMP', 'UTC', 'EVA', 'EVA', 'UTC', 'CMP'
# type: list[str]
result_a = re.findall(r'[A-Z]{3}', TEXT)

# Find all integers in text (as long as possible)
# Example: '11', '20', '1969', ...
# type: list[str]
result_b = re.findall(r'[0-9]+', TEXT)



# Find all times in text
# Example: '20:17', '02:56'
# type: list[str]
result_c = re.findall(r'[0-9]+:[0-9]+', TEXT)

# Find all floats in text
# Example: '47.5', '21.5'
# type: list[str]
result_d = re.findall(r'[0-9]+\.[0-9]+', TEXT)



# Find all capitalized words
# Example: 'Apollo', 'Moon', 'Commander', 'Neil', 'Armstrong', ...
# type: list[str]
result_e = re.findall(r'[A-Z][a-z]+', TEXT)

# Find all names (two capitalized words) in text
# Example: 'Neil Armstrong', 'Buzz Aldrin', 'Apollo Lunar', 'Tranquility Base', ...
# type: list[str]
result_f = re.findall(r'[A-Z][a-z]+ [A-Z][a-z]+', TEXT)

# Find all names with numbers (capitalized word followed by number)
# Example: 'Apollo 11', 'July 20', 'July 21'
# type: list[str]
result_g = re.findall(r'[A-Z][a-z]+ [0-9]+', TEXT)




# Find all dates in US long format
# Example: 'July 20, 1969', 'July 21, 1969'
# type: list[str]
result_h = re.findall(r'[A-Z][a-z]+ [0-9]+, [0-9]+', TEXT)

# Find all durations in text
# Example: '6 hours 39 minutes', '2 hours 31 minutes', '21 hours 36 minutes'
# type: list[str]
result_i = re.findall(r'[0-9]+ hours [0-9]+ minutes', TEXT)

# Solution
