Idiom About
===========
* comprehension, generator expression
* any, all, min, max, sum
* zip, enumerate, chain
* map, filter, reduce, starmap, zip_longest
* range, product, permutations
* partial


Comprehension
-------------
* all value > 1.0

>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor')]

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = []
... for row in DATA:
...     for value in row:
...         if type(value) in (int,float):
...             result.append(value > 1.0)
... result = all(result)
12.2 µs ± 743 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = True
... for row in DATA:
...     for value in row:
...         if type(value) in (int,float):
...             if value <= 1.0:
...                 result = False
...                 break
...
10.5 µs ± 857 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = all(value > 1.0
...              for row in DATA
...              for value in row
...              if type(value) in (int,float))
...
3.71 µs ± 658 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = all(value > 1.0 for row in DATA for value in row if type(value) in (int,float))
...
3.8 µs ± 801 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = all(y > 1.0 for x in DATA for y in x if type(y) in (int,float))
...
4.13 µs ± 941 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)


Map
---
>>> from dataclasses import dataclass

>>> DATA = """root:x:0:0:root:/root:/bin/bash
... bin:x:1:1:bin:/bin:/sbin/nologin
... daemon:x:2:2:daemon:/sbin:/sbin/nologin
... adm:x:3:4:adm:/var/adm:/sbin/nologin
... shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
... halt:x:7:0:halt:/sbin:/sbin/halt
... nobody:x:99:99:Nobody:/:/sbin/nologin
... sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
... watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
... lewis:x:1001:1001:Melissa Lewis:/home/lewis:/bin/bash
... martinez:x:1002:1002:Rick Martinez:/home/martinez:/bin/bash"""

>>> @dataclass
... class SystemAccount:
...     username: str
...     uid: int
>>>
>>> @dataclass
... class UserAccount:
...     username: str
...     uid: int

>>> class Account:
...     def __new__(cls, line):
...         username, _, uid, *_ = line.strip().split(':')
...         uid = int(uid)
...         if uid < 1000:
...             return SystemAccount(username, uid)
...         else:
...             return UserAccount(username, uid)
>>>
>>>
>>> result = map(Account, DATA.splitlines())
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

>>> def account(line):
...     username, _, uid, *_ = line.strip().split(':')
...     uid = int(uid)
...     if uid < 1000:
...         return SystemAccount(username, uid)
...     else:
...         return UserAccount(username, uid)
>>>
>>> def system(account):
...     return account.uid < 1000
>>>
>>>
>>> all_accounts = map(account, DATA.splitlines())
>>> sys_accounts = filter(system, all_accounts)
>>>
>>> list(sys_accounts)  # doctest: +NORMALIZE_WHITESPACE
[SystemAccount(username='root', uid=0),
 SystemAccount(username='bin', uid=1),
 SystemAccount(username='daemon', uid=2),
 SystemAccount(username='adm', uid=3),
 SystemAccount(username='shutdown', uid=6),
 SystemAccount(username='halt', uid=7),
 SystemAccount(username='nobody', uid=99),
 SystemAccount(username='sshd', uid=74)]
