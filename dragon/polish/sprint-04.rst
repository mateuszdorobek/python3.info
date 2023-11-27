Dragon Sprint 04
================
* Assignment: Dragon Sprint 04
* Complexity: easy
* Time: 13 min


Functional Requirements
-----------------------
1. Smok
   przy tworzeniu
   może mieć ustawioną pozycję na ekranie


Use Case
--------
1. Stwórz smoka
2. Stwórz smoka o nazwie "Wawelski"
3. Stwórz smoka bez nazwy
4. Smok przy tworzeniu ma losowe punkty życia
5. Ustaw inicjalną pozycję smoka na x=50, y=100


Tests
-----
.. code-block:: bdd

    Feature: Dragon's position

    Scenario: Create Dragon with default position
        Given Dragon does not exist
         When Dragon is created with name "Wawelski"
         Then Dragon exists
          and position is x=0 y=0

    Scenario: Create Dragon with initial position
        Given Dragon does not exist
         When Dragon is created with name "Wawelski" and position x=50 y=100
         Then Dragon exists
          and Dragon position is x=50 y=100


Acceptance Criteria
-------------------
1. Rozwiązanie jest rozwinięciem kodu z poprzedniego sprintu
2. Rozwiązanie jest w katalogu ``dragon``
3. Rozwiązanie jest zapisane w lokalnym repozytorium (``git commit``)
4. Rozwiązanie jest wypchnięta do centralnego repozytorium (``git push``)


Solution
--------
* Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_04.py>`
