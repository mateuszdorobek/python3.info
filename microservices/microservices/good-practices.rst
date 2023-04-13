Microservices Good Practices
============================


Transaction log tailing
-----------------------
* Reliably publish events whenever state changes by tailing the transaction log.


Dobre praktyki
--------------
* nigdy nie zaczynaj od mikroserwisów od dnia pierwszego
* zbyt wczesne rozdzielanie aplikacji na wczesnym poziomie może prowadzić do wielu problemów
* nie tworzyć mikroserwisów CRUDów dla danych (np. user GET, DELETE, PUT, POST, PATCH)
* mikroserwisy muszą odwzorowywać domenę biznesową
* zawsze używaj wersjonowania api
* zawsze bądź backward compatible
* walidować dane między requestami
* Przepisanie microservices jako osobny katalog z podziałem na tematy
* Przepisanie microservices jako osobne szkolenie
* Reactive manifesto, reactive programming
* spock framework
* Blockchain uruchamianie kodu
* Function as a Service
* Database sharding
* Przykład edok w cloud i bazy po stronie klienta


References
----------
* https://www.youtube.com/watch?v=X0tjziAQfNQ
* https://www.youtube.com/watch?v=gfh-VCTwMw8
