from datetime import date
from unittest import TestCase
from os import getenv


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY
YEAR = 365.25 * DAY
MONTH = YEAR / 12


def today():
    env = getenv('ENVIRONMENT', default='prod')
    if env == 'test':
        return date(2000, 1, 1)
    else:
        return date.today()


class User:
    firstname: str
    lastname: str
    birthday: date | None

    def __init__(self, firstname: str, lastname: str, /,
                 *, birthday: str | None = None,
                 ) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = date.fromisoformat(birthday) if birthday else None

    @property
    def age(self) -> int:
        days = (today() - self.birthday).total_seconds()
        return int(days/YEAR)

    def say_hello(self) -> str:
        return 'hello'

    def say_goodbye(self) -> str:
        return 'goodbye'

    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname}'

    def __repr__(self) -> str:
        clsname = self.__class__.__name__
        firstname = f"'{self.firstname}'"
        lastname = f"'{self.lastname}'"
        birthday = self.birthday.strftime('%Y-%m-%d')
        return f'{clsname}({firstname}, {lastname}, {birthday=})'


class UserInitTest(TestCase):

    def test_init_noname(self):
        with self.assertRaises(TypeError):
            User()  # noqa
        with self.assertRaises(TypeError):
            User('Mark')  # noqa
        with self.assertRaises(TypeError):
            User('Watney')  # noqa
        with self.assertRaises(TypeError):
            User(lastname='Watney')  # noqa
        with self.assertRaises(TypeError):
            User(lastname='Watney')  # noqa

    def test_init_firstname_and_lastname_positional(self):
        user = User('Mark', 'Watney')
        self.assertIsInstance(user, User)
        self.assertEqual(user.firstname, 'Mark')
        self.assertEqual(user.lastname, 'Watney')

    def test_init_firstname_and_lastname_keyword(self):
        with self.assertRaises(TypeError):
            User(firstname='Mark', lastname='Watney')  # noqa

    def test_init_birthday_positional(self):
        with self.assertRaises(TypeError):
            User('Mark', 'Watney', '1969-07-21')  # noqa

    def test_init_birthday_keyword(self):
        user = User('Mark', 'Watney', birthday='1969-07-21')
        self.assertIsInstance(user.birthday, date)
        self.assertEqual(user.birthday, date(1969, 7, 21))


class UserFeatureTest(TestCase):

    def setUp(self) -> None:
        self.user = User('Mark', 'Watney', birthday='1969-07-21')

    def test_age(self):
        self.assertEqual(self.user.age, 30)

    def test_say_hello(self):
        self.assertEqual(self.user.say_hello(), 'hello')

    def test_say_goodbye(self):
        self.assertEqual(self.user.say_goodbye(), 'goodbye')

    def test_str(self):
        self.assertEqual(str(self.user), 'Mark Watney')

    def test_repr(self):
        self.assertEqual(repr(self.user), "User('Mark', 'Watney', birthday='1969-07-21')")
