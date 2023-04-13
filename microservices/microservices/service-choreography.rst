Microservices Choreography
==========================
* Choreografia: informujemy system o zdarzeniu
* Choreografia: system subskrybuje się do eventów
* Choreografia: system reaguje na zmiany stanów
* Orkiestracja: usługa jest odpowiedzialna za informację o zmianie stanu
* Choreografia > Orkiestracja


Hermes
------
* https://github.com/allegro/hermes
* usługa subskrybuje się do danego topicu
* gdy zajdzie zdarzenie
* system wypycha je do subskrybentów
* nakładka na `Apache Kafka`
* zarządza dostarczaniem wiadomości `only once policy`
* throttling
* load ballancing
* security policy dla wiadomości
* można zapchać sieć, gdy ma się zcentralizowaną infrastrukturę
* wykorzystanie HTTP/2.0 (multipleksowanie połączeń http, kompresja nagłówków, TLS)
* Jeżeli jedna usługa pada i to pociąga za sobą cały system, to nie jest to architektura `Microservices`.

.. figure:: img/microservices-hermes.png

.. note:: Jeżeli jedna usługa pada i to pociąga za sobą cały system, to nie jest to architektura `Microservices`.
