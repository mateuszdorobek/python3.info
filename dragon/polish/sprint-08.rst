Dragon Sprint 08
================
* Assignment: Dragon Sprint 08
* Complexity: easy
* Time: 8 min


Functional Requirements
-----------------------
1. Smok
   w trakcie gry
   może zadawać losowe obrażenia z przedziału od 5 do 20


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


Tests
-----
.. code-block:: bdd

    Feature: Dragon's damage

    Scenario: Dragon can make random damage between 5 and 20
        Given Dragon is created with name "Wawelski"
         When Dragon makes damage
         Then value is between 5 and 20


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
* :download:`Solution <assignments/dragon_sprint_08.py>`
