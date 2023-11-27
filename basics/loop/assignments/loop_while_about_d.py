"""
* Assignment: Loop While toStr
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Create `result: str`
    2. Use `while` to iterate over `DATA`
    3. Add current element of `DATA` to `result`
    4. Do not use `str.join()`
    5. Run doctests - all must succeed

Polish:
    1. Stwórz `result: str`
    2. Użyj `while` do iterowania po `DATA`
    3. Dodaj obecny element z `DATA` do `result`
    4. Nie używaj `str.join()`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `Stop` or `Ctrl+C` kills infinite loop

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'str'>
    >>> result
    'hello'
"""

DATA = ['h', 'e', 'l', 'l', 'o']

# Joined DATA values
# type: str
result = ...

# Solution
result = ''
i = 0

while i < len(DATA):
    result += DATA[i]
    i += 1
