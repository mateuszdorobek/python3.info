from random import randint, seed
from unittest import TestCase


class MakesDamage:
    DAMAGE_MIN = 0
    DAMAGE_MAX = 100

    def make_damage(self):
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)


class MakesDamageTest(TestCase):
    def setUp(self) -> None:
        self.character = MakesDamage()

    def test_damage_make(self):
        seed(0)
        dmg = self.character.make_damage()
        self.assertIsInstance(dmg, int)
        self.assertEqual(dmg, 49)

    def test_damage_range(self):
        self.assertEqual(self.character.DAMAGE_MIN, 0)
        self.assertEqual(self.character.DAMAGE_MAX, 100)
