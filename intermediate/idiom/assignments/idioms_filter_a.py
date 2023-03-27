"""
* Assignment: Idioms Filter Chain
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Use generator expression to create `result`
    2. Use `range()` to get numbers:
       a. from 0 (inclusive)
       b. to 10 (exclusive)
    3. Use `filter()` to get odd numbers from `result`
       (and assign to `result`)
    4. Use `map()` to cube all numbers in `result`
    5. Create `result: float` with arithmetic mean of `result`
    6. Do not use `lambda` expressions
    7. Note, that all the time you are working on one data stream
    8. Run doctests - all must succeed

Polish:
    1. Użyj wyrażenia generatorowego do stworzenia `result`
    2. Użyj `range()` aby otrzymać liczby:
       a. od 0 (włącznie)
       b. do 10 (rozłącznie)
    3. Użyj `filter()` aby otrzymać liczby nieparzyste z `result`
       (i przypisz je do `result`)
    4. Użyj `map()` aby podnieść wszystkie liczby w `result` do sześcianu
    5. Stwórz `result: float` ze średnią arytmetyczną z `result`
    6. Nie używaj wyrażeń lambda
    7. Zwróć uwagę, że cały czas pracujesz na jednym strumieniu danych
    8. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * type cast to `list()` to expand generator before calculating mean
    * `mean = sum(...) / len(...)`
    * TypeError: object of type 'map' has no len()
    * ZeroDivisionError: division by zero

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> isfunction(odd)
    True
    >>> isfunction(cube)
    True
    >>> type(result) is float
    True
    >>> result
    245.0
"""

def odd(x):
    return x % 2


def cube(x):
    return x ** 3


# Range numbers from 1 to 10 (exclusive)
# Filter odd numbers
# Cube result
# Calculate mean
# type: float
result = ...


# Solution
result = range(0, 10)
result = filter(odd, result)
result = map(cube, result)
result = list(result)
result = sum(result) / len(result)
