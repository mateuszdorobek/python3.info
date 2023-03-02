import os
from datetime import date
from unittest import TestCase


# Operating system will control this env variable
os.environ['STAGE'] = 'test'


STAGE = os.getenv('STAGE', default='production')

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY
YEAR = 365.25 * DAY
MONTH = YEAR / 12


def today():
    if STAGE == 'test':
        return date(2000, 1, 1)
    else:
        return date.today()


class User:
    username: str
    password: str
    email: str | None
    birthday: date | None
    authenticated: bool

    def __init__(self, *,
                 username: str,
                 password: str,
                 email: str | None = None,
                 birthday: str | None = None,
                 ) -> None:
        self.username = username
        self.password = password
        self.email = email
        self.birthday = date.fromisoformat(birthday) if birthday else None
        self.authenticated = False

    @property
    def age(self) -> int:
        years = (today() - self.birthday).total_seconds() / YEAR
        return int(years)

    def __str__(self) -> str:
        return f'{self.username}'

    def __repr__(self) -> str:
        clsname = self.__class__.__name__
        username = self.username
        return f'{clsname}({username=})'

    def login(self) -> None:
        self.authenticated = True


class UserInitTest(TestCase):

    def test_init_user_keyword(self):
        user = User(username='mwatney', password='Ares3')
        self.assertEqual(user.username, 'mwatney')
        self.assertEqual(user.password, 'Ares3')

    def test_init_user_positional(self):
        with self.assertRaises(TypeError):
            User('mwatney', 'Ares3')  # noqa

    def test_init_email(self):
        user = User(username='mwatney', password='Ares3', email='mwatney@nasa.gov')
        self.assertEqual(user.email, 'mwatney@nasa.gov')

    def test_init_birthday(self):
        user = User(username='mwatney', password='Ares3', birthday='1969-07-21')
        self.assertEqual(user.birthday, date(1969, 7, 21))

    def test_init_annotations(self):
        user = User(username='mwatney', password='Ares3')
        attributes = sorted(vars(user).keys())
        annotations = sorted(User.__annotations__.keys())
        self.assertListEqual(annotations, attributes)


class UserFeatureTest(TestCase):
    def setUp(self) -> None:
        self.user = User(
            username='mwatney',
            password='Ares3',
            email='mwatney@nasa.gov',
            birthday='1969-07-21',
        )

    def test_age(self):
        self.assertEqual(self.user.age, 30)

    def test_str(self):
        self.assertEqual(str(self.user), 'mwatney')

    def test_repr(self):
        self.assertEqual(repr(self.user), "User(username='mwatney')")


class UserAuthTest(TestCase):
    def setUp(self) -> None:
        self.user = User(
            username='mwatney',
            password='Ares3',
            email='mwatney@nasa.gov',
            birthday='1969-07-21',
        )

    def test_password_hidden(self):
        self.assertNotIn('password', str(self.user))
        self.assertNotIn('password', repr(self.user))
        self.assertNotIn(self.user.password, str(self.user))
        self.assertNotIn(self.user.password, repr(self.user))

    def test_authenticated_default(self):
        self.assertFalse(self.user.authenticated)

    def test_login(self):
        self.user.authenticated = False
        self.user.login()
        self.assertTrue(self.user.authenticated)
