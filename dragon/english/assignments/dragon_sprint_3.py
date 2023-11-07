"""
Dragon game
===========
>>> from dragon import Dragon  # doctest: +SKIP
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

>>> dragon.move(left=10, down=20)

Przesuń smoka w prawo o 15 i w górę o 5

>>> dragon.move(left=10, down=20)

Przesuń smoka w dół o 5

>>> dragon.move(left=10, down=20)
"""
from unittest import TestCase


class Dragon:
    def __init__(self, name, /, *, position_x=0, position_y=0):
        self.name = name
        self.position_x = position_x
        self.position_y = position_y

    def set_position(self, *, x, y):
        self.position_x = x
        self.position_y = y

    def move(self, *, left=0, right=0, up=0, down=0):
        self.position_x += right - left
        self.position_y += down - up


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
