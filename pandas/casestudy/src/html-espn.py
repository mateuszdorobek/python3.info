import pandas as pd

DATA = 'https://python3.info/_static/espn-standing.html'
# DATA = 'https://www.espn.com/nba/standings/_/group/league'

tables = pd.read_html(DATA)
teams = tables[0]
scores = tables[1]

first = pd.Series(teams.columns)
teams = pd.concat((first, teams.iloc[:, 0])).reset_index(drop=True)
teams = pd.DataFrame(teams, columns=['Team'])

result = teams.join(scores)
result['Team'] = result['Team'].str.replace(r'[A-Z]+([A-Z])', r'\1', regex=True)

q = result['Team'] == 'A Clippers'
result.loc[q, 'Team'] = 'LA Clippers'
