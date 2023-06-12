"""
* Assignment: OOP MethodClassmethod FromString
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Define class `Account` with:
        a. Field `username: str`
        b. Field `password: str`
        c. Field `uid: int`
        d. Field `gid: int`
        e. Field `gecos: str`
        f. Field `home: str`
        g. Field `shell: str`
        h. Method `from_passwd()` with parameter: `line: str`
    2. Method `from_passwd()` returns instance of a class on which was called
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Account` z:
        a. Polem `username: str`
        b. Polem `password: str`
        c. Polem `uid: int`
        d. Polem `gid: int`
        e. Polem `gecos: str`
        f. Polem `home: str`
        g. Polem `shell: str`
        h. Metodą `from_passwd()` z parametrem `line: str`
    2. Metoda `from_passwd()` zwraca instancję klasy na której została wykonana
    3. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * str.split()
    * int()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Account)
    >>> assert isclass(SystemAccount)
    >>> assert isclass(UserAccount)

    >>> line = 'root:x:0:0:root:/root:/bin/bash'
    >>> root = SystemAccount.from_passwd(line)
    >>> assert root.username == 'root'
    >>> assert root.password == 'x'
    >>> assert root.uid == 0
    >>> assert root.gid == 0
    >>> assert root.gecos == 'root'
    >>> assert root.home == '/root'
    >>> assert root.shell == '/bin/bash'

    >>> line = 'watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash'
    >>> root = UserAccount.from_passwd(line)
    >>> assert root.username == 'watney'
    >>> assert root.password == 'x'
    >>> assert root.uid == 1000
    >>> assert root.gid == 1000
    >>> assert root.gecos == 'Mark Watney'
    >>> assert root.home == '/home/watney'
    >>> assert root.shell == '/bin/bash'
"""

class Account:
    def __init__(self, username, password, uid, gid, gecos, home, shell):
        self.username = username
        self.password = password
        self.uid = uid
        self.gid = gid
        self.gecos = gecos
        self.home = home
        self.shell = shell

# Method `from_passwd()` with parameter: `line: str`
# Method `from_passwd()` returns instance of a class on which was called
# type: Callable[[type[Self], str], Self]
    def from_passwd():
        ...


class SystemAccount(Account):
    pass


class UserAccount(Account):
    pass


# Solution
class Account:
    def __init__(self, username, password, uid, gid, gecos, home, shell):
        self.username = username
        self.password = password
        self.uid = uid
        self.gid = gid
        self.gecos = gecos
        self.home = home
        self.shell = shell

    @classmethod
    def from_passwd(cls, line: str):
        username, password, uid, gid, gecos, home, shell = line.split(':')
        return cls(username, password, int(uid), int(gid), gecos, home, shell)


class SystemAccount(Account):
    pass


class UserAccount(Account):
    pass
