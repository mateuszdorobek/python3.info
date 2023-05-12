"""
* Assignment: Trigonometry
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Dla `x` z przedziału od 0.0 do 1.0 z próbkowaniem co 0.01 przedstaw przebiegi funkcji `sin`, `cos` dla parametrów `2 * np.pi * x`
    2. Stwórz dwa osobne obrazki (figure):
        a. Każdy z przebiegów na osobnym subplot
        b. Na jednym plot dwa przebiegi funkcji
    3. Wykresy (`subplot`) mają być jeden nad drugim
    4. Wykresy podpisz nazwą funkcji trygonometrycznej
    5. Tekst etykiety osi `y` ustaw na "Wartość funkcji"
    6. Pokoloruj nazwy tików `x` dla wykresu `sin` na czerwono
    7. Pokoloruj nazwę (label) dla `cos` na kolor zielony
    8. Na obu wykresach pokaż grid
    9. Narysuj drugi obrazek z nałożonymi na jeden plot wykresami obu funkcji
    10. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `np.sin()`
    * `np.cos()`
"""

import matplotlib.pyplot as plt
import numpy as np


# Solution
x1 = np.arange(0.0, 1.0, 0.01)
y1 = np.sin(2 * np.pi * x1)
plt.plot(x1, y1)

x2 = np.arange(0.0, 1.0, 0.01)
y2 = np.cos(2 * np.pi * x2)
plt.plot(x2, y2)




import matplotlib.pyplot as plt


x = np.arange(0.0, 1.0, 0.01)

fig = plt.figure(1)

ax1 = fig.add_subplot(211)
ax1.plot(x, np.sin(2 * np.pi * x))
ax1.grid(True)
ax1.set_ylabel('Function Value')
ax1.set_title('sin()')

for label in ax1.get_xticklabels():
    label.set_color('red')


ax2 = fig.add_subplot(212)
ax2.plot(x, np.cos(2 * np.pi * x))
ax2.grid(True)
ax2.set_ylabel('Function Value')

label = ax2.set_xlabel('cos()')
label.set_color('green')
label.set_fontsize('large')

# plt.show()
