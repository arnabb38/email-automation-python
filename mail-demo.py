# arnabbasak || linkedin.com/in/arnab-basak

import smtplib
from email.message import EmailMessage
import imghdr

_SENDER_EMAIL_ADDRESS = "sender_email@gmail.com"
_SENDER_EMAIL_PASSWORD = "sender_password"
_RECEIVER_EMAIL_ADDRESS = "receiver_email@example.com"

msg = EmailMessage()
msg['Subject'] = 'Saturday School Team'
msg['From'] = _SENDER_EMAIL_ADDRESS
msg['To'] = _RECEIVER_EMAIL_ADDRESS
msg.set_content("This is email Body!")

with open("~/PATH_TO_IMAGE/saturday.jpg", "rb") as f:
    _DATA = f.read()
    _TYPE = imghdr.what(f.name)
    _NAME = f.name

msg.add_attachment(_DATA, maintype='image', subtype=_TYPE, filename=_NAME)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smpt:
    smpt.login(_SENDER_EMAIL_ADDRESS, _SENDER_EMAIL_PASSWORD)
    smpt.send_message(msg)
