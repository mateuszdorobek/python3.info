"""
* Assignment: Mapping Define Dict
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Create `result: dict` representing input data
    2. Non-functional requirements:
        a. Assignmnet verifies creation of `dict()`
        b. Do not parse data, simply model it using dict
        c. Do not use `str.split()`, `slice`, `getitem`, `for`, `while` or
           any other control-flow statement
    3. Run doctests - all must succeed

Polish:
    1. Stwórz `result: dict` reprezentujący dane wejściowe
    2. Wymagania niefunkcjonalne:
        a. Zadanie sprawdza tworzenie `dict()`
        b. Nie parsuj danych, po prostu zamodeluj je jako dict
        c. Nie używaj `str.split()`, `slice`, `getitem`, `for`, `while` lub
           jakiejkolwiek innej instrukcji sterującej
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'
    >>> assert 'firstname' in result.keys(), \
    'Value `firstname` is not in the result keys'
    >>> assert 'lastname' in result.keys(), \
    'Value `lastname` is not in the result keys'
    >>> assert 'missions' in result.keys(), \
    'Value `missions` is not in the result keys'
    >>> assert 'Mark' in result['firstname'], \
    'Value `Mark` is not in the result values'
    >>> assert 'Watney' in result['lastname'], \
    'Value `Watney` is not in the result values'
    >>> assert 'Ares1' in result['missions'], \
    'Value `Ares1` is not in the result values'
    >>> assert 'Ares3' in result['missions'], \
    'Value `Ares3` is not in the result values'
"""


# firstname - Mark
# lastname - Watney
# missions - Ares1, Ares3

# Define dict with keys: firstname, lastname and missions
# type: dict[str,str|list]
result = ...

# Solution
result = {
    'firstname': 'Mark',
    'lastname': 'Watney',
    'missions': ['Ares1', 'Ares3'],
}
