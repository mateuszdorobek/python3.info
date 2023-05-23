"""
* Assignment: Typing Annotations List of Tuple
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Declare proper types for variable
    2. Run doctests - all must succeed

Polish:
    1. Zadeklaruj odpowiedni typ zmiennej
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

"""

# Declare proper types for variable
data: ...

# Do not modify lines below
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Solution
data: list[list[int]]
