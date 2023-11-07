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
