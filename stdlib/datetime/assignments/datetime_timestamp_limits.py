"""
* Assignment: Datetime Timestamp Limits
* Complexity: easy
* Lines of code: 1 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Convert given dates to `datetime` objects
    3. Print timestamp for each date
    4. What is special about those dates?

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Przekonwertuj podane daty do obiektów `datetime`
    3. Wypisz timestamp każdej daty
    4. Co to za daty?

    >>> assert type(a) is float, \
    '`a` must be a float object'

    >>> assert type(b) is float, \
    '`b` must be a float object'

    >>> assert type(c) is float, \
    '`c` must be a float object'

    >>> a
    -2115947647.0
    >>> b
    0.0
    >>> c
    2147483647.0
"""


# Given
from datetime import datetime


A = '1902-12-13T20:45:53+00:00'
B = '1970-01-01T00:00:00+00:00'
C = '2038-01-19T03:14:07+00:00'

a = ...  # timestamp of A
b = ...  # timestamp of B
c = ...  # timestamp of C


# Solution
a = datetime.fromisoformat(a).timestamp()
b = datetime.fromisoformat(b).timestamp()
c = datetime.fromisoformat(c).timestamp()
