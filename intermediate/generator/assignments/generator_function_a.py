"""
* Assignment: Generator Function Passwd
* Complexity: medium
* Lines of code: 10 lines
* Time: 5 min

English:
    1. Split `DATA` by lines and then by colon `:`
    2. Extract system accounts (users with UID [third field] is less than 1000)
    3. Return list of system account logins
    4. Implement solution using function
    5. Implement solution using generator and `yield` keyword
    6. Run doctests - all must succeed

Polish:
    1. Podziel `DATA` po liniach a następnie po dwukropku `:`
    2. Wyciągnij konta systemowe (użytkownicy z UID (trzecie pole) mniejszym niż 1000)
    3. Zwróć listę loginów użytkowników systemowych
    4. Zaimplementuj rozwiązanie wykorzystując funkcję
    5. Zaimplementuj rozwiązanie wykorzystując generator i słowo kluczowe `yield`
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * ``str.splitlines()``
    * ``str.split()``
    * unpacking expression

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction, isgeneratorfunction

    >>> assert isfunction(function)
    >>> assert isgeneratorfunction(generator)

    >>> list(function(DATA))
    ['root', 'bin', 'daemon', 'adm', 'shutdown', 'halt', 'nobody', 'sshd']

    >>> list(generator(DATA))
    ['root', 'bin', 'daemon', 'adm', 'shutdown', 'halt', 'nobody', 'sshd']
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


# list[str] with usernames when UID [third field] is less than 1000
# type: Callable[[str], list[str]]
def function(data: str):
    ...


# list[str] with usernames when UID [third field] is less than 1000
# type: Generator
def generator(data: str):
    ...


# Solution
def function(data):
    result = []
    for line in data.splitlines():
        username, _, uid, *_ = line.split(':')
        if int(uid) < 1000:
            result.append(username)
    return result


def generator(data):
    for line in data.splitlines():
        username, _, uid, *_ = line.split(':')
        if int(uid) < 1000:
            yield username
