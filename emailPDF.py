from socket import socket
import pyzmail

__author__ = 'oza'

import os
import glob
from email.mime.application import MIMEApplication


def is_rpi():
    """
    Uses -release file to find if device is running Raspbian
    (Assuming this will be the only distro that we will work with, for now)
    :return: boolean
    """
    with open(glob.glob('/etc/*-release')[0], 'r') as f:
	for line in f:
		if 'NAME' in line and 'Raspbian' in line:
			return True
    return False


def send():
    sender=(u'Canary RPi', 'canary.netsec@gmail.com')
    recipients=['oza4@cornell.edu','nr365@cornell.edu','gt286@cornell.edu','ams767@cornell.edu']
    subject=u'PDF from RPi'
    text_content=u'Attached PDF'
    preferred_encoding='iso-8859-1'
    text_encoding='iso-8859-1'

    os.chdir('reports')
    newest_report = max(glob.iglob('*.[Pp][Dd][Ff]'), key=os.path.getctime)

    fp = open(newest_report, 'rb')
    pdf = MIMEApplication(fp.read())
    fp.close()
    pdf.add_header('Content-Disposition', 'attachment',filename=newest_report)
    payload, mail_from, rcpt_to, msg_id=pyzmail.compose_mail(\
            sender, \
            recipients, \
            subject, \
            preferred_encoding, \
            (text_content, text_encoding), \
            html=None, \
            attachments=[pdf])

    smtp_host='smtp.gmail.com'
    smtp_port=587
    smtp_mode='tls'
    smtp_login='canary.netsec@gmail.com'
    smtp_password='Internet Of Things'

    ret=pyzmail.send_mail(payload, mail_from, rcpt_to, smtp_host, \
            smtp_port=smtp_port, smtp_mode=smtp_mode, \
            smtp_login=smtp_login, smtp_password=smtp_password)

    if isinstance(ret, dict):
        if ret:
            print 'failed recipients:', ', '.join(ret.keys())
        else:
            print 'PDF emailed'
    else:
        print 'error:', ret

if __name__ == "__main__":
    send()

