"""
* Assignment: Decorator Class Abspath
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Absolute path is when `path` starts with `current_directory`
    2. Create class decorator `Abspath`
    3. If `path` is relative, then `Abspath` will convert it to absolute
    4. If `path` is absolute, then `Abspath` will not modify it
    5. Note: if you are using Windows operating system,
       then one doctest (with absolute path) can fail
    6. Run doctests - all must succeed

Polish:
    1. Ścieżka bezwzględna jest gdy `path` zaczyna się od `current_directory`
    2. Stwórz klasę dekorator `Abspath`
    3. Jeżeli `path` jest względne, to `Abspath` zamieni ją na bezwzględną
    4. Jeżeli `path` jest bezwzględna, to `Abspath` nie będzie jej modyfikował
    5. Uwaga: jeżeli korzystasz z systemu operacyjnego Windows,
       to jeden z doctestów (ścieżki bezwzględnej) może nie przejść pomyślnie
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `path = Path(path).absolute()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Abspath), \
    'Abspath should be a decorator class'

    >>> assert Abspath(lambda: ...), \
    'Abspath should take function as an argument'

    >>> assert isinstance(Abspath(lambda: ...), Abspath), \
    'Abspath() should return an object which is an instance of Abspath'

    >>> @Abspath
    ... def display(path):
    ...     return str(path)

    >>> current_dir = str(Path().cwd())
    >>> display('iris.csv').startswith(current_dir)
    True
    >>> display('iris.csv').endswith('iris.csv')
    True
    >>> display('/home/python/iris.csv')  # Should pass regardless your OS
    '/home/python/iris.csv'

TODO: Windows Path().absolute()
TODO: Test if function was called
"""

from pathlib import Path


def abspath(func):
    def wrapper(path):
        path = Path(path).absolute()
        return func(path)

    return wrapper


# type: type
class Abspath:
    ...

# Solution
class Abspath:
    def __init__(self, func):
        self._func = func

    def __call__(self, file):
        abspath = Path(file).absolute()
        return self._func(abspath)
