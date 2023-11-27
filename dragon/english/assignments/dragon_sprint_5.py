#%% README.rst

"""
Dragon game
===========
>>> from dragon import Dragon  # doctest: +SKIP
>>> from random import seed; seed(0)
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3,11), 'Python 3.11+ required'

Stwórz smoka o nazwie "Wawelski"
Ustaw inicjalną pozycję smoka na x=1, y=2

>>> dragon = Dragon('Wawelski', position_x=50, position_y=100)

Ustaw nową pozycję na x=10, y=20

>>> dragon.position_set(x=10, y=20)

Przesuń smoka w lewo o 10 i w dół o 20

>>> dragon.position_change(left=10, down=20)

Przesuń smoka w lewo o 10 i w prawo o 15

>>> dragon.position_change(left=10, right=15)

Przesuń smoka w prawo o 15 i w górę o 5

>>> dragon.position_change(right=15, up=5)

Przesuń smoka w dół o 5

>>> dragon.position_change(down=5)

Smok zadaje obrażenia (5-20)

>>> dmg = dragon.make_damage()

Zadaj smokowi DMG obrażeń

>>> try:
...     dragon.take_damage(10)
...     dragon.take_damage(20)
...     dragon.take_damage(30)
...     dragon.take_damage(40)
...     dragon.take_damage(50)
... except dragon.IsDead:
...     drop = dragon.get_drop()
...     print(f'{dragon.name} is dead')
...     print(f'Gold: {drop.gold}')
Wawelski is dead
Gold: 98
"""


#%% position.py


from unittest import TestCase


class HasPosition:
    POSITION_X_MIN = 0
    POSITION_X_MAX = 1920
    POSITION_Y_MIN = 0
    POSITION_Y_MAX = 1080
    POSITION_Z_MIN = -100
    POSITION_Z_MAX = 100

    position_x: int
    position_y: int
    position_z: int

    def __init__(self, position_x=0, position_y=0, position_z=0):
        self.position_set(x=position_x, y=position_y, z=position_z)

    def position_set(self, *, x, y, z=0):
        self.position_x = max(self.POSITION_X_MIN, min(self.POSITION_X_MAX, x))
        self.position_y = max(self.POSITION_Y_MIN, min(self.POSITION_Y_MAX, y))
        self.position_z = max(self.POSITION_Z_MIN, min(self.POSITION_Z_MAX, z))

    def position_change(self, *, left=0, right=0, up=0, down=0, depth=0, altitude=0):
        new_x = self.position_x + right - left
        new_y = self.position_y + down - up
        new_z = self.position_z + altitude - depth
        self.position_set(x=new_x, y=new_y, z=new_z)

    def position_get(self):
        return self.position_x, self.position_y, self.position_z


class PositionTest(TestCase):
    def setUp(self) -> None:
        self.current = HasPosition(position_x=10, position_y=20, position_z=30)

    def test_position_get(self):
        x, y, z = self.current.position_get()
        self.assertEqual(x, 10)
        self.assertEqual(y, 20)
        self.assertEqual(z, 30)

    def test_position_set_default(self):
        with self.assertRaises(TypeError):
            self.current.position_set()  # noqa
        with self.assertRaises(TypeError):
            self.current.position_set(x=1)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_set(y=1)  # noqa

    def test_position_set_positional(self):
        with self.assertRaises(TypeError):
            self.current.position_set(1, 2, 3)  # noqa

    def test_position_set_keyword(self):
        self.current.position_set(x=1, y=2, z=3)
        self.assertEqual(self.current.position_x, 1)
        self.assertEqual(self.current.position_y, 2)
        self.assertEqual(self.current.position_z, 3)

    def test_position_move_positional(self):
        with self.assertRaises(TypeError):
            self.current.position_change(1)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2, 3)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2, 3, 4)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2, 3, 4, 5)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2, 3, 4, 5, 6)  # noqa

    def test_position_border_right(self):
        self.current.position_change(right=10_000)
        self.assertEqual(self.current.position_x, 1920)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 30)

    def test_position_border_left(self):
        self.current.position_change(left=10_000)
        self.assertEqual(self.current.position_x, 0)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 30)

    def test_position_border_up(self):
        self.current.position_change(up=10_000)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 0)
        self.assertEqual(self.current.position_z, 30)

    def test_position_border_down(self):
        self.current.position_change(down=10_000)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 1080)
        self.assertEqual(self.current.position_z, 30)

    def test_position_border_depth(self):
        self.current.position_change(depth=10_000)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, -100)

    def test_position_border_altitude(self):
        self.current.position_change(altitude=10_000)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 100)

    def test_position_move_keyword_right(self):
        self.current.position_change(right=1)
        self.assertEqual(self.current.position_x, 11)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 30)

    def test_position_move_keyword_left(self):
        self.current.position_change(left=1)
        self.assertEqual(self.current.position_x, 9)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 30)

    def test_position_move_keyword_up(self):
        self.current.position_change(up=1)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 19)
        self.assertEqual(self.current.position_z, 30)

    def test_position_move_keyword_down(self):
        self.current.position_change(down=1)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 21)
        self.assertEqual(self.current.position_z, 30)

    def test_position_move_keyword_depth(self):
        self.current.position_change(depth=1)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 29)

    def test_position_move_keyword_altitude(self):
        self.current.position_change(altitude=1)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 31)

    def test_position_move_keyword_axis_x(self):
        self.current.position_change(left=1, right=2)
        self.assertEqual(self.current.position_x, 11)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 30)

    def test_position_move_keyword_axis_y(self):
        self.current.position_change(up=1, down=2)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 21)
        self.assertEqual(self.current.position_z, 30)

    def test_position_move_keyword_axis_z(self):
        self.current.position_change(depth=1, altitude=2)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 31)

    def test_position_move_keyword_axis_xyz(self):
        self.current.position_change(left=1, right=2, up=3, down=4, depth=5, altitude=6)
        self.assertEqual(self.current.position_x, 11)
        self.assertEqual(self.current.position_y, 21)
        self.assertEqual(self.current.position_z, 31)


#%% drop.py


from random import seed, randint
from typing import NamedTuple
from unittest import TestCase


class Drop(NamedTuple):
    gold: int


class HasDrop:
    GOLD_MIN = 0
    GOLD_MAX = 1
    gold: int

    def __init__(self):
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)

    def get_drop(self):
        gold, self.gold = self.gold, 0
        return Drop(gold=gold)


class HasDropTest(TestCase):
    def setUp(self) -> None:
        seed(0)
        self.drop = HasDrop()

    def test_drop_get(self):
        drop = self.drop.get_drop()
        self.assertEqual(drop.gold, 1)

    def test_drop_gold_default(self):
        self.assertEqual(self.drop.gold, 1)

    def test_drop_gold_range(self):
        self.assertEqual(self.drop.GOLD_MIN, 0)
        self.assertEqual(self.drop.GOLD_MAX, 1)


#%% damage.py


from random import randint, seed
from unittest import TestCase


class MakesDamage:
    DAMAGE_MIN = 0
    DAMAGE_MAX = 100

    def make_damage(self):
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)


class MakesDamageTest(TestCase):
    def setUp(self) -> None:
        self.character = MakesDamage()

    def test_damage_make(self):
        seed(0)
        dmg = self.character.make_damage()
        self.assertIsInstance(dmg, int)
        self.assertEqual(dmg, 49)

    def test_damage_range(self):
        self.assertEqual(self.character.DAMAGE_MIN, 0)
        self.assertEqual(self.character.DAMAGE_MAX, 100)


#%% health.py


from random import seed, randint
from unittest import TestCase


class HasHealth:
    HEALTH_MIN = 1
    HEALTH_MAX = 100
    health: int

    def __init__(self):
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)

    class IsDead(Exception):
        pass

    def take_damage(self, damage):
        self.set_health(self.health-damage)

    def is_dead(self):
        return self.health <= 0

    def set_health(self, value):
        self.health = value
        if self.is_dead():
            raise self.IsDead


class HasHealthTest(TestCase):
    def setUp(self) -> None:
        seed(0)
        self.obj = HasHealth()

    def test_health_default(self):
        self.assertEqual(self.obj.health, 50)

    def test_health_range(self):
        self.assertEqual(self.obj.HEALTH_MIN, 1)
        self.assertEqual(self.obj.HEALTH_MAX, 100)

    def test_health_isdead_when_health_zero(self):
        with self.assertRaises(self.obj.IsDead):
            self.obj.set_health(0)
        self.assertTrue(self.obj.is_dead())

    def test_health_isdead_when_health_negative(self):
        with self.assertRaises(self.obj.IsDead):
            self.obj.set_health(-1)
        self.assertTrue(self.obj.is_dead())

    def test_health_take_damage(self):
        self.obj.set_health(2)
        self.obj.take_damage(1)
        self.assertEqual(self.obj.health, 1)


#%% dragon.py


# from damage import MakesDamage
# from position import HasPosition
# from drop import HasDrop
# from health import HasHealth
from random import randint
from unittest import TestCase


class Dragon(HasPosition, HasDrop, HasHealth, MakesDamage):
    HEALTH_MIN = 50
    HEALTH_MAX = 100
    DAMAGE_MIN = 5
    DAMAGE_MAX = 20
    GOLD_MIN = 1
    GOLD_MAX = 100

    def __init__(self, name, /, *, position_x=0, position_y=0, position_z=0):
        self.name = name
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)
        self.position_set(x=position_x, y=position_y, z=position_z)


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
            Dragon('Wawelski', 1, 2, 3)  # noqa

    def test_init_position_keyword(self):
        dragon = Dragon('Wawelski', position_x=1, position_y=2, position_z=3)
        self.assertEqual(dragon.position_x, 1)
        self.assertEqual(dragon.position_y, 2)
        self.assertEqual(dragon.position_z, 3)
