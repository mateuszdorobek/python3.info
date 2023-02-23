from unittest import TestCase


class User:
    firstname: str
    lastname: str
    age: int | None

    def __init__(self, firstname: str, lastname: str,
                 *, age: int | None = None) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.salary = None
        self.job = None

    def say_hello(self) -> str:
        return f'Hello {self.firstname} {self.lastname}'

    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname}'

    def __repr__(self) -> str:
        clsname = self.__class__.__name__
        firstname = self.firstname
        lastname = self.lastname
        return f'{clsname}({firstname=}, {lastname=})'

    def make_older(self, years: int) -> None:
        self.age += years

    def is_astronaut(self):
        if self.job == 'astronaut':
            return True
        else:
            return False

    def is_rich(self):
        if self.salary <= 5000:
            return False
        return True


class UserInitTest(TestCase):

    def test_init_name(self) -> None:
        user = User('Mark', 'Watney')
        self.assertEqual(user.firstname, 'Mark')
        self.assertEqual(user.lastname, 'Watney')

    def test_init_age_positional(self) -> None:
        with self.assertRaises(TypeError):
            User('Mark', 'Watney', 40)  # noqa

    def test_init_age_keyword(self) -> None:
        user = User('Mark', 'Watney', age=40)
        self.assertEqual(user.age, 40)


class UserFeaturesTest(TestCase):

    def setUp(self) -> None:
        self.user = User('Mark', 'Watney', age=40)

    def test_make_older(self):
        self.user.make_older(years=1)
        self.assertEqual(self.user.age, 41)

    def test_hello(self) -> None:
        self.assertEqual(self.user.say_hello(), 'Hello Mark Watney')

    def test_str(self) -> None:
        self.assertEqual(str(self.user), 'Mark Watney')

    def test_repr(self) -> None:
        self.assertEqual(repr(self.user), "User(firstname='Mark', lastname='Watney')")


class UserJobTest(TestCase):

    def setUp(self) -> None:
        self.user = User('Mark', 'Watney', age=40)

    def test_job_default(self) -> None:
        self.assertEqual(self.user.job, None)

    def test_job_isastronaut_when_job_default(self) -> None:
        self.assertFalse(self.user.is_astronaut())

    def test_job_isastronaut_when_job_other(self) -> None:
        self.user.job = 'other'
        self.assertFalse(self.user.is_astronaut())

    def test_job_isastronaut_when_job_astronaut(self) -> None:
        self.user.job = 'astronaut'
        self.assertTrue(self.user.is_astronaut())


class UserSalaryTest(TestCase):

    def setUp(self) -> None:
        self.user = User('Mark', 'Watney', age=40)

    def test_salary_default(self):
        self.assertIsNone(self.user.salary)
        self.assertEqual(self.user.salary, None)

    def test_salary_field(self):
        self.user.salary = 10_000.00
        self.assertAlmostEqual(self.user.salary, 10_000, places=2)

    def test_salary_isrich_negative(self):
        self.user.salary = 1000.00
        self.assertFalse(self.user.is_rich())

    def test_salary_isrich_positive(self):
        self.user.salary = 10_000.00
        self.assertTrue(self.user.is_rich())
