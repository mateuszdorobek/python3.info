Dragon Sprint 05
================
* Assignment: Dragon Sprint 05
* Complexity: easy
* Time: 8 min


Functional Requirements
-----------------------
1. Użytkownik
   w trakcie gry
   może ustawić smoka w dowolne miejsce ekranu


Use Case
--------
1. Stwórz smoka o nazwie "Wawelski"
2. Ustaw inicjalną pozycję smoka na x=50, y=120
3. Pobierz aktualną pozycję
4. Ustaw nową pozycję na x=10, y=20


Tests
-----
.. code-block:: bdd

    Title: Dragon can be set at any position.

    Scenario 1: Dragon can be set at any position.
    When Dragon is created with name "Wawelski",
    When Dragon is set at position x=1 y=2,
    Then Dragon position is x=1 y=2.


Acceptance Criteria
-------------------
1. Rozwiązanie jest rozwinięciem kodu z poprzedniego sprintu
2. Rozwiązanie jest w katalogu ``dragon``
3. Rozwiązanie jest zapisane w lokalnym repozytorium (``git commit``)
4. Rozwiązanie jest wypchnięta do centralnego repozytorium (``git push``)


Solution
--------
* Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_05.py>`
