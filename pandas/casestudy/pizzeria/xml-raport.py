import xml.etree.ElementTree as xml
from pathlib import Path

DATA = '2023.07.07 14.04.36 - PRODUKTY 1 2023.xml'


file = Path(DATA)
root = xml.parse(DATA).getroot()

worksheet = root[3]
table = worksheet[0]
data = list(table)


from lxml.etree import Element, tostring, parse
DATA = '2023.07.07 14.04.36 - PRODUKTY 1 2023.xml'
file = parse(DATA)


NAMESPACES = {
    'o': "urn:schemas-microsoft-com:office:office",
    'x': "urn:schemas-microsoft-com:office:excel",
    'ss': "urn:schemas-microsoft-com:office:spreadsheet",
    'html': "http://www.w3.org/TR/REC-html40",
}
