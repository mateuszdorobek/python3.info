import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.width', 300)
pd.set_option('display.max_columns', 25)
pd.set_option('display.max_rows', 100)
pd.set_option('display.min_rows', 100)
pd.set_option('display.max_seq_items', 100)


MONTHS = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August', 'September',
    'October', 'November', 'December',
]

df = (pd
    .read_csv(
        filepath_or_buffer='https://python3.info/_static/phones-pl.csv',
        parse_dates=['datetime'])
    .assign(
        date=lambda df: df['datetime'].dt.date,
        time=lambda df: df['datetime'].dt.time,
        year=lambda df: df['period'].str.split('-', expand=True)[0],
        month=lambda df: df['period'].str.split('-', expand=True)[1],
        weekday=lambda df: df['datetime'].dt.strftime('%A'))
    .set_index(keys='datetime', drop=True)
    .drop(columns=['id'])
    .convert_dtypes()
    .astype({'month': int})
    .replace({'month': dict(enumerate(MONTHS, start=1))})
    .groupby(['period','item', 'network'])
    .aggregate(
        duration_count=('duration', 'count'),
        duration_sum=('duration', 'sum'),
        duration_mean=('duration', 'mean'),
        duration_std=('duration', 'std'),
        duration_var=('duration', 'var'),
        duration_min=('duration', 'min'),
        duration_q25=('duration', lambda column: column.quantile(.25)),
        duration_q50=('duration', lambda column: column.quantile(.50)),
        duration_q75=('duration', lambda column: column.quantile(.75)),
        duration_max=('duration', 'max'),
        duration_skew=('duration', 'skew'),)
    .convert_dtypes()
    .round(decimals=2)
)

# %%
data = (
    df
    .xs('sms', level=1)
    .loc[:, 'duration_count']
    .droplevel(1)
).plot(
    legend=True,
    grid=True,
    figsize=(16,10),
    title='Number of SMS in given period',
    ylabel='Number of SMS',
    xlabel='Timeframe',
)

# plt.show()
