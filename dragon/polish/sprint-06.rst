Dragon Sprint 06
================
* Assignment: Dragon Sprint 06
* Complexity: easy
* Time: 8 min


Functional Requirements
-----------------------
1. Smok
   w trakcie gry
   może być ustawiony w dowolne miejsce ekranu


Use Case
--------
1. Stwórz smoka
2. Stwórz smoka o nazwie "Wawelski"
3. Stwórz smoka bez nazwy
4. Smok przy tworzeniu ma losowe punkty życia
5. Ustaw inicjalną pozycję smoka na x=50, y=100
6. Pobierz aktualną pozycję
7. Ustaw nową pozycję na x=10, y=20


Tests
-----
.. code-block:: bdd

    Feature: Dragon's position

    Scenario: Dragon can be set at any position
        Given Dragon is created with name "Wawelski"
         When Dragon sets position x=1 y=2
         Then Dragon position is x=1 y=2


Acceptance Criteria
-------------------
1. Rozwiązanie jest rozwinięciem kodu z poprzedniego sprintu
2. Rozwiązanie jest w katalogu ``dragon``
3. Rozwiązanie jest zapisane w lokalnym repozytorium (``git commit``)
4. Rozwiązanie jest wypchnięta do centralnego repozytorium (``git push``)


Solution
--------
* Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_06.py>`
