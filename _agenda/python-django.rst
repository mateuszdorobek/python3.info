Python: Django
==============
* https://www.sages.pl/szkolenia/python-django


Polish
------
1. Wprowadzenie do Django:

    * Instalacja Django
    * Plik konfiguracyjny
    * manage.py i jego opcje
    * Wbudowany serwer HTTP (nasłuchiwanie lokalne oraz na wszystkich interfejsach)
    * IDE oraz narzędzia dla programistów
    * Przykłady serwisów wykorzystujących Django

2. Projekty:

    * Pojęcie projektu Django
    * Tworzenie nowego projektu

3. Aplikacje:

    * Pojęcie projektu i aplikacji Django
    * Tworzenie nowej aplikacji
    * Struktura aplikacji
    * Reużywalność

4. Modele:

    * Modele w Django
    * Typy pól
    * Relacje między modelami
    * Parametry pól, unikalność, wartości null, indeks w bazie, wymagalność pól
    * Ograniczenie wyboru
    * Auto uzupełnianie dat
    * Walidatory
    * Migracje i ich obsługa
    * Dump danych i przywracanie z backupu
    * Klasa Meta

5. Panel administracyjny:

    * Tworzenie superusera
    * Konfiguracja panelu administracyjnego
    * Wyszukiwanie, filtrowanie, autocomplete
    * Tworzenie własnych filtrów
    * Rejestracja modeli
    * Fieldset, Radio Buttony, Checkboxy
    * Widgety
    * Annotated Fields
    * StackedInline i TabularInline
    * Wyświetlanie własnych pól za pomocą list_display
    * Ograniczanie listy wyników (get_queryset)
    * Miękkie kasowanie danych (bez usuwania z bazy)
    * Paginacja
    * Wstrzykiwanie własnych skryptów Java Script oraz styli CSS
    * Modyfikacja wyglądu panelu administracyjnego przez nadpisywanie template’ów

6. ORM:

    * Tworzenie prostych zapytań przy pomocy ORM
    * Tworzenie obiektów, zapis do bazy, aktualizacja
    * Pobieranie obiektów, filtrowanie, łączenie zapytań, sortowanie
    * Zaawansowane zapytania: obiekty Q, wyrażenia F, grupowanie i agregacje
    * Wiele baz danych na raz
    * Inżynieria wsteczna bazy (inspectdb)
    * Podglądanie zapytań do bazy danych
    * Managery dla modeli

7. Routing URL:

    * Wprowadzenie do wyrażeń regularnych
    * Mechanizmy rozwiązywania URL przez Django
    * Łączenie widoków z odpowiednimi URL
    * Rozwiązywanie wsteczne URL
    * Przekierowania
    * Wersjonowanie

8. Widoki:

    * Statusy HTTP, nagłówki zapytań i odpowiedzi
    * Widoki klasowe i funkcyjne
    * Widoki generyczne
    * Widoki asynchroniczne
    * Obsługa błędów
    * Obsługa różnych typów zapytań (JSON, HTTP, CSV)
    * Odczytywanie danych z zapytania
    * Dekoratory ograniczające dostęp

9. Szablony:

    * Składnia szablonów: Zmienne, Znaczniki, Filtry
    * Obsługa URL
    * Hierarcha, dziedziczenie i separacja powtarzalnych części kodu
    * Templatetag
    * Pliki statyczne: obrazki, css, java script

10. Formularze:

    * Klasa Form: typy, definiowanie pól formularza
    * Wyświetlanie formularzy
    * Walidacja formularza
    * Obsługa błędów
    * Tworzenie formularzy bezpośrednio z modelu
    * CSRF

11. Middleware:

    * Mechanizm przetwarzania żądań
    * Tworzenie własnych middleware

12. i18n, l10n:

    * Obsługa różnych formatów dat
    * Praca ze strefami czasowymi
    * Tłumaczenie szablonów i nazw pól (ugettext_lazy)
    * Obsługa różnych formatów numerycznych
    * Tłumaczenie plików Java Script

13. Autoryzacja i uwierzytelnianie w aplikacji Django:

    * System uwierzytelniania Django (django.contrib.auth)
    * Logowanie
    * Mechanizm sesji
    * Definiowanie uprawnień dla użytkownika i grup
    * Ograniczanie dostępu do widoków

14. API:

    * Tworzenie własnych endpointów
    * Obsługa zapytań POST, GET, PUT, PATCH, HEAD, OPTIONS
    * Wersjonowanie API
    * Django REST API
    * Websockets
    * Generowanie dokumentacji do API
    * Django Extensions Graph
    * CSRF oraz CORS

15. Custom Fields:

    * Tworzenie własnych pól

16. Django i skrypty:

    * Tworzenie skryptów wykorzystujących modele i ORM Django
    * Tworzenie własnych Management Commands

17. Testowanie aplikacji Django:

    * Wprowadzenie do modułu django.test
    * Klasa TestCase i asercje specyficzne dla Django
    * Klient Testowy
    * Klasa Response
    * Fixtures
    * Django Debug Toolbar
    * CI/CD aplikacji Django

18. Aplikacja Django w środowisku produkcyjnym:

    * Nginx, uWSGI, async WSGI
    * Serwer Gunicorn
    * Serwowanie plików statycznych i korzystanie z CDN np. AWS S3
    * Docker i Kubernetes
    * Cache


English
-------
1. Introduction to Django:

    * Installation
    * Configuration and settings file
    * manage.py and built-in management commands
    * Built-in HTTP server (listening on localhost on all interfaces)
    * Integrated Development Environment (IDE) debugging tools
    * Real-life services and platforms using Django

2. Projects:

    * Concept of Django projects
    * Creating new project
    * Directory structure

3. Apps:

    * Concept of Django app
    * Creating new app
    * Directory structure
    * Reusability

4. Models:

    * Concept of Django models
    * Field types
    * Model relations
    * Field parameters: unique, null, index, required, limit choices to
    * Date and time autocompletion on create and modify
    * Validators
    * Migrations creation and application
    * Database dump and restore
    * Meta class and model configuration

5. Administration panel:

    * Creating superusers
    * Model registration
    * Admin panel configuration
    * Searching, filtering, autocomplete
    * Custom filters
    * Fieldset, Radio Buttons, Checkboxes
    * Widgets
    * Annotated Fields
    * StackedInline and TabularInline
    * Custom fields and function results in list_display
    * Limiting admin panel query-sets (get_queryset)
    * Data soft-delete (deletion without removing from database)
    * Pagination
    * Injecting JavaScript and CSS styles
    * Admin panel customization by overriding templates

6. Object-Relational Mapper (ORM):

    * Creating simple queries using Django ORM
    * Creating objects, database saves and updates
    * Querying objects, filtering, joining and sorting
    * Advanced queries: Q objects, F expressions, grouping and aggregations
    * Multiple databases and DB routing
    * Database reverse engineering (inspectdb)
    * Database queries debugging and profiling
    * Model Managers

7. URL Routing:

    * Introduction to regular expressions
    * Django URL resolve mechanism
    * URL-Views mapping
    * Reverse URL resolution
    * Redirects
    * API Versioning

8. Views:

    * HTTP statuses, response and request headers
    * Class and function based views
    * Generic views
    * Asynchronous views
    * Error handling
    * Handling JSON, HTTP, CSV responses
    * Request data access
    * Permission model and decorators limiting access

9. Templates:

    * Template Syntax: variables, tags, filters
    * URL handling
    * Template hierarchy, inheritance and reusability
    * Templatetags
    * Static files: images, css, javascript

10. Forms:

    * Form class: types, defining form fields
    * Displaying forms
    * Form validation
    * Error handling
    * Model-based forms
    * CSRF

11. Middleware:

    * Request-response processing injection mechanisms
    * Creating custom middleware

12. i18n, l10n:

    * Date formatting
    * Timezones
    * Text translation (gettext_lazy)
    * Numeric values internationalization
    * JavaScript files internationalization

13. Authorization and authentication:

    * Django auth system (django.contrib.auth)
    * Logging
    * Sessions mechanism
    * Permission systems, apps, groups, users
    * Limiting access to views

14. API:

    * Endpoint set-up
    * Handling requests: POST, GET, PUT, PATCH, HEAD, OPTIONS
    * API versioning
    * Django REST API
    * Websockets
    * API documentation generation
    * Django Extensions Graph
    * CSRF and CORS

15. Custom Model Fields:

    * Creating custom model fields
    * Serialization problems

16. Django management commands:

    * Custom Python scripts using Django framework
    * Custom Management Commands

17. Testing:

    * Introduction to django.test module
    * TestCase class and Django specific assertions
    * Test Client
    * Response class
    * Fixtures
    * Django Debug Toolbar
    * CI/CD

18. Django in production environment:

    * Nginx configuration, SSL certificates, proxy_pass
    * Gunicorn, uWSGI, async WSGI
    * CDN staticfiles serving using AWS S3
    * Docker and Kubernetes deployment
    * Caching mechanism
    * Session caching
