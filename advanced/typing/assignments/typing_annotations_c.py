"""
* Assignment: Typing Annotations Optional
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Declare proper types for variables
    2. Use optional with | notation (pipe)
    3. Run doctests - all must succeed

Polish:
    1. Zadeklaruj odpowiedni typ zmiennych
    2. Użyj optional z notacją | (pionowej kreski)
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert data is None, \
    'Do not modify variable `data` value, just add type annotation'
"""

# Declare proper types for variables
# Use alias with | notation (pipe)
T = ...

# Do not modify lines below
data: T = 1
data: T = None

# Solution
T = int | None
