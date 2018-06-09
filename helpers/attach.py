import os
import smtplib
import os.path as op
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import COMMASPACE, formatdate
from email import encoders
import codecs


def send_mail(send_from, passwd, send_to, subject, message, files=[],
              server="smtp.gmail.com", port=587, use_tls=True, html=True):
    """Compose and send email with provided info and attachments.

    Args:
        send_from (str): from name
        send_to (str): to name
        subject (str): message title
        message (str): message body
        files (list[str]): list of file paths to be attached to email
        server (str): mail server host name
        port (int): port number
        use_tls (bool): use TLS mode
    """
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    if html:
        with codecs.open('helpers/msg.html','r', 'utf-8') as f:
            message = f.read()
            message = message.format(cover=message)
        with open('helpers/your_photo.png','rb') as f:
            msgImage = MIMEImage(f.read())
            msgImage.add_header('Content-ID', '<chris>')
        msg.attach(msgImage)
        msg.attach(MIMEText(message, 'html'))
    else:
        msg.attach(MIMEText(message, 'plain'))
        for path in files:
            part = MIMEBase('application', "octet-stream")
            with open(path, 'rb') as file:
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            'attachment; filename="{}"'.format(op.basename(path)))
            msg.attach(part)

    smtp = smtplib.SMTP(server + ':' + str(port))
    if use_tls:
        smtp.starttls()
        smtp.login(send_from, passwd)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
    print('email sent')
