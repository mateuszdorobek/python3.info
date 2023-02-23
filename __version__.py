""" # doctest: +SKIP_FILE
>>> sys.tracebacklimit = 0

>>> assert sys.version_info > (3, 11, 0), \
'Python 3.11+ is required'

>>> assert 'VIRTUAL_ENV' in os.environ, \
'Please make sure you are using venv environment.'
"""

import os
import sys
import importlib
import re


print(f'Python:', sys.version[:6])
print(f'Venv:', 'VIRTUAL_ENV' in os.environ)

with open('requirements.txt') as file:
    for line in file:
        module_name = r.group() if (r := re.search(r'^[\w_\-]+', line)) else None
        if not module_name:
            continue
        try:
            module = importlib.import_module(module_name)
        except Exception as err:
            print(f'{module_name}: {err.__class__.__name__}')
        else:
            version = getattr(module, '__version__', 'unknown')
            print(f'{module_name}: {version}')
