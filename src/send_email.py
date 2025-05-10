"""
This module provides functionality for sending emails, specifically love letters.
It uses the smtplib library for email transmission and includes classes for
managing email settings.
"""
import smtplib
import ssl
from email.message import EmailMessage

from pydantic import Field
from pydantic_settings import BaseSettings


class EmailSettings(BaseSettings):
    """
    Configuration class for email settings.

    This class uses pydantic_settings.BaseSettings to manage email settings,
    loading them from the environment.  It defines the required email addresses
    and authentication key.

    Attributes:
        email (str):  The sender's email address.  This is loaded from the
            environment variable 'MY_EMAIL'.
        key (str):    The sender's email application key or password. This is
            loaded from the environment variable 'MY_EMAIL_KEY'.
        wife_email (str): The recipient's email address (your wife's email).
            This is loaded from the environment variable 'MY_WIFE_EMAIL'.

    Examples:
        To use this class, ensure that the following environment variables are set:
        - MY_EMAIL: Your email address (e.g., "your_email@gmail.com")
        - MY_EMAIL_KEY: Your email application key or password.
        - MY_WIFE_EMAIL: Your wife's email address (e.g., "wife_email@example.com")

        Then, an instance of EmailSettings can be created, and the attributes
        will be automatically populated from the environment:

        >>> settings = EmailSettings()
        >>> print(settings.email)
        your_email@gmail.com
        >>> print(settings.key)
        your_email_key
        >>> print(settings.wife_email)
        wife_email@example.com
    """
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
    port = 465
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print('Love letter sent successfully!')
