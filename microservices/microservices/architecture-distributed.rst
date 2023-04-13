Microservices Distributed Systems
=================================
* Niezależne domeny awarii
* Możliwość pisania w wielu językach
* Równoległość komponentów (concurrency)
* Brak globalnego zegara i możliwości jednoznacznego określenia czasu i kolejności
* zapewnienie spójności kosztem dostępności
* zapewnienie wysokiej dostępności kosztem spójności
* wzajemnie się wykluczające
* nie ma ACID!: Atomicity, Consistency, Isolation, Durability
* Dwufazowe Commity
* Brak transakcyjności
* Zastosować mechanizm rekompensacji (np. raz w nocy usuwać zduplikowane dane)
* Brak gwarancji, że komunikat wysłany do hosta zostanie wysłany tylko raz (np. jeżeli dwa razy zostanie wysłany komunikat przez bankomat o naliczeniu opłaty, to operacja zostanie wykonana przez bank tylko raz)


BASE
----
* Basically
* Available (w większości możemy wykonać pewne operacje)
* Soft State (tylko operacje, których stan możemy odbudować, np. przez przegenerowanie cache)
* Eventually consistent (system jest pomiędzy stanem spójnym i niespójnym)


8 błędnych założeń
------------------
* Deutsch, P. The Eight Fallacies of Distributed Computing. Year: 1991. [#Deutsch1991]_
* Sieć jest niezawodna
* Opóźnienia w sieci są zerowe
* Przepustowość sieci jest nieskończona
* Sieć jest bezpieczna
* Topologia sieci się nie zmienia
* Istnieje tylko jeden administrator
* Koszt transportu jest zerowy
* Sieć jest jednorodna


Sieć jest niezawodna
--------------------
* sieć w serwerowni jest niezawodna
* MTBF routera jest 50k h
* netsplit w publicznych cloudach są normalne
* zwiększa się latency


Opóźnienia w sieci są zerowe
----------------------------
* opóźnienia w sieci są zerowe


Przepustowość sieci jest nieskończona
-------------------------------------
* przepustowość sieci jest nieskończona


Sieć jest bezpieczna
--------------------
* większość aplikacji jest chroniona z zewnątrz
* brak szyfrowania wewnątrz sieci


Topologia sieci się nie zmienia
-------------------------------
* przeliczenie BGP i zmiana spanning tree
* ścieżki sieciowe się zmieniają
* pojawiają się nowe instancje


Istnieje tylko jeden administrator
----------------------------------
* różni ludzie z różną wiedzą
* inaczej konfigurują maszyny
* jeden serwer może być lepiej skonfigurowany


Koszt transportu jest zerowy
----------------------------
* narzut czasowy na serializację, deserializację, stos TCP
* czas transportu po medium jest niezerowy


Sieć jest jednorodna
--------------------
* sieć składa się z różnych urządzeń
* mogą być różnie stabilne
* mogą mieć różne charakterystyki


References
----------
.. [#Deutsch1991] Deutsch, P. The Eight Fallacies of Distributed Computing. Year: 1991.
