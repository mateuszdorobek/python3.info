Dragon About
============
.. figure:: img/dragon.gif

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn


Opis
----
* Nie piszemy gry, motyw gry jest tylko narracją do demonstracji OOP
* Zadanie jest symulacją procesu wytwarzania oprogramowania
* Przykłady znajdą zastosowanie w dowolnej domenie biznesowej

Nie piszemy gry i nie będziemy omawiali specyfiki game-dev!
Motyw Smoka z zadania jest tylko narracją do demonstracji obiektowego
paradygmatu programowania i dobrych praktyk programistycznych.
Siłą rzeczy poruszymy kilka kwestii z związanych ze specyfiką gier
(np. to że smok zieje ogniem itp), ale całość dyskusji znajdzie
zastosowanie do dowolnego rodzaju projektów informatycznych i problemów
inżynierii oprogramowania w każdej domenie biznesowej.


Role
----
* Ty - programista
* Prowadzący - Product Owner
* Product Owner nie doradzi Ci w sprawie decyzji architektonicznych

Podczas tego zadania wcielisz się w rolę inżyniera oprogramowania (programisty).
Twoją rolą jest podejmowanie decyzji odnośnie rozwiązania w kodzie,
za które będziesz ponosić konsekwencje, tj. łatwa możliwość wprowadzania
zmian w przyszłych wersjach. Musisz znaleźć balans, między szybkim wdrożeniem
funkcjonalności, łatwością zrozumienia i utrzymywania kodu i nie
zablokowaniem sobie drogi na wprowadzanie zmian w przyszłości.
Pamiętaj o TDD, YAGNI, DRY, KISS, SOLID, emerging architecture
i over-engineering.

Prowadzący będzie zachowywał się jak Product Owner z niewielką wiedzą
techniczną - 10 lat temu był programistą, a teraz większość czasu spędza
w arkuszu kalkulacyjnym i na spotkaniach. Pamiętaj, że doświadczenie Product
Ownera rzutuje na sposób w jaki pisze kryteria akceptacyjne. Jego kariera
programisty może powodować, że w specyfikacji wymagań pojawią się kwestie
techniczne i sugestie jak dany problem rozwiązać. Musisz to odfiltrować
z treści zadania. Niestety to bardzo częsty scenariusz w branży IT.
Product Owner nie podpowie Ci czy lepiej będzie zrobić to w jakiś konkretny
sposób, albo czy jak zastosujesz to pewne rozwiązanie to jaki będzie wpływ
na przyszłość.


Wymagania
---------
* Zadanie jest specyfikacją wymagań biznesowych
* Rozwiązanie musi spełniać kryteria akceptacyjne
* Nie musisz trzymać się kolejności punktów w zadaniu
* Możesz rozwiązywać problemy inaczej niż jest napisane
* Nie wprowadzaj dodatkowych niezamówionych funkcjonalności
* Wymagania w przyszłości mogą się zmieniać

Nie jest to dokumentacja techniczna. Zadanie opisuje "co ma być",
a nie "jak to robić". Zwróć na to uwagę, bo to ważna różnica!
Masz pełną dowolność. Nie musisz trzymać się kolejności punktów
i podpunktów w zadaniu. Możesz także rozwiązać problemy inaczej
niż jest napisane.

Pamiętaj, że jest to wersja `MVP (Minimum Viable Product)` więc
nie wprowadzaj dodatkowych niezamówionych funkcjonalności
(np. dodatkowych postaci, sprawdzania wychodzenia poza planszę itp.).
Wymagania w przyszłości mogą się zmieniać.


Implementacja
-------------
* Sposób implementacji jest dowolny
* Nie korzystaj z modułów spoza biblioteki standardowej
* Nie przeglądaj rozwiązań ani treści kolejnych części zadania

Możesz wprowadzać dodatkowe pola, metody, funkcje, zmienne, stałe,
klasy, obiekty, unittest lub doctest, type annotation - co tylko
chcesz, ale `nie korzystaj z modułów spoza biblioteki standardowej`.
Wyjątkiem są frameworki do testów (``pytest``, ``behave``, ``hypothesis``, itp).

Nie przeglądaj rozwiązań ani treści kolejnych części zadania.
Jeżeli zaglądniesz w przód, to zepsujesz sobie zabawę i naukę.
To zadanie ma niesamowity potencjał edukacyjny. Nie niszcz go.


Hints
-----
* W zadaniu nie ma błędów (testowane na ponad 300 szkoleniach)


Non-functional Requirements
---------------------------
1. Zapisz (commit) i wypchnij (push) aktualny stan repozytorium
2. W swoim katalogu stwórz pusty katalog ``dragon``
3. W katalogu ``dragon`` stwórz pusty plik ``README.rst``
4. Dodaj plik ``README.rst`` do systemu kontroli wersji
5. Zapisz (commit) zmiany jako "Dragon: NAME", gdzie ``NAME`` to Twoje imię
6. Wypchnij (push) zmiany do repozytorium
7. Zapisz kod do rozwiązania zadania w katalogu ``dragon``
8. Po zakończeniu dodaj wszystkie pliki z ``dragon`` do repozytorium
9. Zapisz i wypchnij zmiany do centralnego repozytorium (Github)
