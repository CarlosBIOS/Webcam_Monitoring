import smtplib
import os


def send_emails(photo: str) -> None:
    """
    Send an email to 'receiver' by 'username'.
    The parametr photo it's going to attach in the message
    """
    host: str = 'smtp.gmail.com'
    # Hotmail: smtp.live.com
    # Outlook: outlook.office365.com
    # Yahoo: smtp.mail.yahoo.com
    # port: int = 465  # port do SSL
    port: int = 587  # port do TLS

    username: str = os.getenv('myemail')
    password: str = os.getenv('PASSWORD_PORTFOLIO_WEBSITE')
    receiver: str = username
    message = ''

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(username, receiver, message.encode('utf-8'))
