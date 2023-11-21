# doctest: +SKIP_FILE

#%% README.rst

"""
Dragon
======

Przygotowanie:

>>> from main import Dragon

Stwórz smoka o nazwie "Wawelski"

>>> dragon = Dragon('Wawelski')
"""

#%% main.py
from random import randint


class Dragon:
    name: str

    def __init__(self, name: str, /) -> None:
        self.name = name


#%% tests.py
from unittest import TestCase
from main import Dragon

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
