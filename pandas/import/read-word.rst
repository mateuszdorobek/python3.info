Import Read Word
================
* https://python-docx.readthedocs.io/en/latest/
* Support both ``.docx`` and ``.doc``


Use Case - 0x01
---------------
>>> # doctest: +SKIP
... from csv import DictWriter, QUOTE_ALL
... from docx import Document
...
...
... def clean(text):
...     return (text.
...             .replace('☑', '-')
...             .replace('–', '-')
...             .replace(' -– ', '-')
...             .replace('●', '-')
...             .replace('•', '-')
...             .replace('::', ':')
...             .replace('⌂', '-')
...             .replace('Ω', '-')
...             .replace('☹', '')
...             .replace('😊', '')
...             .replace('„', '"')
...             .replace('”', '"')
...             .replace('“', '"')
...             .replace('‘', ''')
...             .replace('’', ''')
...             .strip())
...
...
... document = Document('_tmp/input.docx')
... result = []
... data = []
...
... for table in document.tables:
...     userstory = {}
...     for i, row in enumerate(table.rows):
...         if i == 0:
...             userstory['ID'] = clean(row.cells[1].text)
...             userstory['Category'] = clean(row.cells[2].text)
...         else:
...             field = ''  # Required for not to carry previous information if header is missing
...             value = ''  # Required for not to carry previous information if header is missing
...             field = clean(row.cells[1].text)
...             value = clean(row.cells[2].text)
...             userstory[field] = value
...     data.append(userstory)
...
...
... for row in data:
...     summary = row.get('Summary', '').strip().replace('\n', '')
...     story = row.get('Story', '')
...     description = row.get('Description', '')
...     details = row.get('Details', '')
...     id = row.get('ID', '').replace('\n', ' ')
...     category = row.get('Category', '').removeprefix('(').removesuffix(')')
...
...     result.append({
...         'Summary': f'[{id}] {summary}',
...         'Description': f'*User Story*\n{story}\n\n' +\
...                        f'*Description*\n{description}\n\n' +\
...                        f'*Details*\n{details}\n\n'})
...
...
... with open('_tmp/output.csv', mode='w') as file:
...     writer = DictWriter(f=file,
...                         fieldnames=['Summary', 'Description'],
...                         quoting=QUOTE_ALL,
...                         delimiter=',',
...                         quotechar='"')
...     writer.writeheader()
...     writer.writerows(result)
