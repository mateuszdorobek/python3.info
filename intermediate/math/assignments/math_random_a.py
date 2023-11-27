"""
* Assignment: Math Random Sample
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: list[int]` with 6 random
       integers without repetition in range from 1 to 49 (inclusive)
    2. Use `random.sample()`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[int]` z 6-oma losowymi
       i nie powtarzającymi się liczbami całkowitymi
       z zakresu od 1 do 49 (włącznie)
    2. Użyj `random.sample()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> sorted(result)
    [3, 17, 25, 27, 32, 33]
"""

from random import sample, seed
seed(0)

# type: list[int]
result = ...

# Solution
result = sample(range(1, 50), k=6)
