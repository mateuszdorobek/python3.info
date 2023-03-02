"""
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 8), 'Python 3.8+ required'
>>> from random import seed; seed(0)

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

>>> try:
...     dragon.take_damage(10)  # Zadaj 10 obrażeń smokowi
...     dragon.take_damage(5)   # Zadaj 5 obrażeń smokowi
...     dragon.take_damage(3)   # Zadaj 3 obrażeń smokowi
...     dragon.take_damage(2)   # Zadaj 2 obrażeń smokowi
...     dragon.take_damage(15)  # Zadaj 15 obrażeń smokowi
...     dragon.take_damage(25)  # Zadaj 25 obrażeń smokowi
...     dragon.take_damage(75)  # Zadaj 75 obrażeń smokowi
... except dragon.IsDead:
...     drop = dragon.get_drop()
...     print(f'{dragon} is dead')
...     print(f'Gold:', drop.gold)
...     print(f'Position:', drop.position)
...
Wawelski is dead
Gold: 98
Position: (20, 40)
"""
from enum import Enum
from functools import wraps
from random import randint
from typing import ClassVar, NamedTuple, NoReturn
from unittest import TestCase


class Status(Enum):
    ALIVE: ClassVar[str] = 'alive'
    DEAD: ClassVar[str] = 'dead'


def if_alive(mth):
    @wraps(mth)
    def wrapper(instance, *args, **kwargs):
        if not hasattr(instance, 'is_alive'):
            return mth(instance, *args, **kwargs)
        if instance.is_alive():
            return mth(instance, *args, **kwargs)
    return wrapper


def if_dead(mth):
    @wraps(mth)
    def wrapper(instance, *args, **kwargs):
        if not hasattr(instance, 'is_dead'):
            return mth(instance, *args, **kwargs)
        if instance.is_dead():
            return mth(instance, *args, **kwargs)
    return wrapper


class HasPosition:
    _position_x: int
    _position_y: int

    def __init__(self, x: int = 0, y: int = 0):
        self.position_set(x=x, y=y)

    @if_alive
    def position_set(self, *, x: int, y: int) -> None:
        self._position_x = x
        self._position_y = y

    def position_get(self):
        return self._position_x, self._position_y

    @if_alive
    def position_change(self, left: int = 0, right: int = 0,
                        down: int = 0, up: int = 0) -> None:
        current_x, current_y = self.position_get()
        new_x = current_x + right - left
        new_y = current_y + down - up
        self.position_set(x=new_x, y=new_y)


class Drop(NamedTuple):
    gold: int
    position: tuple[int,int]


class Dragon(HasPosition):
    _name: str
    _health: int
    _status: Status
    _texture: str
    _gold: int

    GOLD_MIN: ClassVar[int] = 1
    GOLD_MAX: ClassVar[int] = 100
    HEALTH_MIN: ClassVar[int] = 10
    HEALTH_MAX: ClassVar[int] = 50
    DAMAGE_MIN: ClassVar[int] = 5
    DAMAGE_MAX: ClassVar[int] = 20
    TEXTURE_ALIVE: ClassVar[str] = 'img/dragon/alive.png'
    TEXTURE_DEAD: ClassVar[str] = 'img/dragon/dead.png'

    def __init__(self, name: str, /,
                 *, position_x: int = 0, position_y: int = 0) -> None:
        self._name = name
        self._health = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self._gold = randint(self.GOLD_MIN, self.GOLD_MAX)
        self.position_set(x=position_x, y=position_y)
        self._status_update()
        self._texture_update()

    def __str__(self) -> str:
        return self._name

    class IsDead(Exception):
        pass

    @if_alive
    def make_damage(self) -> int:
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    @if_alive
    def take_damage(self, damage: int) -> NoReturn | Exception:
        self._health -= damage
        self._status_update()
        self._texture_update()
        if self.is_dead():
            raise self.IsDead

    def _texture_update(self):
        if self.is_alive():
            self._texture = self.TEXTURE_ALIVE
        else:
            self._texture = self.TEXTURE_DEAD

    def _status_update(self):
        if self.is_alive():
            self._status = Status.ALIVE
        else:
            self._status = Status.DEAD

    @if_dead
    def get_drop(self) -> Drop:
        gold, self._gold = self._gold, 0
        return Drop(gold=gold, position=self.position_get())

    def is_alive(self) -> bool:
        return not self.is_dead()

    def is_dead(self) -> bool:
        return self._health <= 0


class PositionTest(TestCase):
    def setUp(self) -> None:
        self.point = HasPosition(x=1, y=1)

    def test_position_set_positional(self):
        with self.assertRaises(TypeError):
            self.point.position_set(10, 20)

    def test_position_set_keyword(self):
        self.point.position_set(x=10, y=20)
        self.assertEqual(self.point._position_x, 10)
        self.assertEqual(self.point._position_y, 20)

    def test_position_get(self):
        self.point.position_set(x=10, y=20)
        self.assertEqual(self.point.position_get(), (10, 20))

    def test_position_change_left(self):
        self.point.position_change(left=1)
        self.assertEqual(self.point._position_x, 0)
        self.assertEqual(self.point._position_y, 1)

    def test_position_change_right(self):
        self.point.position_change(right=1)
        self.assertEqual(self.point._position_x, 2)
        self.assertEqual(self.point._position_y, 1)

    def test_position_change_horizontal(self):
        self.point.position_change(right=3, left=2)
        self.assertEqual(self.point._position_x, 2)
        self.assertEqual(self.point._position_y, 1)

    def test_position_change_vertical(self):
        self.point.position_change(down=3, up=2)
        self.assertEqual(self.point._position_x, 1)
        self.assertEqual(self.point._position_y, 2)

    def test_position_change_all(self):
        self.point.position_change(right=3, left=2, down=3, up=2)
        self.assertEqual(self.point._position_x, 2)
        self.assertEqual(self.point._position_y, 2)

    def test_position_change_up(self):
        self.point.position_change(up=1)
        self.assertEqual(self.point._position_x, 1)
        self.assertEqual(self.point._position_y, 0)

    def test_position_change_down(self):
        self.point.position_change(down=1)
        self.assertEqual(self.point._position_x, 1)
        self.assertEqual(self.point._position_y, 2)


class DragonTest(TestCase):
    dragon: Dragon

    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski', position_x=1, position_y=1)

    def test_create_name_positional(self):
        dragon = Dragon('Wawelski')
        self.assertEqual(dragon._name, 'Wawelski')

    def test_create_name_keyword(self):
        with self.assertRaises(TypeError):
            Dragon(name='Wawelski')

    def test_create_position_positional(self):
        with self.assertRaises(TypeError):
            Dragon('Wawelski', 1, 2)

    def test_create_position_keyword(self):
        dragon = Dragon('Wawelski', position_x=1, position_y=2)
        self.assertEqual(dragon._position_x, 1)
        self.assertEqual(dragon._position_y, 2)

    def test_damage_make(self):
        dmg = self.dragon.make_damage()
        self.assertIn(dmg, range(5, 21))

    def test_damage_take_and_health_positive(self):
        self.dragon._health = 2
        self.dragon.take_damage(1)
        self.assertEqual(self.dragon._health, 1)

    def test_damage_take_and_health_zero(self):
        self.dragon._health = 1
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(1)
        self.assertEqual(self.dragon._health, 0)

    def test_damage_take_and_health_negative(self):
        self.dragon._health = 1
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(2)
        self.assertEqual(self.dragon._health, -1)

    def test_damage_take_and_lives(self):
        self.dragon._health = 2
        self.dragon.take_damage(1)
        self.assertTrue(self.dragon.is_alive())

    def test_damage_take_and_zero(self):
        self.dragon._health = 1
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(1)

    def test_damage_take_and_dies(self):
        self.dragon._health = 1
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(2)

    def test_is_alive_positive(self):
        self.dragon._health = 1
        self.assertTrue(self.dragon.is_alive())

    def test_is_alive_zero(self):
        self.dragon._health = 0
        self.assertFalse(self.dragon.is_alive())

    def test_is_alive_negative(self):
        self.dragon._health = -1
        self.assertFalse(self.dragon.is_alive())

    def test_is_dead_positive(self):
        self.dragon._health = 1
        self.assertFalse(self.dragon.is_dead())

    def test_is_dead_zero(self):
        self.dragon._health = 0
        self.assertTrue(self.dragon.is_dead())

    def test_is_dead_negative(self):
        self.dragon._health = -1
        self.assertTrue(self.dragon.is_dead())
