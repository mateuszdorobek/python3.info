"""
* Assignment: Iterable List Create
* Required: yes
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Create lists:
        a. `result_a` without elements
        b. `result_a` with elements: 1, 2, 3
        c. `result_b` with elements: 1.1, 2.2, 3.3
        d. `result_c` with elements: 'a', 'b', 'c'
        e. `result_d` with elements: True, False
        f. `result_e` with elements: 1, 2.2, True, 'a'
    2. Run doctests - all must succeed

Polish:
    1. Stwórz listy:
        a. `result_a` bez elementów
        b. `result_a` z elementami: 1, 2, 3
        c. `result_b` z elementami: 1.1, 2.2, 3.3
        d. `result_c` z elementami: 'a', 'b', 'c'
        e. `result_d` z elementami: True, False, True
        f. `result_e` z elementami: 1, 2.2, True, 'a'
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result_a is not Ellipsis, \
    'Assign your result to variable `result_a`'
    >>> assert result_b is not Ellipsis, \
    'Assign your result to variable `result_b`'
    >>> assert result_c is not Ellipsis, \
    'Assign your result to variable `result_c`'
    >>> assert result_d is not Ellipsis, \
    'Assign your result to variable `result_d`'
    >>> assert result_e is not Ellipsis, \
    'Assign your result to variable `result_e`'
    >>> assert result_f is not Ellipsis, \
    'Assign your result to variable `result_f`'

    >>> assert type(result_a) is list, \
    'Variable `result_a` has invalid type, should be list'
    >>> assert type(result_b) is list, \
    'Variable `result_b` has invalid type, should be list'
    >>> assert type(result_c) is list, \
    'Variable `result_c` has invalid type, should be list'
    >>> assert type(result_d) is list, \
    'Variable `result_d` has invalid type, should be list'
    >>> assert type(result_e) is list, \
    'Variable `result_e` has invalid type, should be list'
    >>> assert type(result_f) is list, \
    'Variable `result_f` has invalid type, should be list'

    >>> assert result_a == [], \
    'Variable `result_a` has invalid value, should be []'
    >>> assert result_b == [1, 2, 3], \
    'Variable `result_b` has invalid value, should be [1, 2, 3]'
    >>> assert result_c == [1.1, 2.2, 3.3], \
    'Variable `result_c` has invalid value, should be [1.1, 2.2, 3.3]'
    >>> assert result_d == ['a', 'b', 'c'], \
    'Variable `result_d` has invalid value, should be ["a", "b", "c"]'
    >>> assert result_e == [True, False], \
    'Variable `result_e` has invalid value, should be [True, False]'
    >>> assert result_f == [1, 2.2, True, 'a'], \
    'Variable `result_f` has invalid value, should be [1, 2.2, True, "a"]'
"""

# List without elements
# type: list
result_a = ...

# List with elements: 1, 2, 3
# type: list[int]
result_b = ...

# List with elements: 1.1, 2.2, 3.3
# type: list[float]
result_c = ...

# List with elements: 'a', 'b', 'c'
# type: list[str]
result_d = ...

# List with elements: True, False
# type: list[bool]
result_e = ...

# List with elements: 1, 2.2, True, 'a'
# type: list[int|float|bool|str]
result_f = ...

# Solution
result_a = []
result_b = [1, 2, 3]
result_c = [1.1, 2.2, 3.3]
result_d = ['a', 'b', 'c']
result_e = [True, False]
result_f = [1, 2.2, True, 'a']
