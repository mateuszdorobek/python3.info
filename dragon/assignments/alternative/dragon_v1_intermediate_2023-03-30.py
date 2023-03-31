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
...     print(f'{dragon.name} is dead')
...     print(f'Gold: {drop.gold}')
...     print(f'Position: {drop.position}')
Wawelski is dead
Gold: 98
Position: (20, 40)

Smok powinien zginąć na pozycji: x=20, y=40 i zostawić złoto (1-100)
"""
from random import randint
from typing import ClassVar, NamedTuple
from unittest import TestCase



class HasPosition:
    position_x: int
    position_y: int

    def __init__(self, position_x: int, position_y: int) -> None:
        self.position_x = position_x
        self.position_y = position_y

    def position_set(self, *, x: int, y: int) -> None:
        self.position_x = x
        self.position_y = y

    def position_get(self) -> tuple[int,int]:
        return self.position_x, self.position_y

    def position_change(self, *, left: int = 0, right: int = 0, up: int = 0, down: int = 0) -> None:
        current_x, current_y = self.position_get()
        new_x = current_x + right - left
        new_y = current_y + down - up
        self.position_set(x=new_x, y=new_y)


class Drop(NamedTuple):
    gold: int
    position: tuple[int,int]


class Dragon(HasPosition):
    DAMAGE_MAX: ClassVar[int] = 20
    DAMAGE_MIN: ClassVar[int] = 5
    GOLD_MAX: ClassVar[int] = 100
    GOLD_MIN: ClassVar[int] = 1
    HEALTH_MAX: ClassVar[int] = 100
    HEALTH_MIN: ClassVar[int] = 50
    STATUS_ALIVE: ClassVar[str] = 'alive'
    STATUS_DEAD: ClassVar[str] = 'dead'
    TEXTURE_ALIVE: ClassVar[str] = 'img/dragon/alive.png'
    TEXTURE_DEAD: ClassVar[str] = 'img/dragon/dead.png'

    name: str
    gold: int
    health: int
    texture: str
    status: str

    def __init__(self, name: str, /,
                 *, position_x: int = 0, position_y: int = 0,
                 ) -> None:
        if type(name) is not str: raise TypeError  # maybe
        if type(position_x) is not int: raise TypeError  # maybe
        if type(position_y) is not int: raise TypeError  # maybe
        self.name = name
        self.status = self.STATUS_ALIVE
        self.texture = self.TEXTURE_ALIVE
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)
        self.position_set(x=position_x, y=position_y)

    class IsDead(Exception):
        pass

    class IsAlive(Exception):
        pass

    def make_damage(self) -> int:
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    def take_damage(self, damage, /) -> None:
        new_health = self.health - damage
        self.set_health(new_health)

    def set_health(self, value, /) -> None:
        self.health = value
        self._update_texture()
        self._update_status()
        if self.is_dead():
            raise self.IsDead

    def is_dead(self) -> bool:
        return self.health <= 0

    def is_alive(self) -> bool:
        return not self.is_dead()

    def _update_texture(self) -> None:
        if self.is_dead():
            self.texture = self.TEXTURE_DEAD
        else:
            self.texture = self.TEXTURE_ALIVE

    def _update_status(self) -> None:
        if self.is_dead():
            self.status = self.STATUS_DEAD
        else:
            self.status = self.STATUS_ALIVE

    def get_drop(self) -> Drop:
        if self.health > 0:
            raise self.IsAlive
        gold, self.gold = self.gold, 0
        return Drop(gold=gold, position=self.position_get())


class DragonTest(TestCase):
    def test_init_noargs(self):
        with self.assertRaises(TypeError):
            Dragon()  # noqa

    def test_init_name_positional(self):
        dragon = Dragon('Wawelski')
        self.assertEqual(dragon.name, 'Wawelski')

    def test_init_name_type(self):
        with self.assertRaises(TypeError):
            Dragon(1)  # noqa
        with self.assertRaises(TypeError):
            Dragon(1.0)  # noqa
        with self.assertRaises(TypeError):
            Dragon(True)  # noqa
        with self.assertRaises(TypeError):
            Dragon([])  # noqa
        with self.assertRaises(TypeError):
            Dragon({})  # noqa

    def test_init_name_keyword(self):
        with self.assertRaises(TypeError):
            Dragon(name='Wawelski')  # noqa

    def test_init_position_positional(self):
        with self.assertRaises(TypeError):
            Dragon('Wawelski', 1, 2)  # noqa
        with self.assertRaises(TypeError):
            Dragon('Wawelski', 1, position_y=2)  # noqa

    def test_init_position_keyword(self):
        dragon = Dragon('Wawelski', position_x=1, position_y=2)
        self.assertEqual(dragon.position_x, 1)
        self.assertEqual(dragon.position_y, 2)

    def test_init_position_type(self):
        with self.assertRaises(TypeError):
            Dragon('Wawelski', position_x=1.0, position_y=2)  # noqa
            Dragon('Wawelski', position_x=1, position_y=2.0)   # noqa
        with self.assertRaises(TypeError):
            Dragon('Wawelski', position_x='1', position_y=2)  # noqa
            Dragon('Wawelski', position_x=1, position_y='2')   # noqa
        with self.assertRaises(TypeError):
            Dragon('Wawelski', position_x=[1], position_y=2)  # noqa
            Dragon('Wawelski', position_x=1, position_y=[2])   # noqa

    def test_init_annotations(self):
        current = Dragon.__init__.__annotations__
        expected = {'name': str, 'position_x': int, 'position_y': int, 'return': None}
        self.assertDictEqual(current, expected)


class PositionTest(TestCase):
    def setUp(self) -> None:
        self.current = HasPosition(position_x=10, position_y=20)

    def test_position_set_noargs(self):
        with self.assertRaises(TypeError):
            self.current.position_set()  # noqa
        with self.assertRaises(TypeError):
            self.current.position_set(1)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_set(x=1)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_set(y=1)  # noqa

    def test_position_set_positional(self):
        with self.assertRaises(TypeError):
            self.current.position_set(1, 2)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_set(1, y=2)  # noqa

    def test_position_set_keyword(self):
        self.current.position_set(x=1, y=2)
        self.assertEqual(self.current.position_x, 1)
        self.assertEqual(self.current.position_y, 2)

    def test_position_set_annotations(self):
        current = self.current.position_set.__annotations__
        expected = {'x': int, 'y': int, 'return': None}
        self.assertDictEqual(current, expected)

    def test_position_change_positional(self):
        with self.assertRaises(TypeError):
            self.current.position_change(1)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2, 3)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2, 3, 4)  # noqa

    def test_position_change_left_positional(self):
        self.current.position_change(left=1)
        self.assertEqual(self.current.position_x, 9)
        self.assertEqual(self.current.position_y, 20)

    def test_position_change_right_positional(self):
        self.current.position_change(right=1)
        self.assertEqual(self.current.position_x, 11)
        self.assertEqual(self.current.position_y, 20)

    def test_position_change_up_positional(self):
        self.current.position_change(up=1)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 19)

    def test_position_change_down_positional(self):
        self.current.position_change(down=1)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 21)

    def test_position_change_horizontal_positional(self):
        self.current.position_change(left=1, right=2)
        self.assertEqual(self.current.position_x, 11)
        self.assertEqual(self.current.position_y, 20)

    def test_position_change_vertical_positional(self):
        self.current.position_change(up=1, down=2)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 21)

    def test_position_change_omnidirectional_positional(self):
        self.current.position_change(left=1, right=2, up=3, down=4)
        self.assertEqual(self.current.position_x, 11)
        self.assertEqual(self.current.position_y, 21)

    def test_position_get(self):
        x, y = self.current.position_get()
        self.assertEqual(x, 10)
        self.assertEqual(y, 20)


class TextureTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski')

    def test_texture_init(self):
        self.assertIsInstance(self.dragon.texture, str)
        self.assertIn(self.dragon.texture, 'img/dragon/alive.png')

    def test_texture_when_health_positive(self):
        self.dragon.set_health(1)
        self.assertEqual(self.dragon.texture, 'img/dragon/alive.png')

    def test_texture_when_health_zero(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.set_health(0)
        self.assertEqual(self.dragon.texture, 'img/dragon/dead.png')

    def test_texture_when_health_negative(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.set_health(-1)
        self.assertEqual(self.dragon.texture, 'img/dragon/dead.png')

    def test_texture_update_when_health_positive(self):
        self.dragon.health = 1
        self.dragon._update_texture()
        self.assertEqual(self.dragon.texture, 'img/dragon/alive.png')

    def test_texture_update_when_health_positive(self):
        self.dragon.health = 0
        self.dragon._update_texture()
        self.assertEqual(self.dragon.texture, 'img/dragon/dead.png')

    def test_texture_update_when_health_positive(self):
        self.dragon.health = -1
        self.dragon._update_texture()
        self.assertEqual(self.dragon.texture, 'img/dragon/dead.png')


class StatusTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski')

    def test_status_init(self):
        self.assertIsInstance(self.dragon.status, str)
        self.assertIn(self.dragon.status, 'alive')

    def test_status_health_positive(self):
        self.dragon.set_health(1)
        self.assertEqual(self.dragon.status, 'alive')

    def test_status_health_zero(self):
        self.dragon.set_health(0)
        self.assertEqual(self.dragon.status, 'dead')

    def test_status_health_negative(self):
        self.dragon.set_health(-1)
        self.assertEqual(self.dragon.status, 'dead')

    def test_status_health_positive(self):
        self.dragon.health = 1
        self.dragon._update_status()
        self.assertEqual(self.dragon.status, 'alive')

    def test_status_health_zero(self):
        self.dragon.health = 0
        self.dragon._update_status()
        self.assertEqual(self.dragon.status, 'dead')

    def test_status_health_negative(self):
        self.dragon.health = -1
        self.dragon._update_status()
        self.assertEqual(self.dragon.status, 'dead')


class HealthTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski')

    def test_health_init(self):
        self.assertIsInstance(self.dragon.health, int)
        self.assertIn(self.dragon.health, range(50,101))

    def test_health_set_positional(self):
        self.dragon.health = 2
        self.dragon.set_health(1)
        self.assertEqual(self.dragon.health, 1)

    def test_health_set_keyword(self):
        with self.assertRaises(TypeError):
            self.dragon.set_health(value=1)  # noqa

    def test_health_isdead_when_health_positive(self):
        self.dragon.health = 1
        self.assertFalse(self.dragon.is_dead())

    def test_health_isdead_when_health_zero(self):
        self.dragon.health = 0
        self.assertTrue(self.dragon.is_dead())

    def test_health_isdead_when_health_negative(self):
        self.dragon.health = -1
        self.assertTrue(self.dragon.is_dead())

    def test_health_isalive_when_health_positive(self):
        self.dragon.health = 1
        self.assertTrue(self.dragon.is_alive())

    def test_health_isalive_when_health_zero(self):
        self.dragon.health = 0
        self.assertFalse(self.dragon.is_alive())

    def test_health_isalive_when_health_negative(self):
        self.dragon.health = -1
        self.assertFalse(self.dragon.is_alive())


class DamageTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski')

    def test_damage_make(self):
        dmg = self.dragon.make_damage()
        self.assertIsInstance(dmg, int)
        self.assertIn(dmg, range(5, 21))

    def test_damage_take_keyword(self):
        with self.assertRaises(TypeError):
            self.dragon.take_damage(damage=1)  # noqa

    def test_damage_take_positional(self):
        self.dragon.set_health(3)
        self.dragon.take_damage(2)
        self.assertEqual(self.dragon.health, 1)


class DropTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski')

    def test_drop_when_alive(self):
        self.dragon.health = 1
        with self.assertRaises(self.dragon.IsAlive):
            self.dragon.get_drop()

    def test_drop_when_dead(self):
        self.dragon.health = -1
        drop = self.dragon.get_drop()
        ...
