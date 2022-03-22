import poplib


POP3_HOST = 'localhost'
POP3_PORT = 995
POP3_USER = 'myusername'
POP3_PASS = 'mypassword'


server = poplib.POP3_SSL(host=POP3_HOST, port=POP3_PORT, timeout=30)
server.user(POP3_USER)
server.pass_(POP3_PASS)

status, messages, length = server.list()

for message in messages:
    msgid, length = message.split()
    status, content, length = server.retr(int(msgid))
    mail = '\r\n'.join(line.decode() for line in content)

    print(mail)
    print('-' * 30)

"""
Return-Path: <root@ip-172-31-5-83.eu-central-1.compute.internal>
X-Original-To: upload@localhost
Delivered-To: upload@localhost
Received: by ip-172-31-5-83.eu-central-1.compute.internal (Postfix, from userid 0)
	id 2481544BD5; Thu, 23 May 2019 07:36:17 +0000 (UTC)
Subject: test
To: <upload@localhost>
X-Mailer: mail (GNU Mailutils 3.4)
Message-Id: <20190523073617.2481544BD5@ip-172-31-5-83.eu-central-1.compute.internal>
Date: Thu, 23 May 2019 07:36:17 +0000 (UTC)
From: root <root@ip-172-31-5-83.eu-central-1.compute.internal>

hello
------------------------------
"""
