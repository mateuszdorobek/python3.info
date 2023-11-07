from random import seed, randint
from typing import NamedTuple
from unittest import TestCase


class Drop(NamedTuple):
    gold: int


class HasDrop:
    GOLD_MIN = 0
    GOLD_MAX = 1
    gold: int

    def __init__(self):
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)

    def get_drop(self):
        gold, self.gold = self.gold, 0
        return Drop(gold=gold)


class HasDropTest(TestCase):
    def setUp(self) -> None:
        seed(0)
        self.drop = HasDrop()

    def test_drop_get(self):
        drop = self.drop.get_drop()
        self.assertEqual(drop.gold, 1)

    def test_drop_gold_default(self):
        self.assertEqual(self.drop.gold, 1)

    def test_drop_gold_range(self):
        self.assertEqual(self.drop.GOLD_MIN, 0)
        self.assertEqual(self.drop.GOLD_MAX, 1)
