#!/usr/bin/env python
import smtplib


sender = "sender@gmail.com"
receiver = ["receiver@gmail.com"]
message = "Hello!"

try:
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.set_debuglevel(1)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login(sender, '********')
    session.sendmail(sender, receiver, message)
    session.quit()
except smtplib.SMTPException as e:
    print e.args
