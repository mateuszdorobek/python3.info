import pandas as pd

data = (pd
    .read_excel(
        io='myfile.xlsx',
        sheet_name='Sheet1',
        names=['names', 'column1', 'column2'])
    .loc[:200, 'names']
    .str.split(', ', regex=True, expand=True)
    .melt(ignore_index=True)
    .dropna()
    .loc[:, 'value']
    .sort_values()
    .reset_index(drop=True)
    .unique()
)

result = (pd
    .Series(data)
    .str.split(expand=True)
    .dropna(axis='rows', how='all')
)

result.to_excel('/tmp/myfile.xlsx')
