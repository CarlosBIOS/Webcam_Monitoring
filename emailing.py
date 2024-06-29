import smtplib
import os


def send_emails(message: bytes | str) -> None:
    """Send an email to 'receiver' by 'username'"""
    host: str = 'smtp.gmail.com'
    # Hotmail: smtp.live.com
    # Outlook: outlook.office365.com
    # Yahoo: smtp.mail.yahoo.com
    # port: int = 465  # port do SSL
    port: int = 587  # port do TLS

    username: str = os.getenv('myemail')
    password: str = os.getenv('PASSWORD_PORTFOLIO_WEBSITE')
    receiver: str = username

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(username, receiver, message.encode('utf-8'))
