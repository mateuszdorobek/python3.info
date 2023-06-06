"""
* Assignment: Idiom Zip Dict
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: zip` with enumerated `DATA`
    2. Recreate `enumerate()` behavior
    3. Use only: `len()`, `range()`, `zip()`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: zip` z enumerowanym `DATA`
    2. Odtwórz zachowanie `enumerate()`
    3. Use only: `len()`, `range()`, `zip()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `len()`
    * `range()`
    * `zip()`

Tests:
    >>> next(result)
    (0, 'January')
    >>> next(result)
    (1, 'February')
    >>> next(result)
    (2, 'March')
    >>> next(result)
    (3, 'April')
    >>> next(result)
    Traceback (most recent call last):
    StopIteration
"""
DATA = ['January', 'February', 'March', 'April']

# Solution
result = zip(range(len(DATA)), DATA)
