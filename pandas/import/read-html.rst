Import Read HTML
================
* File paths works also with URLs


SetUp
-----
>>> import pandas as pd
>>>
>>> pd.set_option('display.width', 500)
>>> pd.set_option('display.max_columns', 30)
>>> pd.set_option('display.max_rows', 30)


Read HTML
---------
>>> DATA = 'https://python3.info/_static/apollo11.html'
>>>
>>> tables = pd.read_html(DATA)
>>> df = tables[0]
>>>
>>> df.head(n=5)
                                                   0                 1          2            3
0                                              Event  GET  (hhh:mm:ss)  GMT  Time    GMT  Date
1                       Terminal countdown  started.        -028:00:00   21:00:00  14 Jul 1969
2              Scheduled 11-hour hold  at T-9 hours.        -009:00:00   16:00:00  15 Jul 1969
3                   Countdown resumed at  T-9 hours.        -009:00:00   03:00:00  16 Jul 1969
4  Scheduled 1-hour  32-minute hold at T-3 hours ...        -003:30:00   08:30:00  16 Jul 1969


User Agent
----------
>>> import requests
>>>
>>>
>>> DATA = 'https://python3.info/_static/apollo11.html'
>>> USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
...              '(KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
>>>
>>> resp = requests.get(DATA, headers={'User-Agent': USER_AGENT})
>>> tables = pd.read_html(resp.content)
>>> df = tables[0]
>>>
>>> df.head(n=5)
                                                   0                 1          2            3
0                                              Event  GET  (hhh:mm:ss)  GMT  Time    GMT  Date
1                       Terminal countdown  started.        -028:00:00   21:00:00  14 Jul 1969
2              Scheduled 11-hour hold  at T-9 hours.        -009:00:00   16:00:00  15 Jul 1969
3                   Countdown resumed at  T-9 hours.        -009:00:00   03:00:00  16 Jul 1969
4  Scheduled 1-hour  32-minute hold at T-3 hours ...        -003:30:00   08:30:00  16 Jul 1969


Use Case - 0x01
---------------
>>> # doctest: +SKIP
... URL = 'https://stats.nba.com/stats/leaguestandingsv3?GroupBy=conf&LeagueID=00&Season=2022-23&SeasonType=Regular%20Season&Section=overall'
...
... data = requests.get(URL, headers={
...     'Origin': 'https://www.nba.com',
...     'Referer': 'https://www.nba.com/',
...     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
... }).json()
...
... df = pd.DataFrame(
...     columns=data['resultSets'][0]['headers'],
...     data=data['resultSets'][0]['rowSet'],
... )
...
... df
   LeagueID SeasonID      TeamID       TeamCity       TeamName      TeamSlug Conference ConferenceRecord  PlayoffRank ClinchIndicator   Division DivisionRecord  DivisionRank  WINS  LOSSES  ...   May   Jun   Jul   Aug   Sep  Oct   Nov   Dec Score_80_Plus Opp_Score_80_Plus Score_Below_80  Opp_Score_Below_80 TotalPoints  OppTotalPoints DiffTotalPoints
0        00    22022  1610612743         Denver        Nuggets       nuggets       West            34-18            1             - w  Northwest          10-6              1    53      29  ...  None  None  None  None  None  4-3  10-4   9-5         53-29             53-29          0-0                 0-0          9495            9222             273
1        00    22022  1610612749      Milwaukee          Bucks         bucks       East            35-17            1             - e    Central          11-5              1    58      24  ...  None  None  None  None  None  6-0   9-5   8-7         58-24             58-24          0-0                 0-0          9589            9291             298
2        00    22022  1610612738         Boston        Celtics       celtics       East            34-18            2             - a   Atlantic          11-5              1    57      25  ...  None  None  None  None  None  4-2  14-2   8-6         57-25             57-25          0-0                 0-0          9671            9136             535
3        00    22022  1610612763        Memphis      Grizzlies     grizzlies       West            30-22            2            - sw  Southwest          13-3              1    51      31  ...  None  None  None  None  None  4-3   8-6  10-4         51-31             51-31          0-0                 0-0          9587            9264             323
4        00    22022  1610612755   Philadelphia          76ers        sixers       East            34-18            3             - x   Atlantic          10-6              2    54      28  ...  None  None  None  None  None  4-4   8-6   9-4         54-28             54-28          0-0                 0-0          9448            9094             354
5        00    22022  1610612758     Sacramento          Kings         kings       West            32-20            3             - p    Pacific          9-7               1    48      34  ...  None  None  None  None  None  2-4   9-5   8-6         48-34             48-34          0-0                 0-0          9898            9681             217
6        00    22022  1610612739      Cleveland      Cavaliers     cavaliers       East            34-18            4             - x    Central          13-3              2    51      31  ...  None  None  None  None  None  5-1   9-7   9-6         51-31             51-31          0-0                 0-0          9205            8764             441
7        00    22022  1610612756        Phoenix           Suns          suns       West            30-22            4             - x    Pacific          9-7               2    45      37  ...  None  None  None  None  None  5-1  10-5  5-11         45-37             45-37          0-0                 0-0          9319            9149             170
8        00    22022  1610612746             LA       Clippers      clippers       West            27-25            5             - x    Pacific          9-7               3    44      38  ...  None  None  None  None  None  3-4  10-6   8-7         44-38             44-38          0-0                 0-0          9314            9273              41
9        00    22022  1610612752       New York         Knicks        knicks       East            32-20            5             - x   Atlantic          8-8               3    47      35  ...  None  None  None  None  None  3-3   7-9   9-6         47-35             47-35          0-0                 0-0          9514            9274             240
10       00    22022  1610612744   Golden State       Warriors      warriors       West            30-22            6             - x    Pacific          7-9               4    44      38  ...  None  None  None  None  None  3-4   8-7   8-7         44-38             44-38          0-0                 0-0          9753            9605             148
11       00    22022  1610612751       Brooklyn           Nets          nets       East            30-22            6             - x   Atlantic          7-9               4    45      37  ...  None  None  None  None  None  2-5  10-6  12-1         45-37             45-37          0-0                 0-0          9295            9225              70
12       00    22022  1610612737        Atlanta          Hawks         hawks       East            26-26            7            - pi  Southeast          8-8               2    41      41  ...  None  None  None  None  None  4-3   8-7   5-9         41-41             41-41          0-0                 0-0          9711            9687              24
13       00    22022  1610612747    Los Angeles         Lakers        lakers       West            27-25            7            - pi    Pacific          6-10              5    43      39  ...  None  None  None  None  None  1-5   7-7   7-9         43-39             43-39          0-0                 0-0          9608            9561              47
14       00    22022  1610612748          Miami           Heat          heat       East            24-28            8            - se  Southeast          10-6              1    44      38  ...  None  None  None  None  None  2-5   8-7   9-6         44-38             44-38          0-0                 0-0          8977            9003             -26
15       00    22022  1610612750      Minnesota   Timberwolves  timberwolves       West            29-23            8            - pi  Northwest          8-8               2    42      40  ...  None  None  None  None  None  4-3   7-8  5-10         42-40             42-40          0-0                 0-0          9494            9497              -3
16       00    22022  1610612740    New Orleans       Pelicans      pelicans       West            29-23            9            - pi  Southwest          11-5              2    42      40  ...  None  None  None  None  None  4-2   9-6  10-5         42-40             42-40          0-0                 0-0          9378            9223             155
17       00    22022  1610612761        Toronto        Raptors       raptors       East            26-26            9            - pi   Atlantic          4-12              5    41      41  ...  None  None  None  None  None  4-3   7-7  5-10         41-41             41-41          0-0                 0-0          9254            9133             121
18       00    22022  1610612741        Chicago          Bulls         bulls       East            27-25           10            - pi    Central          7-9               3    40      42  ...  None  None  None  None  None  3-4   6-8   7-8         40-42             40-42          0-0                 0-0          9276            9170             106
19       00    22022  1610612760  Oklahoma City        Thunder       thunder       West            25-27           10            - pi  Northwest          9-7               3    40      42  ...  None  None  None  None  None  3-3  6-10   6-8         40-42             40-42          0-0                 0-0          9633            9544              89
20       00    22022  1610612742         Dallas      Mavericks     mavericks       West            28-24           11             - o  Southwest          9-7               3    38      44  ...  None  None  None  None  None  3-3   7-7  11-6         38-44             38-44          0-0                 0-0          9366            9360               6
21       00    22022  1610612754        Indiana         Pacers        pacers       East            24-28           11             - o    Central          7-9               4    35      47  ...  None  None  None  None  None  3-5   9-4   8-8         35-47             35-47          0-0                 0-0          9535            9796            -261
22       00    22022  1610612762           Utah           Jazz          jazz       West            24-28           12             - o  Northwest          6-10              4    37      45  ...  None  None  None  None  None  6-2   7-9   6-9         37-45             37-45          0-0                 0-0          9600            9677             -77
23       00    22022  1610612764     Washington        Wizards       wizards       East            21-31           12             - o  Southeast          8-8               3    35      47  ...  None  None  None  None  None  3-4   8-7  5-10         35-47             35-47          0-0                 0-0          9279            9378             -99
24       00    22022  1610612753        Orlando          Magic         magic       East            20-32           13             - o  Southeast          7-9               4    34      48  ...  None  None  None  None  None  1-6  4-11   8-7         34-48             34-48          0-0                 0-0          9136            9346            -210
25       00    22022  1610612757       Portland  Trail Blazers       blazers       West            23-29           13             - o  Northwest          7-9               5    33      49  ...  None  None  None  None  None  5-1  6-10   7-6         33-49             33-49          0-0                 0-0          9299            9628            -329
26       00    22022  1610612745        Houston        Rockets       rockets       West            12-40           14             - o  Southwest          4-12              4    22      60  ...  None  None  None  None  None  1-7   4-9  5-10         22-60             22-60          0-0                 0-0          9081            9725            -644
27       00    22022  1610612766      Charlotte        Hornets       hornets       East            15-37           14             - o  Southeast          7-9               5    27      55  ...  None  None  None  None  None  3-4  3-11  4-12         27-55             27-55          0-0                 0-0          9098            9610            -512
28       00    22022  1610612759    San Antonio          Spurs         spurs       West            10-42           15             - o  Southwest          3-13              5    22      60  ...  None  None  None  None  None  5-2  1-14   6-8         22-60             22-60          0-0                 0-0          9269           10092            -823
29       00    22022  1610612765        Detroit        Pistons       pistons       East            8-44            15             - o    Central          2-14              5    17      65  ...  None  None  None  None  None  2-6  3-12  5-11         17-65             17-65          0-0                 0-0          9045            9719            -674
<BLANKLINE>
[30 rows x 88 columns]


Assignments
-----------
.. literalinclude:: assignments/pandas_readhtml_a.py
    :caption: :download:`Solution <assignments/pandas_readhtml_a.py>`
    :end-before: # Solution
