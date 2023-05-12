import pandas as pd
import requests

# This won't work
# DATA = 'https://www.nba.com/standings'
# data = pd.read_html(DATA)


# curl 'https://stats.nba.com/stats/leaguestandingsv3?LeagueID=00&Season=2021-22&SeasonType=Regular%20Season' \
#  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36' \
#  -H 'Origin: https://www.nba.com' \
#  -H 'Referer: https://www.nba.com/'

DATA = 'https://stats.nba.com/stats/leaguestandingsv3?LeagueID=00&Season=2021-22&SeasonType=Regular%20Season'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'

resp = requests.get(DATA, headers={
    'User-Agent': USER_AGENT,
    'Origin': 'https://www.nba.com',
    'Referer': 'https://www.nba.com/',
})

data = resp.json()['resultSets'][0]

df = pd.DataFrame(columns=data['headers'],
                  data=data['rowSet'])
