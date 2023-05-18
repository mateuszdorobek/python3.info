"""
* Assignment: Matplotlib Lifecycle
* Complexity: medium
* Lines of code: 20 lines
* Time: 21 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Opracuj podobny wykres dla danych `DATA`
    2. Weź pod uwagę jedynie `sepal_length` oraz `species`
    3. species ma być w osi `y`
    4. Na osi `x` ma być `sepal_length`
    5. Czerwony marker opisuje średnią długość `sepal_length` dla wszystkich gatunków
    6. Uruchom doctesty - wszystkie muszą się powieść
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


DATA = 'https://python3.info/_static/iris.csv'


# Solution
iris = pd.read_csv(DATA)

means = iris.groupby('species').mean()
data = dict(means['sepal_length'])

group_names = list(data.keys())
group_data = list(data.values())
group_mean = np.mean(group_data)

fig, ax = plt.subplots()
ax.barh(group_names, group_data)

labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.axvline(group_mean, ls='--', color='red')

# plt.show()
