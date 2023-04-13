Microservice Lifecycle
======================
* Przepisywanie architektury
* Tworzenie nowej usługi
* Testowanie
* Platforma uruchamiania
* Monitoring
* SLA usług


Przepisywanie architektury
--------------------------
* Anti Corruption Layer (ACL)
* Tworzenie nowych funckonalności na nowej platformie
* zapewnienie spójności systemów
* kontrola czy dane w nowym systemie są spójne z nowym
* przepisywanie całości
* wdrożenie ludzi
* zatrudnianie w nowej technologii
* konwersja obecnych pracowników

.. figure:: img/microservices-sidecar.png

    Architektura systemu zgodna z Sidecar

.. figure:: img/microservices-anti-corruption-layer.png

    Anti Corruption Layer


Tworzenie nowej usługi
----------------------
* end to end
* założenie repo w Bitbucket
* projekt w JIRA
* CI/CD
* Deployment
* Repozytorium artefaktów
* Publikowanie metryk
* Testy security
* Monitoring i logowanie
* `one-click-project`
* automatyzacja powtarzających się czynności za pomocą toolingu
* Microservice Chassis
* Build your microservices using a microservice chassis framework, which handles cross-cutting concerns
* Spring Boot, Spring Cloud, Dropwizard


Testowanie
----------
* https://martinfowler.com/articles/microservice-testing/
* Historia ze stubami w dużym polskim telecomie


Platforma uruchamiania
----------------------
* Usługi uruchamiane w różnych datacenter jednocześnie
* Wykorzystanie public i private cloud jednocześnie
* Kubernetes
* Tworzenie logicznego klastra, który przykrywa infrastrukturę
* Możliwość dzielenia klastra na biznesowe komponenty i przydzielenia im zasobów
* Możliwość definiowania wykorzystywanych zasobów przez usługę
* Dynamiczne alokowanie zasobów


Monitoring
----------
* automatyczne zapinanie metryk do usług
* raportowanie poziomu SLA
* alerting
* definiowanie progów alertowania
* wykrywanie anomalii (na podstawie dotychczasowej historii, machine learning)


SLA usług
---------
* Definiowanie SLA
* Koszt inwestycji w zwiększenie dostępności np. z 4 na 5 dziewiątek)
* ROI z wprowadzenia poszczególnych usług
* zmienjszone latency
* większa stabilność
* większa redundantność
* Każdy system może mieć inną charakterystykę i inne cechy
