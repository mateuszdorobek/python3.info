Dragon Sprint 11
================
* Assignment: Dragon Sprint 11
* Complexity: easy
* Time: 13 min


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
12. Smok zadaje obrażenia (losowo 5-20)
13. Zadaj 10 obrażeń smokowi
14. Zadaj 20 obrażeń smokowi
15. Zadaj 30 obrażeń smokowi
16. Zadaj 40 obrażeń smokowi
17. Zadaj 50 obrażeń smokowi


Tests
-----
.. code-block:: bdd

    Feature: Dragon's health

    Scenario: Dragon dies and display message
        Given Dragon is created with name "Wawelski"
         When Dragon health is 0
         Then text "Dragon NAME is dead" is displayed

    Scenario: Dragon dies and display gold
        Given Dragon is created with name "Wawelski"
         When Dragon health is 0
         Then text "AMOUNT gold dropped" is displayed


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
* :download:`Solution <assignments/dragon_sprint_11.py>`
