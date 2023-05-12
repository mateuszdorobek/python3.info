"""
* Assignment: Decorator Arguments Staff
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Create decorator `can_login`
    2. To answer if person is staff check field:
       `is_staff` in `users: list[dict]`
    3. Decorator will call decorated function, only if all users
       has field with specified value
    4. Field name and value are given as keyword arguments to decorator
    5. If user is not a staff:
       raise `PermissionError` with message `USERNAME is not a staff`,
       where USERNAME is user's username
    6. Run doctests - all must succeed

Polish:
    1. Stwórz dekorator `can_login`
    2. Aby odpowiedzieć czy osoba jest staffem sprawdź pole:
       `is_staff` in `users: list[dict]`
    3. Dekorator wywoła dekorowaną funkcję, tylko gdy każdy członek
       grupy ma pole o podanej wartości
    4. Nazwa pola i wartość są podawane jako argumenty nazwane do dekoratora
    5. Jeżeli użytkownik nie jest staffem:
       podnieś `PermissionError` z komunikatem `USERNAME is not a staff`,
       gdzie USERNAME to username użytkownika
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(can_login), \
    'Create can_login() function'

    >>> assert isfunction(can_login('field', 'value')), \
    'can_login() should take two positional arguments'

    >>> assert isfunction(can_login(field='field', value='value')), \
    'can_login() should take two keyword arguments: field and value'

    >>> assert isfunction(can_login('field', 'value')(lambda: ...)), \
    'can_login() should return decorator which can take a function'

    >>> group1 = [
    ...     {'is_staff': True, 'username': 'mwatney'},
    ...     {'is_staff': True, 'username': 'mlewis'},
    ...     {'is_staff': True, 'username': 'rmartinez'},
    ... ]
    ...
    >>> group2 = [
    ...     {'is_staff': False, 'username': 'avogel'},
    ...     {'is_staff': True,  'username': 'bjohanssen'},
    ...     {'is_staff': True,  'username': 'cbeck'},
    ... ]

    >>> @can_login(field='is_staff', value=True)
    ... def login(users):
    ...    users = ', '.join(user['username'] for user in users)
    ...    return f'Logging-in: {users}'

    >>> login(group1)
    'Logging-in: mwatney, mlewis, rmartinez'

    >>> login(group2)
    Traceback (most recent call last):
    PermissionError: avogel is not a staff

    >>> @can_login(field='is_staff', value='yes')
    ... def login(users):
    ...    users = ', '.join(user['username'] for user in users)
    ...    return f'Logging-in: {users}'

    >>> login(group1)
    Traceback (most recent call last):
    PermissionError: mwatney is not a staff

    >>> login(group2)
    Traceback (most recent call last):
    PermissionError: avogel is not a staff
"""

# type: Callable[[str,str], Callable]
def can_login(field, value):
    def decorator(func):
        def wrapper(users):
            return func(users)
        return wrapper
    return decorator


# Solution
def can_login(field, value):
    def decorator(func):
        def wrapper(users):
            for member in users:
                if member.get(field) != value:
                    name = member["username"]
                    raise PermissionError(f'{name} is not a staff')
            return func(users)
        return wrapper
    return decorator
