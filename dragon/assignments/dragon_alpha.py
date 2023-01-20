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
...     dragon.take_damage(5)   # Zadaj 5 obrażeń smokowi
...     dragon.take_damage(3)   # Zadaj 3 obrażenia smokowi
...     dragon.take_damage(2)   # Zadaj 2 obrażenia smokowi
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


class PositionMixin:
    _position: Point

    def __init__(self, x: int=0, y: int=0) -> None:
        self.position_set(x=x, y=y)

    def position_get(self) -> Point:
        return self._position

    def position_set(self, *, x: int, y: int) -> None:
        self._position = Point(x, y)

    def position_change(self, *,
                        left: int = 0, right: int = 0,
                        up: int = 0, down: int = 0
                        ) -> None:
        current_x, current_y = self.position_get()
        new_x = current_x + right - left
        new_y = current_y + down - up
        self.position_set(x=new_x, y=new_y)


class Dragon(PositionMixin):
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
                 *, position_x: int = 0, position_y: int = 0) -> None:
        self.name = name
        self.status = Status.ALIVE
        self.texture = self.TEXTURE_ALIVE
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)
        self.position_set(x=position_x, y=position_y)

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
    def take_damage(self, damage, /) -> None:
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
        self.point = PositionMixin(x=10, y=20)

    def test_position_set_keyword(self):
        self.point.position_set(x=1, y=2)
        self.assertEqual(self.point._position.x, 1)
        self.assertEqual(self.point._position.y, 2)

    def test_position_set_positional(self):
        with self.assertRaises(TypeError):
            self.point.position_set(1, 2)  # noqa

    def test_position_change_left(self):
        self.point.position_change(left=1)
        self.assertEqual(self.point._position.x, 9)
        self.assertEqual(self.point._position.y, 20)

    def test_position_change_right(self):
        self.point.position_change(right=1)
        self.assertEqual(self.point._position.x, 11)
        self.assertEqual(self.point._position.y, 20)

    def test_position_change_up(self):
        self.point.position_change(up=1)
        self.assertEqual(self.point._position.x, 10)
        self.assertEqual(self.point._position.y, 19)

    def test_position_change_down(self):
        self.point.position_change(down=1)
        self.assertEqual(self.point._position.x, 10)
        self.assertEqual(self.point._position.y, 21)

    def test_position_change_vertical(self):
        self.point.position_change(left=1, right=2)
        self.assertEqual(self.point._position.x, 11)
        self.assertEqual(self.point._position.y, 20)

    def test_position_change_horizontal(self):
        self.point.position_change(up=1, down=2)
        self.assertEqual(self.point._position.x, 10)
        self.assertEqual(self.point._position.y, 21)

    def test_position_change_omnidirectional(self):
        self.point.position_change(left=1, right=2, up=3, down=4)
        self.assertEqual(self.point._position.x, 11)
        self.assertEqual(self.point._position.y, 21)

    def test_position_change_positional(self):
        with self.assertRaises(TypeError):
            self.point.position_change(1)  # noqa
        with self.assertRaises(TypeError):
            self.point.position_change(1, 2)  # noqa
        with self.assertRaises(TypeError):
            self.point.position_change(1, 2, 3)  # noqa
        with self.assertRaises(TypeError):
            self.point.position_change(1, 2, 3, 4)  # noqa

    def test_position_get(self):
        current_x, current_y = self.point.position_get()
        self.assertEqual(current_x, 10)
        self.assertEqual(current_y, 20)


class DragonTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski', position_x=10, position_y=20)

    def test_init_name_positional(self):
        dragon = Dragon('Wawelski')
        self.assertEqual(dragon.name, 'Wawelski')

    def test_init_name_keyword(self):
        with self.assertRaises(TypeError):
            Dragon(name='Wawelski')  # noqa

    def test_init_position_default(self):
        dragon = Dragon('Wawelski')
        self.assertEqual(dragon._position.x, 0)
        self.assertEqual(dragon._position.y, 0)

    def test_init_position_keyword(self):
        dragon = Dragon('Wawelski', position_x=1, position_y=2)
        self.assertEqual(dragon._position.x, 1)
        self.assertEqual(dragon._position.y, 2)

    def test_init_position_positional(self):
        with self.assertRaises(TypeError):
            Dragon('Wawelski', 1, position_y=2)  # noqa
        with self.assertRaises(TypeError):
            Dragon('Wawelski', 1, 2)  # noqa

    def test_init_health(self):
        self.assertIn(self.dragon.health, range(50, 101))

    def test_init_texture(self):
        self.assertEqual(self.dragon.texture, 'img/dragon/alive.png')

    def test_init_status(self):
        self.assertEqual(self.dragon.status, Status.ALIVE)

    def test_damage_make(self):
        dmg = self.dragon.make_damage()  # noqa
        self.assertIn(dmg, range(5, 21))

    def test_damage_take_keyword(self):
        with self.assertRaises(TypeError):
            self.dragon.take_damage(damage=1)  # noqa

    def test_damage_take_health_positive(self):
        self.dragon.health = 3
        self.dragon.take_damage(2)
        self.assertEqual(self.dragon.health, 1)

    def test_damage_take_health_zero(self):
        self.dragon.health = 2
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(2)

    def test_damage_take_health_negative(self):
        self.dragon.health = 1
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(2)

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

    def test_health_isalive_positive(self):
        self.dragon.health = 1
        self.assertTrue(self.dragon.is_alive())

    def test_health_isalive_zero(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = 0
        self.assertFalse(self.dragon.is_alive())

    def test_health_isalive_negative(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = -1
        self.assertFalse(self.dragon.is_alive())

    def test_health_isdead_positive(self):
        self.dragon.health = 1
        self.assertFalse(self.dragon.is_dead())

    def test_health_isdead_zero(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = 0
        self.assertTrue(self.dragon.is_dead())

    def test_health_isdead_negative(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = -1
        self.assertTrue(self.dragon.is_dead())
