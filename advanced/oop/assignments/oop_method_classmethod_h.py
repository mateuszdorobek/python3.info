"""
* Assignment: OOP MethodClassmethod FromToml
* Complexity: easy
* Lines of code: 6 lines
* Time: 8 min

English:
    1. Define class `Character` with:
        a. Field `character_class: str`
        b. Field `race: str`
        c. Field `alignment: str`
        d. Field `strength: int`
        e. Field `dexterity: int`
        f. Field `constitution: int`
        g. Field `intelligence: int`
        h. Field `wisdom: int`
        i. Field `charisma: int`
        j. Method `from_toml()`
    2. Method `from_toml()`:
        a. Parameter `filename: str`, example: 'myfile.toml'
        b. Parameter `name: str`, example: 'Sarevok'
        c. Returns instance of a class on which was called
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Character` z:
        a. Polem `character_class: str`
        b. Polem `race: str`
        c. Polem `alignment: str`
        d. Polem `strength: int`
        e. Polem `dexterity: int`
        f. Polem `constitution: int`
        g. Polem `intelligence: int`
        h. Polem `wisdom: int`
        i. Polem `charisma: int`
        j. Metodą `from_toml()`
    2. Metoda `from_toml()`:
        a. Parametr `filename: str`, przykład: 'myfile.toml'
        b. Parametr `name: str`, przykład: 'Sarevok'
        b. Zwraca instancję klasy na której została wykonana
    3. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * tomllib.load()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> from inspect import isclass

    >>> assert isclass(Character)
    >>> assert isclass(Fighter)
    >>> assert isclass(WildMage)
    >>> assert isclass(Ranger)
    >>> assert isclass(Thief)

    >>> imoen = Thief.from_toml(FILE, 'Imoen')
    >>> assert type(imoen.character_class) is str
    >>> assert type(imoen.race) is str
    >>> assert type(imoen.alignment) is str
    >>> assert type(imoen.stats) is Stats
    >>> assert imoen.character_class == 'Thief'
    >>> assert imoen.race == 'Human'
    >>> assert imoen.alignment == 'Neutral Good'
    >>> assert imoen.stats == Stats(strength=9, dexterity=18,
    ...                             constitution=16, intelligence=17,
    ...                             wisdom=11, charisma=16)

    >>> minsc = Ranger.from_toml(FILE, 'Minsc')
    >>> assert type(minsc.character_class) is str
    >>> assert type(minsc.race) is str
    >>> assert type(minsc.alignment) is str
    >>> assert type(minsc.stats) is Stats
    >>> assert minsc.character_class == 'Ranger'
    >>> assert minsc.race == 'Human'
    >>> assert minsc.alignment == 'Neutral Good'
    >>> assert minsc.stats == Stats(strength=18, dexterity=15,
    ...                             constitution=15, intelligence=8,
    ...                             wisdom=6, charisma=9)

    >>> neera = WildMage.from_toml(FILE, 'Neera')
    >>> assert type(neera.character_class) is str
    >>> assert type(neera.race) is str
    >>> assert type(neera.alignment) is str
    >>> assert type(neera.stats) is Stats
    >>> assert neera.character_class == 'Wild Mage'
    >>> assert neera.race == 'Half-elf'
    >>> assert neera.alignment == 'Chaotic Neutral'
    >>> assert neera.stats == Stats(strength=11, dexterity=17,
    ...                             constitution=14, intelligence=17,
    ...                             wisdom=10, charisma=11)

    >>> sarevok = Fighter.from_toml(FILE, 'Sarevok')
    >>> assert type(sarevok.character_class) is str
    >>> assert type(sarevok.race) is str
    >>> assert type(sarevok.alignment) is str
    >>> assert type(sarevok.stats) is Stats
    >>> assert sarevok.character_class == 'Fighter'
    >>> assert sarevok.race == 'Human'
    >>> assert sarevok.alignment == 'Chaotic Evil'
    >>> assert sarevok.stats == Stats(strength=18, dexterity=17,
    ...                               constitution=18, intelligence=17,
    ...                               wisdom=10, charisma=15)

    >>> remove(FILE)
"""
import tomllib
from dataclasses import dataclass
from pathlib import Path
from random import randint
from typing import NamedTuple

FILE = '_temporary.toml'

DATA = b"""
[Imoen]
character_class = 'Thief'
race = 'Human'
alignment = 'Neutral Good'
strength = 9
dexterity = 18
constitution = 16
intelligence = 17
wisdom = 11
charisma = 16

[Minsc]
character_class = 'Ranger'
race = 'Human'
alignment = 'Neutral Good'
strength = 18
dexterity = 15
constitution = 15
intelligence = 8
wisdom = 6
charisma = 9

[Neera]
character_class = 'Wild Mage'
race = 'Half-elf'
alignment = 'Chaotic Neutral'
strength = 11
dexterity = 17
constitution = 14
intelligence = 17
wisdom = 10
charisma = 11

[Sarevok]
character_class = 'Fighter'
race = 'Human'
alignment = 'Chaotic Evil'
strength = 18
dexterity = 17
constitution = 18
intelligence = 17
wisdom = 10
charisma = 15
"""

with open(FILE, mode='wb') as file:
    file.write(DATA)

class Stats(NamedTuple):
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int


@dataclass
class Character:
    character_class: str
    race: str
    alignment: str
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    @property
    def stats(self) -> Stats:
        return Stats(
            strength=self.strength,
            dexterity=self.dexterity,
            constitution=self.constitution,
            intelligence=self.intelligence,
            wisdom=self.wisdom,
            charisma=self.charisma)

# Method `from_toml()` with parameter: `data: str`, `name: str`
# Method `from_toml()` returns instance of a class on which was called
# type: Callable[[type[Self], str, str], Self]
    def from_toml():
        ...


class Fighter(Character):
    pass


class WildMage(Character):
    pass


class Ranger(Character):
    pass


class Thief(Character):
    pass


# Solution
@dataclass
class Character:
    character_class: str
    race: str
    alignment: str
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    @property
    def stats(self) -> Stats:
        return Stats(
            strength=self.strength,
            dexterity=self.dexterity,
            constitution=self.constitution,
            intelligence=self.intelligence,
            wisdom=self.wisdom,
            charisma=self.charisma)

    @classmethod
    def from_toml(cls, filename: str, name: str):
        with open(filename, mode='rb') as file:
            characters = tomllib.load(file)
        stats = characters[name]
        return cls(**stats)


class Fighter(Character):
    pass


class WildMage(Character):
    pass


class Ranger(Character):
    pass


class Thief(Character):
    pass
