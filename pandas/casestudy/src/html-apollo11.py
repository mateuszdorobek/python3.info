import sqlite3
import pandas as pd

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 100)
pd.set_option('display.min_rows', 100)
pd.set_option('display.max_seq_items', 100)

# DATA = 'https://history.nasa.gov/SP-4029/Apollo_11i_Timeline.htm'
DATA = 'https://python3.info/_static/apollo11.html'
DATABASE = 'apollo11.sqlite3'


def to_timedelta(text: str) -> pd.Timedelta:
    if type(text) is not str:
        return pd.NaT
    parts = text.split(':')
    hours = parts[0]
    minutes = parts[1]
    seconds = parts[2] if len(parts) == 3 else 0
    return pd.Timedelta(f'{hours}h {minutes}m {seconds}s').round(freq='s')

df = (pd
    .read_html(io=DATA, header=0)[0]
    .rename(columns={
        'Event': 'event',
        'GMT  Date': 'date',
        'GMT  Time': 'time',
        'GET  (hhh:mm:ss)': 'mission_time'})
    .fillna({'time':'00:00:00'})
    .assign(
        time = lambda df: pd.to_datetime(df.time, errors='coerce').dt.time,
        date = lambda df: pd.to_datetime(df.date, errors='coerce').dt.date,
        datetime = lambda df: pd.to_datetime(df.date.astype('str') + 'T' + df.time.astype('str')),
        mission_time = lambda df: df.mission_time.map(to_timedelta))
    .convert_dtypes()
    .set_index('datetime', drop=True)
)

df['category'] = 'INFO'
df.loc[:'1969-07-16 13:32:00', 'category'] = 'DEBUG'
df.loc['1969-07-16 13:32:00':'1969-07-20 17:44:00', 'category'] = 'INFO'
df.loc['1969-07-20 17:44:00':'1969-07-21 21:35:00', 'category'] = 'WARNING'
df.loc['1969-07-24 16:50:35':, 'category'] = 'DEBUG'
df.loc['1969-07-20 20:10:22', 'category'] = 'ERROR'
df.loc['1969-07-20 20:11:02', 'category'] = 'ERROR'
df.loc['1969-07-20 20:14:18', 'category'] = 'ERROR'
df.loc['1969-07-20 20:14:43 ', 'category'] = 'ERROR'
df.loc['1969-07-20 20:14:58', 'category'] = 'ERROR'
df.loc['1969-07-16 13:32:00', 'category'] = 'CRITICAL'
df.loc['1969-07-16 13:33:23', 'category'] = 'CRITICAL'
df.loc['1969-07-16 13:34:44', 'category'] = 'CRITICAL'
df.loc['1969-07-16 13:39:40', 'category'] = 'CRITICAL'
df.loc['1969-07-16 13:43:49', 'category'] = 'CRITICAL'
df.loc['1969-07-16 16:22:13', 'category'] = 'CRITICAL'
df.loc['1969-07-16 16:56:03', 'category'] = 'CRITICAL'
df.loc['1969-07-19 17:21:50', 'category'] = 'CRITICAL'
df.loc['1969-07-19 21:43:36', 'category'] = 'CRITICAL'
df.loc['1969-07-20 17:44:00', 'category'] = 'CRITICAL'
df.loc['1969-07-20 20:05:05', 'category'] = 'CRITICAL'
df.loc['1969-07-20 20:17:39', 'category'] = 'CRITICAL'
df.loc['1969-07-20 22:12:00', 'category'] = 'CRITICAL'
df.loc['1969-07-21 02:39:33', 'category'] = 'CRITICAL'
df.loc['1969-07-21 02:56:15', 'category'] = 'CRITICAL'
df.loc['1969-07-21 03:09:08', 'category'] = 'CRITICAL'
df.loc['1969-07-21 03:15:16', 'category'] = 'CRITICAL'
df.loc['1969-07-21 03:24:19', 'category'] = 'CRITICAL'
df.loc['1969-07-21 03:41:43', 'category'] = 'CRITICAL'
df.loc['1969-07-21 03:48:30', 'category'] = 'CRITICAL'
df.loc['1969-07-21 05:01:39', 'category'] = 'CRITICAL'
df.loc['1969-07-21 05:09:32', 'category'] = 'CRITICAL'
df.loc['1969-07-21 05:11:13', 'category'] = 'CRITICAL'
df.loc['1969-07-21 17:54:00', 'category'] = 'CRITICAL'
df.loc['1969-07-21 18:01:15', 'category'] = 'CRITICAL'
df.loc['1969-07-21 21:35:00', 'category'] = 'CRITICAL'
df.loc['1969-07-22 04:55:42', 'category'] = 'CRITICAL'
df.loc['1969-07-22 04:58:13', 'category'] = 'CRITICAL'
df.loc['1969-07-24 16:21:12', 'category'] = 'CRITICAL'
df.loc['1969-07-24 16:35:05', 'category'] = 'CRITICAL'
df.loc['1969-07-24 16:50:35', 'category'] = 'CRITICAL'
df.loc['1969-07-24 17:29:00', 'category'] = 'CRITICAL'

tv = df['event'].str.contains('TV')
df.loc[tv, 'category'] = 'DEBUG'

df = df[['date', 'time', 'mission_time', 'category', 'event']]

with sqlite3.connect(DATABASE) as db:
    df.to_sql('apollo11', db)
