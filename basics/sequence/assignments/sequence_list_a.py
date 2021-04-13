"""
* Assignment: Sequence List Create
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Create list `result` with elements:
        a. `'a'`
        b. `1`
        c. `2.2`
    2. Compare result with "Tests" section (see below)

Polish:
    1. Stwórz listę `result` z elementami:
        a. `'a'`
        b. `1`
        c. `2.2`
    2. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, 'Assignment solution must be in `result` instead of ... (Ellipsis)'
    >>> assert type(result) is list, 'Variable `result` has invalid type, should be list'
    >>> assert len(result) == 3, 'Variable `result` length should be 3'

    >>> 'a' in result
    True
    >>> 1 in result
    True
    >>> 2.2 in result
    True
"""

# Given
result = ...  # list with 'a' and 1 and 2.2

# Solution
result = ['a', 1, 2.2]
