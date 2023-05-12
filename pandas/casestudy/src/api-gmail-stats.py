import re

import pandas as pd


pd.set_option('display.width', 100)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 50)


FILE = 'myfile.csv'
LABEL = 'moja etykietka'

username = '(?:[a-z0-9=+_\-.]+)'
domain = '(?:[a-z0-9\-.]+)'
tld = '(?:[a-z0-9\-.]+)'
pattern = f'(?P<email>{username}@{domain}\.{tld})'
email = re.compile(pattern, flags=re.IGNORECASE)

df = pd.read_csv(FILE)
addresses = (
    pd.concat((
        df['From'].str.extractall(email).droplevel(level=1),
        df['To'].str.extractall(email).droplevel(level=1),
        df['CC'].str.extractall(email).droplevel(level=1),
        df['BCC'].str.extractall(email).droplevel(level=1),
    ))
    .loc[:, 'email']
    .str.lower()
    .drop_duplicates()
    .sort_values()
    .reset_index(drop=True)
)

label = addresses.str.find(LABEL) > 0
mine = addresses[label].sort_values().reset_index(drop=True)
their = addresses[~label].sort_values().reset_index(drop=True)
