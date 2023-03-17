"""
* Assignment: DesignPatterns Behavioral State
* Complexity: medium
* Lines of code: 34 lines
* Time: 13 min

English:
    1. Implement State pattern
    2. Then add another language:
        a. Chinese hello: 你好
        b. Chinese goodbye: 再见
    3. Run doctests - all must succeed

Polish:
    1. Zaimplementuj wzorzec State
    2. Następnie dodaj nowy język:
        a. Chinese hello: 你好
        b. Chinese goodbye: 再见
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> polish = Translation(Polish())
    >>> english = Translation(English())
    >>> chinese = Translation(Chinese())

    >>> polish.hello()
    'Cześć'
    >>> polish.goodbye()
    'Do widzenia'

    >>> english.hello()
    'Hello'
    >>> english.goodbye()
    'Goodbye'

    >>> chinese.hello()
    '你好'
    >>> chinese.goodbye()
    '再见'
"""
from enum import Enum


class Language(Enum):
    POLISH = 'pl'
    ENGLISH = 'en'
    SPANISH = 'es'


class Translation:
    language: Language

    def __init__(self, language: Language):
        self.language = language

    def hello(self) -> str:
        if self.language is Language.POLISH:
            return 'Cześć'
        elif self.language is Language.ENGLISH:
            return 'Hello'
        elif self.language is Language.SPANISH:
            return 'Buenos Días'
        else:
            return 'Unknown language'

    def goodbye(self) -> str:
        if self.language is Language.POLISH:
            return 'Do widzenia'
        elif self.language is Language.ENGLISH:
            return 'Goodbye'
        elif self.language is Language.SPANISH:
            return 'Adiós'
        else:
            return 'Unknown language'


# Solution
from abc import ABC, abstractmethod


class Language(ABC):
    @abstractmethod
    def hello(self) -> str: ...

    @abstractmethod
    def goodbye(self) -> str: ...


class Polish(Language):
    def goodbye(self) -> str:
        return 'Do widzenia'

    def hello(self) -> str:
        return 'Cześć'


class English(Language):
    def goodbye(self) -> str:
        return 'Goodbye'

    def hello(self) -> str:
        return 'Hello'


class Spanish(Language):
    def goodbye(self) -> str:
        return 'Buenos Días'

    def hello(self) -> str:
        return 'Adiós'


class Chinese(Language):
    def goodbye(self) -> str:
        return '再见'

    def hello(self) -> str:
        return '你好'


class Translation:
    language: Language

    def __init__(self, language: Language):
        self.language = language

    def goodbye(self):
        return self.language.goodbye()

    def hello(self):
        return self.language.hello()



# Alternative Solution
"""
from abc import ABC, abstractproperty
from dataclasses import dataclass

class Language(ABC):
    @abstractproperty
    def hello(self) -> str: ...

    @abstractproperty
    def goodbye(self) -> str: ...


@dataclass
class Polish(Language):
    hello: str = 'Cześć'
    goodbye: str = 'Do widzenia'

@dataclass
class English(Language):
    hello: str = 'Hello'
    goodbye: str = 'Goodbye'


class Translation(Language):
    language: Language

    def __init__(self, language: Language):
        self.language = language

    def hello(self):
        return self.language.hello

    def goodbye(self):
        return self.language.goodbye
"""
