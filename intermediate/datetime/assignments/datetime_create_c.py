"""
* Assignment: Datetime Create Current
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Create `datetime` object with current date and time
    2. Create `date` object with current date
    3. Create `time` object with current time
    4. Date and time must be from system, not hardcoded in code
    5. Run doctests - all must succeed

Polish:
    1. Stwórz obiekt `datetime` z obecną datą i czasem
    2. Stwórz obiekt `date` z obecną datą
    3. Stwórz obiekt `time` z obecnym czasem
    4. Data i czas ma być pobierana z systemu, nie zapisana w kodzie
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert d is not Ellipsis, \
    'Assign result to variable: `d`'
    >>> assert t is not Ellipsis, \
    'Assign result to variable: `t`'
    >>> assert dt is not Ellipsis, \
    'Assign result to variable: `dt`'
    >>> assert type(dt) is datetime, \
    'Variable `dt` has invalid type, must be a datetime'
    >>> assert type(d) is date, \
    'Variable `dt` has invalid type, must be a date'
    >>> assert type(t) is time, \
    'Variable `t` has invalid type, must be a time'
    >>> assert dt != datetime(1, 1, 1)
    >>> assert d != date(1, 1, 1)
    >>> assert t != time()
"""

from datetime import date, datetime, time


# representing current moment
# type: datetime
dt = ...

# representing current moment
# type: date
d = ...

# representing current moment
# type: time
t = ...

# Solution
dt = datetime.now()
d = dt.date()
t = dt.time()
