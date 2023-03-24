"""
* Assignment: Iterable Nested Create
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Create nested list `result` with elements:
        a. tuple: 1, 2, 3
        b. list: 1.1, 2.2, 3.3
        c. set: 'red', 'green', 'blue'
    2. Run doctests - all must succeed

Polish:
    1. Stwórz zagnieżdżoną listę `result` z elementami:
        a. tuple: 1, 2, 3
        b. list: 1.1, 2.2, 3.3
        c. set: 'red', 'green', 'blue'
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert len(result) == 3, \
    'Variable `result` length should be 3'

    >>> assert (1, 2, 3) in result
    >>> assert [1.1, 2.2, 3.3] in result
    >>> assert {'red', 'green', 'blue'} in result
"""

# Result should contain:
# - tuple: 1, 2, 3
# - list: 1.1, 2.2, 3.3
# - set: 'red', 'green', 'blue'
# type: list[tuple|list|set]
result = ...

# Solution
result = [
    (1, 2, 3),
    [1.1, 2.2, 3.3],
    {'red', 'green', 'blue'},
]
