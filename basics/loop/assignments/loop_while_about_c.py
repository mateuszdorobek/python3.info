"""
* Assignment: Loop While toFloat
* Type: class assignment
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Create `result: list[float]`
    2. Use `while` to iterate over `DATA`
    3. Convert current elements of `DATA` to `float`
    4. Converted value append to `result`
    5. Run doctests - all must succeed

Polish:
    1. Stwórz `result: list[float]`
    2. Użyj `while` do iterowania po `DATA`
    3. Przekonwertuj obecny element `DATA` do `float`
    4. Przekonwertowaną wartość dodaj na koniec `result`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `Stop` or `Ctrl+C` kills infinite loop

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'list'>

    >>> assert all(type(x) is float for x in result)

    >>> result
    [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]
"""

DATA = (2, 3, 3.5, 4, 4.5, 5)

# Values from DATA converted to float
# type: list[float]
result = ...

# Solution
result = []
i = 0

while i < len(DATA):
    value = float(DATA[i])
    result.append(value)
    i += 1
