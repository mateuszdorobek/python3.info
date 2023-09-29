.. testsetup:: # doctest: +SKIP_FILE

Dragon game
===========

>>> from dragon import Dragon
>>> from random import seed; seed(0)
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3,11), 'Python 3.11+ required'

Stwórz smoka o nazwie "Wawelski"
Ustaw inicjalną pozycję smoka na x=1, y=2

>>> dragon = Dragon('Wawelski', position_x=50, position_y=120)

Ustaw nową pozycję na x=10, y=20

>>> dragon.position_set(x=10, y=20)

Przesuń smoka w lewo o 10 i w dół o 20

>>> dragon.position_change(left=10, down=20)

Przesuń smoka w lewo o 10 i w prawo o 15

>>> dragon.position_change(left=10, right=15)

Przesuń smoka w prawo o 15 i w górę o 5

>>> dragon.position_change(right=15, up=5)

Przesuń smoka w dół o 5

>>> dragon.position_change(down=5)

Smok zadaje obrażenia (5-20)

>>> dmg = dragon.make_damage()

Zadaj smokowi DMG obrażeń

>>> try:
...     dragon.take_damage(10)
...     dragon.take_damage(20)
...     dragon.take_damage(30)
...     dragon.take_damage(40)
...     dragon.take_damage(50)
... except dragon.IsDead:
...     drop = dragon.get_drop()
...     print(f'{dragon.name} is dead')
...     print(f'Gold: {drop.gold}')
Wawelski is dead
Gold: 98
