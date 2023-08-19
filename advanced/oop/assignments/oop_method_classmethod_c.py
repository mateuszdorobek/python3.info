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
        h. Method `from_passwd()`
    2. Method `from_passwd()`:
        a. Parameter `data: str`, example: 'root:x:0:0:root:/root:/bin/bash'
        b. Returns instance of a class on which was called
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
        h. Metodą `from_passwd()`
    2. Metoda `from_passwd()`:
        a. Parametr `data: str`, przykład: 'root:x:0:0:root:/root:/bin/bash'
        b. Zwraca instancję klasy na której została wykonana
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

    >>> data = 'root:x:0:0:root:/root:/bin/bash'
    >>> admin = SystemAccount.from_passwd(data)
    >>> assert type(admin.username) is str
    >>> assert type(admin.password) is str
    >>> assert type(admin.uid) is int
    >>> assert type(admin.gid) is int
    >>> assert type(admin.gecos) is str
    >>> assert type(admin.home) is str
    >>> assert type(admin.shell) is str
    >>> assert admin.username == 'root'
    >>> assert admin.password == 'x'
    >>> assert admin.uid == 0
    >>> assert admin.gid == 0
    >>> assert admin.gecos == 'root'
    >>> assert admin.home == '/root'
    >>> assert admin.shell == '/bin/bash'

    >>> data = 'watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash'
    >>> user = UserAccount.from_passwd(data)
    >>> assert type(user.username) is str
    >>> assert type(user.password) is str
    >>> assert type(user.uid) is int
    >>> assert type(user.gid) is int
    >>> assert type(user.gecos) is str
    >>> assert type(user.home) is str
    >>> assert type(user.shell) is str
    >>> assert user.username == 'watney'
    >>> assert user.password == 'x'
    >>> assert user.uid == 1000
    >>> assert user.gid == 1000
    >>> assert user.gecos == 'Mark Watney'
    >>> assert user.home == '/home/watney'
    >>> assert user.shell == '/bin/bash'
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

    # parameter: `data: str`
    # example: 'root:x:0:0:root:/root:/bin/bash'
    # hint: uid and gid must be int
    # return: instance of a class on which was called
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
    def from_passwd(cls, data: str):
        username, password, uid, gid, gecos, home, shell = data.split(':')
        return cls(username, password, int(uid), int(gid), gecos, home, shell)


class SystemAccount(Account):
    pass


class UserAccount(Account):
    pass
