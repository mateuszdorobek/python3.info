import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.width', 300)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 100)
pd.set_option('display.min_rows', 100)
pd.set_option('display.max_seq_items', 100)


DATA = 'https://en.wikipedia.org/wiki/Dahab'

tables = pd.read_html(DATA)
sea = tables[2]

air = (
    tables[1]
    .droplevel(0, axis='columns')
    .iloc[:-2]
    .replace({'Month': {
        'Average high °C (°F)': 'temperature high',
        'Daily mean °C (°F)': 'temperature mean',
        'Average low °C (°F)': 'temperature low',
        'Average precipitation mm (inches)': 'precipitation average',
        'Average rainy days': 'precipitation days',
        'Mean daily sunshine hours': 'sunshine hours'}})
    .drop(columns=['Year'])
    .set_index('Month')
    .replace(r' \(.+\)', '', regex=True)
    .astype('float16')
    .convert_dtypes()
    .round(1)
)


# Daily mean temperature
mean_per_month = air.loc['temperature mean', :]
mean = mean_per_month.mean().round(1)  # 23.5
plot = (
    mean_per_month
    .plot(
        kind='line',
        title='Dahab, South Sinai, Egipt\nMean temperature',
        xlabel='Month',
        ylabel='Temperature [°C]',
        grid=True,
        figsize=(16,10),
        label='temperature'))
plt.hlines(
    y=mean,
    xmin=0,
    xmax=mean_per_month.size,
    color='red',
    label='all time mean')
plt.legend()
# plt.show()
