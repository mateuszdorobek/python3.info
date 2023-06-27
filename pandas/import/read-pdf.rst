Import Read PDF
===============
* https://tabula-py.readthedocs.io/en/latest/tabula.html


Use Case - 0x01
---------------
>>> # doctest: +SKIP
... """
... >>> import sys, importlib
... >>> assert sys.version_info >= (3, 11), 'Python 3.11+ required'
...
... >>> try:
... ...     _ = importlib.import_module('tabula')
... ... except Exception as err:
... ...     print('pip install tabula-py')
... """
...
... import pandas as pd
... import tabula
...
...
... pd.set_option('display.width', 250)
... pd.set_option('display.max_columns', 15)
... pd.set_option('display.max_rows', 200)
...
... def clean(df):
...     return (
...         df
...         .convert_dtypes()
...         .rename(axis='columns', to_rename={
...             'Unnamed: 0': 'Number',
...             'Item': 'License_plate',
...             'Course date': 'Date',
...             'Amount charged PLN': 'Amount'})
...         .drop(columns='Lp')
...         .iloc[:-1]
...         .transform({
...             'Data': lambda column: pd.to_datetime(column, format='%d.%m.%Y', errors='coerce'),
...             'Kwota': lambda column: column.str.replace(',', '.').astype('float'),
...             'Rejestracja': lambda column: column.str.extract(r'VRM: ([A-Z0-9a-z]+)Identy')})
...         .fillna(method='ffill')
...         .droplevel(1, axis='columns')
...         .dropna()
...         .set_index('Data'))
...
...
... if __name__ == '__main__':
...     dfs = tabula.read_pdf('myfile.pdf', pages='all')
...     df = pd.concat(map(clean, dfs[4:8])).sort_index()
