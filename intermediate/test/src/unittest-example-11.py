"""
>>> mark = User('mwatney', password='Ares3', birthday='1969-07-21')

>>> mark.say_hello()
'hello'

>>> mark.get_age()
54

>>> mark.say_secret()
Traceback (most recent call last):
PermissionError: Not authenticated

>>> mark.login(username='mwatney', password='Ares3')

>>> mark.say_secret()
'myVoiceIsMyPassword'
"""

import datetime
from datetime import date
from hashlib import sha256
from typing import NoReturn
from unittest import TestCase, mock

YEAR = 365.25


def encrypt(string) -> str:
    in_bytes = string.encode()
    return sha256(in_bytes).hexdigest()


class User:
    username: str
    password: str | None
    birthday: date | None
    authenticated: bool

    def __init__(self, username: str, /,
                 *, password: str | None = None,
                 birthday: str | None = None,
                 ) -> None:
        self.username = username
        self.password = encrypt(password) if password else None
        self.birthday = date.fromisoformat(birthday) if birthday else None
        self.authenticated = False

    def say_hello(self) -> str:
        return 'hello'

    def get_age(self) -> int:
        today = datetime.date.today()
        days = (today - self.birthday).days
        return int(days / YEAR)

    def __str__(self) -> str:
        return f'{self.username}'

    def __repr__(self) -> str:
        clsname = self.__class__.__name__
        username = self.username
        return f"{clsname}('{username}')"

    def login(self, username: str, password: str) -> None | NoReturn:
        valid_username = self.username == username
        valid_password = self.password == encrypt(password)
        if valid_username and valid_password:
            self.authenticated = True
        else:
            raise PermissionError('Incorrect username or/and password')

    def say_secret(self) -> str | NoReturn:
        if self.authenticated:
            return 'myVoiceIsMyPassword'
        else:
            raise PermissionError('Not authenticated')


class UserInitTest(TestCase):
    def test_init_username_default(self):
        with self.assertRaises(TypeError):
            User()  # noqa

    def test_init_username_positional(self):
        user = User('myusername')
        self.assertEqual(user.username, 'myusername')

    def test_init_username_keyword(self):
        with self.assertRaises(TypeError):
            User(username='myusername')  # noqa

    def test_init_password_default(self):
        user = User('myusername')
        self.assertIsNone(user.password)

    def test_init_password_positional(self):
        with self.assertRaises(TypeError):
            User('myusername', 'valid')  # noqa

    def test_init_password_keyword(self):
        user = User('myusername', password='valid')
        sha256_hash = 'ec654fac9599f62e79e2706abef23dfb7c07c08185aa86db4d8695f0b718d1b3'
        self.assertEqual(user.password, sha256_hash)

    def test_init_birthday_default(self):
        user = User('myusername')
        self.assertIsNone(user.birthday)

    def test_init_birthday_positional(self):
        with self.assertRaises(TypeError):
            User('myusername', '2000-01-01')  # noqa

    def test_init_birthday_keyword(self):
        user = User('myusername', birthday='2000-01-01')
        self.assertIsInstance(user.birthday, date)
        self.assertEqual(user.birthday, date(2000, 1, 1))


class UserFeatureTest(TestCase):
    def setUp(self) -> None:
        self.user = User('myusername', birthday='2000-01-01')

    def test_sayhello(self):
        text = self.user.say_hello()
        self.assertEqual(text, 'hello')

    def test_age(self):
        today = date(2010,1,1)
        with mock.patch('datetime.date') as d:
            d.today.return_value = today
            age = self.user.get_age()
        self.assertIsInstance(age, int)
        self.assertIn(age, range(0, 130))
        self.assertEqual(age, 10)

    def test_str(self):
        text = str(self.user)
        self.assertEqual(text, 'myusername')

    def test_repr(self):
        text = repr(self.user)
        self.assertEqual(text, "User('myusername')")

    def test_saysecret_not_authenticated(self):
        self.user.authenticated = False
        with self.assertRaises(PermissionError):
            self.user.say_secret()

    def test_saysecret_authenticated(self):
        self.user.authenticated = True
        text = self.user.say_secret()
        self.assertEqual(text, 'myVoiceIsMyPassword')


class UserAuthenticationTest(TestCase):
    def setUp(self) -> None:
        self.user = User('myusername', password='valid')

    def test_authentication_default(self):
        self.assertFalse(self.user.authenticated)

    def test_authentication_login_valid(self):
        self.user.login(username='myusername', password='valid')
        self.assertTrue(self.user.authenticated)

    def test_authentication_login_invalid(self):
        with self.assertRaises(PermissionError):
            self.user.login(username='myusername', password='invalid')
        self.assertFalse(self.user.authenticated)


class PasswordTest(TestCase):
    def test_password_encrypt_sha256(self):
        encrypted = encrypt('valid')
        self.assertEqual(encrypted, 'ec654fac9599f62e79e2706abef23dfb7c07c08185aa86db4d8695f0b718d1b3')
