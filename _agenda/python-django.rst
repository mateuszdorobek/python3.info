Python: Tworzenie webaplikacji w Django
=======================================
* https://www.sages.pl/szkolenia/python-django


Polish
------
* Wprowadzenie do Django
	* Instalacja Django
	* Plik konfiguracyjny
	* manage.py i jego opcje
	* Wbudowany serwer HTTP (nasłuchiwanie lokalne oraz na wszystkich interfejsach)
	* IDE oraz narzędzia dla programistów
	* Przykłady serwisów wykorzystujących Django
* Projekty
	* Pojęcie projektu Django
	* Tworzenie nowego projektu
* Aplikacje
	* Pojęcie projektu i aplikacji Django
	* Tworzenie nowej aplikacji
	* Struktura aplikacji
	* Reużywalność
* Modele
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
* Panel administracyjny
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
* ORM
	* Tworzenie prostych zapytań przy pomocy ORM
	* Tworzenie obiektów, zapis do bazy, aktualizacja
	* Pobieranie obiektów, filtrowanie, łączenie zapytań, sortowanie
	* Zaawansowane zapytania: obiekty Q, wyrażenia F, grupowanie i agregacje
	* Wiele baz danych na raz
	* Inżynieria wsteczna bazy (inspectdb)
	* Podglądanie zapytań do bazy danych
	* Managery dla modeli
* Routing URL
	* Wprowadzenie do wyrażeń regularnych
	* Mechanizmy rozwiązywania URL przez Django
	* Łączenie widoków z odpowiednimi URL
	* Rozwiązywanie wsteczne URL
	* Przekierowania
	* Wersjonowanie
* Widoki
	* Statusy HTTP, nagłówki zapytań i odpowiedzi
	* Widoki klasowe i funkcyjne
	* Widoki generyczne
	* Widoki asynchroniczne
	* Obsługa błędów
	* Obsługa różnych typów zapytań (JSON, HTTP, CSV)
	* Odczytywanie danych z zapytania
	* Dekoratory ograniczające dostęp
* Szablony
	* Składnia szablonów: Zmienne, Znaczniki, Filtry
	* Obsługa URL
	* Hierarcha, dziedziczenie i separacja powtarzalnych części kodu
	* Templatetag
	* Pliki statyczne: obrazki, css, java script
* Formularze
	* Klasa Form: typy, definiowanie pól formularza
	* Wyświetlanie formularzy
	* Walidacja formularza
	* Obsługa błędów
	* Tworzenie formularzy bezpośrednio z modelu
	* CSRF
* Middleware
	* Mechanizm przetwarzania żądań
	* Tworzenie własnych middleware
* i18n, l10n
	* Obsługa różnych formatów dat
	* Praca ze strefami czasowymi
	* Tłumaczenie szablonów i nazw pól (ugettext_lazy)
	* Obsługa różnych formatów numerycznych
	* Tłumaczenie plików Java Script
* Autoryzacja i uwierzytelnianie w aplikacji Django
	* System uwierzytelniania Django (django.contrib.auth)
	* Logowanie
	* Mechanizm sesji
	* Definiowanie uprawnień dla użytkownika i grup
	* Ograniczanie dostępu do widoków
* API
	* Tworzenie własnych endpointów
	* Obsługa zapytań POST, GET, PUT, PATCH, HEAD, OPTIONS
	* Wersjonowanie API
	* Django REST API
	* Websockets
	* Generowanie dokumentacji do API
	* Django Extensions Graph
	* CSRF oraz CORS
* Custom Fields
	* Tworzenie własnych pól
* Django i skrypty
	* Tworzenie skryptów wykorzystujących modele i ORM Django
	* Tworzenie własnych Management Commands
* Testowanie aplikacji Django
	* Wprowadzenie do modułu django.test
	* Klasa TestCase i asercje specyficzne dla Django
	* Klient Testowy
	* Klasa Response
	* Fixtures
	* Django Debug Toolbar
	* CI/CD aplikacji Django
* Aplikacja Django w środowisku produkcyjnym
	* Nginx, uWSGI, async WSGI
	* Serwer Gunicorn
	* Serwowanie plików statycznych i korzystanie z CDN np. AWS S3
	* Docker i Kubernetes
	* Cache
