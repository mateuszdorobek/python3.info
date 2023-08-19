"""
* Assignment: Idiom Reduce Chain
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define `result` with numbers from `range()`:
       a. from 0 (inclusive)
       b. to 10 (exclusive)
    2. Use `filter()` to get odd numbers from `result`
       (and assign to `result`)
    3. Use `map()` to cube all numbers in `result`
    4. Create `result: float` with arithmetic mean of `result`
    5. Do not use `lambda` expressions
    6. Note, that all the time you are working on one data stream
    7. Run doctests - all must succeed

Polish:
    1. Zdefiniu `result` z liczbami z `range()`:
       a. od 0 (włącznie)
       b. do 10 (rozłącznie)
    2. Użyj `filter()` aby otrzymać liczby nieparzyste z `result`
       (i przypisz je do `result`)
    3. Użyj `map()` aby podnieść wszystkie liczby w `result` do sześcianu
    4. Stwórz `result: float` ze średnią arytmetyczną z `result`
    5. Nie używaj wyrażeń lambda
    6. Zwróć uwagę, że cały czas pracujesz na jednym strumieniu danych
    7. Uruchom doctesty - wszystkie muszą się powieść

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

data = range(0, 10)
data = filter(odd, data)
data = map(cube, data)

# Calculate mean
# type: float
result = ...


# Solution
result = list(data)
result = sum(result) / len(result)
