"""
* Assignment: Iris Scatter
* Complexity: medium
* Lines of code: 20 lines
* Time: 21 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Z podanego powyżej adresu URL pobierz dane
    2. Dla każdego gatunku
    3. Dane stosunku `sepal_length` do `sepal_width` zwizualizuj w formie `scatter` za pomocą `matplotlib`
    4. Każdy gatunek powinien mieć inny kolor
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `pd.groupby()`
"""

import matplotlib.pyplot as plt
import pandas as pd


DATA = 'https://python3.info/_static/iris.csv'


# Solution
iris = pd.read_csv(DATA)

ratio = iris["sepal_length"] / iris["sepal_width"]

for name, group in iris.groupby("species"):
    plt.scatter(group.index, ratio[group.index], label=name)

plt.legend()
#plt.show()
