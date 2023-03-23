"""
* Assignment: Loop While GuessGame1
* Required: no
* Complexity: medium
* Lines of code: 9 lines
* Time: 5 min

English:
    1. Use `input` in `while True` loop to ask user about number
    2. Compare user's number with `HIDDEN`:
       a. If number is equal, print `Exactly` and break game
       b. If number is greater, print `Above`
       c. If number is lower, print `Below`
    3. Run doctests - all must succeed

Polish:
    1. Użyj `input` w pętli `while True` do pytania użytkownika o liczbę
    2. Porównaj liczbę wprowadzoną przez użytkownika z `HIDDEN`:
       a. Jeżeli jest taka sama, to wypisz `Exactly` i zakończ grę
       b. Jeżeli jest większa, to wypisz `Above`
       c. Jeżeli jest mniejsza, to wypisz `Below`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `Stop` or `Ctrl+C` kills infinite loop

Tests:
    >>> import sys; sys.tracebacklimit = 0
"""

# Simulate user input (for test automation)
from unittest.mock import MagicMock
input = MagicMock(side_effect=['0', '9', '1', '8', '2', '7', '3', '6', '4'])


HIDDEN = 4

# Solution
while True:
    guess = int(input('\nType number: '))

    if guess == HIDDEN:
        print('Exactly')
        break
    elif guess > HIDDEN:
        print('Above')
    elif guess < HIDDEN:
        print('Below')
