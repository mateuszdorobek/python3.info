# doctest: +SKIP_FILE

#%% README.rst

"""
Dragon
======

Przygotowanie:

>>> from main import Dragon

Stwórz smoka o nazwie "Wawelski"

>>> dragon = Dragon('Wawelski')

Smok ma punkty życia (losowa liczba od 50 do 100)
"""

#%% main.py
from random import randint


class Dragon:
    name: str
    health: int

    def __init__(self, name: str, /) -> None:
        self.name = name
        self.health = randint(50,100)


#%% tests.py
from random import seed
from unittest import TestCase
from main import Dragon

class InitTest(TestCase):
    def test_init_name_default(self):
        with self.assertRaises(TypeError):
            Dragon()  # noqa

    def test_init_name_positional(self):
        dragon = Dragon('Name')
        self.assertEqual(dragon.name, 'Name')

    def test_init_name_keyword(self):
        with self.assertRaises(TypeError):
            Dragon(name='Name')  # noqa


class HealthTest(TestCase):
    def test_health_default_one(self):
        dragon = Dragon('Name')
        self.assertIsInstance(dragon.health, int)
        self.assertGreaterEqual(dragon.health, 50)
        self.assertLessEqual(dragon.health, 100)

    def test_health_default_many(self):
        for _ in range(100_000):
            dragon = Dragon('Name')
            self.assertIsInstance(dragon.health, int)
            self.assertGreaterEqual(dragon.health, 50)
            self.assertLessEqual(dragon.health, 100)

    def test_health_default_seed(self):
        seed(0)
        dragon = Dragon('Name')
        self.assertIsInstance(dragon.health, int)
        self.assertEqual(dragon.health, 74)
