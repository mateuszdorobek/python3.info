TOML Use Case
=============


SetUp
-----
>>> DATA = b"""
... [project]
... name = "myproject"
... version = "1.0.0"
... requires-python = ">=3.11"
... authors = [{name = "Mark Watney", email = "mwatney@nasa.gov"}]
... readme = "README.md"
... license = {file = "LICENSE"}
... keywords = ["ares", "mars", "nasa", "human-spaceflight"]
... urls.homepage = "https://github.com/myusername/myproject"
... urls.repository = "https://github.com/myusername/myproject.git"
... urls.documentation = "https://github.com/myusername/myproject"
... urls.changelog = "https://github.com/myusername/myproject/releases"
... urls.bugtracker = "https://github.com/myusername/myproject/issues"
... dependencies = [
...     "django == 4.2.*",
...     "django-ninja == 0.19.*"]
... """
>>>
>>> with open('/tmp/myfile.toml', mode='wb') as file:
...     file.write(DATA)
635


Load TOML File
--------------
>>> import tomllib
>>>
>>> with open('/tmp/myfile.toml', mode='rb') as file:
...     data = tomllib.load(file)


Use
---
>>> data['project']  # doctest: +NORMALIZE_WHITESPACE
{'name': 'myproject',
 'version': '1.0.0',
 'requires-python': '>=3.11',
 'authors': [{'name': 'Mark Watney', 'email': 'mwatney@nasa.gov'}],
 'readme': 'README.md',
 'license': {'file': 'LICENSE'},
 'keywords': ['ares', 'mars', 'nasa', 'human-spaceflight'],
 'urls': {'homepage': 'https://github.com/myusername/myproject',
  'repository': 'https://github.com/myusername/myproject.git',
  'documentation': 'https://github.com/myusername/myproject',
  'changelog': 'https://github.com/myusername/myproject/releases',
  'bugtracker': 'https://github.com/myusername/myproject/issues'},
 'dependencies': ['django == 4.2.*', 'django-ninja == 0.19.*']}

>>> data['project']['name']
'myproject'

>>> data['project']['version']
'1.0.0'

>>> data['project']['requires-python']
'>=3.11'

>>> data['project']['authors']
[{'name': 'Mark Watney', 'email': 'mwatney@nasa.gov'}]

>>> data['project']['dependencies']
['django == 4.2.*', 'django-ninja == 0.19.*']

>>> data['project']['urls']  # doctest: +NORMALIZE_WHITESPACE
{'homepage': 'https://github.com/myusername/myproject',
 'repository': 'https://github.com/myusername/myproject.git',
 'documentation': 'https://github.com/myusername/myproject',
 'changelog': 'https://github.com/myusername/myproject/releases',
 'bugtracker': 'https://github.com/myusername/myproject/issues'}
