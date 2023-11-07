from random import seed, randint
from unittest import TestCase


class HasHealth:
    HEALTH_MIN = 1
    HEALTH_MAX = 100
    health: int

    def __init__(self):
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)

    class IsDead(Exception):
        pass

    def take_damage(self, damage):
        self.set_health(self.health-damage)

    def is_dead(self):
        return self.health <= 0

    def set_health(self, value):
        self.health = value
        if self.is_dead():
            raise self.IsDead


class HasHealthTest(TestCase):
    def setUp(self) -> None:
        seed(0)
        self.obj = HasHealth()

    def test_health_default(self):
        self.assertEqual(self.obj.health, 50)

    def test_health_range(self):
        self.assertEqual(self.obj.HEALTH_MIN, 1)
        self.assertEqual(self.obj.HEALTH_MAX, 100)

    def test_health_isdead_when_health_zero(self):
        with self.assertRaises(self.obj.IsDead):
            self.obj.set_health(0)
        self.assertTrue(self.obj.is_dead())

    def test_health_isdead_when_health_negative(self):
        with self.assertRaises(self.obj.IsDead):
            self.obj.set_health(-1)
        self.assertTrue(self.obj.is_dead())

    def test_health_take_damage(self):
        self.obj.set_health(2)
        self.obj.take_damage(1)
        self.assertEqual(self.obj.health, 1)
