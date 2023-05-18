"""
* Assignment: File Read Passwd
* Required: no
* Complexity: hard
* Lines of code: 100 lines
* Time: 55 min

English:
    1. Save listings content to files:
        a. `etc_passwd.txt`
        b. `etc_shadow.txt`
        c. `etc_group.txt`
    2. Copy also comments and empty lines
    3. Parse files and convert it to `result: list[dict]`
    4. Return list of users with `UID` greater than 1000
    5. User dict should contains data collected from all files
    6. Run doctests - all must succeed

Polish:
    1. Zapisz treści listingów do plików:
        a. `etc_passwd.txt`
        b. `etc_shadow.txt`
        c. `etc_group.txt`
    2. Skopiuj również komentarze i puste linie
    3. Sparsuj plik i przedstaw go w formacie `result: list[dict]`
    4. Zwróć listę użytkowników, których `UID` jest większy niż 1000
    5. Dict użytkownika powinien zawierać dane z wszystkich plików
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `from datetime import date`
    * `date.fromtimestamp(timestamp: int)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'username': 'mwatney',
      'uid': 1000,
      'gid': 1000,
      'home': '/home/mwatney',
      'shell': '/bin/bash',
      'algorithm': None,
      'password': None,
      'groups': ['user', 'staff'],
      'last_changed': datetime.date(2015, 4, 25),
      'locked': True},
     {'username': 'mlewis',
      'uid': 1001,
      'gid': 1001,
      'home': '/home/mlewis',
      'shell': '/bin/bash',
      'algorithm': 'SHA-512',
      'password': 'tgfvvFWJJ5FKmoXiP5rXWOjwoEBOEoAuBi3EphRbJqqjWYvhEM2wa67L9XgQ7W591FxUNklkDIQsk4kijuhE50',
      'groups': ['user', 'staff', 'admin'],
      'last_changed': datetime.date(2015, 7, 16),
      'locked': False},
     {'username': 'rmartinez',
      'uid': 1002,
      'gid': 1002,
      'home': '/home/rmartinez',
      'shell': '/bin/bash',
      'algorithm': 'MD5',
      'password': 'SWlkjRWexrXYgc98F.',
      'groups': ['user', 'staff'],
      'last_changed': datetime.date(2005, 2, 11),
      'locked': False}]

      >>> from os import remove
      >>> remove(FILE_GROUP)
      >>> remove(FILE_SHADOW)
      >>> remove(FILE_PASSWD)
"""

from datetime import date
from os.path import dirname, join


BASE_DIR = dirname(__file__)
FILE_GROUP = join(BASE_DIR, 'etc-group.txt')
FILE_SHADOW = join(BASE_DIR, 'etc-shadow.txt')
FILE_PASSWD = join(BASE_DIR, 'etc-passwd.txt')


CONTENT_GROUP = """##
# `/etc/group` structure
#   - Group Name: from `/etc/passwd`
#   - Group Password: `x` indicates that shadow passwords are used)
#   - GID: Group ID
#   - Members: usernames from `/etc/passwd`
##

root::0:root
other::1:
bin::2:root,bin,daemon
sys::3:root,bin,sys,adm
adm::4:root,adm,daemon
mail::6:root
daemon::12:root,daemon
sysadmin::14:root
user::1001:mwatney,mlewis,rmartinez
staff::1002:mwatney,mlewis,rmartinez
admin::1003:mlewis
nobody::60001:
noaccess::60002:
nogroup::65534:"""


CONTENT_PASSWD = """##
# `/etc/passwd` structure:
#   - Username
#   - Password: `x` indicates that shadow passwords are used
#   - UID: User ID number
#   - GID: User's group ID number
#   - GECOS: Full name of the user
#   - Home directory
#   - Login shell
##

root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
nobody:x:99:99:Nobody:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
mwatney:x:1000:1000:Mark mwatney:/home/mwatney:/bin/bash
mlewis:x:1001:1001:Melissa mlewis:/home/mlewis:/bin/bash
rmartinez:x:1002:1002:Rick rmartinez:/home/rmartinez:/bin/bash"""


CONTENT_SHADOW = """##
# `/etc/shadow` structure
#   - Username: from `/etc/passwd`
#   - Password
#   - Last Password Change: Days since 1970-01-01
#   - Minimum days between password changes: 0 - changed at any time
#   - Password validity: Days after which password must be changed, 99999 - many, many years
#   - Warning threshold: Days to warn user of an expiring password, 7 - full week
#   - Account inactive: Days after password expires and account is disabled
#   - Time since account is disabled: Days since 1970-01-01
#   - A reserved field for possible future use
#
# Password field (split by `$`):
#   - algorithm
#   - salt
#   - password hash
#
# Password algorithms:
#   - `1` - MD5
#   - `2a` - Blowfish
#   - `2y` - Blowfish
#   - `5` - SHA-256
#   - `6` - SHA-512
#
# Password special chars:
#   - ` ` (blank entry) - password is not required to log in
#   - `*` (asterisk) - account is disabled, cannot be unlocked, no password has ever been set
#   - `!` (exclamation mark) - account is locked, can be unlocked, no password has ever been set
#   - `!<password_hash>` - account is locked, can be unlocked, but password is set
#   - `!!` (two exclamation marks) - account created, waiting for initial password to be set by admin
##

root:$6$Ke02nYgo.9v0SF4p$hjztYvo/M4buqO4oBX8KZTftjCn6fE4cV5o/I95QPekeQpITwFTRbDUBYBLIUx2mhorQoj9bLN8v.w6btE9xy1:16431:0:99999:7:::
adm:$6$5H0QpwprRiJQR19Y$bXGOh7dIfOWpUb/Tuqr7yQVCqL3UkrJns9.7msfvMg4ZO/PsFC5Tbt32PXAw9qRFEBs1254aLimFeNM8YsYOv.:16431:0:99999:7:::
mwatney:!!:16550::::::
mlewis:$6$P9zn0KwR$tgfvvFWJJ5FKmoXiP5rXWOjwoEBOEoAuBi3EphRbJqqjWYvhEM2wa67L9XgQ7W591FxUNklkDIQsk4kijuhE50:16632:0:99999:7:::
rmartinez:$1$.QKDPc5E$SWlkjRWexrXYgc98F.:12825:0:90:5:30:13096:"""

with open(FILE_GROUP, mode='w') as file:
    file.write(CONTENT_GROUP)

with open(FILE_PASSWD, mode='w') as file:
    file.write(CONTENT_PASSWD)

with open(FILE_SHADOW, mode='w') as file:
    file.write(CONTENT_SHADOW)

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR

ALGORITHMS = {
    '1': 'MD5',
    '2a': 'Blowfish',
    '2y': 'Blowfish',
    '5': 'SHA-256',
    '6': 'SHA-512',
}

# Joined data from all files for users with `UID` greater than 1000
# type: list[dict]
result = ...

# Solution
result_group = {}
result_shadow = {}
result_passwd = {}
result = []

try:
    with open(FILE_GROUP, encoding='utf-8') as file:
        etc_group = file.readlines()
except FileNotFoundError:
    print(f'File {FILE_GROUP} does not exist')
except PermissionError:
    print('Permission denied')

try:
    with open(FILE_SHADOW, encoding='utf-8') as file:
        etc_shadow = file.readlines()
except FileNotFoundError:
    print(f'File {FILE_SHADOW} does not exist')
except PermissionError:
    print('Permission denied')

try:
    with open(FILE_PASSWD, encoding='utf-8') as file:
        etc_passwd = file.readlines()
except FileNotFoundError:
    print(f'File {FILE_PASSWD} does not exist')
except PermissionError:
    print('Permission denied')

for line in etc_group:
    line = line.strip()

    if not line or line.startswith('#'):
        continue

    group_name, _, _, members, *_ = line.split(':')

    if not members:
        continue

    for member in members.split(','):
        if member not in result_group.keys():
            result_group[member] = list()

        result_group[member].append(group_name)

for line in etc_shadow:
    line = line.strip()

    if not line or line.startswith('#'):
        continue

    username, password, last_change, *_ = line.split(':')
    timestamp = int(last_change) * DAY
    last_change = date.fromtimestamp(timestamp)

    if password.startswith('$'):
        locked = False
        password = password.split('$')
        password_algorithm = ALGORITHMS[password[1]]
        password_salt = password[2]
        password_password = password[3]
    else:
        locked = True
        password_algorithm = None
        password_salt = None
        password_password = None

    result_shadow[username] = {
        'password': password_password,
        'salt': password_salt,
        'algorithm': password_algorithm,
        'last_change': last_change,
        'locked': locked,
    }

for line in etc_passwd:
    line = line.strip()

    if not line or line.startswith('#'):
        continue

    record = line.split(':')
    username = record[0]

    result_passwd[username] = {
        'password': record[1],
        'uid': int(record[2]),
        'gid': int(record[3]),
        'gecos': record[4],
        'home': record[5],
        'shell': record[6],
    }

for user in result_passwd:
    passwd = result_passwd.get(user)
    groups = result_group.get(user)
    shadow = result_shadow.get(user)

    if passwd['uid'] < 1000:
        continue

    result.append({
        'username': user,
        'uid': passwd['uid'],
        'gid': passwd['gid'],
        'home': passwd['home'],
        'shell': passwd['shell'],
        'algorithm': shadow['algorithm'],
        'password': shadow['password'],
        'groups': groups,
        'last_changed': shadow['last_change'],
        'locked': shadow['locked']})
