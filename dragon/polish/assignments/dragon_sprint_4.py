"""
Dragon game
===========
>>> from dragon import Dragon  # doctest: +SKIP
>>> from random import seed; seed(0)
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3,11), 'Python 3.11+ required'

Stwórz smoka o nazwie "Wawelski"
Ustaw inicjalną pozycję smoka na x=1, y=2

>>> dragon = Dragon('Wawelski', position_x=50, position_y=120)

Ustaw nową pozycję na x=10, y=20

>>> dragon.set_position(x=10, y=20)

Przesuń smoka w lewo o 10 i w dół o 20

>>> dragon.move(left=10, down=20)

Przesuń smoka w lewo o 10 i w prawo o 15

>>> dragon.move(left=10, right=15)

Przesuń smoka w prawo o 15 i w górę o 5

>>> dragon.move(right=15, up=5)

Przesuń smoka w dół o 5

>>> dragon.move(down=5)

Smok zadaje obrażenia (5-20)

>>> dmg = dragon.make_damage()

Zadaj smokowi DMG obrażeń

>>> dragon.take_damage(10)

>>> dragon.take_damage(20)

>>> dragon.take_damage(30)

>>> dragon.take_damage(40)
Wawelski is dead
Gold: 98
Position: x=20, y=40

>>> dragon.take_damage(50)
Wawelski is dead
Gold: 98
Position: x=20, y=40
"""

from random import randint
from random import seed
from unittest import TestCase


class Dragon:
    HEALTH_MIN = 50
    HEALTH_MAX = 120
    DAMAGE_MIN = 5
    DAMAGE_MAX = 20
    GOLD_MIN = 1
    GOLD_MAX = 100

    def __init__(self, name, /, *, position_x=0, position_y=0):
        self.name = name
        self.position_x = position_x
        self.position_y = position_y
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)

    def set_position(self, *, x, y):
        self.position_x = x
        self.position_y = y

    def move(self, *, left=0, right=0, up=0, down=0):
        self.position_x += right - left
        self.position_y += down - up

    def make_damage(self):
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    def take_damage(self, damage):
        self.set_health(self.health-damage)

    def is_dead(self):
        return self.health <= 0

    def set_health(self, value):
        self.health = value
        if self.is_dead():
            self.make_dead()

    def make_dead(self):
        print(f'{self.name} is dead')
        print(f'Gold: {self.gold}')
        print(f'Position: x={self.position_x}, y={self.position_y}')


class DragonInitTest(TestCase):
    def test_init_name_default(self):
        with self.assertRaises(TypeError):
            Dragon()  # noqa

    def test_init_name_positional(self):
        dragon = Dragon('Wawelski')
        self.assertEqual(dragon.name, 'Wawelski')

    def test_init_name_keyword(self):
        with self.assertRaises(TypeError):
            Dragon(name='Wawelski')  # noqa

    def test_init_position_default(self):
        dragon = Dragon('Wawelski')
        self.assertEqual(dragon.position_x, 0)
        self.assertEqual(dragon.position_y, 0)

    def test_init_position_positional(self):
        with self.assertRaises(TypeError):
            Dragon('Wawelski', 1, 2)  # noqa

    def test_init_position_keyword(self):
        dragon = Dragon('Wawelski', position_x=1, position_y=2)
        self.assertEqual(dragon.position_x, 1)
        self.assertEqual(dragon.position_y, 2)


class PositionTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski', position_x=10, position_y=20)

    def test_position_set_default(self):
        with self.assertRaises(TypeError):
            self.dragon.set_position()  # noqa
        with self.assertRaises(TypeError):
            self.dragon.set_position(x=1)  # noqa
        with self.assertRaises(TypeError):
            self.dragon.set_position(y=1)  # noqa

    def test_position_set_positional(self):
        with self.assertRaises(TypeError):
            self.dragon.set_position(1, 2)  # noqa

    def test_position_set_keyword(self):
        self.dragon.set_position(x=1, y=2)
        self.assertEqual(self.dragon.position_x, 1)
        self.assertEqual(self.dragon.position_y, 2)

    def test_position_move_positional(self):
        with self.assertRaises(TypeError):
            self.dragon.move(1)  # noqa
        with self.assertRaises(TypeError):
            self.dragon.move(1,2)  # noqa
        with self.assertRaises(TypeError):
            self.dragon.move(1,2,3)  # noqa
        with self.assertRaises(TypeError):
            self.dragon.move(1,2,3,4)  # noqa

    def test_position_move_keyword_right(self):
        self.dragon.move(right=1)
        self.assertEqual(self.dragon.position_x, 11)
        self.assertEqual(self.dragon.position_y, 20)

    def test_position_move_keyword_left(self):
        self.dragon.move(left=1)
        self.assertEqual(self.dragon.position_x, 9)
        self.assertEqual(self.dragon.position_y, 20)

    def test_position_move_keyword_up(self):
        self.dragon.move(up=1)
        self.assertEqual(self.dragon.position_x, 10)
        self.assertEqual(self.dragon.position_y, 19)

    def test_position_move_keyword_down(self):
        self.dragon.move(down=1)
        self.assertEqual(self.dragon.position_x, 10)
        self.assertEqual(self.dragon.position_y, 21)

    def test_position_move_keyword_horizontal(self):
        self.dragon.move(left=1, right=2)
        self.assertEqual(self.dragon.position_x, 11)
        self.assertEqual(self.dragon.position_y, 20)

    def test_position_move_keyword_vertical(self):
        self.dragon.move(up=1, down=2)
        self.assertEqual(self.dragon.position_x, 10)
        self.assertEqual(self.dragon.position_y, 21)

    def test_position_move_keyword_omnidirectional(self):
        self.dragon.move(left=1, right=2, up=3, down=4)
        self.assertEqual(self.dragon.position_x, 11)
        self.assertEqual(self.dragon.position_y, 21)


class HealthTest(TestCase):
    def setUp(self) -> None:
        seed(0)
        self.dragon = Dragon('Wawelski')

    def test_health_default(self):
        self.assertEqual(self.dragon.health, 99)

    def test_health_range(self):
        self.assertEqual(self.dragon.HEALTH_MIN, 50)
        self.assertEqual(self.dragon.HEALTH_MAX, 120)


class GoldTest(TestCase):
    def setUp(self) -> None:
        seed(0)
        self.dragon = Dragon('Wawelski')

    def test_gold_default(self):
        self.assertEqual(self.dragon.gold, 98)

    def test_gold_range(self):
        self.assertEqual(self.dragon.GOLD_MIN, 1)
        self.assertEqual(self.dragon.GOLD_MAX, 100)


class DamageTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski')

    def test_damage_make(self):
        seed(0)
        dmg = self.dragon.make_damage()
        self.assertIsInstance(dmg, int)
        self.assertEqual(dmg, 17)

    def test_damage_range(self):
        self.assertEqual(self.dragon.DAMAGE_MIN, 5)
        self.assertEqual(self.dragon.DAMAGE_MAX, 20)

    def test_damage_take(self):
        self.dragon.set_health(2)
        self.dragon.take_damage(1)
        self.assertEqual(self.dragon.health, 1)

    def test_damage_isdead_when_health_zero(self):
        self.dragon.set_health(0)
        self.assertTrue(self.dragon.is_dead())

    def test_damage_isdead_when_health_negative(self):
        self.dragon.set_health(-1)
        self.assertTrue(self.dragon.is_dead())
