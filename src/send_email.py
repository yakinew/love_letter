import smtplib
import ssl
from email.message import EmailMessage
import os

from pydantic import Field
from pydantic_settings import BaseSettings


class EmailSettings(BaseSettings):
    email: str = Field(alias='MY_EMAIL')
    key: str = Field(alias='MY_EMAIL_KEY')
    wife_email: str = Field(alias='MY_WIFE_EMAIL')


def send_love_letter(letter_text: str):
    """
    Sends a love letter email to your wife.

    Args:
        letter_text (str): The text of your love letter.
    """
    # Email configuration
    settings = EmailSettings()
    return send_letter(settings.email, settings.key, settings.wife_email, letter_text)


def send_letter(email: str, password: str, wife_email: str, letter_text: str):
    """
    Sends a love letter email to your wife.

    Args:
        email (str): Your email address.
        password (str): Your email app password.
        wife_email (str): Your wife's email address.
        letter_text (str): The text of your love letter.
    """
    # Email configuration
    subject = 'My Dearest Love'  # You can customize the subject
    body = letter_text
    sender_email = email
    receiver_email = wife_email

    # Create an EmailMessage object
    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.set_content(body)  # Use set_content for plain text

    # Add HTML alternative (optional, for richer formatting)
    # html_body = f"""
    # <html>
    # <body>
    #     <p>{letter_text}</p>
    #     <p>With all my love,</p>
    #     <p>Your Husband</p>
    # </body>
    # </html>
    # """
    # message.add_alternative(html_body, subtype="html")

    # Secure the connection and send the email
    context = ssl.create_default_context()
    try:
        port = 465
        with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print('Love letter sent successfully!')
    except Exception as e:
        print(f"Error sending love letter: {e}")

    # try:
    #     port = 587
    #     with smtplib.SMTP('smtp.gmail.com', port) as server:
    #         server.starttls()
    #         server.login(sender_email, password)
    #         server.sendmail(sender_email, receiver_email, message.as_string())
    #     print('Love letter sent successfully!')
    # except Exception as e:
    #     print(f'Error sending love letter: {e}')
