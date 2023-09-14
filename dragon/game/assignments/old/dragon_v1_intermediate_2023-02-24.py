"""
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3,11), 'Python 3.11+ required'
>>> from random import seed; seed(0)

Stwórz smoka o nazwie "Wawelski"
Ustaw inicjalną pozycję smoka na x=50, y=120
>>> dragon = Dragon('Wawelski', position_x=50, position_y=120)

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

>>> try:
...     dragon.take_damage(10)  # Zadaj 10 obrażeń smokowi
...     dragon.take_damage(5)  # Zadaj 5 obrażeń smokowi
...     dragon.take_damage(3)  # Zadaj 3 obrażenia smokowi
...     dragon.take_damage(2)  # Zadaj 2 obrażenia smokowi
...     dragon.take_damage(15)  # Zadaj 15 obrażeń smokowi
...     dragon.take_damage(25)  # Zadaj 25 obrażeń smokowi
...     dragon.take_damage(75)  # Zadaj 75 obrażeń smokowi
... except dragon.IsDead:
...     drop = dragon.get_drop()
...     print(f'{dragon.name} is dead')
...     print(f'Gold: {drop.gold}')
...     print(f'Position: {drop.position}')
Wawelski is dead
Gold: 98
Position: (20, 40)

Smok powinien zginąć na pozycji: x=20, y=40 i zostawić złoto (1-100)
"""

from enum import Enum
from random import randint
from typing import ClassVar, NamedTuple
from unittest import TestCase


class Status(Enum):
    ALIVE: ClassVar[str] = 'alive'
    DEAD: ClassVar[str] = 'dead'


class Drop(NamedTuple):
    gold: int
    position: tuple[int,int]


class HasPosition:
    position_x: int
    position_y: int

    def __init__(self, position_x: int = 0, position_y: int = 0) -> None:
        self.position_x = position_x
        self.position_y = position_y

    def position_set(self, *, x: int, y: int) -> None:
        self.position_x = x
        self.position_y = y

    def position_change(self, *, right: int = 0, left: int = 0,
                        down: int = 0, up: int = 0) -> None:
            current_x, current_y = self.position_get()
            self.position_set(x=current_x + right - left,
                              y=current_y + down - up)

    def position_get(self) -> tuple[int, int]:
        return self.position_x, self.position_y


class Dragon(HasPosition):
    DAMAGE_MAX: ClassVar[int] = 20
    DAMAGE_MIN: ClassVar[int] = 5
    GOLD_MAX: ClassVar[int] = 100
    GOLD_MIN: ClassVar[int] = 1
    HEALTH_MAX: ClassVar[int] = 100
    HEALTH_MIN: ClassVar[int] = 50
    TEXTURE_ALIVE: ClassVar[str] = 'img/dragon/alive.png'
    TEXTURE_DEAD: ClassVar[str] = 'img/dragon/dead.png'

    name: str
    status: Status
    texture: str
    gold: int
    health: int

    def __init__(self, name: str, /,
                 *, position_x: int = 0, position_y: int = 0) -> None:
        self.name = name
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self.status = Status.ALIVE
        self.texture = self.TEXTURE_ALIVE
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)
        self.position_set(x=position_x, y=position_y)

    class IsDead(Exception):
        pass

    def position_set(self, *, x: int, y: int) -> None:
        if self.is_alive():
            super().position_set(x=x, y=y)

    def _make_dead(self):
        self.status = Status.DEAD
        self.texture = self.TEXTURE_ALIVE
        raise self.IsDead()

    def get_drop(self) -> Drop:
        if self.is_dead():
            gold, self.gold = self.gold, 0
            return Drop(gold=gold, position=self.position_get())

    def make_damage(self) -> int:
        if self.is_alive():
            return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    def take_damage(self, damage, /):
        if self.is_alive():
            self.health -= damage
            if self.is_dead():
                self._make_dead()

    def is_alive(self) -> bool:
        return not self.is_dead()

    def is_dead(self) -> bool:
        return self.health <= 0


class DragonInitTest(TestCase):
    def test_init_name_noname(self):
        with self.assertRaises(TypeError):
            Dragon()  # noqa

    def test_init_name_positional(self):
        dragon = Dragon('Wawelski')
        self.assertEqual(dragon.name, 'Wawelski')

    def test_init_name_keyword(self):
        with self.assertRaises(TypeError):
            Dragon(name='Wawelski')  # noqa

    def test_init_position_keyword(self):
        dragon = Dragon('Wawelski', position_x=1, position_y=2)
        self.assertEqual(dragon.position_x, 1)
        self.assertEqual(dragon.position_y, 2)

    def test_init_position_positional(self):
        with self.assertRaises(TypeError):
            Dragon('Wawelski', 1, 2)  # noqa
        with self.assertRaises(TypeError):
            Dragon('Wawelski', 1, position_y=2)  # noqa


class PositionTest(TestCase):
    def setUp(self) -> None:
        self.position = HasPosition(position_x=10, position_y=20)

    def test_position_set_positional(self):
        with self.assertRaises(TypeError):
            self.position.position_set(1, 2)  # noqa
        with self.assertRaises(TypeError):
            self.position.position_set(1, y=2)  # noqa

    def test_position_set_keyword(self):
        self.position.position_set(x=1, y=2)
        self.assertEqual(self.position.position_x, 1)
        self.assertEqual(self.position.position_y, 2)

    def test_position_set_x_zero(self):
        self.position.position_set(x=0, y=1)
        self.assertEqual(self.position.position_x, 0)
        self.assertEqual(self.position.position_y, 1)

    def test_position_set_y_zero(self):
        self.position.position_set(x=1, y=0)
        self.assertEqual(self.position.position_x, 1)
        self.assertEqual(self.position.position_y, 0)

    def test_position_set_x_negative(self):
        self.position.position_set(x=-1, y=1)
        self.assertEqual(self.position.position_x, -1)
        self.assertEqual(self.position.position_y, 1)

    def test_position_set_y_negative(self):
        self.position.position_set(x=1, y=-1)
        self.assertEqual(self.position.position_x, 1)
        self.assertEqual(self.position.position_y, -1)

    def test_position_change_left(self):
        self.position.position_change(left=1)
        self.assertEqual(self.position.position_x, 9)
        self.assertEqual(self.position.position_y, 20)

    def test_position_change_right(self):
        self.position.position_change(right=1)
        self.assertEqual(self.position.position_x, 11)
        self.assertEqual(self.position.position_y, 20)

    def test_position_change_up(self):
        self.position.position_change(up=1)
        self.assertEqual(self.position.position_x, 10)
        self.assertEqual(self.position.position_y, 19)

    def test_position_change_down(self):
        self.position.position_change(down=1)
        self.assertEqual(self.position.position_x, 10)
        self.assertEqual(self.position.position_y, 21)

    def test_position_change_horizontal(self):
        self.position.position_change(left=1, right=2)
        self.assertEqual(self.position.position_x, 11)
        self.assertEqual(self.position.position_y, 20)

    def test_position_change_vertical(self):
        self.position.position_change(up=1, down=2)
        self.assertEqual(self.position.position_x, 10)
        self.assertEqual(self.position.position_y, 21)

    def test_position_change_omnidirectional(self):
        self.position.position_change(left=1, right=2, up=3, down=4)
        self.assertEqual(self.position.position_x, 11)
        self.assertEqual(self.position.position_y, 21)

    def test_position_change_positional(self):
        with self.assertRaises(TypeError):
            self.position.position_change(1)  # noqa
        with self.assertRaises(TypeError):
            self.position.position_change(1, 2)  # noqa
        with self.assertRaises(TypeError):
            self.position.position_change(1, 2, 3)  # noqa
        with self.assertRaises(TypeError):
            self.position.position_change(1, 2, 3, 4)  # noqa


class DragonHealthTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski')

    def test_health_init(self):
        self.assertIn(self.dragon.health, range(50,101))

    def test_health_isalive_when_health_positive(self):
        self.dragon.health = 1
        self.assertTrue(self.dragon.is_alive())

    def test_health_isalive_when_health_zero(self):
        self.dragon.health = 0
        self.assertFalse(self.dragon.is_alive())

    def test_health_isalive_when_health_negative(self):
        self.dragon.health = -1
        self.assertFalse(self.dragon.is_alive())

    def test_health_isdead_when_health_positive(self):
        self.dragon.health = 1
        self.assertFalse(self.dragon.is_dead())

    def test_health_isdead_when_health_zero(self):
        self.dragon.health = 0
        self.assertTrue(self.dragon.is_dead())

    def test_health_isdead_when_health_negative(self):
        self.dragon.health = -1
        self.assertTrue(self.dragon.is_dead())


class DragonGoldTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski')

    def test_gold_init(self):
        self.assertIn(self.dragon.gold, range(1,101))


class DragonDamageTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski')

    def test_damage_make(self):
        dmg = self.dragon.make_damage()
        self.assertIsInstance(dmg, int)
        self.assertIn(dmg, range(5,21))

    def test_damage_take_kwargs(self):
        with self.assertRaises(TypeError):
            self.dragon.take_damage(damage=1)  # noqa

    def test_damage_take_when_health_positive(self):
        self.dragon.health = 2
        self.dragon.take_damage(1)
        self.assertEqual(self.dragon.health, 1)

    def test_damage_take_when_health_zero(self):
        self.dragon.health = 2
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(2)

    def test_damage_take_when_health_negative(self):
        self.dragon.health = 2
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(3)
