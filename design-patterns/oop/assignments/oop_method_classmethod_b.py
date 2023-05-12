"""
* Assignment: OOP MethodClassmethod CSV
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. To class `CSVMixin` add methods:
        a. `to_csv(self) -> str`
        b. `from_csv(self, text: str) -> 'User' | 'Admin'`
    2. `CSVMixin.to_csv()` should return attribute values separated with coma
    3. `CSVMixin.from_csv()` should return instance of a class on which it was called
    4. Use `@classmethod` decorator in proper place
    5. Run doctests - all must succeed

Polish:
    1. Do klasy `CSVMixin` dodaj metody:
        a. `to_csv(self) -> str`
        b. `from_csv(self, text: str) -> 'User' | 'Admin'`
    2. `CSVMixin.to_csv()` powinna zwracać wartości atrybutów klasy rozdzielone po przecinku
    3. `CSVMixin.from_csv()` powinna zwracać instancje klasy na której została wywołana
    4. Użyj dekoratora `@classmethod` w odpowiednim miejscu
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `CSVMixin.to_csv()` should add newline `\n` at the end of line
    * `CSVMixin.from_csv()` should remove newline `\n` at the end of line

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> from dataclasses import dataclass

    >>> @dataclass
    ... class User(CSVMixin):
    ...     firstname: str
    ...     lastname: str
    ...
    >>> @dataclass
    ... class Admin(CSVMixin):
    ...     firstname: str
    ...     lastname: str

    >>> mark = User('Mark', 'Watney')
    >>> melissa = Admin('Melissa', 'Lewis')

    >>> mark.to_csv()
    'Mark,Watney\\n'
    >>> melissa.to_csv()
    'Melissa,Lewis\\n'

    >>> with open('_temporary.txt', mode='wt') as file:
    ...     data = mark.to_csv() + melissa.to_csv()
    ...     file.writelines(data)

    >>> result = []
    >>> with open('_temporary.txt', mode='rt') as file:
    ...     lines = file.readlines()
    ...     result += [User.from_csv(lines[0])]
    ...     result += [Admin.from_csv(lines[1])]

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [User(firstname='Mark', lastname='Watney'),
     Admin(firstname='Melissa', lastname='Lewis')]

    >>> remove('_temporary.txt')

TODO: dodać test sprawdzający czy linia kończy się newline
"""

class CSVMixin:
    def to_csv(self) -> str:
        ...

    def from_csv(cls, line: str):
        ...


# Solution
class CSVMixin:
    def to_csv(self) -> str:
        data = vars(self).values()
        return ','.join(data) + '\n'

    @classmethod
    def from_csv(cls, line: str):
        data = line.strip().split(',')
        return cls(*data)
