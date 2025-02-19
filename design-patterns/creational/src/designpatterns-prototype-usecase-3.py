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

    def clone(self, **kwargs):
        values = vars(self) | kwargs
        return User(**values)


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

melissa = mark.clone(
    firstname='Melissa',
    lastname='Lewis',
    username='mlewis',
    email='mlewis@nasa.gov',
)

print(melissa)
# User(firstname='Melissa', lastname='Lewis', username='mwatney', password='Ares3', email='mwatney@nasa.gov', last_login=None, role='admin', groups=['admins', 'users'])
