"""
* Assignment: OOP MethodClassmethod FromDict
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define class `Animal` with:
        a. Field `english_name: str`
        b. Field `latin_name: str`
        c. Method `from_dict()`
    2. Method `from_dict()`:
        a. Parameter `data: dict[str,str]`, example: {'english_name': 'Cat', 'latin_name': 'Felis catus'}
        b. Returns instance of a class on which was called
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Animal` z:
        a. Polem `english_name: str`
        b. Polem `latin_name: str`
        c. Metodą `from_dict()`
    2. Metoda `from_dict()`:
        a. Parametr `data: dict[str,str]`, przykład: {'english_name': 'Cat', 'latin_name': 'Felis catus'}
        b. Zwraca instancję klasy na której została wykonana
    3. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * dict.get()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass
    >>> from types import NoneType

    >>> assert isclass(Animal)
    >>> assert isclass(Cat)
    >>> assert isclass(Dog)

    >>> CAT = {'english_name': 'Cat', 'latin_name': 'Felis catus'}
    >>> cat = Cat.from_dict(CAT)
    >>> assert type(cat.english_name) is str
    >>> assert type(cat.latin_name) is str
    >>> assert cat.english_name == 'Cat'
    >>> assert cat.latin_name == 'Felis catus'

    >>> DOG = {'english_name': 'Dog', 'latin_name': 'Canis familiaris'}
    >>> dog = Dog.from_dict(DOG)
    >>> assert type(dog.english_name) is str
    >>> assert type(dog.latin_name) is str
    >>> assert dog.english_name == 'Dog'
    >>> assert dog.latin_name == 'Canis familiaris'

    >>> PLATYPUS = {'english_name': 'Platypus'}
    >>> platypus = Platypus.from_dict(PLATYPUS)
    >>> assert type(platypus.english_name) is str
    >>> assert type(platypus.latin_name) is NoneType
    >>> assert platypus.english_name == 'Platypus'
    >>> assert platypus.latin_name is None
"""


class Animal:
    def __init__(self, english_name, latin_name):
        self.english_name = english_name
        self.latin_name = latin_name

    # parameter: `data: dict[str,str]`
    # example: {'english_name': 'Cat', 'latin_name': 'Felis catus'}
    # hint: Platypus has `latin_name` field empty (None)
    # return: instance of a class on which was called
    # type: Callable[[type[Self], dict[str,str]], Self]
    def from_dict():
        ...


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class Platypus(Animal):
    pass


# Solution
class Animal:
    def __init__(self, english_name, latin_name):
        self.english_name = english_name
        self.latin_name = latin_name

    @classmethod
    def from_dict(cls, data: dict):
        english_name = data.get('english_name')
        latin_name = data.get('latin_name')
        return cls(english_name, latin_name)


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class Platypus(Animal):
    pass
