"""
>>> from random import seed; seed(0)
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), 'Python 3.10+ required'

Stwórz smoka w pozycji x=50, y=120 i nazwij go "Wawelski"
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

Smok zadaje obrażenia
>>> dmg = dragon.make_damage()

Zadaj X obrażeń smokowi
>>> try:
...     dragon.take_damage(10)
...     dragon.take_damage(5)
...     dragon.take_damage(3)
...     dragon.take_damage(2)
...     dragon.take_damage(15)
...     dragon.take_damage(25)
...     dragon.take_damage(75)
... except dragon.IsDead:
...     drop = dragon.get_drop()
...     print(f'{dragon.name} is dead')
...     print(f'Gold {drop.gold}')
...     print(f'Position {drop.position}')
Wawelski is dead
Gold 50
Position (20, 40)

Smok powinien zginąć na pozycji: x=20, y=40
"""
from enum import Enum
from random import randint
from typing import ClassVar, NamedTuple
from unittest import TestCase


class Status(Enum):
    ALIVE: str = 'alive'
    DEAD: str = 'dead'


class Point(NamedTuple):
    x: int = 0
    y: int = 0

    def __str__(self):
        return f'({self.x}, {self.y})'


class Drop(NamedTuple):
    gold: int
    position: Point


def when(condition_method_name):
    def decorator(mth):
        def wrapper(character, *args, **kwargs):
            condition = getattr(character, condition_method_name)
            if condition():
                return mth(character, *args, **kwargs)
        return wrapper
    return decorator


class HasPosition:
    position_x: int
    position_y: int

    def __init__(self, x: int=0, y: int=0) -> None:
        self.position_x = x
        self.position_y = y

    def position_get(self) -> Point:
        return Point(self.position_x, self.position_y)

    def position_set(self, *, x: int, y: int) -> None:
        self.position_x = x
        self.position_y = y

    def position_change(self, *,
                        left: int = 0, right: int = 0,
                        up: int = 0, down: int = 0
                        ) -> None:
        current_x, current_y = self.position_get()
        new_x = current_x + right - left
        new_y = current_y + down - up
        self.position_set(x=new_x, y=new_y)


class Dragon(HasPosition):
    name: str
    health = property()
    _health_current: int

    DAMAGE_MAX: ClassVar[int] = 20
    DAMAGE_MIN: ClassVar[int] = 5
    GOLD_MAX: ClassVar[int] = 100
    GOLD_MIN: ClassVar[int] = 1
    HEALTH_MAX: ClassVar[int] = 100
    HEALTH_MIN: ClassVar[int] = 50
    TEXTURE_ALIVE: ClassVar[str] = 'img/dragon/alive.png'
    TEXTURE_DEAD: ClassVar[str] = 'img/dragon/dead.png'

    class IsDead(Exception):
        pass

    def __init__(self, name: str, /,
                 *, position_x: int = 0, position_y: int = 0
                 ) -> None:
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self.name = name
        self.position_set(x=position_x, y=position_y)
        self.status = Status.ALIVE
        self.texture = self.TEXTURE_ALIVE

    @when('is_alive')
    def make_damage(self) -> int:
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    @health.getter
    def health(self):
        return self._health_current

    @health.setter
    def health(self, value):
        self._health_current = value
        if self.is_alive():
            self.status = Status.ALIVE
            self.texture = self.TEXTURE_ALIVE
        else:
            self.status = Status.DEAD
            self.texture = self.TEXTURE_DEAD
            raise self.IsDead

    @when('is_alive')
    def take_damage(self, damage) -> None:
        self.health -= damage

    @when('is_dead')
    def get_drop(self) -> Drop:
        gold, self.gold = self.gold, 0
        return Drop(gold=gold, position=self.position_get())

    def is_dead(self):
        return self.health <= 0

    def is_alive(self):
        return not self.is_dead()


class HasPositionTest(TestCase):
    def setUp(self) -> None:
        self.position = HasPosition(x=10, y=20)

    def test_position_set_keyword(self):
        self.position.position_set(x=1, y=2)
        self.assertEqual(self.position.position_x, 1)
        self.assertEqual(self.position.position_y, 2)

    def test_position_set_positional(self):
        with self.assertRaises(TypeError):
            self.position.position_set(1, 2)  # noqa

    def test_position_change_down(self):
        self.position.position_change(down=1)
        self.assertEqual(self.position.position_x, 10)
        self.assertEqual(self.position.position_y, 21)

    def test_position_change_up(self):
        self.position.position_change(up=1)
        self.assertEqual(self.position.position_x, 10)
        self.assertEqual(self.position.position_y, 19)

    def test_position_change_left(self):
        self.position.position_change(left=1)
        self.assertEqual(self.position.position_x, 9)
        self.assertEqual(self.position.position_y, 20)

    def test_position_change_right(self):
        self.position.position_change(right=1)
        self.assertEqual(self.position.position_x, 11)
        self.assertEqual(self.position.position_y, 20)

    def test_position_change_vertical(self):
        self.position.position_change(left=1, right=2)
        self.assertEqual(self.position.position_x, 11)
        self.assertEqual(self.position.position_y, 20)

    def test_position_change_horizontal(self):
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

    def test_position_get(self):
        x, y = self.position.position_get()
        self.assertEqual(x, 10)
        self.assertEqual(y, 20)


class DragonTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski', position_x=10, position_y=20)

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
            Dragon('Wawelski', 1, position_y=2)  # noqa
        with self.assertRaises(TypeError):
            Dragon('Wawelski', 1, 2)  # noqa

    def test_init_health(self):
        self.assertIn(self.dragon.health, range(50, 101))

    def test_damage_make(self):
        dmg = self.dragon.make_damage()
        self.assertIn(dmg, range(5, 21))

    def test_damage_take_health_positive(self):
        self.dragon.health = 2
        self.dragon.take_damage(1)
        self.assertEqual(self.dragon.health, 1)

    def test_damage_take_health_zero(self):
        self.dragon.health = 2
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(2)

    def test_damage_take_health_negative(self):
        self.dragon.health = 2
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(3)

    def test_status_health_positive(self):
        self.dragon.health = 1
        self.assertEqual(self.dragon.status, Status.ALIVE)

    def test_status_health_zero(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = 0
        self.assertEqual(self.dragon.status, Status.DEAD)

    def test_status_health_negative(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = -1
        self.assertEqual(self.dragon.status, Status.DEAD)

    def test_texture_health_positive(self):
        self.dragon.health = 1
        self.assertEqual(self.dragon.texture, 'img/dragon/alive.png')

    def test_texture_health_zero(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = 0
        self.assertEqual(self.dragon.texture, 'img/dragon/dead.png')

    def test_texture_health_negative(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = -1
        self.assertEqual(self.dragon.texture, 'img/dragon/dead.png')
