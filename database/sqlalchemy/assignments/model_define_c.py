"""
* Assignment: Model Define ProductOrders
* Complexity: medium
* Lines of code: 20 lines
* Time: 13 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Stwórz model `User` z polami:
        a. firstname - imię
        b. lastname - nazwisko
        c. born - data urodzenia
        d. ssn - PESEL
        e. email - adres email
        f. phone - telefon z numerem kierunkowym kraju
    2. Stwórz model `Address` z polami:
        a. type - rodzaj adresu: rozliczeniowy, dostawy
        b. street - ulica, numer domu, numer mieszkania
        c. postcode - kod pocztowy
        d. city - miasto
        e. region - województwo lub stan
        f. country - kraj
    3. Stwórz model `Product`:
        a. ean13 - Kod kreskowy EAN-13
        b. name - Nazwa produktu
        c. price - Cena netto
    4. Stwórz model `Orders`:
        a. user - Użytkownik
        b. product - Produkt
    5. Wymagania funkcjonalne:
        a. Użytkownik ma tylko jeden email i jeden telefon
        b. Użytkownik może mieć jeden adres rozliczeniowy i jeden do wysyłki
        c. Adres może nie mieć ulicy lub kodu pocztowego
        d. Użytkownik może zakupić wiele produktów
        e. Produkt mógł nie zostać kupiony
    6. Wymagania niefunkcjonalne:
        a. Użyj SQLAlchemy ORM do stworzenia modeli
        b. Dodaj pola `id` jeżeli są potrzebne
        c. Możesz użyć dowolnego modułu z biblioteki standardowej
        d. Możesz użyć SQLAlchemy i Alembic
        e. Nie instaluj ani nie używaj dodatkowych pakietów
"""


# Solution
