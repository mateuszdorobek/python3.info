"""
* Assignment: Decorator Function Staff
* Complexity: easy
* Lines of code: 3 lines
* Time: 8 min

English:
    1. Modify decorator `can_login`
    2. To answer if person is staff check field:
       `is_staff` in `users: list[dict]`
    3. Decorator will call decorated function, only if all users are staff
    4. If user is not a staff:
       raise `PermissionError` with message `USERNAME is not a staff`,
       where USERNAME is user's username
    5. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj dekorator `can_login`
    2. Aby odpowiedzieć czy osoba jest staffem sprawdź pole:
       `is_staff` in `users: list[dict]`
    3. Dekorator wywoła dekorowaną funkcję, tylko gdy każdy członek jest staff
    4. Jeżeli użytkownik nie jest staffem:
       podnieś `PermissionError` z komunikatem `USERNAME is not a staff`,
       gdzie USERNAME to username użytkownika
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(can_login), \
    'Create can_login() function'

    >>> assert isfunction(can_login(lambda: ...)), \
    'can_login() should take function as an argument'

    >>> @can_login
    ... def login(users):
    ...     users = ', '.join(user['username'] for user in users)
    ...     return f'Logging-in: {users}'

    >>> login(group1)
    'Logging-in: mwatney, mlewis, rmartinez'

    >>> login(group2)
    Traceback (most recent call last):
    PermissionError: avogel is not a staff
"""

group1 = [
    {'is_staff': True, 'username': 'mwatney'},
    {'is_staff': True, 'username': 'mlewis'},
    {'is_staff': True, 'username': 'rmartinez'},
]

group2 = [
    {'is_staff': False, 'username': 'avogel'},
    {'is_staff': True,  'username': 'bjohanssen'},
    {'is_staff': True,  'username': 'cbeck'},
]


# type: Callable[[Callable], Callable]
def can_login(func):
    def wrapper(users):
        return func(users)
    return wrapper


# Solution
def can_login(func):
    def wrapper(users):
        for member in users:
            if not member['is_staff']:
                username = member["username"]
                raise PermissionError(f'{username} is not a staff')
        return func(users)
    return wrapper
