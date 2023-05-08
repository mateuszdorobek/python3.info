"""
* Assignment: FuncProg Recurrence Fibonacci
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Fibonacci series is created by adding two previous numbers, i.e.:
       1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
    2. Define function `fib(n)` using recursion to generate
       items of the Fibonacci series
    3. For `n` less or equal to 1, return 1
    4. Else return sum `fib(n-1)` and `fib(n-2)`
    5. Run doctests - all must succeed

Polish:
    1. Ciąg Fibonacciego powstaje przez dodawanie dwóch poprzednich liczb, np:
       1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
    2. Zdefiniuj funkcję `fib(n)` używającą rekurencji do generowania
       wyrazów ciągu Fibonacciego
    3. Dla `n` mniejszej lub równej 1, zwróć 1
    4. W przeciwnym wypadku zwróć sumę `fib(n-1)` i `fib(n-2)`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> fib(1)
    1
    >>> fib(2)
    2
    >>> fib(5)
    8
    >>> fib(9)
    55
    >>> fib(10)
    89
    >>> [fib(x) for x in range(10)]
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
"""


# Use recursion to add two previous numbers;
# For `n` less or equal to 1, return 1;
# Else return sum `fib(n-1)` and `fib(n-2)`
# type: Callable[[int], int]
def fib():
    ...

# Solution
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)
