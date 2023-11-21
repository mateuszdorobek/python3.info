"""
* Assignment: Generator Function Iris
* Complexity: easy
* Lines of code: 8 lines
* Time: 5 min

English:
    1. Write filter for `DATA` which returns `features: list[float]` for given `species: str`
    2. Implement solution using function
    3. Implement solution using generator and `yield` keyword
    4. Compare results of both using `sys.getsizeof()`
    5. What will happen if input data will be bigger?
    6. Note, that in different Python versions you'll get slightly
       different values for getsizeof generator and function:
        a. 216 for generator in Python 3.12
        b. 224 for generator in Python 3.11
        c. 104 for generator in Python 3.10
        d. 112 for generator in Python 3.9
        e. 112 for generator in Python 3.8
        f. 120 for generator in Python 3.7
    7. Run doctests - all must succeed

Polish:
    1. Napisz filtr dla `DATA` zwracający `features: list[float]` dla danego gatunku `species: str`
    2. Zaimplementuj rozwiązanie wykorzystując funkcję
    3. Zaimplementuj rozwiązanie wykorzystując generator i słowo kluczowe `yield`
    4. Porównaj wyniki obu używając `sys.getsizeof()`
    5. Co się stanie, gdy ilość danych będzie większa?
    6. Zwróć uwagę, że w zależności od wersji Python wartości getsizeof
       dla funkcji i generatora mogą się nieznaczenie różnić:
        a. 216 dla generator w Python 3.12
        b. 224 dla generator w Python 3.11
        c. 104 dla generator w Python 3.10
        d. 112 dla generator w Python 3.9
        e. 112 dla generator w Python 3.8
        f. 120 dla generator w Python 3.7
    7. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from sys import getsizeof
    >>> from inspect import isfunction, isgeneratorfunction

    >>> assert isfunction(function)
    >>> assert isgeneratorfunction(generator)

    >>> list(function(DATA, 'setosa'))
    [[5.1, 3.5, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]]
    >>> list(generator(DATA, 'setosa'))
    [[5.1, 3.5, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]]

    >>> getsizeof(function(DATA, 'setosa'))
    88
    >>> getsizeof(function(DATA*10, 'setosa'))
    248
    >>> getsizeof(function(DATA*100, 'setosa'))
    1656
    >>> getsizeof(generator(DATA, 'setosa'))
    216
    >>> getsizeof(generator(DATA*10, 'setosa'))
    216
    >>> getsizeof(generator(DATA*100, 'setosa'))
    216
"""

DATA = [
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]


# Function get `features: list[float]` from `DATA` for given `species`
# type: Callable[[list[float|str], str], list[float]]
def function(data: list, species: str):
    ...


# Generator get `features: list[float]` from `DATA` for given `species`
# type: Generator
def generator(data: list, species: str):
    ...


# Solution
def function(data: list, species: str):
    result = []
    for *features, label in data:
        if label == species:
            result.append(features)
    return result


def generator(data: list, species: str):
    for *features, label in data:
        if label == species:
            yield features
