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
    (25.91375, -60.15503),
    (-11.01983, -166.48477),
    (-11.01983, -166.48477),
]

# Solution
data: list[tuple[float,float]]
