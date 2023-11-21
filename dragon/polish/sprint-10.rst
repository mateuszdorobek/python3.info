Dragon Sprint 10
================
* Assignment: Dragon Sprint 10
* Complexity: easy
* Time: 8 min


Functional Requirements
-----------------------
1. Smok
   gdy zginie
   na ekranie wyświetla się komunikat ``Dragon NAME is dead``, gdzie `NAME` to nazwa smoka

2. Smok
   gdy zginie
   na ekranie wyświetla się ile złota wypadło (losowa liczba od 1 do 100)


Use Case
--------
1. Stwórz smoka o nazwie "Wawelski"
2. Ustaw inicjalną pozycję smoka na x=50, y=120
3. Pobierz aktualną pozycję
4. Ustaw nową pozycję na x=10, y=20
5. Przesuń smoka w lewo o 10 i w dół o 20
6. Przesuń smoka w lewo o 10 i w prawo o 15
7. Przesuń smoka w prawo o 15 i w górę o 5
8. Przesuń smoka w dół o 5
9. Smok zadaje obrażenia (losowo 5-20)
10. Zadaj 10 obrażeń smokowi
11. Zadaj 20 obrażeń smokowi
12. Zadaj 30 obrażeń smokowi
13. Zadaj 40 obrażeń smokowi
14. Zadaj 50 obrażeń smokowi


Tests
-----
.. code-block:: bdd

    Feature: Dragon dies with message and drops gold

    Scenario: Dragon dies and display message
        Given Dragon is created with name "Wawelski"
         When Dragon health is 0
         Then display "Dragon NAME is dead"

    Scenario: Dragon dies and display gold
        Given Dragon is created with name "Wawelski"
         When Dragon health is 0
         Then display "AMOUNT gold dropped"


Acceptance Criteria
-------------------
1. Rozwiązanie jest rozwinięciem kodu z poprzedniego sprintu
2. Rozwiązanie jest w katalogu ``dragon``
3. Rozwiązanie jest zapisane w lokalnym repozytorium (``git commit``)
4. Rozwiązanie jest wypchnięta do centralnego repozytorium (``git push``)


Hints
-----
* ``from random import randint``
* ``randint(a, b)`` - random integer between ``a`` and ``b`` (inclusive!)


Solution
--------
* Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_10.py>`
