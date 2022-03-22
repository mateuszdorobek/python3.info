import imaplib
import email
from pprint import pprint
from quopri import decodestring
from datetime import datetime


# Gmail requires to generate One-Time App Password
# https://security.google.com/settings/security/apppasswords
IMAP4_HOST = 'imap.gmail.com'
IMAP4_PORT = 993
IMAP4_USER = 'myusername'
IMAP4_PASS = 'mypassword'
IMAP4_MAILBOX = 'INBOX'


imap = imaplib.IMAP4_SSL(
    host=IMAP4_HOST,
    port=IMAP4_PORT)

imap.login(
    user=IMAP4_USER,
    password=IMAP4_PASS)

imap.select(
    mailbox=IMAP4_MAILBOX,
    readonly=False)


def get_str(text):
    return decodestring(text).decode()


def get_date(text):
    try:
        return datetime.strptime(headers['Date'], '%a, %d %b %Y %H:%M:%S %z')
    except ValueError:
        return text


def get_body(msg):
    type = msg.get_content_maintype()

    if type == 'multipart':
        for part in msg.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload(decode=True).decode('utf-8')

    elif type == 'text':
        return msg.get_payload(decode=True).decode('utf-8')


status, result = imap.search(None, 'ALL')
# Variable `status` is OK
# Variable `result` is [b'1 2 3 4 ...']
messages = result[1][0].split()

for msgid in messages:
    status, data = imap.fetch(msgid, '(RFC822)')
    mail = data[0][1].decode()
    mail = email.message_from_string(mail)

    headers = dict(mail._headers)
    mail = {
        'to': get_str(headers['To']),
        'sender': get_str(headers['From']),
        'subject': get_str(headers['Subject']),
        'date': get_date(headers['Date']),
        'body': get_body(mail)
    }
    pprint(mail)

imap.close()
imap.logout()
