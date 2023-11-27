Dragon Sprint 02
================
* Assignment: Dragon Sprint 02
* Complexity: easy
* Time: 8 min


Functional Requirements
-----------------------
1. Smok
   przy tworzeniu
   wyświetla błąd jeżeli nie ma imienia


Use Case
--------
1. Stwórz smoka
2. Stwórz smoka o nazwie "Wawelski"
3. Stwórz smoka bez nazwy


Tests
-----
.. code-block:: bdd

    Feature: Dragon create

    Scenario: Create Dragon without name (display an error)
        Given Dragon does not exist
         When Dragon is created without name
         Then display error


Acceptance Criteria
-------------------
1. Rozwiązanie jest rozwinięciem kodu z poprzedniego sprintu
2. Rozwiązanie jest w katalogu ``dragon``
3. Rozwiązanie jest zapisane w lokalnym repozytorium (``git commit``)
4. Rozwiązanie jest wypchnięta do centralnego repozytorium (``git push``)


Solution
--------
* Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Solution <assignments/dragon_sprint_02.py>`
