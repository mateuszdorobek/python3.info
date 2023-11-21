Dragon Sprint 03
================
* Assignment: Dragon Sprint 03
* Complexity: easy
* Time: 8 min


Functional Requirements
-----------------------
1. Użytkownik
   przy tworzeniu smoka
   może ustawić pozycję smoka na ekranie


Use Case
--------
1. Stwórz smoka o nazwie "Wawelski"
2. Ustaw inicjalną pozycję smoka na x=50, y=120


Tests
-----
.. code-block:: bdd

    Feature: Create Dragon with position.

    Scenario: Create Dragon with default position.
        Given Dragon does not exist,
         When Dragon is created with name "Wawelski",
         Then Dragon exists,
          and position is x=0 y=0.

    Scenario: Create Dragon with initial position.
        Given Dragon does not exist,
         When Dragon is created with name "Wawelski" and position x=50 y=120,
         Then Dragon exists,
          and Dragon position is x=50 y=120.


Acceptance Criteria
-------------------
1. Rozwiązanie jest rozwinięciem kodu z poprzedniego sprintu
2. Rozwiązanie jest w katalogu ``dragon``
3. Rozwiązanie jest zapisane w lokalnym repozytorium (``git commit``)
4. Rozwiązanie jest wypchnięta do centralnego repozytorium (``git push``)


Solution
--------
* Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_03.py>`
