Dragon Sprint 07
===============
* Assignment: Dragon Sprint 07
* Complexity: easy
* Time: 13 min


Functional Requirements
-----------------------
1. Smok
   w trakcie gry
   może być przesuwany w prawo o zadaną wartość

2. Smok
   w trakcie gry
   może być przesuwany w lewo o zadaną wartość

3. Smok
   w trakcie gry
   może być przesuwany w dół o zadaną wartość

4. Smok
   w trakcie gry
   może być przesuwany do góry o zadaną wartość

5. Smok
   w trakcie gry
   może być jednocześnie przesuwany horyzontalnie (w lewo, w prawo)

6. Smok
   w trakcie gry
   może być jednocześnie przesuwany wertykalnie (w górę i w dół)

7. Smok
   w trakcie gry
   może być jednocześnie przesuwany dookólnie (w lewo, w prawo, w górę i w dół)


Non-Functional Requirements
---------------------------
1. Przyjmij górny lewy róg ekranu za punkt początkowy
2. Idąc w prawo dodajesz ``x``
3. Idąc w lewo odejmujesz ``x``
4. Idąc w górę odejmujesz ``y``
5. Idąc w dół dodajesz ``y``


Use Case
--------
1. Stwórz smoka
2. Stwórz smoka o nazwie "Wawelski"
3. Stwórz smoka bez nazwy
4. Smok przy tworzeniu ma losowe punkty życia
5. Ustaw inicjalną pozycję smoka na x=50, y=100
6. Pobierz aktualną pozycję
7. Ustaw nową pozycję na x=10, y=20
8. Przesuń smoka w lewo o 10 i w dół o 20
9. Przesuń smoka w lewo o 10 i w prawo o 15
10. Przesuń smoka w prawo o 15 i w górę o 5
11. Przesuń smoka w dół o 5


Tests
-----
.. code-block:: bdd

    Feature: Dragon's position

    Scenario: Dragon moves left
        Given Dragon is created with name "Wawelski" and position x=10 y=20
         When Dragon move left by 1
         Then Dragon position is x=9 y=20

    Scenario: Dragon moves right
        Given Dragon is created with name "Wawelski" and position x=10 y=20
         When Dragon move right by 1
         Then Dragon position is x=11 y=20

    Scenario: Dragon moves down
        Given Dragon is created with name "Wawelski" and position x=10 y=20
         When Dragon move down by 1
         Then Dragon position is x=10 y=21

    Scenario: Dragon moves up
        Given Dragon is created with name "Wawelski" and position x=10 y=20
         When Dragon move up by 1
         Then Dragon position is x=10 y=19

    Scenario: Dragon moves horizontal
        Given Dragon is created with name "Wawelski" and position x=10 y=20
         When Dragon move left by 1 and right by 2
         Then Dragon position is x=11 y=20

    Scenario: Dragon moves vertical
        Given Dragon is created with name "Wawelski" and position x=10 y=20
         When Dragon move up by 1 and down by 2
         Then Dragon position is x=10 y=21

    Scenario: Dragon moves omnidirectional
        Given Dragon is created with name "Wawelski" and position x=10 y=20
         When Dragon move left by 1 and right by 2 and up by 3 and left by 4
         Then Dragon position is x=11 y=21


Acceptance Criteria
-------------------
1. Rozwiązanie jest rozwinięciem kodu z poprzedniego sprintu
2. Rozwiązanie jest w katalogu ``dragon``
3. Rozwiązanie jest zapisane w lokalnym repozytorium (``git commit``)
4. Rozwiązanie jest wypchnięta do centralnego repozytorium (``git push``)


Hints
-----
* To nie błąd: "lewo o 10 i w prawo o 15"
* Pozycja końcowa powinna być: x=20, y=40


Solution
--------
* Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_07.py>`
