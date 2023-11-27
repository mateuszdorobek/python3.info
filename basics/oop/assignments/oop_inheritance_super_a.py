"""
* Assignment: OOP Overload Super
* Type: class assignment
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Create class `Astronaut` which inherits from `Person`
    2. Class `Astronaut` takes two arguments `name` and `mission`
    3. Set attribute `mission` in `Astronaut` inicializer method
    4. Call initializer method of `Person` passing `name` as an argument
    5. Define method `show()` returning name and after coma - a mission name
    6. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `Astronaut` dziedziczącą po `Person`
    2. Klasa `Astronaut` przyjmuje dwa argumenty `name` i `mission`
    3. Ustaw atrybut `mission` w metodzie inicjalizacyjnej w `Astronaut`
    4. Wywołaj metodę inicjalizacyjną z `Person` podając `name` jako argument
    5. Zdefiniuj metodę `show()` zwracającą imię i po przecinku - nazwę misji
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> watney = Astronaut('Watney', 'Ares 3')
    >>> watney.show()
    'Watney, Ares 3'
    >>> lewis = Astronaut('Lewis', 'Ares 3')
    >>> lewis.show()
    'Lewis, Ares 3'
"""


class Person:
    def __init__(self, name):
        self.name = name


# Solution
class Astronaut(Person):
    def __init__(self, name, mission):
        super().__init__(name)
        self.mission = mission

    def show(self):
        return f'{self.name}, {self.mission}'
