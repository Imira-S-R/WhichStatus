import smtplib, ssl
import requests
import config
from datetime import datetime
import time

def send_down_email(status_code):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = config.FROM_EMAIL  # Enter your address
    receiver_email = config.TO_EMAIL  # Enter receiver address
    password = config.FROM_EMAIL_PASSWORD
    message = """\
Subject: NOTICE: Website DOWN
Hi,

Your website {} is down

Event Timestamp: {}

Status code: {}

WhichStatus will alert you when it is back up.

Sincerely,
WhichStatus
""".format(config.URL, str(datetime.now().time().strftime("%H:%M:%S")), str(status_code))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def check_status():

    while True:
        time.sleep(5)
        status_code = requests.get(config.URL).status_code
        if status_code != 200:
            pass
        elif status_code == 200:
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = config.FROM_EMAIL  # Enter your address
            receiver_email = config.TO_EMAIL  # Enter receiver address
            password = config.FROM_EMAIL_PASSWORD
            message = """\
Subject: NOTICE: Website UP
Hi,

Your website {} is UP again

Event Timestamp: {}

Status code: {}

Sincerely,
WhichStatus
""".format(config.URL, str(datetime.now().time().strftime("%H:%M:%S")), str(status_code))
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            return 'done'
