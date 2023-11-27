"""
* Assignment: Type Int Time
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define variables for:
        a. workbreak: 10 minutes
        b. workday: 8 hours
        c. workweek: 5 days
        d. workmonth: 4 weeks
    2. All variables must be in seconds
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienne dla:
        a. workbreak: 10 minut
        b. workday: 8 godzin
        c. workweek: 5 dni
        d. workmonth: 4 tygodnie
    2. Wszystkie zmienne muszą być wyrażone w sekundach
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert workbreak is not Ellipsis, \
    'Assign your result to variable `workbreak`'
    >>> assert workday is not Ellipsis, \
    'Assign your result to variable `workday`'
    >>> assert workweek is not Ellipsis, \
    'Assign your result to variable `workweek`'
    >>> assert workmonth is not Ellipsis, \
    'Assign your result to variable `workmonth`'

    >>> assert type(workbreak) is int, \
    'Variable `workbreak` has invalid type, should be int'
    >>> assert type(workday) is int, \
    'Variable `workday` has invalid type, should be int'
    >>> assert type(workweek) is int, \
    'Variable `workweek` has invalid type, should be int'
    >>> assert type(workmonth) is int, \
    'Variable `workmonth` has invalid type, should be int'

    >>> assert workbreak == 600, \
    'Variable `workbreak` has invalid value. Check your calculation.'
    >>> assert workday == 28_800, \
    'Variable `workday` has invalid value. Check your calculation.'
    >>> assert workweek == 432_000, \
    'Variable `workweek` has invalid value. Check your calculation.'
    >>> assert workmonth == 2_419_200, \
    'Variable `workmonth` has invalid value. Check your calculation.'
"""


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY

# workbreak: 10 minutes
# type: int
workbreak = ...

# workday: 8 hours
# type: int
workday = ...

# workweek: 5 days
# type: int
workweek = ...

# workmonth: 4 weeks
# type: int
workmonth = ...

# Solution
workbreak = 10*MINUTE
workday = 8*HOUR
workweek = 5*DAY
workmonth = 4*WEEK
