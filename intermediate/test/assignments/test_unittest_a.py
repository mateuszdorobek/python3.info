"""
* Assignment: DevOps Unittest Rectangle
* Complexity: medium
* Lines of code: 100 lines
* Time: 21 min

English:
    1. Write unittest for `Rectangle`
    2. Run unittest - all must succeed

Polish:
    1. Napisz testy jednostkowe dla `Rectangle`
    2. Uruchom unittest - wszystkie muszą się powieść
"""

import unittest


class Rectangle:

    def __init__(self, a, b):
        self.side_a = a
        self.side_b = b

        if a <= 0 or b <= 0:
            raise ValueError('Side length must be positive')

    def area(self) -> int:
        return self.side_a * self.side_b

    def circumference(self) -> int:
        return (self.side_a + self.side_b) * 2

    def __str__(self):
        return f'Rectangle({self.side_a}, {self.side_b})'


# Solution
class RectangleTest(unittest.TestCase):

    def setUp(self):
        self.rectangle_1_by_4 = Rectangle(1, 4)
        self.rectangle_2_by_5 = Rectangle(2, 5)

    def test_bok_a(self):
        self.assertEquals(self.rectangle_1_by_4.side_a, 1)
        self.assertEquals(self.rectangle_2_by_5.side_a, 2)

    def test_bok_b(self):
        self.assertEquals(self.rectangle_1_by_4.side_b, 4)
        self.assertEquals(self.rectangle_2_by_5.side_b, 5)

    def test_negative_side_a(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 5)

    def test_negative_side_b(self):
        with self.assertRaises(ValueError):
            Rectangle(5, -1)

    def test_zero_side_a(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1)

    def test_zero_side_b(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_abnormal_side(self):
        with self.assertRaises(TypeError):
            Rectangle('one', 0)

    def test_area(self):
        self.assertEquals(Rectangle(2, 5).area(), 10)
        self.assertEquals(Rectangle(1, 4).area(), 4)

    def test_pole_setup(self):
        self.assertEquals(self.rectangle_1_by_4.area(), 4)
        self.assertEquals(self.rectangle_2_by_5.area(), 10)

    def test_circumference_positive(self):
        self.assertEquals(Rectangle(2, 5).circumference(), 14)
        self.assertEquals(Rectangle(1, 4).circumference(), 10)

    def test_circumference_negative(self):
        self.assertNotEquals(Rectangle(2, 5).circumference(), 10)
        self.assertNotEquals(Rectangle(1, 4).circumference(), 5)
