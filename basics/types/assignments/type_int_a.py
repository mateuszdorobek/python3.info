"""
* Assignment: Type Int Time
* Type: class assignment
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Define variables for:
        a. second: 1 second
        b: minute: 60 seconds
        c. hour: 60 minutes
        d. day: 24 hours
        e. week: 7 days
    2. All variables must be in seconds
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienne dla:
        a. second: 1 sekunda
        b: minute: 60 sekund
        c. hour: 60 minut
        d. day: 24 godzin
        e. week: 7 dni
    2. Wszystkie zmienne muszą być wyrażone w sekundach
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert second is not Ellipsis, \
    'Assign your result to variable `second`'
    >>> assert minute is not Ellipsis, \
    'Assign your result to variable `minute`'
    >>> assert hour is not Ellipsis, \
    'Assign your result to variable `hour`'
    >>> assert day is not Ellipsis, \
    'Assign your result to variable `day`'
    >>> assert week is not Ellipsis, \
    'Assign your result to variable `week`'
    >>> assert type(second) is int, \
    'Variable `second` has invalid type, should be int'
    >>> assert type(minute) is int, \
    'Variable `minute` has invalid type, should be int'
    >>> assert type(hour) is int, \
    'Variable `hour` has invalid type, should be int'
    >>> assert type(day) is int, \
    'Variable `day` has invalid type, should be int'
    >>> assert type(week) is int, \
    'Variable `week` has invalid type, should be int'

    >>> assert second == 1, \
    'Variable `second` has invalid value. Check your calculation.'
    >>> assert minute == 60, \
    'Variable `minute` has invalid value. Check your calculation.'
    >>> assert hour == 3600, \
    'Variable `hour` has invalid value. Check your calculation.'
    >>> assert day == 86400, \
    'Variable `day` has invalid value. Check your calculation.'
    >>> assert week == 604800, \
    'Variable `week` has invalid value. Check your calculation.'
"""

# second: 1 second
# type: int
second = ...

# minute: 60 seconds
# type: int
minute = ...

# hour: 60 minutes
# type: int
hour = ...

# day: 24 hours
# type: int
day = ...

# week: 7 days
# type: int
week = ...

# Solution
second = 1
minute = 60 * second
hour = 60 * minute
day = 24 * hour
week = 7 * day
