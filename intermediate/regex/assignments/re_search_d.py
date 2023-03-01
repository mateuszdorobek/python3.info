"""
* Assignment: RE Search Datetime
* Complexity: hard
* Lines of code: 4 lines
* Time: 13 min

English:
    1. Use regular expressions to check text [1] contains time in UTC (format: `%H:%M UTC`)
    2. Note, that this is slightly modified text than previously
    3. Check if text contains time in UTC (format: `%H:%M UTC`)
    4. Found match must be a valid time
    5. Run doctests - all must succeed

Polish:
    1. Użyj wyrażeń regularnych do sprawdzenia czy tekst [1] zawiera godzinę w UTC (format: `%H:%M UTC`)
    2. Zwróć uwagę, że to lekko zmodyfikowany tekst niż poprzednio
    3. Sprawdź czy tekst zawiera godzinę w UTC (format: `%H:%M UTC`)
    4. Znalezisko musi być poprawnym czasem
    5. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] Wikipedia Apollo 11,
        URL: https://en.wikipedia.org/wiki/Apollo_11
        Year: 2019
        Retrieved: 2019-12-14

Hints:
    * `re.Match.group()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is str, 'result must be a str'
    >>> assert result.endswith('UTC'), 'result must contain timezone'

    >>> result
    '02:56 UTC'
"""

import re


TEXT = ("Apollo 11 was the spaceflight that first landed humans on the Moon. "
        "Commander Neil Armstrong and lunar module pilot Buzz Aldrin formed "
        "the American crew that landed the Apollo Lunar Module Eagle on July "
        "20, 1969, at 24:56 UTC. Armstrong became the first person to step "
        "onto the lunar surface six hours and 39 minutes later on July 21 at "
        "02:56 UTC; Aldrin joined him 19 minutes later. They spent about two "
        "and a quarter hours together outside the spacecraft, and they "
        "collected 47.5 pounds (21.5 kg) of lunar material to bring back to "
        "Earth. Command module pilot Michael Collins flew the command module "
        "Columbia alone in lunar orbit while they were on the Moon's surface."
        "Armstrong and Aldrin spent 21 hours, 36 minutes on the lunar surface"
        "at a site they named Tranquility Base before lifting off to rejoin "
        "Columbia in lunar orbit.")


# Pattern for searching time with timezone in 24 format, i.e. '23:59 UTC'
# type: str
pattern = ...

# use re.search() to find pattern in TEXT
# use .group() to get the value from re.Match object
# type: str
result = ...


# Solution
hour = r'([01][0-9]|2[0-3])'
minute = r'[0-5][0-9]'
pattern = f'{hour}:{minute} UTC'
result = re.search(pattern, TEXT).group()
