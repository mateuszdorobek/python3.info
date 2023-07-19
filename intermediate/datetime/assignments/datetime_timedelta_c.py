"""
* Assignment: Datetime Timedelta Period
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Between the first flight to space and the first step on the moon passed:
        * 8 years
        * 3 months
        * 8 days
        * 13 hours
        * 19 minutes
        * 15 seconds
    2. Assumption:
        a. year = 365.25 days
        b. month = 30.4375 days
    3. Define `result: timedelta` representing given period
    4. Run doctests - all must succeed

Polish:
    1. Między pierwszym lotem w kosmos a pierwszym krokiem na Księżycu minęło:
        * 8 lat
        * 3 miesięcy
        * 8 dni
        * 13 godzin
        * 19 minut
        * 15 sekund
    2. Założenie:
        a. rok = 365.25 dni
        b. miesiąc = 30.4375 dni
    3. Zdefiniuj `result: timedelta` reprezentujące dany okres
    4. Uruchom doctesty - wszystkie muszą się powieść


Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is timedelta, \
    'Variable `result` has invalid type, must be a timedelta'

    >>> result
    datetime.timedelta(days=3021, seconds=74955)
"""

from datetime import timedelta


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
MONTH = 30.4375 * DAY
YEAR = 365.25 * DAY


# - 8 years
# - 3 months
# - 8 days
# - 13 hours
# - 19 minutes
# - 15 seconds
# type: timedelta
result = ...


# Solution
period = int(8*YEAR + 3*MONTH + 8*DAY + 13*HOUR + 19*MINUTE + 15*SECOND)
result = timedelta(seconds=period)
