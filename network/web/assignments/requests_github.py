"""
>>> sorted(result)  # doctest: +SKIP
['bpo-27275', 'bpo-33671', 'bpo-34013', 'bpo-35183', 'bpo-37880', 'bpo-39091', 'bpo-41737', 'bpo-41886', 'bpo-43625', 'bpo-44206', 'bpo-44648', 'bpo-44667', 'bpo-44771', 'bpo-44781', 'bpo-44782', 'bpo-44784', 'bpo-44785', 'bpo-44792', 'bpo-44793', 'bpo-44794', 'bpo-44806', 'bpo-44808']
"""

import re
import sys
from datetime import datetime, timezone
import requests


USERNAME = '...'
TOKEN = '...'


DATA_REPOS = 'https://python3.info/_static/github-python-repos.json'
# DATA_REPOS = 'https://api.github.com/orgs/python/repos?per_page=10000'
DATA_COMMITS = 'https://python3.info/_static/github-python-commits.json'
# DATA_COMMITS = 'https://api.github.com/repos/python/cpython/commits'

PATTERN = r'bpo-[0-9]+'

commits = list()
result = set()


def GET(url):
    data = requests.get(url, auth=(USERNAME, TOKEN)).json()
    if type(data) is dict and data['message'].startswith('API rate limit exceeded'):
        print('API rate limit exceeded')
        sys.exit(1)
    return data


for repository in GET(DATA_REPOS):
    if repository['name'] == 'cpython':
        DATA_COMMITS = repository['commits_url'].replace('{/sha}', '')
        break


for commit in GET(DATA_COMMITS):
    sha = commit['sha']
    author = commit['commit']['author']['name']
    email = commit['commit']['author']['email']
    date = datetime.strptime(commit['commit']['author']['date'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
    message = commit['commit']['message']

    if issue := re.findall(PATTERN, message):
        result.update(issue)

    commits.append({
        'sha': sha,
        'author': author,
        'email': email,
        'date': date,
        'message': message})
