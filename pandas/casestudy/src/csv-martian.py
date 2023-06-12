import pandas as pd

pd.set_option('display.width', 600)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 10)


df = (
    pd
    .read_csv('https://python.astrotech.io/_static/martian-pl.csv')
    .convert_dtypes()
    .replace({'born': {
        'styczeń': 'January',
        'luty': 'February',
        'marzec': 'March',
        'kwiecień': 'April',
        'maj': 'May',
        'czerwiec': 'June',
        'lipiec': 'July',
        'sierpień': 'August',
        'wrzesień': 'September',
        'październik': 'October',
        'listopad': 'November',
        'grudzień': 'December'}}, regex=True)
    .assign(
        date_of_birth = lambda df: pd.to_datetime(df['born']),
        dob_weekday = lambda df: df['date_of_birth'].dt.strftime('%A'),
        dob_month = lambda df: df['date_of_birth'].dt.strftime('%B'),
        dob_date = lambda df: df['date_of_birth'].dt.date,
        dob_time = lambda df: df['date_of_birth'].dt.time,
        email_username = lambda df: df['email'].str.split('@', expand=True)[0],
        email_domain = lambda df: df['email'].str.split('@', expand=True)[1],
        dob = lambda df: df['ssn'].astype('str').convert_dtypes().str.zfill(11).str.slice(0,6)
    )
)

df
#   firstname   lastname              born  gender          ssn                email               phone date_of_birth dob_weekday dob_month    dob_date  dob_time email_username email_domain     dob
# 0      Mark     Watney   12 October 1994    male  94101212345     mwatney@nasa.gov   +1 (234) 555-0000    1994-10-12   Wednesday   October  1994-10-12  00:00:00        mwatney     nasa.gov  941012
# 1   Melissa      Lewis       7 July 1995  female  95071512345      mlewis@nasa.gov   +1 (234) 555-0001    1995-07-07      Friday      July  1995-07-07  00:00:00         mlewis     nasa.gov  950715
# 2      Rick   Martinez   21 January 1996    male  96012112345   rmartinez@nasa.gov   +1 (234) 555-0010    1996-01-21      Sunday   January  1996-01-21  00:00:00      rmartinez     nasa.gov  960121
# 3      Alex      Vogel  15 November 1994    male  94111512345       avogel@esa.int  +49 (234) 555-0011    1994-11-15     Tuesday  November  1994-11-15  00:00:00         avogel      esa.int  941115
# 4      Beth  Johanssen        9 May 2006  female   6250912345  bjohanssen@nasa.gov   +1 (234) 555-0100    2006-05-09     Tuesday       May  2006-05-09  00:00:00     bjohanssen     nasa.gov  062509
# 5     Chris       Beck     2 August 1999    male  99080212345       cbeck@nasa.gov   +1 (234) 555-0101    1999-08-02      Monday    August  1999-08-02  00:00:00          cbeck     nasa.gov  990802
