"""
* Assignment: Loop While Range
* Type: class assignment
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Generate `result: list[int]` with numbers from 0 to 5 (exclusive)
    2. Do not use `range()`
    3. Run doctests - all must succeed

Polish:
    1. Wygeneruj `result: list[int]` z liczbami od 0 do 5 (rozłącznie)
    2. Nie używaj `range()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list
    >>> assert all(type(x) is int for x in result)

    >>> result
    [0, 1, 2, 3, 4]
"""


# List with numbers from 0 to 5 (exclusive)
# type: list[int]
result = ...

# Solution
result = []
i = 0

while i < 5:
    result.append(i)
    i += 1
