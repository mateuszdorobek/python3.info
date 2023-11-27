"""
* Assignment: Loop For Range
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Generate `result: list[int]` with numbers from 0 (inclusive) to 5 (exclusive)
    2. You can use `range()` in a loop, but not conversion: `list(range())`
    3. Run doctests - all must succeed

Polish:
    1. Wygeneruj `result: list[int]` z liczbami od 0 (włącznie) do 5 (rozłącznie)
    2. Możesz użyć `range()` w pętli, ale nie konwersji: `list(range())`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is int for x in result), \
    'All elements in `result` should be int'

    >>> result
    [0, 1, 2, 3, 4]
"""


# List with numbers from 0 to 5 (exclusive)
# type: list[int]
result = ...

# Solution
result = []

for i in range(0,5):
    result.append(i)
