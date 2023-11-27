"""
* Assignment: Comprehension About Create
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Use list comprehension
    2. Generate `result: list[int]` of numbers from 5 to 20 (without 20)
    3. Run doctests - all must succeed

Polish:
    1. Użyj rozwinięcia listowego
    2. Wygeneruj `result: list[int]` liczb z przedziału 5 do 20 (bez 20)
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `range()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list, \
    'Result should be a list'

    >>> assert all(type(x) is int for x in result), \
    'Result should be a list of int'

    >>> result
    [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
"""

# Numbers from 5 to 20 (without 20)
# type: list[int]
result = ...

# Solution
result = [x for x in range(5, 20)]
