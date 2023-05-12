import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


DATA = 'https://python3.info/_static/phones.xlsx'

MONTHS_PL = ['styczeń', 'luty', 'marzec', 'kwiecień',
             'maj', 'czerwiec', 'lipiec', 'sierpień',
             'wrzesień', 'październik', 'listopad', 'grudzień']
MONTHS = dict(enumerate(MONTHS_PL, start=1))


df = pd.read_excel(
        io='/Users/matt/Desktop/phones.xlsx',
        sheet_name='Polish',
        skiprows=1,
        index_col=0,
        parse_dates=['datetime'])

df.info(memory_usage='deep')

df['date'] = df['datetime'].dt.date
df['time'] = df['datetime'].dt.time
df[['period_year', 'period_month']] = df['period'].str.split('-', expand=True)
df['period_monthname'] = df['period_month'].astype(int).map(MONTHS)

result = df.groupby(['period', 'item', 'network']).agg(
    duration_count=('duration', 'count'),
    duration_sum=('duration', 'sum'),
    duration_min=('duration', 'min'),
    duration_max=('duration', 'max'),
    duration_mean=('duration', 'mean'),
    duration_mean_round=('duration', lambda group: group.mean().astype(int)),
    duration_median=('duration', 'median'),
    duration_std=('duration', 'std'),
    first=('datetime', 'first'),
    last=('datetime', 'last'),
)

result['duration_sum'].plot(kind='line', figsize=(16,10))
