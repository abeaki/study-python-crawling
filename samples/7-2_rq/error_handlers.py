import os
import signal
import smtplib
from email.mime.text import MIMEText
from traceback import format_exception

EMAIL = 'orangain@gmail.com'


def send_mail(job, exc_type, exc_value, traceback):
    """
    ジョブの失敗時にメールを送信するための関数
    """

    msg = MIMEText('Failed job: {0}\n\n{1}'.format(
        job, ''.join(format_exception(exc_type, exc_value, traceback))))
    msg['Subject'] = 'Job failed'
    msg['From'] = EMAIL
    msg['To'] = EMAIL

    with smtplib.SMTP('localhost') as smtp:
        smtp.send_message(msg)
        print('Message was sent')
