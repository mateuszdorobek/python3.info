"""
* Assignment: Loop WhileElse Else
* Type: homework
* Complexity: medium
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Modify game code below
    2. User can try `MAX_TRIES` times, if he/sh does not guess number by then
       print `Game over, max tries achieved.`
    3. Use `while ... else` syntax
    4. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj kod gry poniżej
    2. Użytkownik może próbować `MAX_TRIES` razy, jeżeli w tym czasie nie zgadnie
       to wypisz `Game over, max tries achieved.`
    3. Użyj składni `while ... else`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `Stop` or `Ctrl+C` kills infinite loop

Tests:
    >>> import sys; sys.tracebacklimit = 0
"""


# Simulate user input (for test automation)
from unittest.mock import MagicMock
input = MagicMock(side_effect=['0', '9', '1', '8', '2', '7', '3', '6', '4'])


HIDDEN = 4
MAX_TRIES = 4


while True:
    guess = input('\nType number: ')

    if int(guess) > HIDDEN:
        print('Above')
    elif int(guess) < HIDDEN:
        print('Below')
    else:
        print('Exactly')
        break

# Solution
input = MagicMock(side_effect=['0', '9', '1', '8', '2', '7', '3', '6', '4'])
current = 0

while current < MAX_TRIES:
    current += 1
    guess = input('\nType number: ')

    if int(guess) > HIDDEN:
        print('Above')
    elif int(guess) < HIDDEN:
        print('Below')
    else:
        print('Exactly')
        break
else:
    print('Game over, max tries achieved.')
