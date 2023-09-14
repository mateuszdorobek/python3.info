"""
>>> import sys; sys.tracebacklimit = 0
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
...     dragon.take_damage(10)  # Zadaj 10 obrażeń smokowi # noqa
...     dragon.take_damage(5)  # Zadaj 5 obrażeń smokowi # noqa
...     dragon.take_damage(3)  # Zadaj 3 obrażeń smokowi # noqa
...     dragon.take_damage(2)  # Zadaj 2 obrażeń smokowi # noqa
...     dragon.take_damage(15)  # Zadaj 15 obrażeń smokowi # noqa
...     dragon.take_damage(25)  # Zadaj 25 obrażeń smokowi # noqa
...     dragon.take_damage(75)  # Zadaj 75 obrażeń smokowi # noqa
... except dragon.IsDead:
...     drop = dragon.get_drop()
...     print(f'{dragon.name} is dead')
...     print(f'Position: {drop.position}')
...     print(f'Gold: {drop.gold}')
Wawelski is dead
Position: (20, 40)
Gold: 98
"""
from enum import Enum
from functools import wraps
from random import randint
from typing import ClassVar, NamedTuple
from unittest import TestCase


def if_alive(mth):
    @wraps(mth)
    def wrapper(instance: 'Dragon', *args, **kwargs):
        if hasattr(instance, 'is_alive'):
            if instance.is_alive():
                return mth(instance, *args, **kwargs)
        else:
            return mth(instance, *args, **kwargs)
    return wrapper


def if_dead(mth):
    @wraps(mth)
    def wrapper(instance: 'Dragon', *args, **kwargs):
        if hasattr(instance, 'is_dead'):
            if instance.is_dead():
                return mth(instance, *args, **kwargs)
        else:
            return mth(instance, *args, **kwargs)
    return wrapper

# Point
class HasPosition:
    position_x: int
    position_y: int

    def __init__(self, x: int, y: int) -> None:
        self.position_x = x
        self.position_y = y

    @if_alive
    def position_set(self, *, x: int, y: int) -> None:  # noqa
        self.position_x = x
        self.position_y = y

    def position_change(self, *, left: int = 0, right: int = 0,
                        down: int = 0, up: int = 0) -> None:
        current_x, current_y = self.position_get()
        new_x = current_x + right - left
        new_y = current_y + down - up
        self.position_set(x=new_x, y=new_y)  # noqa

    def position_get(self):
        return self.position_x, self.position_y


class Status(Enum):
    ALIVE: ClassVar[str] = 'alive'
    DEAD: ClassVar[str] = 'dead'


class Drop(NamedTuple):
    position: tuple[int,int]
    gold: int


# CanDamage
#   DAMAGE_MIN
#   DAMAGE_MAX
#   def damage_make()

# HasGold
#   gold
#   GOLD_MIN
#   GOLD_MAX

# HasHealth
#   health
#   HEALTH_MIN
#   HEALTH_MAX
#   is_alive()
#   is_dead()
#   _make_dead()
#   take_damage()
#   update_status()

# HasTexture
#   texture: str
#   TEXTURE_ALIVE
#   TEXTURE_DEAD
#   _update_texture()

class Dragon(HasPosition):
    DAMAGE_MAX: ClassVar[int] = 20
    DAMAGE_MIN: ClassVar[int] = 5
    GOLD_MAX: ClassVar[int] = 100
    GOLD_MIN: ClassVar[int] = 1
    HEALTH_MAX: ClassVar[int] = 100
    HEALTH_MIN: ClassVar[int] = 50
    TEXTURE_ALIVE: ClassVar[str] = 'img/dragon/alive.png'
    TEXTURE_DEAD: ClassVar[str] = 'img/dragon/dead.png'

    def __init__(self, name: str, /,  # noqa
                 *, position_x: int = 0, position_y: int = 0) -> None:
        self.name = name
        self.status = Status.ALIVE
        self.texture = self.TEXTURE_ALIVE
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)
        self.position_set(x=position_x, y=position_y)  # noqa

    class IsDead(Exception):
        pass

    @if_alive
    def make_damage(self) -> int:
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    @if_alive
    def take_damage(self, damage: int, /):
        self.health -= damage
        if self.is_dead():
            self._make_dead()  # noqa

    @if_dead
    def _make_dead(self):
        self.texture = self.TEXTURE_DEAD
        self.status = Status.DEAD
        raise self.IsDead

    def is_alive(self):
        return not self.is_dead()

    def is_dead(self):
        return self.health <= 0

    @if_dead
    def get_drop(self) -> Drop:
        gold, self.gold = self.gold, 0
        return Drop(gold=gold, position=self.position_get())


class PositionTest(TestCase):
    def setUp(self) -> None:
        self.point = HasPosition(x=1, y=2)

    def test_position_set_keyword(self):
        self.point.position_set(x=10, y=20)  # noqa
        self.assertEqual(self.point.position_x, 10)
        self.assertEqual(self.point.position_y, 20)

    def test_position_set_positional(self):
        with self.assertRaises(TypeError):
            self.point.position_set(10, 20)  # noqa

    def test_position_change_left(self):
        self.point.position_change(left=1)  # noqa
        self.assertEqual(self.point.position_x, 0)
        self.assertEqual(self.point.position_y, 2)

    def test_position_change_right(self):
        self.point.position_change(right=1)  # noqa
        self.assertEqual(self.point.position_x, 2)
        self.assertEqual(self.point.position_y, 2)

    def test_position_change_up(self):
        self.point.position_change(up=1)  # noqa
        self.assertEqual(self.point.position_x, 1)
        self.assertEqual(self.point.position_y, 1)

    def test_position_change_down(self):
        self.point.position_change(down=1)  # noqa
        self.assertEqual(self.point.position_x, 1)
        self.assertEqual(self.point.position_y, 3)

    def test_position_change_vertical(self):
        self.point.position_change(up=1, down=2)  # noqa
        self.assertEqual(self.point.position_x, 1)
        self.assertEqual(self.point.position_y, 3)

    def test_position_change_horizontal(self):
        self.point.position_change(left=1, right=2)  # noqa
        self.assertEqual(self.point.position_x, 2)
        self.assertEqual(self.point.position_y, 2)

    def test_position_change_all(self):
        self.point.position_change(left=1, right=2, down=3, up=4)  # noqa
        self.assertEqual(self.point.position_x, 2)
        self.assertEqual(self.point.position_y, 1)

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
        self.assertEqual(current_x, 1)
        self.assertEqual(current_y, 2)





class DragonTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski', position_x=1, position_y=2)

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

    def test_damage_make(self):
        dmg = self.dragon.make_damage()  # noqa
        self.assertIn(dmg, range(Dragon.DAMAGE_MIN, Dragon.DAMAGE_MAX+1))

    def test_damage_take_positional(self):
        try:
            self.dragon.take_damage(1)  # noqa
        except Exception:
            raise AssertionError('TypeError raised')

    def test_damage_take_keyword(self):
        with self.assertRaises(TypeError):
            self.dragon.take_damage(damage=1)  # noqa

    def test_damage_take_positive(self):
        self.dragon.health = 3
        self.dragon.take_damage(2)  # noqa
        self.assertEqual(self.dragon.health, 1)

    def test_damage_take_zero(self):
        self.dragon.health = 2
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(2)  # noqa

    def test_damage_take_negative(self):
        self.dragon.health = 1
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(2)  # noqa

    def test_health_init(self):
        self.assertIn(self.dragon.health, range(Dragon.HEALTH_MIN, Dragon.HEALTH_MAX+1))

    def test_texture_init(self):
        self.assertEqual(self.dragon.texture, Dragon.TEXTURE_ALIVE)

    def test_texture_alive(self):
        self.dragon.health = 2
        self.dragon.take_damage(1)  # noqa
        self.assertEqual(self.dragon.texture, Dragon.TEXTURE_ALIVE)

    def test_texture_dead_zero(self):
        self.dragon.health = 2
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(2)  # noqa
        self.assertEqual(self.dragon.texture, Dragon.TEXTURE_DEAD)

    def test_texture_dead_negative(self):
        self.dragon.health = 2
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(3)  # noqa
        self.assertEqual(self.dragon.texture, Dragon.TEXTURE_DEAD)

    def test_status_init(self):
        self.assertEqual(self.dragon.status, Status.ALIVE)

    def test_status_alive(self):
        self.dragon.health = 2
        self.dragon.take_damage(1)  # noqa
        self.assertEqual(self.dragon.status, Status.ALIVE)

    def test_status_dead_zero(self):
        self.dragon.health = 2
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(2)  # noqa
        self.assertEqual(self.dragon.status, Status.DEAD)

    def test_status_dead_negative(self):
        self.dragon.health = 2
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(3)  # noqa
        self.assertEqual(self.dragon.status, Status.DEAD)

    def test_health_isalive_positive(self):
        self.dragon.health = 1
        self.assertTrue(self.dragon.is_alive())

    def test_health_isalive_zero(self):
        self.dragon.health = 0
        self.assertFalse(self.dragon.is_alive())

    def test_health_isalive_negative(self):
        self.dragon.health = -1
        self.assertFalse(self.dragon.is_alive())

    def test_health_isdead_positive(self):
        self.dragon.health = 1
        self.assertFalse(self.dragon.is_dead())

    def test_health_isdead_zero(self):
        self.dragon.health = 0
        self.assertTrue(self.dragon.is_dead())

    def test_health_isdead_negative(self):
        self.dragon.health = -1
        self.assertTrue(self.dragon.is_dead())

    def test_health_make_dead(self):
        self.dragon.health = 0
        with self.assertRaises(self.dragon.IsDead):
            self.dragon._make_dead()  # noqa
        self.assertEqual(self.dragon.texture, Dragon.TEXTURE_DEAD)
        self.assertEqual(self.dragon.status, Status.DEAD)
