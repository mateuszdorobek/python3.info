"""
* Assignment: Type Int Time
* Type: class assignment
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Define variables for:
        a. result_a: 69 seconds
        b. result_b: 13 minutes 37 seconds
        c. result_c: 2 hours 56 minutes
        d. result_d: 1 day 2 hours 8 minutes
        e. result_e: 3 weeks 1 day 3 hours 3 minutes 7 seconds
    2. All variables must be in seconds
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienne dla:
        a. result_a: 69 sekunda
        b. result_b: 13 minut 37 sekund
        c. result_c: 2 godziny 56 minut
        d. result_d: 1 dzień 2 godziny 8 minut
        e. result_e: 3 tygodnie 1 dzień 3 godziny 3 minuty 7 sekund
    2. Wszystkie zmienne muszą być wyrażone w sekundach
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result_a is not Ellipsis, \
    'Assign your result to variable `result_a`'
    >>> assert result_b is not Ellipsis, \
    'Assign your result to variable `result_b`'
    >>> assert result_c is not Ellipsis, \
    'Assign your result to variable `result_c`'
    >>> assert result_d is not Ellipsis, \
    'Assign your result to variable `result_d`'
    >>> assert result_e is not Ellipsis, \
    'Assign your result to variable `result_e`'
    >>> assert type(result_a) is int, \
    'Variable `result_a` has invalid type, should be int'
    >>> assert type(result_b) is int, \
    'Variable `result_b` has invalid type, should be int'
    >>> assert type(result_c) is int, \
    'Variable `result_c` has invalid type, should be int'
    >>> assert type(result_d) is int, \
    'Variable `result_d` has invalid type, should be int'
    >>> assert type(result_e) is int, \
    'Variable `result_e` has invalid type, should be int'

    >>> assert result_a == 69, \
    'Variable `result_a` has invalid value. Check your calculation.'
    >>> assert result_b == 817, \
    'Variable `result_b` has invalid value. Check your calculation.'
    >>> assert result_c == 10560, \
    'Variable `result_c` has invalid value. Check your calculation.'
    >>> assert result_d == 94080, \
    'Variable `result_d` has invalid value. Check your calculation.'
    >>> assert result_e == 1911787, \
    'Variable `result_e` has invalid value. Check your calculation.'
"""


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY

# 69 seconds
# type: int
result_a = ...

# 13 minutes 37 seconds
# type: int
result_b = ...

# 2 hours 56 minutes
# type: int
result_c = ...

# 1 day 2 hours 8 minutes
# type: int
result_d = ...

# 3 weeks 1 day 3 hours 3 minutes 7 seconds
# type: int
result_e = ...

# Solution
result_a = 69 * SECOND
result_b = 13*MINUTE + 37*SECOND
result_c = 2*HOUR + 56*MINUTE
result_d = 1*DAY + 2*HOUR + 8*MINUTE
result_e = 3*WEEK + 1*DAY + 3*HOUR + 3*MINUTE + 7*SECOND
