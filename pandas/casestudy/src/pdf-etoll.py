"""
>>> import sys, importlib
>>> assert sys.version_info >= (3, 11), 'Python 3.11+ required'

>>> try:
...     _ = importlib.import_module('tabula')
... except Exception as err:
...     print('pip install tabula-py')
"""

import pandas as pd
import tabula


pd.set_option('display.width', 250)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 200)

COLUMNS = {
    'Unnamed: 0': 'Lp',
    'Pozycja / Item': 'Rejestracja',
    'Data prze jazdu / Course date': 'Data',
    'Data prze jazdu / Course date Kwota nal iczona PLN / Amount charged PLN': 'Data',
    'Kwota nal iczona PLN / Amount charged PLN': 'Kwota',
    'Unnamed: 1': 'Kwota',
}

def to_float(column):
    return column.str.replace(',', '.').astype('float')

def to_datetime(column):
    return pd.to_datetime(column, format='%d.%m.%Y', errors='coerce')

def to_rejestracja(column):
    return column.str.extract(r'VRM: ([A-Z0-9a-z]+)Identy')

def clean(df):
    return (
        df
        .convert_dtypes()
        .rename(COLUMNS, axis='columns')
        .drop(columns='Lp')
        .iloc[:-1]
        .transform({
            'Data': to_datetime,
            'Kwota': to_float,
            'Rejestracja': to_rejestracja})
        .fillna(method='ffill')
        .droplevel(1, axis='columns')
        .dropna()
        .set_index('Data'))


if __name__ == '__main__':
    dfs = tabula.read_pdf('myfile.pdf', pages='all')
    df = pd.concat(map(clean, dfs[4:8])).sort_index()
