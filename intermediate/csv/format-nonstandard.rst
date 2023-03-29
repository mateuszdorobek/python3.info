CSV Non-Standard
================

Ini
---
* setup.cfg
* ``delimiter='='``

.. code-block:: text

    key=MP
    name=MyProject
    language=py
    encoding=UTF-8
    verbose=true

>>> delimiter = '='
>>> result = [row.split(delimiter) for row in DATA.splitlines()]  # doctest: +SKIP


Config
------
* ``/etc/postgresql/*/main/postgresql.conf``
* ``delimiter=' = '``

.. code-block:: text

    listen_addresses = 'localhost'
    port = 5432
    max_connections = 100
    ssl = on
    password_encryption = on
    db_user_namespace = off

>>> delimiter = ' = '
>>> result = [row.split(delimiter) for row in DATA.splitlines()]  # doctest: +SKIP


Toml
----
* pyproject.toml
* ``delimiter='='``

.. code-block:: toml

    namespace_packages = false
    explicit_package_bases = false
    ignore_missing_imports = false
    follow_imports = "normal"
    follow_imports_for_stubs = false
    no_site_packages = false
    no_silence_site_packages = false
    # Platform configuration
    python_version = "3.10"
    platform = "linux-64"



Passwd
------
* ``/etc/passwd``
* ``delimiter=':'``

.. code-block:: text

    root:x:0:0:root:/root:/bin/bash
    bin:x:1:1:bin:/bin:/sbin/nologin
    daemon:x:2:2:daemon:/sbin:/sbin/nologin
    adm:x:3:4:adm:/var/adm:/sbin/nologin
    shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
    halt:x:7:0:halt:/sbin:/sbin/halt
    nobody:x:99:99:Nobody:/:/sbin/nologin
    sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
    watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
    lewis:x:1001:1001:Melissa Lewis:/home/lewis:/bin/bash
    martinez:x:1002:1002:Rick Martinez:/home/martinez:/bin/bash

>>> delimiter = ':'
>>> result = [row.split(delimiter) for row in DATA.splitlines()]  # doctest: +SKIP


SSHd Config
-----------
* ``/etc/ssh/sshd_config``
* ``delimiter=' '``

.. code-block:: text

    ChrootDirectory none
    ClientAliveCountMax 3
    ClientAliveInterval 0
    Compression delayed
    MaxStartups 10:30:100
    PidFile /var/run/sshd.pid
    X11Forwarding no
    X11UseLocalhost yes

>>> delimiter = ' '
>>> result = [row.split(delimiter) for row in DATA.splitlines()]  # doctest: +SKIP


Hosts
-----
* ``delimiter='\s+'``

.. code-block:: text

    ##
    # `/etc/hosts` structure:
    #   - IPv4 or IPv6
    #   - Hostnames
    ##

    127.0.0.1       localhost
    127.0.0.1       astromatt
    10.13.37.1      nasa.gov esa.int
    255.255.255.255 broadcasthost
    ::1             localhost


Crontab
-------
* ``/etc/crontab``
* ``delimiter='\s+'``

.. code-block:: text

    # [Minute] [Hour] [Day_of_the_Month] [Month_of_the_Year] [Day_of_the_Week] [command]
    */5 * * * *          /usr/bin/python3 /home/python/run-5min.py 1>/dev/null
    * * * * *            /usr/bin/python3 /home/python/run-1min.py 1>/dev/null
    00 * * * *           /home/python/run.py 1>/dev/null
    * * * jan,may,aug *  /home/python/run.py
    0 17 * * sun,fri     /home/python/run.py
    0 */4 * * *          /home/python/run.py
    0 4,17 * * sun,mon   /home/python/run.py


Key-Value
---------
* ``/etc/locate.rc``
* ``delimiter='='``

.. code-block:: text

    TMPDIR="/tmp"
    FCODES="/var/db/locate.database"
    SEARCHPATHS="/"
    PRUNEPATHS="/tmp /var/tmp"

.. code-block:: text

    # temp directory
    TMPDIR="/tmp"

    # the actual database
    #FCODES="/var/db/locate.database"

    # directories to be put in the database
    SEARCHPATHS="/"

    # directories unwanted in output
    #PRUNEPATHS="/tmp /var/tmp"


Docker
------
* ``.env`` from Docker
* ``delimiter='='``

.. code-block:: docker

    DATABASE_ENGINE=postgresql
    DATABASE_SERVER=localhost
    DATABASE_PORT=5432
    DATABASE_NAME=mydatabase
    DATABASE_USERNAME=myusername
    DATABASE_PASSWORD=mypassword


Sensors
-------
* ``delimiter=';'``

.. code-block:: text

    Name,         Long,       Lat,        ModuleType
    "ESA EAC",    50.8524881, 7.1315254,  Indoor

    Date,         Time,       Temperature, Humidity, CO2, Noise, Pressure
    "2000-01-01", "00:00:00", 22.6,        46,       981, 32,    1019.1
    "2000-01-01", "00:05:00", 22.6,        46,       981, 31,    1019.1
    "2000-01-01", "00:10:00", 22.6,        46,       968, 32,    1019.1

.. code-block:: text

    Name;Long;Lat;ModuleName;ModuleType
    "European Astronaut Centre";50.8524881,7.1315254;;Indoor
    Timestamp;"Timezone : Europe/Berlin";Temperature;Humidity;CO2;Noise;Pressure
    1622498702;"2021/06/01 00:05:02";22.6;46;981;32;1019.1
    1622499004;"2021/06/01 00:10:04";22.6;46;981;31;1019.1
    1622499306;"2021/06/01 00:15:06";22.6;46;968;32;1019.1
    1622499608;"2021/06/01 00:20:08";22.5;46;940;31;1019.1
    1622499912;"2021/06/01 00:25:12";22.5;46;907;32;1019
    1622500214;"2021/06/01 00:30:14";22.5;46;877;31;1019
    1622500517;"2021/06/01 00:35:17";22.4;46;873;32;1019


>>> DATA= """Name;Long;Lat;ModuleName;ModuleType
... "European Astronaut Centre";50.8524881,7.1315254;;Indoor
... Timestamp;"Timezone : Europe/Berlin";Temperature;Humidity;CO2;Noise;Pressure
... 1622498702;"2021/06/01 00:05:02";22.6;46;981;32;1019.1
... 1622499004;"2021/06/01 00:10:04";22.6;46;981;31;1019.1
... 1622499306;"2021/06/01 00:15:06";22.6;46;968;32;1019.1
... 1622499608;"2021/06/01 00:20:08";22.5;46;940;31;1019.1
... 1622499912;"2021/06/01 00:25:12";22.5;46;907;32;1019
... 1622500214;"2021/06/01 00:30:14";22.5;46;877;31;1019
... 1622500517;"2021/06/01 00:35:17";22.4;46;873;32;1019"""
>>>
>>>
>>> metadata_header, metadata_values, data_header, *data_values = DATA.splitlines()
>>>
>>> metadata_header = metadata_header.split(';')
>>> metadata_values = metadata_values.split(';')
>>> data_header = data_header.split(';')
>>> data_values = [line.split(';') for line in data_values]
>>>
>>>
>>> metadata_header
['Name', 'Long', 'Lat', 'ModuleName', 'ModuleType']
>>>
>>> metadata_values
['"European Astronaut Centre"', '50.8524881,7.1315254', '', 'Indoor']
>>>
>>> data_header
['Timestamp', '"Timezone : Europe/Berlin"', 'Temperature', 'Humidity', 'CO2', 'Noise', 'Pressure']
>>>
>>> data_values  # doctest: +NORMALIZE_WHITESPACE
[['1622498702', '"2021/06/01 00:05:02"', '22.6', '46', '981', '32', '1019.1'],
 ['1622499004', '"2021/06/01 00:10:04"', '22.6', '46', '981', '31', '1019.1'],
 ['1622499306', '"2021/06/01 00:15:06"', '22.6', '46', '968', '32', '1019.1'],
 ['1622499608', '"2021/06/01 00:20:08"', '22.5', '46', '940', '31', '1019.1'],
 ['1622499912', '"2021/06/01 00:25:12"', '22.5', '46', '907', '32', '1019'],
 ['1622500214', '"2021/06/01 00:30:14"', '22.5', '46', '877', '31', '1019'],
 ['1622500517', '"2021/06/01 00:35:17"', '22.4', '46', '873', '32', '1019']]
