Dragon About
============


Sprint 1
--------
* 09:00 - 09:10 - Setup, git commit and push
* 09:10 - 09:15 - Assignment requirements
* 09:15 - 09:25 - Students write code then git commit and push
* 09:25 - 09:40 - Code review of 3 selected participants
* 09:40 - 10:00 - Trainer demonstrates solution
* 10:00 - 10:10 - Coffee Break


Sprint 2
--------
* 10:10 - 10:15 - Assignment requirements
* 10:15 - 10:50 - Students write code then git commit and push
* 10:50 - 11:05 - Code review of 3 selected participants
* 11:05 - 11:50 - Trainer demonstrates solution
* 11:50 - 12:00 - Coffee Break


Sprint 3
--------
* 12:00 - 12:05 - Assignment requirements, setup
* 12:05 - 12:40 - Students write code then git commit and push
* 12:40 - 13:00 - Code review of 3 selected participants
* 13:00 - 13:45 - Trainer demonstrates solution
* 13:30 - 14:15 - Lunch Break


Sprint 4
--------
* 15:30 - 15:35 - Assignment requirements
* 15:35 - 16:00 - Students write code then git commit and push
* 16:00 - 16:15 - Code review of 3 selected participants
* 16:15 - 16:45 - Trainer demonstrates refactoring
* 16:45 - 17:00 - Closing remarks and survey


English
-------
**The task is a simulation of the software development process.**
The Dragon motive is just a narration for demonstration of the object-oriented
programming paradigm and good programming practices. We will not write
a game and we will not discuss game-dev specifics! However we will mention
a few issues related to the specificity of the games (e.g. that the dragon
breathes fire, etc.), but besides that the whole discussion will apply to
any type of IT projects and software engineering problems in virtually each
business domain.

**You - programmer, Trainer - Product Owner.**
In this task you will play the role of a software engineer (programmer),
and the Trainer will act as a Product Owner with little technical knowledge
- 10 years ago he was a programmer, and now he spends most of his time
in a spreadsheet and in meetings. Remember that Product Owner's technical
background influences on the way how he writes the acceptance criteria.
His software engineering career may cause that requirements will include
not only feature specification, but also suggestions on how to solve problems
or implement them. You have to filter it out from the content of the task.
Unfortunately, this is a very common scenario in the IT industry.

**A task is a specification of business requirements.**
It is not a technical documentation. The assignment describes "what should be",
not "how to do it". Mind that, because it's an important difference!

**The method of implementation is up to you.**
You can add additional fields, methods, functions, variables, constants,
classes, objects, unittest or doctest, type annotation - whatever
you want, but `don't use modules outside the standard library`.
The exceptions are test frameworks (``pytest``, ``hypothesis``, etc).

**The solution must meet the acceptance criteria.**
Remember that this is version `1.0` so do not add additional
unspecified functionalities (e.g. additional characters, game board
boundary checks, etc.). For this reason, you don't have to hold on
the order of points and sub-points in the assignment. You can also
solve problems in the different way from what's written.
You have full freedom.

**Product Owner will not advise you on architectural decisions.**
He won't tell you if it's better to do it in a certain way, or what will
be the impact on future if you apply certain solution. You have to make
decisions and bear their consequences, i.e. easy possibility to introduce
changes in future versions. You need to find a balance between fast
implementation functionality, ease of understanding and maintaining the code,
and no blocking yourself from making changes in the future. Remember about
TDD, YAGNI, DRY, KISS, SOLID, emerging architecture and over-engineering.

**Do not search for solutions or the content of the next parts.**
If you look ahead, you will spoil your fun and learning. This assignment
has incredible educational potential. Don't destroy it.

Good luck, have fun!

PS. There are no errors in the assignment (tested on more than 300 trainings)

Non-functional requirements:

    1. Commit and push your current state of repository
    2. In your directory create an empty directory ``dragon``
    3. In ``dragon`` directory create an empty file ``README.rst``
    4. Add file to the version control system (should be automatic)
    5. Commit with message: "Dragon: NAME", where ``NAME`` is your first name
    6. Push changes to the repository
    7. Write a solution to the assignment in ``dragon`` directory
    8. Upon completing add all files in ``dragon`` to repository
    9. Commit and push changes to the central repository (Github)


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

PS. W zadaniu nie ma błędów (testowane na ponad 300 szkoleniach)

Wymagania niefunkcjonalne:

    1. Zapisz (commit) i wypchnij (push) aktualny stan repozytorium
    2. W swoim katalogu stwórz pusty katalog ``dragon``
    3. W katalogu ``dragon`` stwórz pusty plik ``README.rst``
    4. Dodaj plik ``README.rst`` do systemu kontroli wersji
    5. Zapisz (commit) zmiany jako "Dragon: NAME", gdzie ``NAME`` to Twoje imię
    6. Wypchnij (push) zmiany do repozytorium
    7. Zapisz kod do rozwiązania zadania w katalogu ``dragon``
    8. Po zakończeniu dodaj wszystkie pliki z ``dragon`` do repozytorium
    9. Zapisz i wypchnij zmiany do centralnego repozytorium (Github)
