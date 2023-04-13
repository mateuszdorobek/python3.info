"""
* Assignment: Model Define User
* Complexity: easy
* Lines of code: 20 lines
* Time: 8 min

TODO: English Translation

Polish:
    1. Użyj SQLAlchemy Core do stworzenia modeli
    2. Stwórz model `User` dla danych:
        a. Imię
        b. Nazwisko
        c. Data urodzenia
        d. PESEL
        e. Adres email
        f. Telefon z numerem kierunkowym kraju
    3. Wymagania funkcjonalne:
        a. Imię i nazwisko musi być wypełnione
        b. Data urodzenia, PESEL, email i telefon mogą być puste
        c. Adresy email nie mogą się powtarzać
        d. Kolumna lastname oraz pesel powinna być indeksowana
        e. Użytkownik może mieć wiele adresów email i numerów telefonów
    4. Wymagania niefunkcjonalne:
        a. Dodaj pola systemowe i diagnostyczne (`id`, `created`, `modified`)
           jeżeli uważasz to za stosowne
        b. Stwórz definicje modelu
        c. Stwórz relacje
    5. Wymagania systemowe:
        d. Możesz użyć dowolnego modułu z biblioteki standardowej
        e. Nie instaluj ani nie używaj dodatkowych pakietów
        f. Wyjątek: możesz użyć SQLAlchemy do stworzenia modeli
        g. Wyjątek: możesz użyć Alembic do migracji schematu
"""


# Solution
