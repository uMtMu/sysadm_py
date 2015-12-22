#!/usr/bin/env python
# -*- coding:utf-8 -*- 
import subprocess
import inspect
import socket


def runner(cmd):
    try:
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        return p.communicate()
    except OSError:
        print "Komut bulunamadı!!"

mail_from = "paytr-ankara@paytr.com"
mail_to = "teknik@paytr.com"
mail_sender = "/usr/bin/sendmail"


def send_mail(subject, body):
    print "From:" + mail_from
    print "To:" + mail_to
    print("Subject:(%s) [%s] %s" % 
          (inspect.stack()[1][1], socket.gethostname(),  subject))
    print "Body:" + body
    print "Send with " + mail_sender


if __name__ == "__main__":
    try:
        print 40 * "*"
        out, err = runner(['lsusb'])
        print out
        out, err = runner(['lsudb'])
        print err
    except TypeError as e:
        print "Geçersiz geri dönüş değeri!!"
