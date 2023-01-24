Python: FastAPI
===============
* https://www.sages.pl/szkolenia/python-fastapi


Polish
------
1. Wprowadzenie do FastAPI:

    * Instalacja FastAPI i środowiska uruchomieniowego
    * Wbudowany serwer HTTP (nasłuchiwanie lokalne oraz na wszystkich interfejsach)
    * IDE oraz narzędzia dla programistów

2. Protokół HTTP:

    * Request-Response
    * Metody protokołu (czasowniki HTTP)
    * Nagłówki żądań i odpowiedzi
    * Statusy
    * Mimetype
    * Uwierzytelnianie
    * Pobieranie danych z serwera
    * Przesyłanie danych do serwera
    * Debugging
    * HTTPS
    * Uwierzytelnianie

3. Type annotations:

    * Typy
    * Sekwencje
    * Mapy
    * Funkcje
    * Klasy

4. Projekty FastAPI:

    * Konwencja nazewnicza
    * Podział projektu na wiele plików
    * Mechanizm importów
    * Reużywalność
    * Wersjonowanie API

5. Schematy Pydantic:

    * Omówienie Pydantic
    * Tworzenie schematów
    * Konwersja i walidacja

6. Widoki synchroniczne:

    * URL Routing
    * Obsługa zapytań GET, POST, PUT, DELETE
    * Parametry w URL, parametry żądania
    * Nagłówki zapytań i odpowiedzi
    * Schematy wejściowe i wyjściowe
    * Kody statusu, tagi

7. Dokumentacja:

    * Swagger, redoc
    * Korzystanie ze Swagger w procesie wytwarzania oprogramowania

8. Modele bazy danych:

    * Modele w SQLAlchemy
    * Typy pól
    * Relacje między modelami
    * Parametry pól, unikalność, wartości null, indeks w bazie, wymagalność pól
    * Migracje schematów bazy za pomocą Alembic i ich obsługa
    * Schematy dla modeli ORM
    * Tworzenie zapytań przy pomocy ORM
    * Tworzenie obiektów, zapis do bazy, aktualizacja
    * Pobieranie obiektów, filtrowanie, łączenie zapytań, sortowanie
    * Podglądanie zapytań do bazy danych

9. Middleware:

    * Mechanizm przetwarzania żądań
    * Tworzenie własnych middleware

10. Autoryzacja i uwierzytelnianie:

    * System uwierzytelniania JSON Web Token (JWT)
    * Logowanie
    * Mechanizm sesji
    * Definiowanie uprawnień dla użytkownika i grup
    * Ograniczanie dostępu do widoków

11. Websockets:

    * Omówienie technologii
    * Prosta implementacja

12. Widoki asynchroniczne:

    * Korzystanie z widoków asynchronicznych
    * Ograniczenia
    * Biblioteki async

13. Testowanie API:

    * Debugging
    * Fixtures
    * CI/CD aplikacji FastAPI

14. Aplikacja FastAPI w środowisku produkcyjnym:

    * Uvicorn, ASGI (async WSGI)
    * Docker i Kubernetes

15. Architektura mikroserwisowa:

    * Architektura mikroserwisowa
    * Skalowalność
    * BFF - Backend for Frontend
    * API Gateway
    * Load Balancing
