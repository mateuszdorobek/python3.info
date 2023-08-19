"""
* Assignment: Protocol Descriptor ValueRange
* Complexity: easy
* Lines of code: 9 lines
* Time: 13 min

English:
    1. Define descriptor class `ValueRange` with attributes:
        a. `name: str`
        b. `min: float`
        c. `max: float`
        d. `value: float`
    2. Define class `User` with attributes:
        a. `age = ValueRange('Age', min=28, max=42)`
        b. `height = ValueRange('Height', min=150, max=200)`
    3. Setting `User` attribute should invoke boundary check of `ValueRange`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę-deskryptor `ValueRange` z atrybutami:
        a. `name: str`
        b. `min: float`
        c. `max: float`
        d. `value: float`
    2. Zdefiniuj klasę `User` z atrybutami:
        a. `age = ValueRange('Age', min=28, max=42)`
        b. `height = ValueRange('Height', min=150, max=200)`
    3. Ustawianie atrybutu `User` powinno wywołać sprawdzanie zakresu z `ValueRange`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> mark = User('Mark Watney', 36, 170)

    >>> melissa = User('Melissa Lewis', 44, 170)
    Traceback (most recent call last):
    ValueError: Age is not between 28 and 42

    >>> alex = User('Alex Vogel', 40, 201)
    Traceback (most recent call last):
    ValueError: Height is not between 150 and 200
"""

class ValueRange:
    name: str
    min: float
    max: float

    def __init__(self, name, min, max):
        pass


class User:
    name: str
    age = ValueRange('Age', min=28, max=42)
    height = ValueRange('Height', min=150, max=200)

    def __init__(self, name, age, height):
        self.name = name
        self.height = height
        self.age = age

    def __repr__(self):
        name = self.name
        age = self.age.value
        height = self.height.value
        return f'User({name=}, {age=}, {height=})'


# Solution

class ValueRange:
    name: str
    min: float
    max: float

    def __init__(self, name, min, max):
        self.name = name
        self.max = max
        self.min = min

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not self.min <= value <= self.max:
            raise ValueError(f'{self.name} is not between {self.min} and {self.max}')
        setattr(instance, self.name, value)


class User:
    age = ValueRange('Age', min=28, max=42)
    height = ValueRange('Height', min=150, max=200)

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
