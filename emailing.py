import smtplib
import os
import imghdr
from email.message import EmailMessage


def send_emails(photo_path: str) -> None:
    """
    Send an email to 'receiver' by 'username'.
    The parametr photo it's going to attach in the message
    """
    # Temos que criar esta instância, pois como queremos colocar uma foto na mensagem, precisamos de algo mais complexo
    email_message: EmailMessage = EmailMessage()
    email_message['Subject'] = 'New customer showed up!'
    email_message.set_content('Hey, we just saw a new customer!')

    with open(photo_path, 'rb', encoding='utf-8') as file:
        content = file.read()

    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(os.getenv('myemail'), os.getenv('PASSWORD_PORTFOLIO_WEBSITE'))
    gmail.sendmail(os.getenv('myemail'), os.getenv('myemail'), email_message.as_string())
    gmail.quit()
