"""
* Assignment: Decorator Method Alive
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Create `if_alive` method decorator
    2. Decorator will allow running `make_damage` method
       only if `current_health` is greater than 0
    3. Run doctests - all must succeed

Polish:
    1. Stwórz dekorator metody `if_alive`
    2. Dekorator pozwoli na wykonanie metody `make_damage`,
       tylko gdy `current_health` jest większe niż 0
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(if_alive), \
    'Create if_alive() function'

    >>> assert isfunction(if_alive(lambda: ...)), \
    'if_alive() should take method as an argument'

    >>> class Hero:
    ...    def __init__(self, name):
    ...        self.name = name
    ...        self.current_health = 100
    ...
    ...    @if_alive
    ...    def make_damage(self):
    ...        return 10

    >>> hero = Hero('Mark Watney')
    >>> hero.make_damage()
    10
    >>> hero.current_health = -10
    >>> hero.make_damage()
    Traceback (most recent call last):
    RuntimeError: Hero is dead and cannot make damage
"""


# type: Callable[[Callable], Callable]
def if_alive(method):
    def wrapper(hero, *args, **kwargs):
        return method(hero, *args, **kwargs)

    return wrapper


# Solution
def if_alive(method):
    def wrapper(self, *args, **kwargs):
        if self.current_health <= 0:
            raise RuntimeError('Hero is dead and cannot make damage')
        return method(self, *args, **kwargs)

    return wrapper
