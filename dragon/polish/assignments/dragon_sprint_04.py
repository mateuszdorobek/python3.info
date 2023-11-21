# doctest: +SKIP_FILE

#%% README.rst

"""
Dragon
======
Przygotowanie:

>>> from dragon import Dragon

Stwórz smoka o nazwie "Wawelski"
Smok ma punkty życia (losowa liczba od 50 do 100)

>>> dragon = Dragon('Wawelski')

Ustaw inicjalną pozycję smoka na x=50, y=120

>>> dragon = Dragon('Wawelski', position_x=50, position_y=120)

Ustaw nową pozycję na x=10, y=20

>>> dragon.set_position(x=10, y=20)

Pobierz aktualną pozycję

>>> position = dragon.get_position()
"""

#%% main.py
from random import randint


class Dragon:
    name: str
    health: int
    position_x: int
    position_y: int

    def __init__(self, name: str, /,
                 *, position_x: int = 0, position_y: int = 0) -> None:
        self.name = name
        self.health = randint(50,100)
        self.position_x = position_x
        self.position_y = position_y

    def set_position(self, *, x: int, y: int) -> None:
        self.position_x = x
        self.position_y = y

    def get_position(self) -> tuple[int,int]:
        return self.position_x, self.position_y


#%% tests.py
from random import seed
from unittest import TestCase
from main import Dragon


class InitTest(TestCase):
    def test_init_name_default(self):
        with self.assertRaises(TypeError):
            dragon = Dragon()  # noqa

    def test_init_name_positional(self):
        dragon = Dragon('Name')
        self.assertEqual(dragon.name, 'Name')

    def test_init_name_keyword(self):
        with self.assertRaises(TypeError):
            dragon = Dragon(name='Name')  # noqa

    def test_init_position_default(self):
        dragon = Dragon('Name')
        self.assertEqual(dragon.position_x, 0)
        self.assertEqual(dragon.position_y, 0)

    def test_init_position_positional(self):
        with self.assertRaises(TypeError):
            dragon = Dragon('Name', 1)  # noqa
        with self.assertRaises(TypeError):
            dragon = Dragon('Name', 1, 2)  # noqa

    def test_init_position_keyword(self):
        dragon = Dragon('Name', position_x=1, position_y=2)
        self.assertEqual(dragon.position_x, 1)
        self.assertEqual(dragon.position_y, 2)


class HealthTest(TestCase):
    def setUp(self):
        seed(0)
        self.dragon = Dragon('Name')

    def test_health_default_seed(self):
        self.assertIsInstance(self.dragon.health, int)
        self.assertEqual(self.dragon.health, 74)

    def test_health_default_one(self):
        self.assertIsInstance(self.dragon.health, int)
        self.assertGreaterEqual(self.dragon.health, 50)
        self.assertLessEqual(self.dragon.health, 100)

    def test_health_default_many(self):
        for _ in range(100_000):
            self.assertIsInstance(self.dragon.health, int)
            self.assertGreaterEqual(self.dragon.health, 50)
            self.assertLessEqual(self.dragon.health, 100)


class PositionTest(TestCase):
    def setUp(self):
        self.dragon = Dragon('Name', position_x=1, position_y=2)

    def test_position_set_default(self):
        with self.assertRaises(TypeError):
            self.dragon.set_position()  # noqa

    def test_position_set_positional(self):
        with self.assertRaises(TypeError):
            self.dragon.set_position(1)  # noqa
        with self.assertRaises(TypeError):
            self.dragon.set_position(1, 2)  # noqa

    def test_position_set_keyword_one(self):
        with self.assertRaises(TypeError):
            self.dragon.set_position(x=1)  # noqa
        with self.assertRaises(TypeError):
            self.dragon.set_position(y=1)  # noqa

    def test_position_set_keyword_xy(self):
        self.dragon.set_position(x=10, y=20)
        self.assertEqual(self.dragon.position_x, 10)
        self.assertEqual(self.dragon.position_y, 20)

    def test_position_get(self):
        x, y = self.dragon.get_position()
        self.assertEqual(x, 1)
        self.assertEqual(y, 2)
