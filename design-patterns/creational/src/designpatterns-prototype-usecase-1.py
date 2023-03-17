from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal


@dataclass
class User:
    firstname: str
    lastname: str
    username: str
    password: str
    email: str
    last_login: datetime | None
    role: Literal['admin', 'user', 'guest']
    groups: list[str] = field(default_factory=list)

    def clone(self):
        return User(
            firstname = self.firstname,
            lastname = self.lastname,
            username = self.username,
            password = self.password,
            email = self.email,
            last_login = self.last_login,
            role = self.role,
            groups = self.groups)


mark = User(
    firstname='Mark',
    lastname='Watney',
    username='mwatney',
    password='Ares3',
    email='mwatney@nasa.gov',
    last_login=None,
    role='admin',
    groups=['admins', 'users'],
)

melissa = mark.clone()

print(melissa)
# User(firstname='Mark', lastname='Watney', username='mwatney', password='Ares3', email='mwatney@nasa.gov', last_login=None, role='admin', groups=['admins', 'users'])

melissa.firstname = 'Melissa'
melissa.lastname = 'Lewis'
melissa.username = 'mlewis'
melissa.email = 'mlewis@nasa.gov'

print(melissa)
# User(firstname='Melissa', lastname='Lewis', username='mlewis', password='Ares3', email='mlewis@nasa.gov', last_login=None, role='admin', groups=['admins', 'users'])
