from datetime import date
from unittest import TestCase


class User:
    def __init__(self, name, /, *, birthday=None):
        self.name = name
        self.birthday = date.fromisoformat(birthday) if birthday else None

    def age(self):
        YEAR = 365.25
        today = date.today()
        age = (today - self.birthday).days / YEAR
        return round(age)


class UserTest(TestCase):

    # Initialization tests

    def test_init_noname(self):
        with self.assertRaises(TypeError):
            User()  # noqa

    def test_init_name_positional(self):
        u = User('Mark')
        self.assertEqual(u.name, 'Mark')

    def test_init_name_keyword(self):
        with self.assertRaises(TypeError):
            User(name='Mark')  # noqa

    def test_init_birthday_positional(self):
        with self.assertRaises(TypeError):
            User('Mark', '1969-07-21')  # noqa

    def test_init_birthday_keyword(self):
        u = User('Mark', birthday='1969-07-21')
        self.assertEqual(u.birthday, date(1969, 7, 21))

    # Other tests

    def setUp(self) -> None:
        self.user = User('Mark', birthday='1969-07-21')

    def test_age(self):
        today = date(2000, 1, 1)
        self.assertEqual(self.user.age(), 53)
