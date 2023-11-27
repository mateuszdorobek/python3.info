Dragon Sprint 00
================
* Assignment: Dragon Sprint 00
* Complexity: easy
* Time: 8 min


Functional Requirements
-----------------------
1. Kontroler
   podczas gry
   może stworzyć smoka


Use Case
--------
1. Stwórz smoka


Tests
-----
.. code-block:: bdd

    Feature: Dragon create

    Scenario: Create Dragon
        Given Dragon does not exist
         When Dragon is created
         Then Dragon exists


Acceptance Criteria
-------------------
1. Rozwiązanie jest w katalogu ``dragon``
2. Rozwiązanie jest zapisane w lokalnym repozytorium (``git commit``)
3. Rozwiązanie jest wypchnięta do centralnego repozytorium (``git push``)


Solution
--------
* Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_00.py>`
