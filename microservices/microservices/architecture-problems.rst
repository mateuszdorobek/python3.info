Microservice Problems
=====================
* Polyglot Programming i Polyglot Persistence
* Ludzie
* Handoff
* Wiązanie usług (coupling)
* Microdata
* Audyt i Compliance


Polyglot Programming i Polyglot Persistence
-------------------------------------------
* overhead związany z wielością usług
* nowe technologie
* różne działające równoległe wersje np. baz danych
* Deprecation policy
* Przykład Webapi
* Przykład Visual Fox Pro -> Java
* Przykład Twitter API


Ludzie
------
* poziom wiedzy jest nierówny
* różna wiedza na temat spójności systemów
* różne doświadczenie
* zmiana zespołów
* próg wejścia
* zatrudnianie w nowej technologii
* konwersja obecnych pracowników
* zmiana przyzwyczajeń
* zmiana języka programowania i technologii
* Ludzie muszą testować
* Wymiana wiedzy pomiędzy ludźmi (eurowizja)
* Hackatony wdrożeniowe


Handoff
-------
* ze względu na bardzo rozproszone środowisko ludzie uruchamiają swoje usługi sami
* duża i rozproszona wiedza na temat działania systemu
* utrzymywanie przez zespół
* przekazywania usług
* zmiany HRowe
* dyżury w każdym zespole


Wiązanie usług (coupling)
-------------------------
* zaprzecza systemowi wysyłania eventów
* ze względu na rozwój domen w różnym tempie pojawia się pokusa, aby obejść usługę i samemu zaimplementować funkcjonalność


Microdata
---------
* eksport danych do Hadoopa
* normalizacja danych z różnych technologii i baz danych
* brak informacji na świecie jak to robić
* inny sposób dostępu do danych dla analityki (dostęp do miliardów rekordów po HTTP i API nie jest optymalny)
* Replikacja baz danych
* BSON
* Protocol Buffers (Protobuf)
* Trhift


Audyt i Compliance
------------------
* problemy z monitorowaniem
* problemy z rozproszoną wiedzą
* sprawdzanie czy wszystko się liczy poprawnie
* wyciąganie raportów i danych audytowych
* monolit - jedno zapytanie do bazy danych i joiny
* microservices - dane są rozproszone (różne systemy, bazy danych, technologie)
* tworzenie audit logów
* przygotowanie systemu od początku pod audyty
