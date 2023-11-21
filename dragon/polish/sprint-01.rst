Dragon Sprint 01
================
* Assignment: Dragon Sprint 01
* Complexity: easy
* Time: 8 min


Functional Requirements
-----------------------
1. Użytkownik
   może stworzyć smoka,
   który ma imie


Use Case
--------
1. Stwórz smoka o nazwie "Wawelski"


Tests
-----
.. code-block:: bdd

    Feature: Create Dragon with name.

    Scenario: Prevent creating Dragon without name.
        Given Dragon does not exist,
         When Dragon is created without name,
         Then display error.

    Scenario: Create Dragon with name.
        Given Dragon does not exist,
         When Dragon is created with name "Wawelski",
         Then Dragon exists,
          and Dragon name is "Wawelski".


Acceptance Criteria
-------------------
1. Rozwiązanie jest rozwinięciem kodu z poprzedniego sprintu
2. Rozwiązanie jest w katalogu ``dragon``
3. Rozwiązanie jest zapisane w lokalnym repozytorium (``git commit``)
4. Rozwiązanie jest wypchnięta do centralnego repozytorium (``git push``)


Solution
--------
* Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_01.py>`
