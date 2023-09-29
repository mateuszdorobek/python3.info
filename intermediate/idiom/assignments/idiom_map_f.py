"""
* Assignment: Idiom Map Login
* Complexity: medium
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: map` with logged users from `DATA`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: map` z zalogowanymi użytkownikami z `DATA`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * map()
    * class.method(instance)

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'

    >>> assert type(result) is map, \
    'Variable `result` has invalid type, should be map'

    >>> result = list(result)
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, must be a list'

    >>> assert all(type(element) is str for element in result), \
    'All elements in `result` must be a str'

    >>> pprint(result, width=30)
    ['User logged-in: mwatney',
     'User logged-in: mlewis']
"""

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        return f'User logged-in: {self.username}'


USERS = [
    User('mwatney', 'Ares3'),
    User('mlewis', 'Nasa69'),
]

result = ...

# Solution
result = map(User.login, USERS)
