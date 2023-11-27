"""
* Assignment: Sequence Frozenset Create
* Type: homework
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Create frozensets:
        a. `result_a` with elements: 1, 2, 3
        b. `result_b` with elements: 1.1, 2.2, 3.3
        c. `result_c` with elements: 'a', 'b', 'c'
        d. `result_d` with elements: True, False
        e. `result_e` with elements: 1, 2.2, True, 'a'
    2. Run doctests - all must succeed

Polish:
    1. Stwórz frozensety:
        a. `result_a` z elementami: 1, 2, 3
        b. `result_b` z elementami: 1.1, 2.2, 3.3
        c. `result_c` z elementami: 'a', 'b', 'c'
        d. `result_d` z elementami: True, False, True
        e. `result_e` z elementami: 1, 2.2, True, 'a'
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result_a is not Ellipsis, \
    'Assign result to variable: `result_a`'
    >>> assert result_b is not Ellipsis, \
    'Assign result to variable: `result_b`'
    >>> assert result_c is not Ellipsis, \
    'Assign result to variable: `result_c`'
    >>> assert result_d is not Ellipsis, \
    'Assign result to variable: `result_d`'
    >>> assert result_e is not Ellipsis, \
    'Assign result to variable: `result_e`'

    >>> assert type(result_a) is frozenset, \
    'Variable `result_a` has invalid type, should be frozenset'
    >>> assert type(result_b) is frozenset, \
    'Variable `result_b` has invalid type, should be frozenset'
    >>> assert type(result_c) is frozenset, \
    'Variable `result_c` has invalid type, should be frozenset'
    >>> assert type(result_d) is frozenset, \
    'Variable `result_d` has invalid type, should be frozenset'
    >>> assert type(result_e) is frozenset, \
    'Variable `result_e` has invalid type, should be frozenset'

    >>> assert result_a == frozenset({1, 2, 3}), \
    'Variable `result_a` has invalid value, should be frozenset({1, 2, 3})'
    >>> assert result_b == frozenset({1.1, 2.2, 3.3}), \
    'Variable `result_b` has invalid value, should be frozenset({1.1, 2.2, 3.3})'
    >>> assert result_c == frozenset({'a', 'b', 'c'}), \
    'Variable `result_c` has invalid value, should be frozenset({"a", "b", "c"})'
    >>> assert result_d == frozenset({True, False}), \
    'Variable `result_d` has invalid value, should be frozenset({True, False})'
    >>> assert result_e == frozenset({1, 2.2, True, 'a'}), \
    'Variable `result_e` has invalid value, should be frozenset({1, 2.2, True, "a"})'
"""

# with elements: 1, 2, 3
# type: frozenset[int]
result_a = ...

# with elements: 1.1, 2.2, 3.3
# type: frozenset[float]
result_b = ...

# with elements: 'a', 'b', 'c'
# type: frozenset[str]
result_c = ...

# with elements: True, False
# type: frozenset[bool]
result_d = ...

# with elements: 1, 2.2, True, 'a'
# type: frozenset[int|float|bool|str]
result_e = ...

# Solution
result_a = frozenset({1, 2, 3})
result_b = frozenset({1.1, 2.2, 3.3})
result_c = frozenset({'a', 'b', 'c'})
result_d = frozenset({True, False})
result_e = frozenset({1, 2.2, True, 'a'})
