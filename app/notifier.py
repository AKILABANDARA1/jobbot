import smtplib
from email.message import EmailMessage
from app.config import Config

def send_email(to_address, subject, body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = Config.EMAIL_USER
    msg["To"] = to_address
    msg.set_content(body)

    with smtplib.SMTP_SSL(Config.EMAIL_HOST, Config.EMAIL_PORT) as server:
        server.login(Config.EMAIL_USER, Config.EMAIL_PASS)
        server.send_message(msg)

