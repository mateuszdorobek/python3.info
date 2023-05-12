import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 100)
pd.set_option('display.min_rows', 10)
pd.set_option('display.max_seq_items', 100)

data: pd.DataFrame
fig: plt.Figure
axes: plt.Axes

#%%

DATA = 'https://python3.info/_static/sensors-optima.xlsx'
LUX = 1
LIGHT_NOISE_THRESHOLD = 20*LUX

# Locations
# - Sleeping Quarters upper
# - Kitchen Lab Table
# - Kitchen behind glovebox
# - Lab middle room
# - Bathroom
# - Gym lower
# - Sleeping Quarters lower


#%% Import and clean data
def mission_day(df):
    mission_start = df.index.min()
    mission_end = df.index.max()
    mission_days = pd.date_range(mission_start, mission_end, freq='D', normalize=True).date
    to_replace = {date:i for i, date in enumerate(mission_days)}
    return df['date'].replace(to_replace)

def was_active(df, noise_threshold=LIGHT_NOISE_THRESHOLD):
    return df['value'] > noise_threshold


df = (
    pd.read_excel(
        io=DATA,
        sheet_name='Luminance',
        header=1,
        parse_dates=['datetime'],
        usecols=['datetime', 'device', 'location', 'value', 'type'],
        index_col='datetime')
    .assign(
        date = lambda df: df.index.date,
        time = lambda df: df.index.round(freq='s').time,
        day = lambda df: mission_day(df),
        hour = lambda df: df.index.hour,
        activity = lambda df: was_active(df).astype('int'))
    .convert_dtypes()
)

#%% Inspect dataframe
df.info(memory_usage='deep')

#%% Inspect data
df['value'].describe()

# Pokaż, jakie wartości występują najczęściej
# Widać, że większość pomiarów znajduje się poniżej 7 luxów
# Mogą to być np. zapalone diody monitorów, ekrany urządzeń itp.
# To jest tzw. próg szumu
# poniżej to szum - np. świecąca w tle dioda monitora
# powyżej to sygnał - zapalone światło
df['value'].hist(bins=20)
plt.show()  # doctest: +SKIP


#%% Illuminance
data = (
    df
    .loc[:, 'value']
    .resample('H')
    .mean()
    .round()
    .astype('int16'))

ax = data.plot(
    kind='line',
    title='Changes in illuminance during analog mission',
    xlabel='Mission Day',
    ylabel='Illuminance [lux]',
    figsize=(8,8))

ax.set_xticklabels(range(0,7), minor=True)
ax.set_xmargin(0)
plt.show()  # doctest: +SKIP


#%% Activity
# np.sign()
# - zwraca -1, jeżeli wartość jest mniejsza niż 0
# - zwraca 0, jeżeli wartość jest równa 0
# - zwraca 1, jeżeli wartość jest mniejsza niż 0
data = (
    df
    .loc[:, ['day', 'hour', 'activity']]
    .groupby(['day', 'hour'])
    .mean()
    .apply(np.sign)
    .astype('int'))

fig, axes = plt.subplots(
    nrows=8,
    ncols=1,
    figsize=(10,20),
    sharex='all',
    sharey='all',
    constrained_layout=True)

for day, dane in data.groupby(level=0):
    dane.droplevel('day').plot(
            ax=axes[day],
            kind='line',
            title=f'Day {day}',
            legend=None,
            yticks=[0,1],
            xticks=range(0,25),
            ylabel=None)

for ax in axes.flatten():
    ax.set_xmargin(0)
    ax.set_yticklabels(['sleep', 'awake'])
    ax.set_xticklabels([f'{hour:02}:00' for hour in range(0,25)])
    ax.xaxis.set_tick_params(labelbottom=True)
    ax.yaxis.set_tick_params(labelleft=True)
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    plt.setp(ax.get_xticklabels(), rotation=90, ha='right', rotation_mode='anchor')

fig.tight_layout(pad=5.0)
fig.suptitle('Changes in activity during analog mission', fontsize=20)
fig.supxlabel('Time of a day [UTC]', fontsize=16)
fig.supylabel('Activity [sleep/awake]', fontsize=16)
fig.subplots_adjust(top=0.925, bottom=0.075)

plt.setp(ax.get_xticklabels(), rotation=90, ha='right', rotation_mode='anchor')
plt.show()  # doctest: +SKIP


#%% Actinogram
data = (
    df
    .loc[:, ['day', 'hour', 'value']]
    .groupby(['day', 'hour'])
    .mean()
    .round()
    .astype('int16')
    .reset_index()
    .pivot(index='day', columns='hour', values='value')
)

rows = [f'Day {day}' for day in range(data.index.size)]
columns = [f'{hour:02}:00' for hour in data.columns]
values = data.values

fig, ax = plt.subplots(figsize=(15,5))
im = ax.imshow(values)

ax.set_yticks(np.arange(len(rows)), labels=rows)
ax.set_xticks(np.arange(len(columns)), labels=columns)
ax.set_title('Actinogram')
ax.set_xlabel('Time of a day [UTC]')
ax.set_ylabel('Mission day')

plt.setp(ax.get_xticklabels(), rotation=90, ha='right', rotation_mode='anchor')

fig.colorbar(im, ax=ax, shrink=0.85, label='Luminescence [lux]')
fig.tight_layout()
plt.show()  # doctest: +SKIP
