Dragon About
============
.. figure:: img/dragon.gif

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn


Agenda
------
* 09:00 - 09:20 - Assignment introduction (functional and non-functional requirements)
* 09:20 - 10:50 - Students write code
* 10:50 - 11:00 - Git commit and push, break
* 11:00 - 11:40 - Code review (2-3 volunteers)
* 11:40 - 11:45 - Break
* 11:45 - 13:15 - Trainer writes code (TDD)
* 13:15 - 14:00 - Lunch
* 14:00 - 15:30 - Trainer performs refactoring
* 15:30 - 15:45 - Survey, break
* 15:45 - 17:00 - ...


English
-------
* Assignment is simulation of a software development process.
* Assignment is a business requirements specification.
* Solution must fulfill all the acceptance criteria.
* How to implement those criteria is up to you.
* You - programmer, Instructor - Product Owner.
* Product Owner will not help you in architectural decisions.
* Do not check neither solution nor future versions (beta and rc).

Post Notes:

    a. Trainer acts as Product Owner with little technical knowledge
    b. You are the software engineer who need to decide and live with
       consequences of your choices
    c. Task is a narrative story telling to demonstrate OOP
       and good engineering practices
    d. Calculated last position of the game should be x=20, y=40
    e. You can introduce new fields, methods, functions, variables,
       constants, classes, objects, whatever you want
    f. Don't use modules form outside the Python Standard Library
    g. Task is business requirement specification, not a technical
       documentation, i.e., "what Dragon has to do, not how to do it"
    h. You don't have to keep order of specification while writing code
    i. This is `1.0` version, so no new functionality like
       negative position checking etc
    j. You can create tests, i.e.: unittest, doctest
    k. Do not read solution or any future iterations of this exercise;
       if you read future tasks, you will spoil fun and learning

Good luck, have fun!



Polish
------
**Zadanie jest symulacją procesu wytwarzania oprogramowania.**
Motyw Smoka z zadania jest tylko narracją do demonstracji obiektowego
paradygmatu programowania i dobrych praktyk programistycznych. Nie piszemy
gry i nie będziemy omawiali specyfiki game-dev! Siłą rzeczy poruszymy kilka
kwestii z związanych ze specyfiką gier (np. to że smok zieje ogniem itp),
ale całość dyskusji znajdzie zastosowanie do dowolnego rodzaju projektów
informatycznych i problemów inżynierii oprogramowania w każdej domenie
biznesowej.

**Ty - programista, Prowadzący - Product Owner.**
Przy tym zadaniu wcielisz się w rolę inżyniera oprogramowania (programisty),
a Prowadzący będzie zachowywał się jak Product Owner z niewielką wiedzą
techniczną - 10 lat temu był programistą, a teraz większość czasu spędza
w arkuszu kalkulacyjnym i na spotkaniach. Pamiętaj, że doświadczenie Product
Ownera rzutuje na sposób w jaki pisze kryteria akceptacyjne. Jego kariera
programisty może powodować, że w specyfikacji wymagań pojawią się kwestie
techniczne i sugestie jak dany problem rozwiązać. Musisz to odfiltrować
z treści zadania. Niestety to bardzo częsty scenariusz w branży IT.

**Zadanie jest specyfikacją wymagań biznesowych.**
Nie jest to dokumentacja techniczna. Zadanie opisuje "co ma być",
a nie "jak to robić". Zwróć na to uwagę, bo to ważna różnica!

**Sposób implementacji jest dowolny.**
Możesz wprowadzać dodatkowe pola, metody, funkcje, zmienne, stałe,
klasy, obiekty, unittest lub doctest, type annotation - co tylko
chcesz, ale `nie korzystaj z modułów spoza biblioteki standardowej`.
Wyjątkiem są frameworki do testów (``pytest``, ``hypothesis``, itp).

**Rozwiązanie musi spełniać kryteria akceptacyjne.**
Pamiętaj, że jest to wersja `1.0` więc nie wprowadzaj dodatkowych
niezamówionych funkcjonalności (np. dodatkowych postaci, sprawdzania
wychodzenia poza planszę itp.). Z tego powodu nie musisz trzymać się
kolejności punktów i podpunktów w zadaniu, a także rozwiązać problemy
inaczej niż jest napisane. Masz pełną dowolność.

**Product Owner nie doradzi Ci w sprawie decyzji architektonicznych.**
Nie podpowie Ci czy lepiej będzie zrobić to w jakiś konkretny sposób,
albo czy jak zastosujesz to pewne rozwiązanie to jaki będzie wpływ na
przyszłość. Zadanie polega na tym, że to Ty musisz podejmować decyzje
i ponosić ich konsekwencje, tj. łatwa możliwość wprowadzania zmian w
przyszłych wersjach. Musisz znaleźć balans, między wdrożeniem szybkim
funkcjonalności, łatwością zrozumienia i utrzymywania kodu i nie
zablokowaniem sobie drogi na wprowadzanie zmian w przyszłości.
Pamiętaj o TDD, YAGNI, DRY, KISS, SOLID, emerging architecture
i over-engineering.

**Nie przeglądaj rozwiązań ani treści kolejnych części zadania.**
Jeżeli zaglądniesz w przód, to zepsujesz sobie zabawę i naukę.
To zadanie ma niesamowity potencjał edukacyjny. Nie niszcz go.

Powodzenia i miłej zabawy!
