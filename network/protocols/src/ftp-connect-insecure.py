from ftplib import FTP


FTP_HOST = 'ftp.pureftpd.org'
FTP_USER = 'anonymous'
FTP_PASS = ''


with FTP(host=FTP_HOST, user=FTP_USER, passwd=FTP_PASS, timeout=30) as ftp:
    ftp.dir()

# drwxr-xr-x   18 1000       1008             1024 Jul 21  2016 .
# drwxr-xr-x   18 1000       1008             1024 Jul 21  2016 ..
# lrwxr-xr-x    1 1000       20                 20 Jun 20  2011 6jack -> pure-ftpd/misc/6jack
# lrwxr-xr-x    1 1000       1008               12 Feb 24  2012 OpenBSD -> misc/OpenBSD
# drwxr-xr-x    2 1000       1008              512 Feb 10  2015 antilink
# lrwxr-xr-x    1 0          1008               24 Feb  1  2006 blogbench -> pure-ftpd/misc/blogbench
# lrwxr-xr-x    1 0          1008               21 Feb  1  2006 bsdcam -> pure-ftpd/misc/bsdcam
# ...
