"""
* Assignment: OOP ObjectConstructor Passwd
* Complexity: easy
* Lines of code: 21 lines
* Time: 13 min

English:
    TODO: English translation
    X. Run doctests - all must succeed

Polish:
    1. Iteruj po liniach w `DATA` i podziel linię po dwukropku
    2. Stwórz klasę `Account`, która zwraca instancje klas
       `UserAccount` lub `SystemAccount` w zależności od wartości pola UID
    3. User ID (UID) to trzecie pole, np.
       `root:x:0:0:root:/root:/bin/bash` to UID jest równy `0`
    4. Jeżeli UID jest:
       a. poniżej 1000, to konto jest systemowe (`SystemAccount`)
       b. 1000 lub więcej, to konto użytkownika (`UserAccount`)
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.splitlines()`
    * `str.split()`
    * `str.strip()`
    * `map()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> list(result)  # doctest: +NORMALIZE_WHITESPACE
    [SystemAccount(username='root', uid=0),
     SystemAccount(username='bin', uid=1),
     SystemAccount(username='daemon', uid=2),
     SystemAccount(username='adm', uid=3),
     SystemAccount(username='shutdown', uid=6),
     SystemAccount(username='halt', uid=7),
     SystemAccount(username='nobody', uid=99),
     SystemAccount(username='sshd', uid=74),
     UserAccount(username='watney', uid=1000),
     UserAccount(username='lewis', uid=1001),
     UserAccount(username='martinez', uid=1002)]
"""

DATA = """root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
nobody:x:99:99:Nobody:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
lewis:x:1001:1001:Melissa Lewis:/home/lewis:/bin/bash
martinez:x:1002:1002:Rick Martinez:/home/martinez:/bin/bash"""

from dataclasses import dataclass


@dataclass
class SystemAccount:
    username: str
    uid: int

@dataclass
class UserAccount:
    username: str
    uid: int


# Parse DATA and convert to UserAccount or SystemAccount
# type: list[Account]
result = ...

# Solution
class Account:
    def __new__(cls, records):
        username, _, uid, *_ = records.split(':')
        uid = int(uid)
        if uid < 1000:
            return SystemAccount(username, uid)
        else:
            return UserAccount(username, uid)


# Parse DATA and convert to UserAccount or SystemAccount
# type: list[Account]
result = map(Account, DATA.splitlines())
