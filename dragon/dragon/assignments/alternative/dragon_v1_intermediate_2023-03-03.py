"""
>>> from random import seed; seed(0)
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 11), 'Python 3.11+ required'

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
...     print(f'{dragon} is dead')
...     print(f'Position: {drop.position}')
...     print(f'Gold: {drop.gold}')
Wawelski is dead
Position: x=20, y=40
Gold: 50

Smok powinien zginąć na pozycji: x=20, y=40 i zostawić złoto (1-100)

"""
from enum import StrEnum, auto
from random import randint
from typing import ClassVar, NamedTuple
from unittest import TestCase


class Point(NamedTuple):
    x: int
    y: int

    def __str__(self):
        return f'x={self.x}, y={self.y}'


class HasPosition:
    position: Point

    def __init__(self, position_x: int = 0, position_y: int = 0):
        self.position_set(x=position_x, y=position_y)

    def position_set(self, *, x: int, y: int) -> None:
        self.position = Point(x, y)

    def position_get(self) -> Point:
        return self.position

    def position_change(self, *,
                        left: int = 0, right: int = 0,
                        up: int = 0, down: int = 0) -> None:
        if not any([left,right,up,down]):
            raise TypeError
        current = self.position_get()
        new_x = current.x + right - left
        new_y = current.y + down - up
        self.position_set(x=new_x, y=new_y)


class Status(StrEnum):
    ALIVE = auto()
    DEAD = auto()


class Drop(NamedTuple):
    gold: int
    position: Point


class Dragon(HasPosition):
    DAMAGE_MAX: ClassVar[int] = 20
    DAMAGE_MIN: ClassVar[int] = 5
    GOLD_MAX: ClassVar[int] = 100
    GOLD_MIN: ClassVar[int] = 1
    HEALTH_MAX: ClassVar[int] = 100
    HEALTH_MIN: ClassVar[int] = 50
    TEXTURE_ALIVE: ClassVar[str] = 'img/dragon/alive.png'
    TEXTURE_DEAD: ClassVar[str] = 'img/dragon/dead.png'
    health = property()

    name: str
    texture: str
    gold: int
    status: str
    _health: int

    def __init__(self, name: str, /,
                 *, position_x: int = 0, position_y: int = 0,
                 ) -> None:
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self.name = name
        self.status = Status.ALIVE
        self.texture = self.TEXTURE_ALIVE
        self.position_set(x=position_x, y=position_y)

    class IsDead(Exception):
        pass

    class IsAlive(Exception):
        pass

    @health.getter
    def health(self) -> None:
        return self._health

    @health.setter
    def health(self, value) -> IsDead | None:
        self._health = value
        if self.is_dead():
            self._die()

    def _die(self) -> IsDead:
        self.status = Status.DEAD
        self.texture = self.TEXTURE_DEAD
        raise self.IsDead

    def make_damage(self) -> int:
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    def take_damage(self, damage) -> None:
        self.health -= damage

    def __str__(self) -> str:
        return f'{self.name}'

    def get_drop(self) -> Drop | IsAlive:
        if self.is_alive():
            raise self.IsAlive
        gold, self.gold = self.gold, 0
        return Drop(gold=gold, position=self.position_get())

    def is_alive(self) -> bool:
        return not self.is_dead()

    def is_dead(self) -> bool:
        return self.health <= 0


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

    def test_init_position_default(self):
        dragon = Dragon('Name')
        self.assertEqual(dragon.position, Point(x=0, y=0))

    def test_init_position_keyword(self):
        dragon = Dragon('Name', position_x=1, position_y=2)
        self.assertEqual(dragon.position, Point(x=1, y=2))

    def test_init_position_positional(self):
        with self.assertRaises(TypeError):
            Dragon('Name', 1, position_y=2)  # noqa
        with self.assertRaises(TypeError):
            Dragon('Name', 1, 2)  # noqa


class DragonTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Name')

    def test_str(self):
        self.assertEqual(str(self.dragon), 'Name')


class PositionTest(TestCase):
    def setUp(self) -> None:
        self.current = HasPosition(position_x=10, position_y=20)

    def test_position_set_default(self):
        with self.assertRaises(TypeError):
            self.current.position_set()

    def test_position_set_positional(self):
        with self.assertRaises(TypeError):
            self.current.position_set(1, y=2)
        with self.assertRaises(TypeError):
            self.current.position_set(1, 2)

    def test_position_set_keyword(self):
        self.current.position_set(x=10, y=20)
        self.assertEqual(self.current.position, Point(x=10, y=20))

    def test_position_change_default(self):
        with self.assertRaises(TypeError):
            self.current.position_change()  # noqa

    def test_position_change_positional(self):
        with self.assertRaises(TypeError):
            self.current.position_change(1)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2, 3)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2, 3, 4)  # noqa

    def test_position_change_keyword_left(self):
        self.current.position_change(left=1)
        self.assertEqual(self.current.position, Point(x=9, y=20))

    def test_position_change_keyword_right(self):
        self.current.position_change(right=1)
        self.assertEqual(self.current.position, Point(x=11, y=20))

    def test_position_change_keyword_up(self):
        self.current.position_change(up=1)
        self.assertEqual(self.current.position, Point(x=10, y=19))

    def test_position_change_keyword_down(self):
        self.current.position_change(down=1)
        self.assertEqual(self.current.position, Point(x=10, y=21))

    def test_position_change_keyword_horizontal(self):
        self.current.position_change(left=1, right=2)
        self.assertEqual(self.current.position, Point(x=11, y=20))

    def test_position_change_keyword_vertical(self):
        self.current.position_change(up=1, down=2)
        self.assertEqual(self.current.position, Point(x=10, y=21))

    def test_position_change_keyword_omnidirectional(self):
        self.current.position_change(left=1, right=2, up=3, down=4)
        self.assertEqual(self.current.position, Point(x=11, y=21))

    def test_position_get(self):
        current = self.current.position_get()
        self.assertEqual(current, Point(x=10, y=20))


class HealthTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Name')

    def test_health_init(self):
        self.assertIn(self.dragon.health, range(50,101))

    def test_health_positive(self):
        self.dragon.health = 1
        self.assertTrue(self.dragon.is_alive())
        self.assertFalse(self.dragon.is_dead())

    def test_health_zero(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = 0
        self.assertFalse(self.dragon.is_alive())
        self.assertTrue(self.dragon.is_dead())

    def test_health_negative(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = -1
        self.assertFalse(self.dragon.is_alive())
        self.assertTrue(self.dragon.is_dead())

    def test_die(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon._die()
        self.assertEqual(self.dragon.status, 'dead')
        self.assertEqual(self.dragon.texture, 'img/dragon/dead.png')


class DamageTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Name')

    def test_damage_make(self):
        dmg = self.dragon.make_damage()
        self.assertIn(dmg, range(5,21))

    def test_damage_take(self):
        self.dragon.health = 10
        self.dragon.take_damage(1)
        self.assertEqual(self.dragon.health, 9)


class GoldTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Name')

    def test_gold_init(self):
        self.assertIn(self.dragon.gold, range(1,101))


class Texture(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Name')

    def test_texture_init(self):
        self.assertEqual(self.dragon.texture, 'img/dragon/alive.png')

    def test_texture_alive(self):
        self.dragon.health = 1
        self.assertEqual(self.dragon.texture, 'img/dragon/alive.png')

    def test_texture_dead(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = -1
        self.assertEqual(self.dragon.texture, 'img/dragon/dead.png')


class StatusTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Name')

    def test_status_init(self):
        self.assertEqual(self.dragon.status, 'alive')

    def test_status_alive(self):
        self.dragon.health = 1
        self.assertEqual(self.dragon.status, 'alive')

    def test_status_dead(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = -1
        self.assertEqual(self.dragon.status, 'dead')


class DropTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Name')

    def test_drop_alive(self):
        self.dragon.health = 1
        with self.assertRaises(self.dragon.IsAlive):
            self.dragon.get_drop()

    def test_drop_dead(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = -1
        drop = self.dragon.get_drop()
        self.assertIsInstance(drop, Drop)


