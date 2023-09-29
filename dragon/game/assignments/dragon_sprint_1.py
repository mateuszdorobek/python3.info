"""
Dragon game
===========
Stwórz smoka o nazwie "Wawelski"
>>> dragon = Dragon('Wawelski')
"""
from unittest import TestCase


class Dragon:
    def __init__(self, name, /):
        self.name = name



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
