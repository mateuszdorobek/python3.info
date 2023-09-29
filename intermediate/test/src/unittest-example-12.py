import hashlib
from datetime import date
from unittest import TestCase

def password_encode(username: str | None, password: str | None) -> str:
    if username is None and password is None:
        raise ValueError('Username and password cannot be none at the same time')
    string = f'{username}:{password}'
    return hashlib.sha256(string.encode()).hexdigest()


class User:
    username: str
    password: str | None
    birthday: date | None

    def __init__(self, username: str, /, *, password: str | None = None, birthday: str | date | None = None) -> None:
        self.username = username
        self.password = password_encode(username, password)
        self.birthday = date.fromisoformat(birthday) if birthday else None
        self._authenticated = False

    def __str__(self):
        return f'{self.username}'

    def __repr__(self):
        clsname = self.__class__.__name__
        username = self.username
        birthday = self.birthday.isoformat()
        return f"{clsname}('{username}', {birthday=})"

    def say_hello(self) -> str:
        return 'hello'

    def is_authenticated(self) -> bool:
        return self._authenticated

    def logout(self) -> None:
        self._authenticated = False

    def login(self, password: str) -> None:
        encrypted = password_encode(self.username, password)
        if self.password == encrypted:
            self._authenticated = True


class PasswordEncoderTest(TestCase):
    def test_encode_username_and_password(self):
        result = password_encode('myusername', 'validpassword')
        self.assertEqual(result, '37ac6a95b12ae0fb66676e1b7b47e7cffca2b957d2057c14ad8b02e7def2cea3')

    def test_encode_empty_password(self):
        result = password_encode('myusername', None)
        self.assertEqual(result, '10c8b03c7b173081a489538b2cbcf16776ef547377dd99d4737d065b1ab4c17e')

    def test_encode_empty_username(self):
        result = password_encode(None, 'validpassword')
        self.assertEqual(result, '80881add7148cb7f7835994f984f816c2fb936989bee075e8d9c5de613857030')

    def test_encode_empty_username_and_password(self):
        with self.assertRaises(ValueError):
            password_encode(None, None)


class UserInitTest(TestCase):
    def test_init_username_default(self):
        with self.assertRaises(TypeError):
            User()  # noqa

    def test_init_username_positional(self):
        user = User("myusername")
        self.assertEqual(user.username, "myusername")

    def test_init_username_keyword(self):
        with self.assertRaises(TypeError):
            User(username="myusername")  # noqa

    def test_init_password_default(self):
        user = User("myusername")  # noqa
        self.assertEqual(user.password, '10c8b03c7b173081a489538b2cbcf16776ef547377dd99d4737d065b1ab4c17e')

    def test_init_password_positional(self):
        with self.assertRaises(TypeError):
            User("myusername", "validpassword")  # noqa

    def test_init_password_keyword(self):
        user = User("myusername", password="validpassword")
        self.assertEqual(user.password, "37ac6a95b12ae0fb66676e1b7b47e7cffca2b957d2057c14ad8b02e7def2cea3")

    def test_init_birthday_default(self):
        user = User("myusername", password="validpassword")  # noqa
        self.assertIsNone(user.birthday)

    def test_init_birthday_positional(self):
        with self.assertRaises(TypeError):
            User("myusername", "validpassword", "2000-01-01")  # noqa

    def test_init_birthday_keyword(self):
        user = User("myusername", password="validpassword", birthday="2000-01-02")  # noqa
        self.assertIsInstance(user.birthday, date)
        self.assertEqual(user.birthday, date(2000, 1, 2))


class UserFunctionalityTest(TestCase):
    def setUp(self):
        self.user = User("myusername", password="validpassword", birthday="2000-01-02")

    def test_str(self):
        result = str(self.user)
        self.assertEqual(result, 'myusername')

    def test_repr(self):
        result = repr(self.user)
        self.assertEqual(result, "User('myusername', birthday='2000-01-02')")

    def test_sayhello(self):
        result = self.user.say_hello()
        self.assertEqual(result, 'hello')


class UserAuthenticationTest(TestCase):
    def setUp(self):
        self.user = User("myusername", password="validpassword")

    def test_authenticated_default(self):
        self.assertFalse(self.user._authenticated)

    def test_authenticated_when_logged_in(self):
        self.user._authenticated = True
        self.assertTrue(self.user.is_authenticated())

    def test_authenticated_when_logged_out(self):
        self.user._authenticated = False
        self.assertFalse(self.user.is_authenticated())

    def test_login_valid(self):
        self.user._authenticated = False
        self.user.login('validpassword')
        self.assertTrue(self.user._authenticated)

    def test_login_invalid(self):
        self.user._authenticated = False
        self.user.login('invalidpassword')
        self.assertFalse(self.user._authenticated)

    def test_logout(self):
        self.user._authenticated = True
        self.user.logout()
        self.assertFalse(self.user._authenticated)
