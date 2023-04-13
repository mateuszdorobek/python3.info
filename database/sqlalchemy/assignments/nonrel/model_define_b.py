"""
* Assignment: Model Define Address
* Complexity: easy
* Lines of code: 20 lines
* Time: 8 min

TODO: English Translation

Polish:
    1. Użyj SQLAlchemy Core do stworzenia modeli
    2. Stwórz model `Address` dla danych:
        a. Rodzaj adresu: rozliczeniowy, dostawy
        b. Ulica wraz z numerem domu i numerem mieszkania
        c. Kod pocztowy
        d. Miasto
        e. Województwo, prowincja lub stan
        f. Kraj
    3. Wymagania funkcjonalne:
        a. Adres może nie mieć ulicy lub kodu pocztowego
        b. Miasto jest indeksowane
        c. Typ nie może być pusty
    4. Wymagania niefunkcjonalne:
        a. Dodaj pola systemowe i diagnostyczne (`id`, `created`, `modified`)
           jeżeli uważasz to za stosowne
        b. Stwórz definicje modelu
        c. Nie twórz żadnych relacji
    5. Wymagania systemowe:
        d. Możesz użyć dowolnego modułu z biblioteki standardowej
        e. Nie instaluj ani nie używaj dodatkowych pakietów
        f. Wyjątek: możesz użyć SQLAlchemy do stworzenia modeli
        g. Wyjątek: możesz użyć Alembic do migracji schematu
"""


# Solution
